from actions import Actions
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
        self.act = Actions()
        self.act.init_actions(self.mappa)

    def next_turn(self) -> None:
        print("-------------------------------")
        self.act.turn_action()
        self.mappa.show_mappa()
        self.counter +=1
        print(f"Ход номер {self.counter}")
        print("-------------------------------")

    def start_simulation(self) -> None:
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
