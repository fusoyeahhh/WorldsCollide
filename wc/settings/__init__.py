from ..memory.space import Reserve
from ..instruction import asm

from .auto_sprint import AutoSprint
from .scan_all import ScanAll
from .random_rng import RandomRNG
from .permadeath import Permadeath
from .y_npc import YNPC

__all__ = ["Settings"]
class Settings:
    def __init__(self):
        self.auto_sprint = AutoSprint()
        self.scan_all = ScanAll()
        self.random_rng = RandomRNG()
        self.permadeath = Permadeath()
        self.y_npc = YNPC()

        # do not auto load save file after game over
        space = Reserve(0x00c4fe, 0x00c500, "load where to return to after game over", asm.NOP())
        space.write(
            asm.LDA(0xff, asm.IMM8), # do not auto load save file after game over
        )

        space = Reserve(0x2e8393, 0x2e8393, "wor overworld song")
        space.write(0x4c) # change from dark world to searching for friends
