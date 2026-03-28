from domain.trait import Trait
from domain.genome import Genome
from domain.biome import Biome

class CamoTrait(Trait):

    def __init__(self):
        super().__init__("camouflage", ["camouflage"])

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        return genome.get_trait("camouflage")
    
    def fitness(self, phenotype_value, biome):
        energy_cost = phenotype_value * 0.5
        organism.consume_energy(energy_cost)
        return phenotype_value * biome.get_visibility() * biome.get_predator_pressure()
    
    def energy_cost(self, phenotype_value):        
        energy_cost = phenotype_value * 0.5
        return energy_cost