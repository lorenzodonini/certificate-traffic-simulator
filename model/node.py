from model import network_manager

# Node-Local Service Manager (NLSM)


class Node:
    def __init__(self, node_id, slsm):
        self.slsm = slsm
        self.id = slsm.space_id + ".NSLM" + str(node_id)
        self.services = {}  # <id, service>
        self.available = True

    def __should_renew_certificate(self, service_id, now):
        service = self.services[service_id]
        return service.certificate and service.certificate.is_expired(now)

    def deploy_service(self, new_service, now):
        if new_service.service_id in self.services:
            raise KeyError("Service " + str(new_service) + " is already deployed on node " + str(self))
        self.services[new_service.service_id] = new_service
        if not new_service.certificate or new_service.certificate.is_expired(now):
            self.renew_certificate(new_service)

    def is_service_running(self, service_id):
        return self.services[service_id] is not None

    def renew_certificate(self, service):
        if not self.available:
            return
        certificate = self.slsm.renew_certificate(self, service)
        if not certificate:
            raise ValueError("Cannot set empty certificate for service " + str(service))
        service.certificate = certificate

    def run_services(self):
        if not self.available:
            return
        now = network_manager.NetworkManager().current_time
        for s in self.services.values():
            if not s.is_certificate_valid(now) or self.__should_renew_certificate(s.service_id, now):
                self.renew_certificate(s)
            s.run(now)

    def __str__(self):
        return str(self.id)
