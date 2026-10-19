from mapp import Map


def count_objects(mappa: Map, object_class: type) -> int:
    count = 0
    for row in mappa.mappa:
        for cell in row:
            if isinstance(cell, object_class):
                count += 1
    return count
