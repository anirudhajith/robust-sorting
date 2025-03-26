import random
import comparator.base as base

class Uniform(base.Comparator):
    def __init__(self, width):
        self.width = width # width of the uniform distribution (half of the range)

    def compare(self, x, y):
        return random.uniform(x - self.width, x + self.width) - random.uniform(y - self.width, y + self.width)
    
    def get_sigma(self):
        # The standard deviation of a uniform distribution is width / sqrt(3)
        return self.width / (3 ** 0.5)