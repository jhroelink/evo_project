from domain.trait import Trait
from domain.genome import Genome
from domain.biome import Biome
from domain.organism import Organism

class SpeedTrait(Trait):

    def __init__(self):
        super().__init__("speed", ["speed"])

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        return genome.get_trait("speed")
    
    def fitness(self, phenotype_value, biome: Biome):
        return phenotype_value * biome.predator_pressure
    
    def energy_cost(self, phenotype_value):        
        energy_cost = phenotype_value * 0.5
        return energy_cost