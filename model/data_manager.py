import csv


class DataManager:
    def __init__(self, output_path):
        self.out_file = open(output_path, mode='w', newline='')
        fieldnames = ['sim_time', 'nodes', 'services', 'generated_traffic_B', 'average_traffic_Bps']
        self.writer = csv.DictWriter(self.out_file, fieldnames=fieldnames)
        self.writer.writeheader()

    def log_data(self, time, nodes, services_per_node, generated_traffic, traffic_per_second):
        row = dict()
        row['sim_time'] = time
        row['nodes'] = nodes
        row['services'] = services_per_node
        row['generated_traffic_B'] = generated_traffic
        row['average_traffic_Bps'] = traffic_per_second
        self.writer.writerow(row)
