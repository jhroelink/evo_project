from domain.genome import Genome
from domain.environment import Environment
from domain.trait import Trait

class TraitSystem:
    def __init__(self, traits: list):
        self.traits = traits

    def evaluate(self, genome: Genome, environment: Environment):
        total_fitness = 0
        for trait in self.traits:
            phenotype_value = trait.phenotype(genome)
            total_fitness += trait.fitness(phenotype_value, environment)
        return total_fitness