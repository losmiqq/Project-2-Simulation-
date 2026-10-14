# Project 2 — Ecosystem Simulation

A Python-based grid simulation of a simple ecosystem featuring predators, herbivores, and environmental objects.

The project demonstrates object-oriented programming, pathfinding with Breadth-First Search (BFS), grid-based world management, and turn-based simulation logic.

## Features

- **Grid-based world:** A 10 × 10 map containing creatures and environmental objects.
- **Object-oriented design:** Entities are organized into classes with shared behavior and inheritance.
- **Predators and herbivores:** Creatures move around the map and interact with other entities.
- **Pathfinding:** Breadth-First Search (BFS) is used to find paths toward target objects.
- **Resource management:** Herbivores search for grass, while predators search for herbivores.
- **Automatic replenishment:** Grass and herbivores are respawned when their population reaches zero.
- **Turn-based simulation:** Creatures perform their actions during each simulation turn.
- **Pause and resume:** Press the spacebar to pause or resume the simulation.
- **Console visualization:** The map is displayed in the terminal using emoji representations of objects.

## World Objects

The simulation uses emojis to represent creatures and environmental objects on the grid map.

| Emoji | Object | Description |
|---|---|---|
| 🐉 | Predator | Hunts herbivores. |
| 🦓 | Herbivore | Searches for grass. |
| 🌹 | Grass | A food source for herbivores. |
| 🌲 | Tree | An environmental object on the map. |
| 🗿 | Rock | An environmental object on the map. |

Each emoji represents an object occupying a cell on the simulation map.

## Technologies

- Python 3
- Object-oriented programming (OOP)
- Breadth-First Search (BFS)
- Python standard library

## Requirements

- Python 3 installed on your system
- A terminal or command-line interface

The current keyboard control implementation uses Python's `msvcrt` module and is intended for Windows.

## How to Run

1. Clone or download the repository.
2. Open the project directory in your terminal.
3. Run the application:

   ```bash
   python main.py
   ```

## Controls

| Key | Action |
|---|---|
| Spacebar | Pause or resume the simulation |
| q or Q | Stop the program |

## Project Structure

```text
Project-2-Simulation-/
├── main.py
├── simulation.py
├── mapp.py
├── entity.py
├── creature.py
├── objects.py
├── bfs_path.py
├── actions.py
├── adding_objects.py
├── count_objs.py
├── .gitignore
└── README.md
```

### Module Overview

- **`main.py`** — Entry point of the application.
- **`simulation.py`** — Initializes the simulation and controls the main loop, turns, and pause state.
- **`mapp.py`** — Implements the grid map and operations for placing, moving, removing, and locating objects.
- **`entity.py`** — Defines the base entity class.
- **`creature.py`** — Implements creature behavior and movement.
- **`objects.py`** — Defines environmental objects such as grass, trees, and stones.
- **`bfs_path.py`** — Implements the BFS pathfinding algorithm.
- **`actions.py`** — Coordinates creature actions and resource replenishment during simulation turns.
- **`adding_objects.py`** — Provides functionality for adding objects to the map.
- **`count_objs.py`** — Counts objects of a specified class on the map.

## Simulation Overview

The simulation creates a map and populates it with creatures and environmental objects.

During each turn:

1. Herbivores search for grass and move toward their targets.
2. Predators search for herbivores and move toward their targets.
3. The map is updated as creatures move and interact with objects.
4. Grass and herbivores are replenished when their respective counts reach zero.
5. The updated map is displayed in the terminal.

BFS is used to determine paths through the grid, allowing creatures to navigate toward their targets.

## Current Status

The project is under development. New features and improvements may be added as the simulation evolves.
