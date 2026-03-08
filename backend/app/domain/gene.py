import random
import numpy as np

class Gene:
    def __init__(self, name: str, value: float, mutation_rate: float):
        self.name = name
        self.value = value
        self.mutation_rate = mutation_rate

    def mutate(self):
        if random.random() < self.mutation_rate:
            self.value += np.random.normal(0, 0.1)
    