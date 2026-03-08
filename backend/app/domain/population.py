from domain.organism import Organism  # Organism class
from domain.environment import Environment       # Environment class
from domain.trait import Trait            # Base Trait class or TraitSystem

class Population:
    def __init__(self, organisms: list):
        self.organisms = organisms
        self.generation = 0

    def evaluate(self, environment, trait_system):
        for organism in self.organisms:
            organism.evaluate_fitness(environment, trait_system)

        