import importlib
import json

for mod_name in ["blitzes", "commands", "dances", "entities", "espers", "gates",
                 "items", "lores", "rages", "spells", "status_effects", "swdtechs"]:
    mod = importlib.import_module("." + mod_name, "_wc.constants")
    all_constants = {}
    for obj in vars(mod):
        if not obj.startswith("__"):
            all_constants[obj] = getattr(mod, obj)

    print(f"--- {mod_name} ---")
    try:
        print(json.dumps(all_constants, indent=2))
    except TypeError:
        print("One or more objects in module is unserializable")

for mod_name in ["condition_bits", "conditions", "results"]:
    mod = importlib.import_module(".objectives." + mod_name, "_wc.constants")
    all_constants = {}
    for obj in vars(mod):
        if not obj.startswith("__"):
            all_constants[obj] = getattr(mod, obj)

    print(f"--- {mod_name} ---")
    try:
        print(json.dumps(all_constants, indent=2))
    except TypeError:
        print("One or more objects in module is unserializable")
