from .space import Space
from .free import free

class Memory:
    def __init__(self):
        # TODO: rewrite this to not do module level manipulations
        self.rom = Space.rom
        free()

    def write(self, output_file, no_rom_output=False):
        #import args
        #if not args.no_rom_output:
            #self.rom.write(args.output_file)
        if not no_rom_output:
            self.rom.write(output_file)
