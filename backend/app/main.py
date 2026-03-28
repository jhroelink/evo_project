# main.py

from domain.gene import Gene
from domain.organism import Organism
from domain.population import Population
from domain.genome import Genome
from domain.trait_system import TraitSystem
from domain.traits.speed_trait import SpeedTrait
from domain.map import Map
from domain.biome import Biome
from domain.simulation import Simulation

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

def init_simulation():
    # Create map
    world_map = Map(10, 10)

    # Create biomes
    biome1 = Biome("High pressure", 5, 10, 10)
    biome2 = Biome("Low Pressure", 20, 1, 1)

    # Fill map
    for x in range(world_map.width):
        for y in range(world_map.height):
            if x % 2 == 0:
                world_map.set_biome(x, y, biome1)
            else:
                world_map.set_biome(x, y, biome2)

    # Create genes
    gene1_speed = Gene("speed", 1.0, 0.05)
    gene2_speed = Gene("speed", 0.2, 0.05)

    # Create genomes
    genome1 = Genome([gene1_speed])
    genome2 = Genome([gene2_speed])

    # Create organisms
    organism1 = Organism(genome1, 2, 3)
    organism2 = Organism(genome2, 6, 7)

    # Create population
    population = Population([organism1, organism2])

    # Trait system
    trait_system = TraitSystem([SpeedTrait()])

    return Simulation(world_map, population, trait_system)


def run_simulation(sim):
    # Evaluate fitness
    for organism in sim.population.organisms:
        organism.evaluate_fitness_organism(sim.world_map, sim.trait_system)
        organism.evaluate_energy_organism(sim.trait_system)

    
    # Print map
    print("\nMap:")
    print_map(sim.world_map, sim.population.organisms)

    # Print results
    print("\nFitness:")
    for i, org in enumerate(sim.population.organisms, start=1):
        print(f"Organism {i} fitness: {org.fitness}")
        print(f"Organism {i} energy:  {org.energy}")


if __name__ == "__main__":
    sim = init_simulation()
    print(len(sim.population.organisms))
    i = 0
    while sim.population.organisms[0].energy > 0 and i < 50:
        run_simulation(sim)
        i += 1