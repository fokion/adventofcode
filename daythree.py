import  numpy as np

from MatrixHandler import MatrixHandler


fp = open('./input-day-3.txt')
wires = fp.readlines()

handler = MatrixHandler()

wirings = []
for wire in wires:
    commands = wire.split(",")
    wirings.append(handler.add_wire(commands))
print(handler.get_cross(wirings[0],wirings[1]))
print(handler.get_intersect(wirings[0],wirings[1]))








