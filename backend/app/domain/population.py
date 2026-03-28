from domain.organism import Organism
from domain.biome import Biome
from domain.trait_system import TraitSystem

class Population:
    def __init__(self, organisms: list):
        self.organisms = organisms
        self.generation = 0

    def evaluate_fitness_population(self, biome: Biome, trait_system: TraitSystem):
        for organism in self.organisms:
            organism.evaluate_fitness(biome, trait_system)

    def evaluate_energy_costs_population(self, biome: Biome, trait_system: TraitSystem):
        for organism in self.organisms:
            organism.evaluate_energy_costs(trait_system)