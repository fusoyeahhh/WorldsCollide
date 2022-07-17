from . import free, heap, label, memory, rom, space

space.Space.rom = rom.ROM("../../progressive_randomizer/ff6.smc")
mem = memory.Memory()
print(mem.rom)