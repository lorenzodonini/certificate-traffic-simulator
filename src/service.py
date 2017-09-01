class Service:
    def __init__(self, name):
        self.name = name
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

