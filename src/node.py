from src import service


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.services = {}  # <service, certificate>

    def deploy_service(self, new_service):
        self.services[new_service] = None

    def issue_certificate(self, for_service):
        pass

    def __str__(self):
        return str(self.id)