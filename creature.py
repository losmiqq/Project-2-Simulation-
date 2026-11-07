from entity import Entity
from bfs_path import BFS
from mapp import Map
from objects import Grass
from abc import ABC, abstractmethod



def find_nearest_path(
        world: Map,
        position: tuple[int, int] | None,
        targets: list[tuple[int, int]] | None
        ) -> None | list[tuple[int, int]]:

    if not targets or position is None:
        return None

    paths = [BFS(position, pos, world) for pos in targets]
    paths = [pose for pose in paths if pose is not None]
    if not paths:
        return None

    return min(paths, key=len)


Position = tuple[int, int]


class Creature(Entity, ABC):
    def __init__(self, name: str, speed: int, hp: int) -> None:
        super().__init__(name)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, mappa: Map, list_pos: list[Position]) -> None:
        raise NotImplementedError


class Herbivore(Creature):
    def eat(self) -> None:
        pass

    def make_move(self, mappa: Map, list_pos: list[Position]) -> None:
        path = find_nearest_path(mappa, self.position, list_pos)
        if path is None:
            return

        if len(path) == 2:
            new_pos = path[1]
            target = mappa.what_is_this(new_pos)
            if isinstance(target, Grass):
                self.eat()
                mappa.rewrite_pos(self, target)
        else:
            speed = self.speed
            while speed >= len(path) - 1:
                speed -= 1

            new_pos = path[speed]

            target = mappa.what_is_this(new_pos)
            if target == ".":
                mappa.move(self, new_pos)


class Predator(Creature):
    def __init__(self, name: str, speed: int, hp: int, attack_power: int) -> None:
        super().__init__(name, speed, hp)
        self.attack_power = attack_power

    def attack(self, obj) -> None:
        obj.hp -= self.attack_power

    def make_move(self, mappa: Map, list_pos: list[Position]) -> None:
        path = find_nearest_path(mappa, self.position, list_pos)
        if path is None:
            return

        if len(path) == 2:
            new_pos = path[1]
            target = mappa.what_is_this(new_pos)
            if isinstance(target, Herbivore):
                self.attack(target)
                if target.hp <= 0:
                    new_pos = target.position
                    mappa.rewrite_pos(self, target)
        else:
            speed = self.speed
            while speed >= len(path) - 1:
                speed -= 1

            new_pos = path[speed]

            target = mappa.what_is_this(new_pos)
            if target == ".":
                mappa.move(self, new_pos)
