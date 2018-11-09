"""
A generalized goal-based agent system that, instead of using mathematical models, uses trial and error.
This property makes it very versatile to fit many situations.
"""

import copy
import random

# TODO: detect actions with action decorator

class Agent:
    """The entity that does actions to improve the environment"""

    def __init__(self, environment, actions):
        self.environment = environment
        self.actions = actions

    def perform_best(self, future_projections=1, environment=None):
        """Find action with the best outcome and perform it

        Find best action by sandboxing each action, measuring its impact on the environment, and selecting
        one of those with the highest scoring sandboxed environment.
        """

        if environment is None: environment = self.environment
        max_actions = []    # array to randomly choose from equal scores
        max_score = None

        for action in self.actions:
            score = 0   # sum of all future projections
            future_self = copy.deepcopy(self)   # will copy self.environment as well
            getattr(future_self, action.__name__)()     # bound to future_self, instead of self

            for _ in range(future_projections):
                future_self.perform_random()
                score += future_self.environment.score()

            if max_score is None or score >= max_score:
                max_actions, max_score = [action], score
            elif score == max_score:
                max_actions.append(action)

        action = random.choice(max_actions)
        action()    # reflexive actions only right now
        return action

    def perform_random(self, environment=None):
        if environment is None: environment = self.environment

        action = random.choice(self.actions)
        action()
        return action

class Environment:
    """For these purposes, the target of the agent"""

    def score():
        """Score the environment, with higher numbers obviously being better"""

        raise NotImplementedError()
