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
