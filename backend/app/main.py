# main.py

from domain.gene import Gene
from domain.organism import Organism
from domain.population import Population
from domain.genome import Genome
from domain.environment import Environment
from domain.trait_system import TraitSystem
from domain.traits.speed_trait import SpeedTrait

def run_simulation():
    # Create genomes
    gene_speed = Gene("speed", 1.0, 0.05)
    genome1 = Genome([gene_speed])
    genome2 = Genome([Gene("speed", 0.2, 0.05)])

    # Create organisms
    organism1 = Organism(genome1)
    organism2 = Organism(genome2)

    # Create population
    population = Population([organism1, organism2])

    # Create environment
    environment = Environment(food_density=10.0, predator_pressure=10.0)

    # Create trait system
    trait_system = TraitSystem([SpeedTrait()])

    # Evaluate population fitness
    population.evaluate(environment, trait_system)

    # Print results
    for i, org in enumerate(population.organisms, start=1):
        print(f"Organism {i} fitness: {org.fitness}")

if __name__ == "__main__":
    run_simulation()