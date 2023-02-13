import numpy as np

### Player A : 1
### Player B : 2


class P4:
    def __init__(self):
        self.rows = 7
        self.columns = 6
        self.matrix = np.array([])

    def start(self):
        self.matrix = np.zeros((self.columns, self.rows))

    def slide(self,x_position, player):
        y_position = self.columns -1
        while self.matrix[y_position, x_position] != 0:
            y_position -= 1
            if y_position == -1:
                return False
        self.add((x_position, y_position), player)

    def add(self, position, value):
        self.matrix[position[1], position[0]] = value

    def test(self):
        if self.x_test() or self.y_test():
            pass

    def x_test(self):
        for i in self.matrix:
            for j in range(len(i)-3):
                if i[j:4] == np.ones(4) or i[j:4] == -np.ones(4):
                    return True
        return False

    def y_test(self):
        pass


    def __str__(self):
        return str(self.matrix)


board = P4()
board.start()
print(board)
