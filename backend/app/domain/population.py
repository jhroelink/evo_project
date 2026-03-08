from domain.organism import Organism
from domain.environment import Environment
from domain.trait_system import TraitSystem

class Population:
    def __init__(self, organisms: list):
        self.organisms = organisms
        self.generation = 0

    def evaluate(self, environment: Environment, trait_system: TraitSystem):
        for organism in self.organisms:
            organism.evaluate_fitness(environment, trait_system)

        