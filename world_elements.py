from collections import Iterable


class Location:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class Character:
    def __init__(self, name, description, actions=None):
        self.name = name
        self.description = description
        if actions is not None and not isinstance(actions, Iterable):
            raise TypeError("actions must be iterable")
        self.actions = actions



class PlayableCharacter:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions
