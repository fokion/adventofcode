
class MatrixHandler:
    DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

    def __init__(self):
      pass

    def add_wire(self,commands):
        y = 0
        x = 0
        wiring = {}
        length = 0
        for command in commands:
            direction = str(command[0])
            steps = int(command[1:])
            for _ in range(steps):
                x += self.DX[direction]
                y += self.DY[direction]
                length += 1
                if (x, y) not in wiring:
                    wiring[(x, y)] = length
        return wiring

    def get_cross(self,wire1 , wire2):
        both = set(wire1.keys()) & set(wire2.keys())
        return min([abs(x)+abs(y) for (x,y) in both])

    def get_intersect(self, wire1, wire2):
        both = set(wire1.keys()) & set(wire2.keys())
        return min([wire1[p] + wire2[p] for p in both])



