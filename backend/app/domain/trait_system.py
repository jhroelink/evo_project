from domain.genome import Genome
from domain.biome import Biome
from domain.trait import Trait

class TraitSystem:
    def __init__(self, traits: list):
        self.traits = traits

    def evaluate_fitness_traits(self, genome: Genome, biome: Biome):
        total_fitness = 0
        for trait in self.traits:
            phenotype_value = trait.phenotype(genome)
            total_fitness += trait.fitness(phenotype_value, biome)
        return total_fitness
    
    def evaluate_energy_costs_traits(self, genome: Genome):
        total_energy_cost = 5
        for trait in self.traits:
            phenotype_value = trait.phenotype(genome)
            total_energy_cost += trait.energy_cost(phenotype_value)
        return total_energy_cost