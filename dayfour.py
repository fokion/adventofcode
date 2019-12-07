from PasswordVerifier import PasswordVerifier

verifier = PasswordVerifier()
verifier.set_max_length(6)
verifier.set_range(0, 222222)
assert verifier.adjacent_values_are_valid("111111") == True,"111111 is valid for the adjacent values"
assert verifier.values_are_equal_or_higher("123456") == True, "123456 is valid for the values equal or higher"
assert verifier.values_are_equal_or_higher("123426") == False, "123426 is invalid for the values equal or higher"

verifier = PasswordVerifier()
verifier.set_max_length(6)
verifier.set_range(367479, 893698)
print(verifier.find_numbers())
print(verifier.find_numbers_for_part_two())