from collections import deque


def BFS(start, target, mappa):
    queue = deque()
    visited = set()
    came_from = dict()

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        if current == target:
            current = target
            path = [current]

            while current != start:
                path.append(came_from[current])
                current = came_from[current]
            path.reverse()
            return path
        neighbors = mappa.get_neighbors(current)

        for neighbor in neighbors:
            if neighbor not in visited and (
                mappa.what_is_this(neighbor) == "." or neighbor == target
            ):
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
