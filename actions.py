from adding_objects import add_objects_to_map
from creature import Predator, Herbivore
from mapp import Map
from objects import Grass, Tree, Stone
from count_objs import count_objects


class Actions:
    def init_actions(self, mappa: Map) -> None:
        self.Mappa = mappa

        add_objects_to_map(self.Mappa, Predator, 2, "🐉", 1, 100, 50)
        add_objects_to_map(self.Mappa, Herbivore, 3, "🦓", 2, 120)
        add_objects_to_map(self.Mappa, Grass, 3, "🌹")
        add_objects_to_map(self.Mappa, Tree, 2, "🌲")
        add_objects_to_map(self.Mappa, Stone, 1, "🗿")

    def turn_action(self) -> None:
        if count_objects(self.Mappa.mappa, Grass) == 0:
            add_objects_to_map(self.Mappa, Grass, 3, "🌹")
        if count_objects(self.Mappa.mappa, Herbivore) == 0:
            add_objects_to_map(self.Mappa, Herbivore, 3, "🦓", 2, 120)
        self.turn_herbivore_action()
        self.turn_predator_action()

    def turn_herbivore_action(self) -> None:
        for herbivore in self.Mappa.get_list_of_objects(Herbivore):
            grass_list = [
                grass.position for grass in self.Mappa.get_list_of_objects(Grass)
            ]
            if grass_list:
                herbivore.make_move(self.Mappa, grass_list)
            else:
                return

    def turn_predator_action(self) -> None:
        for predator in self.Mappa.get_list_of_objects(Predator):
            herbivore_list = [
                herbivore.position
                for herbivore in self.Mappa.get_list_of_objects(Herbivore)
            ]
            if herbivore_list:
                predator.make_move(self.Mappa, herbivore_list)
            else:
                return
