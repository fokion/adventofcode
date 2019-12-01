import math

print("Starting...")
try:
    fp = open('./input-day-1.txt')
    modules = fp.readlines()
    sumOfMasses = 0
    for rawModule in modules:
        module = rawModule.replace('\n', '')

        mass = math.floor(int(module) / 3) - 2

        sumOfMasses += mass
    print("Sum of all the mass = ",sumOfMasses)
finally:
    fp.close()
    print("Finished...")
