from src import certificate
import random

# Site-Local Certificate Authority (SLCA)


class CertificateAuthority:
    def __init__(self, site_key, certificate_config):
        self.certificate_validity = certificate_config.validity
        self.certificate_expiration_backoff = certificate_config.expiration_backoff
        self.certificate_size = certificate_config.size
        self.site_key = site_key

    def issue_certificate(self, node, service):
        random_backoff = random.randint(0, self.certificate_expiration_backoff)
        return certificate.Certificate(node.id,
                                       service.service_id,
                                       self.site_key,
                                       0,
                                       self.certificate_validity,
                                       self.certificate_size,
                                       random_backoff)
