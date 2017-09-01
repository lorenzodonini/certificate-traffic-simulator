from datetime import datetime
from datetime import timedelta


class Certificate:
    def __init__(self, service_id, duration=1000):
        self.start_time = datetime.now()
        self.duration = duration
        self.id = ''
        # self.signature = service_id + self.start_time

    def __expiration_time__(self):
        return self.start_time + timedelta(seconds=self.duration)

    def is_valid(self):
        return datetime.now() < self.__expiration_time__()

    def __str__(self):
        return self.id + " -> start: " + str(self.start_time) + ", end: " + str(self.__expiration_time__())

