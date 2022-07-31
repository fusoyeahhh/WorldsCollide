import random

from ._objective_condition import *

class Condition(ObjectiveCondition):
    NAME = "Dragons"
    def __init__(self, min_count, max_count):
        self.count = random.randint(min_count, max_count)
        super().__init__(ConditionType.EventWord, event_word.DRAGONS_DEFEATED, self.count)

    def __str__(self):
        return super().__str__(self.count)