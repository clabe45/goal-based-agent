import random

from ai import *

class FoodAgent(Agent):
    def __init__(self, environment):
        super().__init__(environment, [self.farm, self.advance_tech, self.give])
        self.food = 0
        self.farming_tech = 1

    def farm(self):
        self.food += self.farming_tech

    def advance_tech(self):
        self.farming_tech += 1

    def give(self):
        """Give food to environment"""

        self.environment.food += (1 - self.environment.corruption) * self.food  # take percentage of food away
        self.food = 0

class Region(Environment):
    def __init__(self):
        self.corruption = 0
        self.food = 0

    def score(self):
        return self.food

# compare agents acting with different foresights
for foresight in range(1, 30+1, 1):
    region = Region()
    region.corruption = random.uniform(0.0, 0.25)   # add random (uncontrollable) factor
    agent = FoodAgent(region)
    for step in range(100):
        agent.perform_best(foresight)
    print(foresight, '=>', '%.1f' % round(region.score(),2))
