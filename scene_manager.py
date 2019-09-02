from collections import Iterable
from user_interface import CommandManager


class Scene:

    def __init__(self, location, characters, actions):
        self.title = location.title
        self.location = location
        if actions is not None and not isinstance(actions, Iterable):
            raise TypeError("actions must be iterable")
        self.actions = actions
        if not isinstance(characters, Iterable):
            raise TypeError("actions must be iterable")
        self.characters = characters


class SceneManager:

    instance = None

    def __init__(self, main_char, scene_queue):
        if not isinstance(scene_queue, Iterable) and scene_queue is not None:
            raise TypeError("scene queue must be iterable")
        self.scene_queue = scene_queue
        self.current_scene = 0
        self.main_char = main_char
        self.available_commands = []
        self.command_manager = None


    def next_scene(self):
        self.current_scene += 1

    def previous_scene(self):
        self.current_scene -= 1

    def play_scene(self):
        active_scene = self.scene_queue[self.current_scene]
        self.command_manager = CommandManager(self.main_char, active_scene)
        self.available_commands = []
        self.present_scene(active_scene)

    def execute_action(self, i):
        self.available_commands[i]()

    def present_scene(self, scene):
        print(scene.location.title)
        print(scene.location.description)
        if len(scene.characters) > 1:
            print("there are:")
        else:
            print("there is")
        for character in scene.characters:
            print(character.name, character.description)
        for i, command in enumerate(self.command_manager.available_commands):
            print(f"{i+1}. {command.title}: {command.description}")
            self.available_commands.append(command.execute)


def get_scene_manager(main_char=None, scene_queue=None):
    if SceneManager.instance is None:
        SceneManager.instance = SceneManager(main_char, scene_queue)
    if main_char is not None:
        SceneManager.instance.main_char = main_char
    if scene_queue is not None:
        SceneManager.instance.scene_queue = scene_queue
    return SceneManager.instance
