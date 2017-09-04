from functools import reduce


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NetworkManager(metaclass=Singleton):
    def __init__(self):
        self.monitored_traffic = {}  # <src, traffic>
        self.current_time = 0

    def total_generated_traffic(self):
        if len(self.monitored_traffic) == 0:
            return 0
        return reduce(lambda total, val: total+val, self.monitored_traffic.values())

    def generate_traffic(self, source, amount):
        traffic = 0
        if source in self.monitored_traffic:
            traffic = self.monitored_traffic[source] + amount
        else:
            traffic += amount
        self.monitored_traffic[source] = traffic


instance = NetworkManager()
