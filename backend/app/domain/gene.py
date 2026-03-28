import random
import numpy as np

class Gene:
    def __init__(self, name: str, value: float, mutation_rate: float):
        self.name = name
        self.value = value
        self.mutation_rate = mutation_rate

    def mutate(self):
        if random.random() < self.mutation_rate:
            self.value *= np.random.normal(1.0, 0.05)
            self.value = max(0.0, min(self.value, 10.0))
            
    def copy(self):
        return Gene(self.name, self.value, self.mutation_rate)