# TODO: improve 

from ai import *

class HealthyAgent(Agent):
    def __init__(self):
        super().__init__(self, [self.eat, self.sleep])  # the environment is itself

        # environment stuff
        self.satiety = self.energy = 0

    def eat(self):
        self.satiety += 1

    def sleep(self):
        self.energy += 1

    # since this *is* the environment, make sure to duck-implement |score()|
    def score(self):
        return agent.satiety**2 + agent.energy*2

agent = HealthyAgent()
for _ in range(100):
    agent.perform_best(100)
    print(agent.satiety, agent.energy)
