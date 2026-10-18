def add_objects_to_map(mappa: Map, obj_class: type, count: int, *args) -> None:
    for _ in range(count):
        obj = obj_class(*args)
        mappa.add_pos_random(obj)
