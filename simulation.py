from actions import Actions
from mapp import Map
import os
import time
import msvcrt


class Simulation:
    def __init__(self):
        self.pause = True
        self.running = True
        self.mappa = Map()
        self.act = Actions()
        self.act.init_actions(self.mappa)

    def next_turn(self):
        print("-------------------------------")
        self.act.turn_action()
        self.mappa.show_mappa()
        print("-------------------------------")

    def start_simulation(self):
        while True:
            self.pause_simulation()
            if self.pause:
                os.system("cls" if os.name == "nt" else "clear")
                self.next_turn()
                time.sleep(1.5)
            else:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting when paused

    def pause_simulation(self):
        if msvcrt.kbhit():
            if msvcrt.getch() == b" ":  # Check if ' ' key is pressed
                self.pause = not self.pause  # Toggle the pause state
