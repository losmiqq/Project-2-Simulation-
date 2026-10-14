from typing import NoReturn

from actions import Actions
from mapp import Map
import os
import time
import msvcrt


class Simulation():
    def __init__(self) -> None:
        self.pause = True
        self.running = True
        self.mappa = Map()
        self.act = Actions()
        self.act.init_actions(self.mappa)



    def next_turn(self) -> None:
        print("-------------------------------")
        self.act.turn_action()
        self.mappa.show_mappa()
        print("-------------------------------")



    def start_simulation(self) -> None:
        while self.stop_simulation():
            self.pause_simulation()
            if self.running:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.next_turn()
                time.sleep(1.5)
            else:
                time.sleep(0.1)


    def pause_simulation(self) -> None:
        if msvcrt.kbhit():
            if msvcrt.getch() == b' ':
                self.pause = not self.pause

    def stop_simulation(self) -> None:
        if msvcrt.kbhit():
            if msvcrt.getch() == b'q' or msvcrt.getch() == b'Q':
                self.running = False
