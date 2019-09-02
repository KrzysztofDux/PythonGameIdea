from collections import Iterable
from itertools import chain


class CommandManager:

    def __init__(self, main_char, scene):
        if not isinstance(main_char.actions, Iterable) or not isinstance(scene.actions, Iterable):
            raise TypeError("actions must be iterable")
        self.available_commands = chain(main_char.actions, scene.actions)
        for character in scene.characters:
            if character.actions is not None:
                self.available_commands = chain(self.available_commands, character.actions)


class Command:

    def __init__(self, name, execute, **kwargs):
        if not callable(execute):
            raise TypeError("execute must be callable")
        self.execute = execute
        self.name = name
        self.params = kwargs

    def execute(self):
        pass

