# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def unique_letters(input_string):
    result = len(input_string) == len(set(input_string))
    return result


def unique_letters_no_structs(input_string):
    for letter in input_string:
        if input_string.count(letter) > 1:
            return False
    return True


# 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(one, two):
    from itertools import permutations
    return tuple(two) in list(permutations(one))
