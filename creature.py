from entity import Entity
from bfs_path import BFS
from mapp import Map
from objects import Grass
from abc import abstractmethod


class Creature(Entity):
    def __init__(self, name: str, speed: int, hp: int) -> None:
        super().__init__(name)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, obj: Entity, mappa: Map) -> None:
        pass


class Herbivore(Creature):
    def eat(self) -> None:
        # В будущем мб добавить разновидность травы и трава будет давать хп
        pass

    def make_move(self, mappa: Map, list_pos: list) -> None:
        if not list_pos:
            return
        old_pos = self.position
        poses = [BFS(old_pos, pos, mappa) for pos in list_pos]
        speed = self.speed
        new_path = min(poses, key=len)
        if speed < len(new_path) - 1:
            new_pos = new_path[speed]
        else:
            new_pos = new_path[1]

        target = mappa.what_is_this(new_pos)
        if target == ".":
            mappa.move(self, new_pos)
        else:
            if isinstance(target, Grass):
                self.eat()
                mappa.rewrite_pos(self, target)


class Predator(Creature):
    def __init__(self, name: str, speed: int, hp: int, atack_power: int) -> None:
        super().__init__(name, speed, hp)
        self.attack_power = atack_power

    def attack(self, obj):
        obj.hp -= self.attack_power

    def make_move(self, mappa: Map, list_pos: list) -> None:
        if list_pos == False:
            return
        old_pos = self.position
        poses = [BFS(old_pos, pos, mappa) for pos in list_pos]
        speed = self.speed

        new_path = min(poses, key=len)
        if speed < len(new_path) - 1:
            new_pos = new_path[speed]
        else:
            new_pos = new_path[1]

        target = mappa.what_is_this(new_pos)
        if target == ".":
            mappa.move(self, new_pos)
        else:
            if isinstance(target, Herbivore):
                self.attack(target)
                if target.hp <= 0:
                    new_pos = target.position
                    mappa.rewrite_pos(self, target)
