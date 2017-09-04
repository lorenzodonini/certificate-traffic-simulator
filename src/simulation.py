#!/usr/bin/python3

from src import node, service, data_manager, network_manager, smart_space
from sys import argv
import argparse


INCREMENTAL_NODE_SPAWN = 0
INCREMENTAL_SERVICE_SPAWN = 1
INCREMENTAL_MIXED_SPAWN = 2
FULL_SPAWN = 3


class Simulation:
    def __init__(self, args):
        self.network_manager = network_manager.NetworkManager()
        self.config = args
        self.space = None
        self.sim_duration = args.duration
        self.logger = data_manager.DataManager(args.output)
        certificate_config = {'validity': args.certificate_validity,
                              'expiration_backoff': args.certificate_renew_backoff,
                              'size': args.certificate_size}
        self.__setup__(args.mode, certificate_config)

    def __setup__(self, mode, certificate_config):
        self.space = smart_space.SmartSpace(0, certificate_config)
        if mode == FULL_SPAWN:
            for j in range(0, self.config.nodes):
                self.__instantiate_node__(self.space)

    def __tick__(self):
        self.network_manager.current_time += 1
        # Compute progress
        if ((self.network_manager.current_time * 100 / self.sim_duration) % 10) == 0:
            print(str(int(self.network_manager.current_time * 100 / self.sim_duration)) + "% of simulation run")
        return self.network_manager.current_time < self.sim_duration

    def __instantiate_node__(self, space):
        if len(space.nodes) >= self.config.nodes:
            return
        n = node.Node(len(space.nodes), space)
        space.add_node(n)
        if self.config.mode == INCREMENTAL_SERVICE_SPAWN \
                or self.config.mode == INCREMENTAL_MIXED_SPAWN:
            return
        for k in range(0, self.config.services):
            self.__instantiate_service__(n)

    def __instantiate_service__(self, n):
        if len(n.services) >= self.config.services:
            return
        s = service.Service(len(n.services), 'Service' + str(len(n.services)))
        n.deploy_service(s)

    def __log_data__(self, space, traffic, total_traffic):
        if self.logger:
            services = len(space.nodes[0].services) if len(space.nodes) > 0 else 0
            self.logger.log_data(self.network_manager.current_time,
                                 len(space.nodes),
                                 services,
                                 traffic,
                                 (total_traffic / self.network_manager.current_time))

    def run(self):
        if not self.space:
            raise RuntimeError("Simulation was not setup")

        traffic = 0
        print("Simulation started!")
        while self.__tick__():
            if self.config.mode == INCREMENTAL_NODE_SPAWN \
                    or self.config.mode == INCREMENTAL_MIXED_SPAWN:
                self.__instantiate_node__(self.space)
            for n in self.space.nodes:
                if self.config.mode == INCREMENTAL_SERVICE_SPAWN \
                        or self.config.mode == INCREMENTAL_MIXED_SPAWN:
                    self.__instantiate_service__(n)
                n.run_services()
            # Update generated traffic
            total_traffic = self.network_manager.total_generated_traffic()
            traffic = total_traffic - traffic
            self.__log_data__(self.space, traffic, total_traffic)
            traffic = total_traffic

        print("Simulation ended")

# class NodeSimulation(Simulation):
#     def __setup__(self, mode, smart_spaces, certificate_config):
#         for i in range(0, smart_spaces):
#             space = smart_space.SmartSpace(i, certificate_config)
#             self.spaces.append(space)
#             if mode == SimulationMode.FULL_SPAWN:
#                 for j in range(0, self.config.nodes):
#                     self.__instantiate_node__(space)
#


def main(args):
    sim = Simulation(args)
    sim.run()


def parse_args():
    parser = argparse.ArgumentParser(description='Parse simulation parameters')
    parser.add_argument('-n', '--nodes', help="Amount of nodes used for the simulation", type=int, default=50, dest='nodes')
    parser.add_argument('-s', '--services', help="Amount of services per node for the simulation", type=int, default=20, dest='services')
    parser.add_argument('-cv', '--cert-validity', help="Certificate validity in minutes", type=int, default=1000, dest='certificate_validity')
    parser.add_argument('-cr', '--cert-renew-backoff', help="Max renewal backoff time before certificate expiration in minutes", type=int, default=100, dest='certificate_renew_backoff')
    parser.add_argument('-cs', '--cert-size', help="Certificate size in bytes", type=int, default=256, dest='certificate_size')
    parser.add_argument('-d', '--duration', help="Total duration of simulation in minutes", type=int, default=20000, dest='duration')
    parser.add_argument('-m', '--mode', help="Mode (0,1). Mode 0 instantiates 1 more node every minute. Mode 1 instantiates all nodes at startup", type=int, default=0, dest='mode')
    parser.add_argument('-o', '--output-file', help="Path of the output file on which the data should be saved in csv format", type=str, default="sim_output.csv", dest='output')

    args = argv[1:]
    args = parser.parse_args(args)
    return args


if __name__ == '__main__':
    main(parse_args())
