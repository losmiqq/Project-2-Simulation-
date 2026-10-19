from actions import PopulateWorld, SpawnGrass, SpawnHerbivores, MoveCreatures
from mapp import Map
import os
import time
import msvcrt


class Simulation:
    def __init__(self) -> None:
        self.counter = 0
        self.pause = True
        self.running = True
        self.mappa = Map()
        self.init_actions = [PopulateWorld()]

        self.turn_actions =[SpawnGrass(), SpawnHerbivores(), MoveCreatures()]

    def next_turn(self) -> None:
        print("-------------------------------")
        for action in self.turn_actions:
            action.execute(self.mappa)
        self.mappa.show_mappa()
        self.counter +=1
        print(f"Ход номер {self.counter}")
        print("-------------------------------")

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.mappa)
        while True:
            self.pause_simulation()
            if self.pause:
                os.system("cls" if os.name == "nt" else "clear")
                self.next_turn()
                time.sleep(1.5)
            else:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting when paused

    def pause_simulation(self) -> None:
        if msvcrt.kbhit():
            if msvcrt.getch() == b" ":  # Check if ' ' key is pressed
                self.pause = not self.pause  # Toggle the pause state
