from entity import Entity
from bfs_path import BFS
from mapp import Map
from objects import Grass
from abc import abstractmethod



def find_nearest_path(
        world: Map,
        position: tuple[int, int] | None,
        targets: list | None
        ) -> None | list[tuple[int, int]]:

    if not targets or position is None:
        return None

    paths = [BFS(position, pos, world) for pos in targets]
    paths = [pose for pose in paths if pose is not None]
    if not paths:
        return None

    return min(paths, key=len)

class Creature(Entity):
    def __init__(self, name: str, speed: int, hp: int) -> None:
        super().__init__(name)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, mappa: Map, list_pos: list) -> None:
        pass


class Herbivore(Creature):
    def eat(self) -> None:
        # В будущем мб добавить разновидность травы и трава будет давать хп
        pass

    def make_move(self, mappa: Map, list_pos: list) -> None:
        path = find_nearest_path(mappa, self.position, list_pos)
        if path is None:
            return

        speed = self.speed
        if speed < len(path) - 1:
            new_pos = path[speed]
        else:
            new_pos = path[1]

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
        path = find_nearest_path(mappa, self.position, list_pos)
        if path is None:
            return

        speed = self.speed
        if speed < len(path) - 1:
            new_pos = path[speed]
        else:
            new_pos = path[1]

        target = mappa.what_is_this(new_pos)
        if target == ".":
            mappa.move(self, new_pos)
        else:
            if isinstance(target, Herbivore):
                self.attack(target)
                if target.hp <= 0:
                    new_pos = target.position
                    mappa.rewrite_pos(self, target)
