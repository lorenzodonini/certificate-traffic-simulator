class Certificate:

    def __init__(self, node_id, service_id, signature_key, issue_time, validity=1000, size=256, expiration_backoff=100):
        self.issue_time = issue_time
        self.validity = validity
        self.expiration_time = self.issue_time + self.validity - expiration_backoff
        self.size = size
        # This is only for simulation purposes. The actual certificate would be generated differently
        self.signature = str(node_id) + '.' + str(service_id) + '.' + str(signature_key)

    def is_expired(self, now):
        return now >= self.expiration_time

    def is_valid(self, now):
        return now < (self.issue_time + self.validity)

    def __str__(self):
        return self.signature + " -> start: " + str(self.issue_time) + ", end: " + str(self.expiration_time)

