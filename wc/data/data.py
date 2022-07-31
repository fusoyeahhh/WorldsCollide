from . import (
    dialogs,
    metamorph_groups,
    swdtechs,
    blitzes,
    rages,
    dances,
    steal,
    magiteks,
    coliseum,
    map,
)
from .character import characters
from .enemy import enemies
from .lore import lores
from .spell import spells
from .item import items
from .esper import espers
from .shop import shops


class Data:
    def __init__(self, rom, args):
        self.dialogs = dialogs

        self.spells = spells.Spells(rom, args)
        self.spells.mod()

        self.characters = characters.Characters(rom, args, self.spells)
        self.characters.mod()

        self.items = items.Items(rom, args, self.dialogs, self.characters)
        self.items.mod()

        self.metamorph_groups = metamorph_groups.MetamorphGroups(rom)
        self.metamorph_groups.mod()

        self.maps = map.Maps(rom, args, self.items)
        self.maps.mod(self.characters)

        self.enemies = enemies.Enemies(rom, args)
        self.enemies.mod(self.maps)

        self.swdtechs = swdtechs.SwdTechs(rom, args, self.characters)
        self.swdtechs.mod()

        self.blitzes = blitzes.Blitzes(rom, args, self.characters)
        self.blitzes.mod()

        self.lores = lores.Lores(rom, args, self.characters)
        self.lores.mod()

        self.rages = rages.Rages(rom, args, self.enemies)
        self.rages.mod()

        self.dances = dances.Dances(rom, args, self.characters)
        self.dances.mod()

        self.steal = steal.Steal(rom, args)
        self.steal.mod()
        self.magiteks = magiteks.Magiteks(rom, args)
        self.magiteks.mod()

        self.espers = espers.Espers(rom, args, self.spells, self.characters)
        self.espers.mod(self.dialogs)

        self.shops = shops.Shops(rom, args, self.items)
        self.shops.mod()

        self.coliseum = coliseum.Coliseum(rom, args, self.enemies, self.items)
        self.coliseum.mod()

    def write(self):
        self.dialogs.write()
        self.characters.write()
        self.items.write()
        self.metamorph_groups.write()
        self.maps.write()
        self.enemies.write()
        self.spells.write()
        self.swdtechs.write()
        self.blitzes.write()
        self.lores.write()
        self.rages.write()
        self.dances.write()
        self.steal.write()
        self.magiteks.write()
        self.espers.write()
        self.shops.write()
        self.coliseum.write()