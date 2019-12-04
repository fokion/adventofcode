import numpy
print("Starting...")

def castingToInt(x):
    return int(x)

try:
    fp = open('./input-day-2.txt')
    digits = fp.readline().strip().split(',')
    index = 0
    size = len(digits)
    while index < size:
        digit = int(digits[index])
        if(digit == 1):
            # do addition
            indexOfNumberOne = int(digits[index+1])
            indexOfNumberTwo = int(digits[index+2])
            indexOfOutput = int(digits[index+3])
            digits[indexOfOutput] = int(digits[indexOfNumberOne])+int(digits[indexOfNumberTwo])
        elif (digit == 2):
            #multiply
            indexOfNumberOne = int(digits[index + 1])
            indexOfNumberTwo = int(digits[index + 2])
            indexOfOutput = int(digits[index + 3])
            digits[indexOfOutput] = int(digits[indexOfNumberOne]) * int(digits[indexOfNumberTwo])
        elif (digit == 99):
            break
        index+=4
    print(str(digits[0]))
    print(digits)

finally:
    fp.close()
    print("Finished...")
