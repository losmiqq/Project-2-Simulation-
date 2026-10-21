from adding_objects import add_objects_to_map
from creature import Predator, Herbivore
from objects import Grass, Tree, Stone
from count_objs import count_objects



class PopulateWorld():
    def execute(self, mappa):
        add_objects_to_map(mappa, Predator, 2, "🐉", 1, 100, 50)
        add_objects_to_map(mappa, Herbivore, 3, "🦓", 2, 120)
        add_objects_to_map(mappa, Grass, 3, "🌹")
        add_objects_to_map(mappa, Tree, 2, "🌲")
        add_objects_to_map(mappa, Stone, 1, "🗿")


class SpawnGrass():
    def execute(self, mappa):
        if count_objects(mappa, Grass) == 0:
            add_objects_to_map(mappa, Grass, 3, "🌹")


class SpawnHerbivores():
    def execute(self, mappa):
        if count_objects(mappa, Herbivore) == 0:
            add_objects_to_map(mappa, Herbivore, 3, "🦓", 2, 120)

class MoveCreatures():
    def execute(self, mappa):
        for herbivore in mappa.get_list_of_objects(Herbivore):
            grass_list = [
                grass.position for grass in mappa.get_list_of_objects(Grass)
            ]
            if grass_list:
                herbivore.make_move(mappa, grass_list)

        for predator in mappa.get_list_of_objects(Predator):
            herbivore_list = [
                herbivore.position
                for herbivore in mappa.get_list_of_objects(Herbivore)
            ]
            if herbivore_list:
                predator.make_move(mappa, herbivore_list)
