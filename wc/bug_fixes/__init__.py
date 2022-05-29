from .evade import Evade
from .sketch import Sketch
from .vanish_doom import VanishDoom
from .jump import Jump
from .retort import Retort
from .enemy_damage_counter import EnemyDamageCounter

__all__ = ["BugFixes"]
class BugFixes:
    def __init__(self):
        self.evade = Evade()
        self.sketch = Sketch()
        self.vanish_doom = VanishDoom()
        self.jump = Jump()
        self.retort = Retort()
        self.enemy_damage_counter = EnemyDamageCounter()
