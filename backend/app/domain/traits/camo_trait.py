from domain.trait import Trait
from domain.genome import Genome
from domain.environment import Environment

class CamoTrait(Trait):

    def __init__(self):
        super().__init__("camouflage", ["camouflage"])

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        return genome.get_trait("camouflage")
    
    def fitness(self, phenotype_value, environment):
        return phenotype_value * environment.visibility * environment.predator_pressure