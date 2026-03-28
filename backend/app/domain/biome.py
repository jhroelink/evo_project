class Biome:
    def __init__(self, name, food_density, predator_pressure, visibility) -> None:
        self.name = name
        # 0 to 1
        self.food_density = food_density
        self.predator_pressure = predator_pressure
        self.visibility = visibility

    def get_food_density(self):
        return self.food_density
    
    def get_predator_pressure(self):
        return self.predator_pressure
    
    def get_visibility(self):
        return self.visibility