class PasswordVerifier:
    def __init__(self):
        pass

    def set_max_length(self, length):
        self.length = length

    def set_range(self, from_value, to_value):
        self.from_value = from_value
        self.to_value = to_value


    def adjacent_values_are_valid(self,number_as_string):
        previous_number = -1
        for position in range(0,self.length):
            current_number = int(number_as_string[position])
            if previous_number != -1 and previous_number == current_number:
                return True
            previous_number = current_number
        return False

    def values_are_equal_or_higher(self, number_as_string):
        previous_number = int(number_as_string[0])
        for position in range(1, len(number_as_string)):
            current_number = int(number_as_string[position])
            if current_number < previous_number:
                return False
            previous_number = current_number
        return True

    def validate(self, possible_number):
        if (possible_number >= self.from_value and possible_number <= self.to_value):
            if (len(str(possible_number)) == self.length):
                if (self.adjacent_values_are_valid(str(possible_number))):
                    if (self.values_are_equal_or_higher(str(possible_number))):
                        return True

        return False

    def find_numbers(self):
        available_passwords = 0
        for number in range(self.from_value, self.to_value):
            if self.validate(number):
                available_passwords += 1
        return available_passwords
