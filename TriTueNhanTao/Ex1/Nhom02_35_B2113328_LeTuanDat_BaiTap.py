tankcapacity_x = 9
tankcapacity_y = 4
Empty = 0
Goal = 6
MaxLength = 5000

action = ["First State", "Pour Water Full X", "Pour Water Full Y",
          "Pour Water Empty X", "Pour Water Empty Y",
          "Pour Water X to Y", "Pour Water Y to X"]

class State:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def print_state(self):
        print("   X: {0} --- Y: {1}".format(self.x, self.y))

    def pourWaterFullX(self):
        return State(tankcapacity_x, self.y) if self.x < tankcapacity_x else None

    def pourWaterFullY(self):
        return State(self.x, tankcapacity_y) if self.y < tankcapacity_y else None

    def pourWaterEmptyX(self):
        return State(Empty, self.y) if self.x > 0 else None

    def pourWaterEmptyY(self):
        return State(self.x, Empty) if self.y > 0 else None

    def pourWaterXY(self):
        return State(max(self.x - (tankcapacity_y - self.y), 0),
                     min(self.x + self.y, tankcapacity_y)) if self.x > 0 and self.y < tankcapacity_y else None

    def pourWaterYX(self):
        return State(min(self.x + self.y, tankcapacity_x),
                     max(self.y - (tankcapacity_x - self.x), 0)) if self.y > 0 and self.x < tankcapacity_x else None

    def call_operator(self, opt):
        match opt:
            case 1:
                return self.pourWaterFullX()
            case 2:
                return self.pourWaterFullY()
            case 3:
                return self.pourWaterEmptyX()
            case 4:
                return self.pourWaterEmptyY()
            case 5:
                return self.pourWaterXY()
            case 6:
                return self.pourWaterYX()
            case _:
                print("Error calls operators")
                return None

if __name__ == '__main__':
    cur = State(5, 4)
    cur.print_state()
    for opt in range (7):
        call = cur.call_operator(opt)
        if call == 1:
            print(f"Hanh dong {action[opt]} thanh cong")
            cur.print_state()