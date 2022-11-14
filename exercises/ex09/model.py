"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = ""  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Finds the distance between two points given."""
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Changes the cells location each tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.sickness = -1

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"
    
    def contract_disease(self) -> None:
        """Chenges the attribute sickness of a class."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """If cell is vulnerable it returns true."""
        return self.sickness == constants.VULNERABLE
    
    def is_infected(self) -> bool:
        """If cell is infected it returns true."""
        return self.sickness >= constants.INFECTED

    def contact_with(self, other: Cell) -> None:
        """Checks if either cells are infected and then infects it respectively."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """After 3 seconds, the cell becomes immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> None:
        """If immune the function returns true."""
        return self.sickness == constants.IMMUNE


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells > cells:
            raise ValueError("too many cells")
        elif infected_cells <= 0:
            raise ValueError("too little cells")
        if immune_cells > cells or immune_cells < 0:
            raise ValueError
        self.population = []
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected_cells:
                cell.contract_disease()
            if i > constants.INFECTED_CELLS and i <= infected_cells + immune_cells:
                cell.immunize()
            self.population.append(cell)

    def check_contacts(self) -> None:
        """Checks if contact between cells has occured and then infects a cell."""
        for i in range(0, len(self.population) - 1):
            for z in range(i + 1, len(self.population)):
                if Point.distance(self.population[i].location, self.population[z].location) < 2 * constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[z])
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

        # TODO
        return Point(0.0, 0.0)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True