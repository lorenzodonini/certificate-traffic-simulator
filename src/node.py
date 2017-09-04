# Node-Local Service Manager (NLSM)


class Node:
    def __init__(self, node_id, slsm):
        self.id = node_id
        self.slsm = slsm
        self.services = {}  # <id, service>

    def __should_renew_certificate(self, service_id, now):
        service = self.services[service_id]
        return service and service.certificate and service.certificate.is_expired(now)

    def deploy_service(self, new_service):
        if self.services[new_service.service_id]:
            raise KeyError("Service is already deployed on the node")
        self.services[new_service.service_id] = new_service
        self.renew_certificate(new_service)

    def is_service_running(self, service_id):
        return self.services[service_id] is not None

    def renew_certificate(self, service):
        certificate = self.slsm.renew_certificate(self, service)
        if not certificate:
            raise ValueError("Cannot set empty certificate")
        service.certificate = certificate

    def run_services(self, now):
        for s in self.services:
            if not s.is_certificate_valid() or self.__should_renew_certificate(s.service_id, now):
                self.renew_certificate(s)
            s.run(now)

    def __str__(self):
        return str(self.id)
