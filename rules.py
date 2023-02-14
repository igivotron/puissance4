import numpy as np

### Player A : 1
### Player B : -1

class P4:
    def __init__(self):
        self.rows = 7
        self.columns = 6
        self.matrix = np.array([])
        self.loop = True
        self.y_position = 0

    def start(self):
        self.matrix = np.zeros((self.columns, self.rows),int)

    def slide(self,x_position, player):
        self.y_position = self.columns -1
        while self.matrix[self.y_position,x_position] != 0:
            self.y_position -= 1
            if self.y_position == -1:
                return False
        self.add((x_position, self.y_position), player)
        if self.test():
            self.win(player)
        return True

    def add(self, position, value):
        self.matrix[position[1], position[0]] = value

    def test(self):
        if self.x_test() or self.y_test():
            return True
        else:
            return False

    def transfer(self):
        return self.matrix.T

    def x_test(self):
        for i in self.matrix:
            for j in range(len(i)-3):
                if np.sum(i[j:j+4]) == 4 or np.sum(i[j:j+4]) == -4:
                    return True

    def y_test(self):
        for i in self.transfer():
            for j in range(len(i)-3):
                if np.sum(i[j:j+4]) == 4 or np.sum(i[j:j+4]) == -4:
                    return True

    def win(self, player):
        self.loop = False
        print("","#"*16,"\n","Game over","\n",player,"won","\n","#"*17,)

    def __str__(self):
        return str(self.matrix)
