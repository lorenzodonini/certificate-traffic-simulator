import csv


class DataManager:
    def __init__(self, output_path):
        self.out_file = open(output_path, mode='w', newline='')
        fieldnames = ['sim_time', 'nodes', 'services', 'generated_traffic', 'traffic_per_minute']
        self.writer = csv.DictWriter(self.out_file, fieldnames=fieldnames)
        self.writer.writeheader()

    def log_data(self, time, nodes, services_per_node, generated_traffic, traffic_per_minute):
        row = dict()
        row['sim_time'] = time
        row['nodes'] = nodes
        row['services'] = services_per_node
        row['generated_traffic'] = generated_traffic
        row['traffic_per_minute'] = traffic_per_minute
        self.writer.writerow(row)
