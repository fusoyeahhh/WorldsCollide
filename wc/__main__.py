from . import args
from . import log

from .memory.memory import Memory
from .data.data import Data
from .event.events import Events
from .menus.menus import Menus
from .battle import Battle
from .settings import Settings
from .bug_fixes import BugFixes


def main():
    memory = Memory()
    data = Data(memory.rom, args)

    events = Events(memory.rom, args, data)
    menus = Menus(data.characters, data.dances)
    battle = Battle()
    settings = Settings()
    bug_fixes = BugFixes()

    data.write()
    memory.write()

if __name__ == '__main__':
    main()
