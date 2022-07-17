import importlib
import json
import glob
import pathlib

from ..memory import space, rom, memory
space.Space.rom = rom.ROM("../../progressive_randomizer/ff6.smc")
mem = memory.Memory()
print(mem.rom)

for _mod_name in glob.glob("_wc/instruction/field/y_npc/*.py"):
    mod_name = pathlib.Path(_mod_name).stem
    #if mod_name.startswith("_"):
        #continue
    print(f"--- {mod_name}: {_mod_name} ---")
    try:
        mod = importlib.import_module("." + mod_name, "_wc.instruction.field.y_npc")
    except MemoryError:
        print("One or more objects in module is allocating")
        continue
    #except ImportError as e:
        #print("Module has circular import")
        #print(e)
    #except AttributeError as e:
        #print("Module has circular import")
        #print(e)
    #except ModuleNotFoundError as e:
        #print("Module has missing import")
        #print(e)
    continue

    all_constants = {}
    for obj in vars(mod):
        if not obj.startswith("__"):
            all_constants[obj] = getattr(mod, obj)

    try:
        print(json.dumps(all_constants, indent=2))
    except TypeError:
        print("One or more objects in module is unserializable")

#from .dialogs import dialog, dialogs, free