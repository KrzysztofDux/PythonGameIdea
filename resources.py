from scene_manager import Scene, get_scene_manager
from gameplay_mechanics import Action
from world_elements import Location, Character, PlayableCharacter


def muscle_flexing():
    print("HAYYYAH~~~")


main_char = PlayableCharacter("Great hero", "He's so strong!",
                              [Action("Flex your muscles", "Because they're big!", muscle_flexing)])

locations = {
    "forest_0": {"title": "Las", "desc": "There's a lot of mushrooms here."},
    "desert_0": {"title": "Desert", "desc": "It's hot in here!"},
}


def get_location(key):
    return Location(locations[key]["title"], locations[key]["desc"])


characters = [
    {"name": "Little Red Riding Hood", "desc": "She's going to visit her grandmother"},
    {"name": "Fenek the fox", "desc": "His ears are so cool!"}
]


def get_character(number):
    return Character(characters[number]["name"], characters[number]["desc"])


actions = [
    {"title": "Pick up mushrooms", "desc": "Because it's nice and healthy.",
     "action": lambda: print("A lot of mushrooms!")},
    {"title": "Enough of the forest, let's get out of here", "desc": "It's to moist in here.",
     "action": get_scene_manager().next_scene},
    {"title": "Sunbathe", "desc": "Be careful not get a sunburn!",
     "action": lambda: print("Waaarm B~)")},
    {"title": "Gosh darn, it's too hot!", "desc": "Time to get back!",
     "action": get_scene_manager().previous_scene},
]


def get_action(number):
    return Action(actions[number]["title"], actions[number]["desc"], actions[number]["action"])


first_scene = Scene(get_location("forest_0"), [get_character(0)], [get_action(0), get_action(1)])
second_scene = Scene(get_location("desert_0"), [get_character(1)], [get_action(2), get_action(3)])

scenes = [first_scene, second_scene]
