import numpy as np


class Richard:
    """
    Represents a basic neural network.
    Sources:
        https://databoys.github.io/Feedforward/
        https://www.heatonresearch.com/2017/06/01/hidden-layers.html
    """

    def __init__(self):
        # Set the number of each type of node
        self.input_count = 52 * 2 + 1  # Every possible card that could be in the player's hand
        self.hidden_counts = [52 * 2] * 2  # The number of nodes in each hidden layer
        self.output_count = 52 * 2 + 1  # Every possible card that could be played plus pass
        layer_counts = [self.input_count] + self.hidden_counts + [self.output_count]
        # Start with random numbers for connection weights
        self.network = [np.random.randn(y, x) for x, y in zip(layer_counts[:-1], layer_counts[1:])]

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def feed_forward(self, inputs):
        if self.input_count != len(inputs):
            raise ValueError('Richard network expected ' + str(self.input_count) + ' inputs but got ' + str(len(inputs))
                             + '.')
        current_activations = inputs
        for layer in self.network:
            current_activations = Richard.sigmoid(np.dot(layer, current_activations))
        return current_activations
