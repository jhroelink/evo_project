from domain.gene import Gene

class Genome:
    def __init__(self, genes):
        self.genes = {gene.name: gene for gene in genes}

    def mutate(self):
        new_genes = []

        for gene in self.genes.values():
            new_gene = gene.copy()
            new_gene.mutate()
            new_genes.append(new_gene)

        return Genome(new_genes)

    def get_trait(self, name):
        return self.genes[name].value