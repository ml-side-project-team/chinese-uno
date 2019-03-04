import numpy as np


class RichardEvolve:

    def __init__(self, mutation_rate=0.005):
        self.mutation_rate = mutation_rate

    def breed_networks(self, mom, dad):
        network = []
        for layer in range(len(mom)):
            new_layer = []
            for weight in range(len(mom[layer])):
                new_layer.append(np.random.choice([mom[layer][weight], dad[layer][weight]]))
            network.append(new_layer)
        return network

    def mutate_network(self, network):
        for layer in range(len(network)):
            for weight in range(len(network[layer])):
                if np.random.rand() <= self.mutation_rate:
                    network[layer][weight] = np.random.randn()
