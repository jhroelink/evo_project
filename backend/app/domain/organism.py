from domain.genome import Genome
from domain.environment import Environment
from domain.trait import Trait  # or TraitSystem if you have one


class Organism:
    def __init__(self, genome):
        self.genome = genome
        self.age = 0
        self.energy = 100
        self.fitness = 0
        self.alive = True

    def evaluate_fitness(self, environment, trait_system):
        self.fitness = trait_system.evaluate(self.genome, environment)

    def age_step(self):
        self.age += 1

    
    