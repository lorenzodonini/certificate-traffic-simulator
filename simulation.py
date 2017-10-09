#!/usr/local/bin/python3

from model import network_manager
from model.data_manager import DataManager
from model.smart_space import SmartSpace
from model.node import Node
from model.service import Service
from sys import argv
import argparse
import random


class Simulation:
    def __init__(self, args):
        self.network_manager = network_manager.NetworkManager()
        self.config = args
        self.space = None
        self.sim_duration = args.duration
        self.hide_idle_ticks = args.hide
        self.logger = DataManager(args.output)
        self.offline_nodes = {}
        certificate_config = {'validity': args.certificate_validity,
                              'expiration_backoff': args.certificate_renew_backoff,
                              'size': args.certificate_size}
        self.__setup__(certificate_config)

    def __setup__(self, certificate_config):
        self.space = SmartSpace(0, certificate_config)
        if self.config.node_interval == 0:
            # Instantiate all nodes
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
        n = Node(len(space.nodes), space)
        space.add_node(n)
        if self.config.service_interval == 0:
            # Instantiate all services for this node
            for k in range(0, self.config.services):
                self.__instantiate_service__(n, True)

    def __instantiate_service__(self, n, initial_certificate=False):
        if len(n.services) >= self.config.services:
            return
        request_size = sum([random.randint(1, self.config.certificate_request) * x for x in range(1, random.randint(1, self.config.access_groups))])
        s = Service(len(n.services), 'Service' + str(len(n.services)), request_size)
        if initial_certificate:
            # Generate initial certificate
            certificate = self.space.slca.issue_certificate(n, s, network_manager.NetworkManager().current_time)
            if not certificate:
                raise ValueError("Cannot set empty certificate for service " + str(s))
            s.certificate = certificate
        # Deploy service on node
        n.deploy_service(s, self.network_manager.current_time)

    def __update_nodes__(self, space):
        for n_id, (n, reboot_time) in list(self.offline_nodes.items()):
            if network_manager.NetworkManager().current_time >= reboot_time:
                n.available = True
                del self.offline_nodes[n_id]
        if self.config.node_interval > 0 and (self.network_manager.current_time % self.config.node_interval) == 0:
            self.__instantiate_node__(space)

    def __update_services__(self, n):
        if self.config.service_interval > 0 and (self.network_manager.current_time % self.config.service_interval) == 0:
            self.__instantiate_service__(n)

    def __handle_churn__(self, n):
        # Randomly cause node churn
        if n.id not in self.offline_nodes and random.randint(1, self.config.duration) <= self.config.duration - (
                self.config.duration / 100 * self.config.node_availability):
            n.available = False
            self.offline_nodes[n.id] = (n, self.network_manager.current_time + random.randint(1, self.config.churn_time))

    def __log_data__(self, space, total_services, traffic, total_traffic):
        if self.logger:
            if self.hide_idle_ticks and traffic == 0:
                return
            self.logger.log_data(self.network_manager.current_time,
                                 len(space.nodes),
                                 total_services,
                                 traffic,
                                 (total_traffic / self.network_manager.current_time),
                                 self.config.certificate_validity)

    def run(self):
        if not self.space:
            raise RuntimeError("Simulation was not setup")

        traffic = 0
        self.network_manager.monitored_traffic = dict()
        print("Simulation started!")
        while self.__tick__():
            self.__update_nodes__(self.space)
            total_services = 0
            for n in self.space.nodes:
                self.__handle_churn__(n)
                self.__update_services__(n)
                n.run_services()
                total_services += len(n.services)
            # Update generated traffic
            total_traffic = self.network_manager.total_generated_traffic()
            traffic = total_traffic - traffic
            self.__log_data__(self.space, total_services, traffic, total_traffic)
            traffic = total_traffic

        print("Simulation ended")


def main(args):
    sim = Simulation(args)
    sim.run()


def parse_args():
    parser = argparse.ArgumentParser(description='Parse simulation parameters')
    parser.add_argument('-n', '--nodes', help="Amount of nodes used for the simulation", type=int, default=50, dest='nodes')
    parser.add_argument('-ni', '--node-interval', help="Interval in seconds between the spawning of a node and the next one", type=int, default=0, dest='node_interval')
    parser.add_argument('-na', '--node-availability', help="Percentage availability of a node", type=float, default=99.999, dest='node_availability')
    parser.add_argument('-nc', '--node-churn-time', help="Maximum churn time of a node", type=int, default=1000, dest="churn_time")
    parser.add_argument('-s', '--services', help="Amount of services per node for the simulation", type=int, default=20, dest='services')
    parser.add_argument('-si', '--service-interval', help="Interval in seconds between the spawning of a service and the next one", type=int, default=0, dest='service_interval')
    parser.add_argument('-cv', '--cert-validity', help="Certificate validity in seconds", type=int, default=1000, dest='certificate_validity')
    parser.add_argument('-cr', '--cert-renew-backoff', help="Max renewal backoff time before certificate expiration in seconds", type=int, default=200, dest='certificate_renew_backoff')
    parser.add_argument('-cs', '--cert-size', help="Certificate size in bytes", type=int, default=734, dest='certificate_size')
    parser.add_argument('-cp', '--cert-request-payload', help="Payload size of a certificate renewal request for a single group", type=int, default=200, dest='certificate_request')
    parser.add_argument('-cg', '--cert-access-groups', help="Maximum amount of groups that a service on a node belongs to", type=int, default=4, dest='access_groups')
    parser.add_argument('-d', '--duration', help="Total duration of simulation in seconds", type=int, default=100000, dest='duration')
    parser.add_argument('-o', '--out', help="Path of the output file on which the data should be saved in csv format", type=str, default="sim_output.csv", dest='output')
    parser.add_argument('-i', '--hide-idle', help="Hides moments in time with no activity, only logging the ones with active traffic", type=bool, default=True, dest='hide')

    args = argv[1:]
    args = parser.parse_args(args)
    return args


if __name__ == '__main__':
    main(parse_args())
