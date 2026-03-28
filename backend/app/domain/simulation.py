import random as random


class Simulation:
    def __init__(self, world_map, population, trait_system):
        self.world_map = world_map
        self.population = population
        self.trait_system = trait_system
        self.time = 0

    def step(self):
        new_organisms = []

        for organism in self.population.organisms:

            if not organism.alive:
                continue

            # 1. Age
            organism.age_step()

            # 2. Baseline metabolism
            organism.consume_energy(1)

            # 3. Death by age
            if organism.is_old():
                organism.alive = False
                continue

            # 4. Move
            organism.move(self.world_map, self.trait_system)

            # 5. Eat
            biome = self.world_map.get_biome(organism.x, organism.y)
            organism.eat(biome, self.trait_system)

            # Hide from Predators
            # Camo and visibility can play role
            
            
            # 6. Trait-based energy cost
            # organism.evaluate_energy_organism(self.trait_system)

            # 7. Fitness
            organism.evaluate_fitness_organism(self.world_map, self.trait_system)

            # 8. Reproduction
            if organism.can_reproduce():
                if random.random() < organism.reproduction_probability():
                    child = organism.reproduce()
                    new_organisms.append(child)

        # 9. Add offspring
        self.population.organisms.extend(new_organisms)

        # 10. Remove dead organisms
        self.population.organisms = [
            o for o in self.population.organisms if o.alive
        ]

        self.time += 1