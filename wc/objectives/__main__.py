import importlib
import json
import glob
import pathlib

from ..memory import space, rom, memory
space.Space.rom = rom.ROM("../../progressive_randomizer/ff6.smc")
mem = memory.Memory()
print(mem.rom)

mod_names = glob.glob("_wc/objectives/conditions/*.py")

for _mod_name in mod_names:
    mod_name = pathlib.Path(_mod_name).stem
    if mod_name.startswith("_"):
        continue
    print(f"--- {mod_name} : {_mod_name} ---")
    mod = importlib.import_module("." + mod_name, "_wc.objectives.conditions")
    continue

    all_constants = {}
    for obj in vars(mod):
        if not obj.startswith("__"):
            all_constants[obj] = getattr(mod, obj)

    try:
        print(json.dumps(all_constants, indent=2))
    except TypeError:
        print("One or more objects in module is unserializable")

mod_names = glob.glob("_wc/objectives/*.py")

for _mod_name in mod_names:
    mod_name = pathlib.Path(_mod_name).stem
    print(f"--- {mod_name} : {_mod_name} ---")
    mod = importlib.import_module("." + mod_name, "_wc.objectives")
    all_constants = {}
    for obj in vars(mod):
        if not obj.startswith("__"):
            all_constants[obj] = getattr(mod, obj)

    try:
        print(json.dumps(all_constants, indent=2))
    except TypeError:
        print("One or more objects in module is unserializable")