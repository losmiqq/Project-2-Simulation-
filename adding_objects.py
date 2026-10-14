

def add_objects_to_map(mappa, obj_class, count, *args):
    for _ in range(count):
        obj = obj_class(*args)
        mappa.add_pos_random(obj)

