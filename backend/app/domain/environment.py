class Environment:
    def __init__(self, food_density, predator_pressure, visibility):
        self.food_density = food_density
        self.predator_pressure = predator_pressure
        self.visibility = visibility
        
    def update(self):
        pass

    def compute_fitness(self):
        pass
    