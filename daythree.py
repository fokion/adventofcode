import  numpy as np

from MatrixHandler import MatrixHandler


fp = open('./test-3.txt')
wires = fp.readlines()
width = 1000
height = 1000
matrix = np.full((width, height), ' ')
startingPoint_x = height - 500
startingPoint_y = 300
handler =  MatrixHandler(matrix,startingPoint_x,startingPoint_y)
intersections = set()
wire_index = 0
for wire in wires:
    commands = wire.split(",")
    handler.add_wire(commands)
print(handler.getIntersections())






