import unittest

from book import section_1


class TestSection1(unittest.TestCase):
    def test_section_1_1(self):
        assert section_1.unique_letters(input_string='abcdef')
        assert not section_1.unique_letters(input_string='abcdefa')
        assert section_1.unique_letters_no_structs(input_string='abcdef')
        assert not section_1.unique_letters_no_structs(input_string='abcdefa')

    def test_section_1_2(self):
        assert section_1.check_permutation(one='abc', two='bca')
        assert not section_1.check_permutation(one='abc', two='bcd')
        assert section_1.check_permutation_no_libs(one='abc', two='bca')
        assert not section_1.check_permutation_no_libs(one='abc', two='bcd')

    def test_section_1_3(self):
        assert section_1.urlify(input_string='Mr  John   Smith    ', some_int=13) == 'Mr%20John%20Smith'

    def test_section_1_5(self):
        assert section_1.one_away(one='pale', two='ple')
        assert section_1.one_away(one='pales', two='pale')
        assert section_1.one_away(one='pale', two='bale')
        assert not section_1.one_away(one='pale', two='bake')

    def test_section_1_6(self):
        assert section_1.string_compression('aabcccccaaa') == 'a2b1c5a3'

    def test_section_1_7(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
        assert section_1.rotate_matrix(matrix=matrix) == output
