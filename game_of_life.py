from enum import Enum


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Cell:
    def __init__(self, state, neighbor_count=0):
        self.state = state
        self.neighbor_count = neighbor_count


class GameOfLife:
    def __init__(self, grid=None):
        if grid:
            self.grid = {}
            self.input_grid(grid)
        else:
            self.grid = {}

    def _get_cell(self, x, y):
        if (x, y) in self.grid:
            return self.grid[(x, y)]
        else:
            cell = Cell(CellState.DEAD)
            self.grid.update({(x, y): cell})
            return cell

    def _update_neighbor_counts(self):
        for (x, y), cell in list(self.grid.items()):
            neighbor_coordinates = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
            for (x_i, y_i) in neighbor_coordinates:
                if cell.state == CellState.ALIVE:
                    self._visit_neighbor(x + x_i, y + y_i)

    def _visit_neighbor(self, x, y):
        cell = self._get_cell(x, y)
        cell.neighbor_count += 1

    def input_grid(self, grid):
        for row, _ in enumerate(grid):
            for col, _ in enumerate(grid[0]):
                if grid[row][col] == 1:
                    self.insert(CellState.ALIVE, row, col)

    def insert(self, state, x, y):
        if (x, y) in self.grid:
            raise IndexError
        else:
            if state == CellState.ALIVE:
                cell = Cell(state)
                self.grid.update({(x, y): cell})

    def advance_state(self):
        self._update_neighbor_counts()
        marked_for_death = []
        for (x, y), cell in self.grid.items():
            if cell.state == CellState.ALIVE and cell.neighbor_count not in [2, 3]:
                marked_for_death.append((x, y))
            elif cell.state == CellState.DEAD and cell.neighbor_count in [3]:
                cell.state = CellState.ALIVE
                cell.neighbor_count = 0
            elif cell.state == CellState.ALIVE:
                cell.neighbor_count = 0
            elif cell.state == CellState.DEAD:
                marked_for_death.append((x, y))

        for (x, y) in marked_for_death:
            del self.grid[(x, y)]

    def output_grid(self, pos_x, pos_y):
        # TODO: Explore changing boundaries
        grid = [[0 for _ in range(pos_y)] for _ in range(pos_x)]
        for x in range(pos_x):
            for y in range(pos_y):
                if (x, y) in self.grid and self.grid[(x, y)].state == CellState.ALIVE:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0
        return grid


if __name__ == "__main__":
    test_grid = [
                  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
                ]
    gameboard = GameOfLife()
    gameboard.input_grid(test_grid)
    print(gameboard.output_grid(10, 10))

    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))
    gameboard.advance_state()
    print(gameboard.output_grid(10, 10))


