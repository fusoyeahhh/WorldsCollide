import random

from ..constants.commands import *
from .. import objectives

from .character import characters_asm
from .character import Character

#import args

#from log import section, format_option

class Commands:
    def __init__(self, characters):
        self.characters = characters

    def mod_commands(self):
        command_set = set(name_id[name] for name in RANDOM_POSSIBLE_COMMANDS)
        command_list = list(command_set)

        allowed_commands = command_set | set([name_id["Fight"], RANDOM_COMMAND, RANDOM_UNIQUE_COMMAND, NONE_COMMAND])

        # if morph was explicitly selected remove from available command list
        morph_id = name_id["Morph"]
        for command in args.character_commands:
            if command == morph_id:
                command_list.remove(morph_id)

        for exclude_command in args.random_exclude_commands:
            try:
                command_set.discard(exclude_command)
                command_list.remove(exclude_command)
            except ValueError:
                pass

        # if suplex a train condition exists, guarantee blitz
        blitz_id = name_id["Blitz"]
        if objectives.suplex_train_condition_exists and blitz_id not in args.character_commands:
            # try to replace a random "Random" or "Random Unique" command with Blitz (even if blitz in excluded commands)
            possible_indices = []
            for index, command in enumerate(args.character_commands):
                if command == RANDOM_COMMAND or command == RANDOM_UNIQUE_COMMAND:
                    possible_indices.append(index)

            if not possible_indices:
                # suplex a train explicitly picked and all commands explicitly picked (but none are blitz)
                # force a random command to be blitz instead
                possible_indices = list(range(len(args.character_commands)))

            random_index = random.choice(possible_indices)
            args.character_commands[random_index] = blitz_id
            command_set.discard(blitz_id)

        for index, command in enumerate(args.character_commands):
            if command not in allowed_commands and (index != 0 or command != name_id["Morph"]) and (index != 12 or command != name_id["Leap"]):
                raise ValueError(f"Invalid character command {command}")
            elif command == RANDOM_COMMAND:
                args.character_commands[index] = random.choice(command_list)
                if args.character_commands[index] == morph_id:
                    command_list.remove(morph_id) # only one character gets morph
            elif command == NONE_COMMAND:
                args.character_commands[index] = name_id["None"]

            command_set.discard(args.character_commands[index])

        for index, command in enumerate(args.character_commands):
            if command == RANDOM_UNIQUE_COMMAND:
                args.character_commands[index] = random.choice(tuple(command_set))
                command_set.discard(args.character_commands[index])

        # apply the commands to the characters
        for index in range(len(args.character_commands[ : -2])):
            self.characters[index].commands[1] = args.character_commands[index]
        self.characters[Character.GAU].commands[0] = args.character_commands[-2] # rage
        self.characters[Character.GAU].commands[1] = args.character_commands[-1] # leap

    def shuffle_commands(self):
        commands = []
        for index in range(len(COMMAND_OPTIONS) - 1):
            commands.append(self.characters[index].commands[1])
        commands.append(self.characters[Character.GAU].commands[0]) # rage

        random.shuffle(commands)

        for index in range(len(COMMAND_OPTIONS) - 1):
            self.characters[index].commands[1] = commands[index]
        self.characters[Character.GAU].commands[0] = commands[-1] # rage

    def mod(self):
        if args.commands:
            self.mod_commands()
        if args.shuffle_commands:
            self.shuffle_commands()

        if args.commands or args.shuffle_commands:
            characters_asm.update_morph_character(self.characters[ : Character.CHARACTER_COUNT])

    def log(self):
        lcolumn = []
        for index, option in enumerate(COMMAND_OPTIONS[ : -2]):
            lcolumn.append(format_option(option, id_name[self.characters[index].commands[1]]))
        lcolumn.append(format_option(COMMAND_OPTIONS[-2], id_name[self.characters[Character.GAU].commands[0]]))
        lcolumn.append(format_option(COMMAND_OPTIONS[-1], id_name[self.characters[Character.GAU].commands[1]]))

        section("Commands", lcolumn, [])
