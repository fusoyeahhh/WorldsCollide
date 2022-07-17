from ..ability_data import AbilityData
from .. import text

NAME_SIZE = 10

class Lore(AbilityData):
    def __init__(self, id, name_data, ability_data):
        super().__init__(id, ability_data)

        self.id = id
        self.name = text.get_string(name_data, text.TEXT2).rstrip('\0')

    def name_data(self):
        data = text.get_bytes(self.name, text.TEXT2)
        data.extend([0xff] * (NAME_SIZE - len(data)))
        return data

    def get_name(self):
        return self.name.strip('\0')

    def print(self):
        print(f"{self.id} {self.get_name()}")
