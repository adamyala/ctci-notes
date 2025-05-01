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


def check_permutation_no_libs(one, two):
    set_one = set(one)
    set_two = set(two)
    missing_from_two = set_one.difference(set_two)
    missing_from_one = set_two.difference(set_one)
    if not missing_from_one and not missing_from_two:
        return True


# 1.3
# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional
# characters,and that you are given the "true" length of the string.
def urlify(input_string, some_int):
    words = input_string.split()
    urlified = '%20'.join(words)
    return urlified
