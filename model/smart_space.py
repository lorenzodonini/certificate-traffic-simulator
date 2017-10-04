from model import certificate_authority, network_manager
import random

# Site-Local Service Manager (SLSM)


class SmartSpace:
    def __init__(self, space_id, certificate_config):
        self.space_id = "SLSM" + str(space_id)
        self.nodes = []
        self.request_payload = certificate_config['request']
        self.access_groups = certificate_config['access_groups']
        self.slca = certificate_authority.CertificateAuthority(self.space_id, 'Key' + str(self.space_id), certificate_config)

    def add_node(self, node):
        self.nodes.append(node)

    def renew_certificate(self, node, service):
        if not node.is_service_running(service.service_id):
            return None
        new_certificate = self.slca.issue_certificate(node, service, network_manager.NetworkManager().current_time)
        request_size = sum([random.randint(1, self.request_payload) * x for x in range(1, random.randint(1, self.access_groups))])
        network_manager.NetworkManager().generate_traffic(node.id, request_size)
        network_manager.NetworkManager().generate_traffic(node.id, new_certificate.size)  # SLSM -> NLSM
        return new_certificate
