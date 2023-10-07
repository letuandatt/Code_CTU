Box = 4

class Coord:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def index_of(self):
        return Box * self.x + self.y

class Constrains:
    def __init__(self, oprt = None, value = 0):
        self.List_Coord = []
        self.oprt = oprt
        self.value = value

class KenKen:
    def __init__(self):
        self.cells = [[0 for col in range(Box)] for row in range(Box)]
        self.cages = []

    def get_value_cell(self, coord):
        return self.cells[coord.x][coord.y]

    def get_cage(self, coord):
        for i in range(len(self.cages)):
            for e in self.cages[i].List_Coord:
                if e.x == coord.x and e.y == coord.y:
                    return i

    def is_filled(self):
        for row, rows in enumerate(self.cells):
            for col, cols in enumerate(rows):
                if cols == 0:
                    return False
        return True

    def is_full_cage(self, index):
        for e in self.cages[index].List_Coord:
            if self.get_value_cell(e) == 0:
                return False
        return True

    def check_duplicate(self, coord, value):
        for i in range(Box):
            if self.cells[i][coord.y] == value:
                return False
        for i in range(Box):
            if self.cells[coord.x][i] == value:
                return False
        return True

    def check_cage(self, coord):
        idx_cage = self.get_cage(coord)
        value_cage = self.cages[idx_cage].value
        cal = self.cages[idx_cage].oprt
        list_coord = self.cages[idx_cage].List_Coord
        if cal == '+':
            total = 0
            for i in range(len(list_coord)):
                total += self.get_value_cell(list_coord[i])
            yes_1 = True if total == value_cage and self.is_full_cage(idx_cage) else False
            yes_2 = True if total < value_cage and not self.is_full_cage(idx_cage) else False
            return True if yes_1 or yes_2 else False
        elif cal == '-':
            if not self.is_full_cage(idx_cage):
                return True
            else:
                diff = 0
                for i in range(len(list_coord)):
                    diff -= self.get_value_cell(list_coord[i])
                    diff = abs(diff)
                return True if diff == value_cage else False
        elif cal == 'x':
            mult = 1
            for i in range(len(list_coord)):
                cell_value = self.get_value_cell(list_coord[i])
                mult *= (1 if cell_value == 0 else cell_value)
            yes_1 = True if mult == value_cage and self.is_full_cage(idx_cage) else False
            yes_2 = True if mult <= value_cage and not self.is_full_cage(idx_cage) else False
            return True if yes_1 or yes_2 else False
        elif cal == '/':
            if not self.is_full_cage(idx_cage):
                return True
            else:
                div = 1
                for i in range(len(list_coord)):
                    cell_value = self.get_value_cell(list_coord[i])
                    x = 1 if cell_value == 0 else cell_value
                    div = div // x if div > x else x // div
                return True if div == value_cage else False
        elif cal == '=':
            return False if value_cage != self.get_value_cell(coord) else True
        else:
            return False

    def show(self):
        print("KenKen:")
        for i in range(Box):
            if i % Box == 0:
                print("-------------")
            for j in range(Box):
                if j % Box == 0:
                    print("|", end='')
                print(f"{self.cells[i][j]:>2}|", end='')
            print()
        print("-------------")


    def show_cage(self):
        print("KenKen:")
        for i in range(Box):
            if i % Box == 0:
                print("-----------------")
            for j in range(Box):
                coord = Coord(i, j)
                if j % Box == 0:
                    print("|", end='')
                total_value = self.cages[self.get_cage(coord)].value
                oprt = self.cages[self.get_cage(coord)].oprt
                print(f"{total_value:>2}{oprt}|", end='')
            print()
        print("-----------------")

    def input(self):
        data = {
            0: [2, '/', 2, 0, 0, 0, 1],
            1: [7, '+', 2, 0, 2, 1, 2],
            2: [4, '=', 1, 0, 3],
            3: [1, '-', 2, 1, 0, 2, 0],
            4: [3, '-', 2, 1, 1, 2, 1],
            5: [2, '-', 2, 1, 3, 2, 3],
            6: [1, '-', 2, 3, 0, 3, 1],
            7: [4, 'x', 3, 2, 2, 3, 2, 3, 3],
        }
        # data = {
        #     0: [2, '/', 2, 0, 0, 1, 0],
        #     1: [36, 'x', 4, 0, 1, 0, 2, 1, 1, 1, 2],
        #     2: [2, '+', 1, 0, 3],
        #     3: [3, '-', 2, 1, 3, 2, 3],
        #     4: [2, '-', 2, 2, 1, 2, 2],
        #     5: [1, '-', 2, 3, 2, 3, 3],
        #     6: [8, '+', 3, 2, 0, 3, 0, 3, 1],
        # }
        self.cages = [Constrains() for i in range(len(data))]
        for i in range(len(data)):
            self.cages[i].value = data[i][0]
            self.cages[i].oprt = data[i][1]
            step = 3
            for num_coord in range(data[i][2]):
                x = data[i][step]
                y = data[i][step + 1]
                self.cages[i].List_Coord.append(Coord(x, y))
                step += 2

    def solve(self, row, col):
        if self.is_filled():
            return True
        if col == Box:
            row += 1
            col = 0
        global count
        for i in range(1, Box + 1):
            coord = Coord(row, col)
            if self.check_duplicate(coord, i):
                self.cells[row][col] = i
                count += 1
                if self.check_cage(coord):
                    if self.solve(row, col + 1) == True:
                        return True
            self.cells[row][col] = 0

count = 0

if __name__ == '__main__':
    kenken = KenKen()
    kenken.input()
    kenken.show()
    kenken.show_cage()
    if kenken.solve(0, 0):
        print("Tìm lời giải thành công")
        kenken.show()
    else:
        print("Không thể tìm ra đáp án")
    print("Số lượng trạng thái: ", count)