import numpy
print("Starting...")

def readDigits():
    fp = open('./input-day-2.txt')
    digits = fp.readline().strip().split(',')
    return digits

try:
    originalDigits = readDigits()
    expectedOutput = 19690720
    verb = 0
    noun = 0
    digits = numpy.copy(originalDigits)
    while (verb == 0 & noun == 0) | (int(digits[0]) != expectedOutput):
        digits = numpy.copy(originalDigits)
        verb+=1
        noun+=1
        digits[1] = verb
        digits[2] = noun
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



finally:
    fp.close()
    print("Finished...")
