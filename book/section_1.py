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


# 1.4
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
# of letters. The palindrome does not need to be limited to just dictionary words.


# 1.5
# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def one_away(one, two):
    set_one = set(one)
    set_two = set(two)
    differing_letters = set_one.difference(set_two)
    return len(differing_letters) == 1


# 1.6
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should
# return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
def string_compression(input_string):
    counts = []
    current_letter = None
    count = 0

    for letter in input_string:
        if current_letter and current_letter != letter:
            counts.append([current_letter, count])
            count = 0
        current_letter = letter
        count += 1
    counts.append([current_letter, count])

    output = ''
    for count in counts:
        output += (count[0] + str(count[1]))

    return output


# 1.7
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_matrix(matrix):
    new_matrix = [[] for _ in range(len(matrix))]
    for old_row in list(reversed(matrix)):
        for index, element in enumerate(old_row):
            new_matrix[index].append(element)
    return new_matrix

# 1.8
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
def zero_matrix(matrix):
    zero_coords = []
    for y, row in enumerate(matrix):
        for x, element in enumerate(row):
            if element == 0:
                zero_coords.append([y, x])

    for y, x in zero_coords:
        target_row = matrix[y]
        for index in range(len(target_row)):
            target_row[index] = 0
        for index, _ in enumerate(matrix):
            matrix[index][x] = 0
    return matrix

