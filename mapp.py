import random as r

from entity import Entity


class Map:
    def __init__(self) -> None:
        self.num_row = 10
        self.num_column = 10
        self.mappa = [
            ["." for j in range(self.num_row)] for i in range(self.num_column)
        ]

    def add_pos(self, obj: Entity, new_pos: tuple[int, int]) -> None:
        if obj.position is not None:
            return

        i, j = new_pos
        if i not in range(self.num_row) or j not in range(self.num_column):
            return

        if self.mappa[i][j] != ".":
            return

        self.mappa[i][j] = obj
        obj.position = i, j

    def add_pos_random(self, obj: Entity) -> None:
        if obj.position is not None:
            return

        while True:
            i = r.randrange(self.num_row)
            j = r.randrange(self.num_column)
            if self.mappa[i][j] != ".":
                continue
            else:
                self.mappa[i][j] = obj
                obj.position = i, j
                break

    def get_list_of_objects(self, obj_class: type[Entity]) -> list[Entity]:
        objects = []
        for row in range(self.num_row):
            for column in range(self.num_column):
                cell = self.mappa[row][column]
                if isinstance(cell, obj_class):
                    objects.append(cell)
        return objects

    def delete_pos(self, obj: Entity) -> None:
        if obj.position is None:
            return

        row, column = obj.position
        if row in range(self.num_row) and column in range(self.num_column):
            if self.mappa[row][column] is obj:
                self.mappa[row][column] = "."
                obj.position = None

    def rewrite_pos(self, creature: Entity, target: Entity) -> None:
        if creature.position is None or target.position is None:
            return

        new_pos = target.position

        if new_pos[0] not in range(self.num_row) or new_pos[1] not in range(self.num_column):
            return

        self.delete_pos(target)
        self.delete_pos(creature)
        self.add_pos(creature, new_pos)

    def move(self, obj: Entity, new_pos: tuple[int, int]) -> None:
        if obj.position is None:
            return
        i, j = new_pos

        if i not in range(self.num_row) or j not in range(self.num_column):
            return

        if self.mappa[i][j] != ".":
            return

        self.delete_pos(obj)
        self.add_pos(obj, new_pos)

    def what_is_this(self, pos: tuple[int, int]) -> str | Entity:
        i, j = pos
        return self.mappa[i][j]

    def get_neighbors(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        row, column = pos
        up = row - 1, column
        upright = row - 1, column + 1
        right = row, column + 1
        downright = row + 1, column + 1
        down = row + 1, column
        downleft = row + 1, column - 1
        left = row, column - 1
        upleft = row - 1, column - 1
        neighbors = [up, upright, right, downright, down, downleft, left, upleft]
        correct_neighbors = []
        for i in neighbors:
            if i[0] in range(self.num_row) and i[1] in range(self.num_column):
                correct_neighbors.append(i)
        return correct_neighbors
