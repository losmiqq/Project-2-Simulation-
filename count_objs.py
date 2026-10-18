def count_objects(mappa, object_class):
    count = 0
    for row in mappa:
        for cell in row:
            if isinstance(cell, object_class):
                count += 1
    return count
