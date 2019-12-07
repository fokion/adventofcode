import  numpy as np
class MatrixHandler:

    def __init__(self, matrix,starting_point_x,starting_point_y):
        self.matrix = matrix
        self.intersections = set()
        self.last_x = starting_point_x
        self.last_y = starting_point_y
        self.wiresAdded = 0
        self.matrix[self.last_x, self.last_y] = "O"

    def mark_board_with_fixed_y(self, y, from_x, to_x):
        for x in range(from_x, to_x):
            if self.matrix[x, y] != " ":
                self.matrix[x, y] = "X"
                self.intersections.add(str(x) + "," + str(y))
            elif self.matrix[x, y] == " ":
                self.matrix[x, y] = "|"

    def mark_board_with_fixed_x(self, x, from_y, to_y):
        for y in range(from_y, to_y):
            if self.matrix[x, y] != " ":
                self.matrix[x, y] = "X"
                self.intersections.add(str(x) + "," + str(y))
            elif self.matrix[x, y] == " ":
                self.matrix[x, y] = "-"

    def add_wire(self,commands):
        self.wiresAdded+=1
        for command in commands:
            type_of_movement = str(command[0])
            number_of_moves = int(command[1:])
            if type_of_movement == "R":
                self.mark_board_with_fixed_x(self.last_x, self.last_y+1, (self.last_y + number_of_moves))
                self.last_y += number_of_moves
            elif type_of_movement == "L":
                self.mark_board_with_fixed_x(self.last_x, (self.last_y - number_of_moves), self.last_y)
                self.last_y -= number_of_moves
            elif type_of_movement == "U":
                self.mark_board_with_fixed_y(self.last_y, self.last_x+1, (self.last_x + number_of_moves))
                self.last_x += number_of_moves
            else:
                self.mark_board_with_fixed_y(self.last_y, (self.last_x - number_of_moves), self.last_x)
                self.last_x -= number_of_moves
        self.print_state("wire__"+str(self.wiresAdded))

    def getIntersections(self):
        return self.intersections

    def print_state(self,name):
        np.savetxt("matrix__" + str(name) + ".txt", self.matrix, delimiter='', fmt="%s")
