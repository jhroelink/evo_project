class Genome:
    def __init__(self, genes):
        self.genes = {gene.name: gene for gene in genes}

    def mutate(self):
        for gene in self.genes.values():
            gene.mutate()

    def get_trait(self, name):
        return self.genes[name].value