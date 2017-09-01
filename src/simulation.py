from src import node
from sys import argv
import argparse


class Simulation:
    def __init__(self, args, logger=None):
        self.nodes = []
        self.sim_time = 0
        self.sim_duration = args.duration
        self.logger = logger
        for i in range(0, args.nodes):
            n = node.Node(i)
            self.nodes.append(n)

    def __tick__(self):
        self.sim_time += 1
        if self.sim_time >= self.sim_duration:
            return False

    def __log_data__(self):
        if self.logger:
            pass
        return

    def run(self):
        while self.__tick__():
            pass
        print("Simulation ended")


def main(args):
    s = Simulation(args)


def parse_args():
    parser = argparse.ArgumentParser(description='Parse simulation parameters')
    parser.add_argument('-n', '--nodes', help="Amount of nodes used for the simulation", type=int, default=50, dest='nodes')
    parser.add_argument('-s', '--services', help="Amount of services per node for the simulation", type=int, default=20, dest='services')
    parser.add_argument('-c', '--cert-lifetime', help="Certificate lifetime in minutes", type=int, default=1000, dest='certificate_lifetime')
    parser.add_argument('-r', '--cert-refresh', help="Max renewal time before certificate expiration in minutes", type=int, default=100, dest='certificate_refresh')
    parser.add_argument('-d', '--duration', help="Total duration of simulation in minutes", type=int, default=20000, dest='duration')

    args = argv[1:]
    args = parser.parse_args(args)
    return args


if __name__ == '__main__':
    main(parse_args())
