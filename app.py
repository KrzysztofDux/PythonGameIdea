from scene_manager import get_scene_manager
from resources import main_char, scenes


def start():

    scene_manager = get_scene_manager(main_char, scenes)
    game_running = True

    while game_running:
        current_scene = scene_manager.current_scene
        scene_manager.play_scene()
        while current_scene == scene_manager.current_scene:
            inp = int(input("Action Number: ")) - 1
            if inp == -1:
                game_running = False
                break
            scene_manager.execute_action(inp)

    print("Closing...")


if __name__ == '__main__':
    start()
