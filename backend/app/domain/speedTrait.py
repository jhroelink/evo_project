class SpeedTrait(Trait):

    def __init__(self):
        super().__init__("speed")

    def phenotype(self, genome):
        """
        Convert gene values to phenotype value
        """
        return genome.get_trait("speed")
    
    def fitness(self, genome, environment):
        speed = self.phenotype(genome)
        return speed * environment.predator_pressure