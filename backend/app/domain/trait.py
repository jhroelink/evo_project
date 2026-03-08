from domain.genome import Genome
from domain.environment import Environment

class Trait:

    def __init__(self, name, gene_names):
        self.name = name
        self.gene_names = gene_names

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        raise NotImplementedError

    def fitness(self, phenotype_value, environment):
        """
        Compute fitness contribution
        """
        raise NotImplementedError