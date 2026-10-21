from actions import PopulateWorld, SpawnGrass, SpawnHerbivores, MoveCreatures
from mapp import Map
from map_renderer import show_mappa
import os
import time
from pynput import keyboard


class Simulation:
    def __init__(self) -> None:
        self.counter = 0
        self.pause = False
        self.running = True
        self.mappa = Map()
        self.init_actions = [PopulateWorld()]

        self.turn_actions =[SpawnGrass(), SpawnHerbivores(), MoveCreatures()]

    def next_turn(self) -> None:
        print("-------------------------------")
        for action in self.turn_actions:
            action.execute(self.mappa)
        show_mappa(self.mappa)
        self.counter +=1
        print(f"Ход номер {self.counter}")
        print("-------------------------------")

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.mappa)

        listener = keyboard.Listener(on_press=self.handle_key)
        listener.start()
        try:
            while self.running:
                if not self.pause:
                    os.system("cls" if os.name == "nt" else "clear")
                    self.next_turn()
                    time.sleep(1.5)
                else:
                    time.sleep(0.1)  # Sleep briefly to avoid busy waiting when paused
        finally:
            listener.stop()

    def pause_simulation(self) -> None:
        self.pause = True

    def resume_simulation(self) -> None:
        self.pause = False

    def handle_key(self, key) -> None:
        if key == keyboard.Key.space:
            self.pause = not self.pause

        elif hasattr(key, "char") and key.char and key.char.lower() == "q":
            self.running = False
