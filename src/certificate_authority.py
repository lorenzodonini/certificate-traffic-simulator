from src import certificate
import random

# Site-Local Certificate Authority (SLCA)


class CertificateAuthority:
    def __init__(self, slsm_id, site_key, certificate_config):
        self.certificate_validity = certificate_config['validity']
        self.certificate_expiration_backoff = certificate_config['expiration_backoff']
        self.certificate_size = certificate_config['size']
        self.site_key = site_key
        self.id = str(slsm_id) + ".SLCA"

    def issue_certificate(self, node, service, now):
        random_backoff = random.randint(0, self.certificate_expiration_backoff)
        return certificate.Certificate(node.id,
                                       service.service_id,
                                       self.site_key,
                                       now,
                                       self.certificate_validity,
                                       self.certificate_size,
                                       random_backoff)
