class Entity:
    def __init__(self, name: str, position: tuple[int, int] | None = None) -> None:
        self.name = name
        self.position = position
