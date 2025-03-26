import random
import comparator.base as base

class Gaussian(base.Comparator):
    def __init__(self, sigma):
        self.sigma = sigma

    def compare(self, x, y):
        return random.gauss(x, self.sigma) - random.gauss(y, self.sigma)
    
    def get_sigma(self):
        return self.sigma