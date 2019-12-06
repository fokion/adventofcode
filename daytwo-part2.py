import numpy

print("Starting...")


def read_digits_from_file():
    fp = open('./input-day-2.txt')
    digits = fp.readline().strip().split(',')
    fp.close()
    return digits



expectedOutput = 19690720



def calculate_first_position(noun, verb):
    digits = read_digits_from_file()
    digits[1] = noun
    digits[2] = verb
    index = 0
    size = len(digits)
    while index < size:
        digit = int(digits[index])
        if digit == 99:
            break
        index_of_number_one = int(digits[index + 1])
        index_of_number_two = int(digits[index + 2])
        index_of_output = int(digits[index + 3])
        if digit == 1:
            # do addition
            digits[index_of_output] = int(digits[index_of_number_one]) + int(digits[index_of_number_two])
        elif digit == 2:
            # multiply
            digits[index_of_output] = int(digits[index_of_number_one]) * int(digits[index_of_number_two])
        index += 4
    return digits

for noun in range(0, 100, 1):
    for verb in range(0, 100, 1):
        digits = calculate_first_position(noun, verb)
        codeAtFirstPosition = digits[0]
        if noun == 12 and verb == 2:
          print("Answer part 1 : ",codeAtFirstPosition)
        if codeAtFirstPosition == 19690720:
            ans = 100 * noun + verb
            print("Answer part 2 : ",ans)
            break
