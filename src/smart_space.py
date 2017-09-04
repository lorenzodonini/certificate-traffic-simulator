from src import certificate_authority
from src import certificate

# Site-Local Service Manager (SLSM)


class SmartSpace:
    def __init__(self, space_id):
        self.space_id = space_id
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def renew_certificate(self, old_certificate):
        pass
