class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 2D grid of biomes
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def set_biome(self, x, y, biome):
        self.grid[y][x] = biome

    def get_biome(self, x, y):
        return self.grid[y][x]