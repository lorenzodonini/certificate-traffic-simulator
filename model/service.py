class Service:
    def __init__(self, service_id, name, request_payload):
        self.name = name
        self.service_id = service_id
        self.request_payload = request_payload
        self.certificate = None

    def is_certificate_valid(self, now):
        return self.certificate and self.certificate.is_valid(now)

    def run(self, now):
        if not self.is_certificate_valid(now):
            raise PermissionError(str(self) + ' has invalid certificate')
        # Do some stuff
        pass

    def __str__(self):
        return str(self.service_id) + ' - ' + str(self.name)

