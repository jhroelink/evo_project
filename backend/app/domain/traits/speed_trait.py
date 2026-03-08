from domain.trait import Trait
from domain.genome import Genome
from domain.environment import Environment

class SpeedTrait(Trait):

    def __init__(self):
        super().__init__("speed", ["speed"])

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        return genome.get_trait("speed")
    
    def fitness(self, phenotype_value, environment):
        # speed = self.phenotype(genome)
        return phenotype_value * environment.predator_pressure