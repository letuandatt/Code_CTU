size = 8

queens = [[0 for row in range(size)] for col in range(size)]

def is_valid(row, col):
    for i in range(row):
        if queens[i] == col or abs(i - row) == abs(col - i):
            return False
    return True

def show():
    for i in range(size):
        for j in range(size):
            if queens[i] == j:
                print("Q  ", end=" ")
            else:
                print("-  ", end=" ")
        print()

    c = input("Press 'y' to see more or 'n' to stop: ")
    if c == "n":
        print("Stop ... 100%")
        exit()

def put_queen(row):
    for col in range(size):
        if is_valid(row, col):
            queens[row] = col
            if row == size - 1:
                show()
            else:
                put_queen(row + 1)
            queens[row] = 0

if __name__ == '__main__':
    put_queen(0)