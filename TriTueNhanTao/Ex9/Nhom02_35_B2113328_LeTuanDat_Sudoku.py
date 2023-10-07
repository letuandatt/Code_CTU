nb_rows = 9
nb_cols = 9
max_value = 10
Empty = 0
area_square_size = 3
inf = 99999

class Coord:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def index_of(self):
        return nb_rows * self.x + self.y

    def position_of_vertex(self, vertex):
        return Coord(vertex // nb_rows, vertex % nb_cols)

class Constrains:
    def __init__(self):
        self.data = [[0 for _ in range(nb_rows * nb_cols)] for _ in range(nb_rows * nb_cols)]
        self.n = nb_rows * nb_cols

    def init_constrains(self):
        for i in range(self.n):
            for j in range(self.n):
                self.data[i][j] = 0

    def add_constrains(self, source, target):
        u = source.index_of()
        v = target.index_of()
        if self.data[u][v] == 0:
            self.data[u][v] = 1
            self.data[v][u] = 1
            return True
        return False

    def get_constrains(self, coord):
        v = coord.index_of()
        result = []
        for i in range(self.n):
            if self.data[v][i] == 1:
                result.append(coord.position_of_vertex(i))
        return result

class Sudoku:
    def __init__(self):
        self.cells = [[0 for _ in range(nb_cols)] for _ in range(nb_rows)]
        self.constrains = Constrains()

    def init_sudoku(self):
        for i in range(nb_rows):
            for j in range(nb_cols):
                self.cells[i][j] = Empty
        self.constrains.init_constrains()

    def init_sudoku_with_values(self, inputs):
        for i in range(nb_rows):
            for j in range(nb_cols):
                self.cells[i][j] = inputs[i][j]
        self.constrains.init_constrains()

    def print_sudoku(self):
        print("Sudoku:")
        for i in range(nb_rows):
            if i % area_square_size == 0:
                print("-------------------------")
            for j in range(nb_cols):
                if j % area_square_size == 0:
                    print("| ", end="")
                print(self.cells[i][j], end=" ")
            print("|")
        print("-------------------------")

    def is_filled_sudoku(self):
        for i in range(nb_rows):
            for j in range(nb_cols):
                if self.cells[i][j] == Empty:
                    return False
        return True

    def spread_constrains_from(self, position, changeds):
        row = position.x
        col = position.y
        for i in range(nb_rows):
            if i != row:
                pos = Coord(i, col)
                if self.constrains.add_constrains(position, pos):
                    changeds.append(pos)
        for i in range(nb_cols):
            if i != col:
                pos = Coord(row, i)
                if self.constrains.add_constrains(position, pos):
                    changeds.append(pos)
        for i in range(area_square_size):
            for j in range(area_square_size):
                areaX = (row // area_square_size) * area_square_size
                areaY = (col // area_square_size) * area_square_size
                if areaX + i != row or areaY + j != col:
                    pos = Coord(areaX + i, areaY + j)
                    if self.constrains.add_constrains(position, pos):
                        changeds.append(pos)

    def get_available_values(self, position):
        pos_list = self.constrains.get_constrains(position)
        availables = [1] * max_value
        for i in range(len(pos_list)):
            pos = pos_list.pop(0)
            if self.cells[pos.x][pos.y] != Empty:
                availables[self.cells[pos.x][pos.y]] = Empty
        result = []
        for i in range(1, max_value):
            if availables[i]:
                result.append(i)
        return result

    def get_next_min_domain_cell(self):
        minLength = inf
        result = Coord(0, 0)
        for i in range(nb_rows):
            for j in range(nb_cols):
                if self.cells[i][j] == Empty:
                    pos = Coord(i, j)
                    availablesLength = len(self.get_available_values(pos))
                    if availablesLength < minLength:
                        minLength = availablesLength
                        return pos
        return result

    exploredCounter = 0

    def sudoku_back_tracking(self):
        global exploredCounter
        if self.is_filled_sudoku():
            return True
        position = self.get_next_min_domain_cell()
        availables = self.get_available_values(position)
        if len(availables) == 0:
            return False
        for j in range(len(availables)):
            value = availables.pop(0)
            self.cells[position.x][position.y] = value
            exploredCounter += 1
            if self.sudoku_back_tracking():
                return True
            self.cells[position.x][position.y] = Empty
        return False

    def solve_sudoku(self):
        global exploredCounter
        for i in range(nb_rows):
            for j in range(nb_cols):
                if sudoku.cells[i][j] == Empty:
                    history = []
                    pos = Coord(i, j)
                    self.spread_constrains_from(pos, history)
        exploredCounter = 0
        if self.sudoku_back_tracking():
            print("Solved!")
        else:
            print("Can not solve!")
        print("Explored", exploredCounter, "states.")
        return sudoku

inputs = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

inputs2 = [
    [0, 5, 4, 0, 7, 9, 6, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 5, 0],
    [7, 0, 0, 0, 4, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 1],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 3, 0, 0, 9, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 0, 8, 0, 0, 6, 0],
]

inputs3 = [
    [5, 0, 6, 0, 1, 4, 8, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [3, 0, 1, 0, 0, 8, 0, 7, 6],
    [8, 0, 3, 6, 0, 9, 0, 0, 0],
    [9, 0, 0, 0, 2, 0, 0, 0, 1],
    [0, 0, 0, 3, 0, 1, 9, 0, 8],
    [1, 7, 0, 5, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [6, 0, 5, 4, 8, 0, 1, 0, 2],
]

inputs4 = [
    [0, 3, 4, 6, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 8, 6, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 4],
    [1, 0, 3, 0, 6, 9, 0, 4, 2],
    [0, 0, 2, 5, 7, 4, 3, 0, 0],
    [4, 6, 0, 3, 1, 0, 9, 0, 8],
    [6, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 1, 8, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 7, 4, 6, 0],
]

if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.init_sudoku_with_values(inputs2)
    sudoku.print_sudoku()
    sudoku.solve_sudoku()
    sudoku.print_sudoku()