# main.py

from domain.gene import Gene
from domain.organism import Organism
from domain.population import Population
from domain.genome import Genome
from domain.trait_system import TraitSystem
from domain.traits.speed_trait import SpeedTrait
from domain.map import Map
from domain.environment import Environment


def print_map(map_obj, organisms):
    """
    Simple ASCII map showing organism positions.
    """
    grid = [["." for _ in range(map_obj.width)] for _ in range(map_obj.height)]

    for org in organisms:
        if org.alive:
            grid[org.y][org.x] = "O"

    for row in grid:
        print(" ".join(row))


def run_simulation():

    # Create map
    world_map = Map(10, 10)

    # Fill map with same biome for now
    for x in range(world_map.width):
        for y in range(world_map.height):
            world_map.set_biome(x, y, Environment(food_density=10.0, predator_pressure=10.0))

    # Create genomes
    gene_speed = Gene("speed", 1.0, 0.05)
    genome1 = Genome([gene_speed])
    genome2 = Genome([Gene("speed", 0.2, 0.05)])

    # Create organisms with positions
    organism1 = Organism(genome1, 2, 3)
    organism2 = Organism(genome2, 6, 7)

    # Create population
    population = Population([organism1, organism2])

    # Create trait system
    trait_system = TraitSystem([SpeedTrait()])

    # Evaluate fitness
    for organism in population.organisms:
        organism.evaluate_fitness(world_map, trait_system)

    # Print map
    print("\nMap:")
    print_map(world_map, population.organisms)

    # Print results
    print("\nFitness:")
    for i, org in enumerate(population.organisms, start=1):
        print(f"Organism {i} fitness: {org.fitness}")


if __name__ == "__main__":
    run_simulation()