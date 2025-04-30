import unittest

from book import section_1


class TestSection1(unittest.TestCase):
    def test_section_1_1(self):
        assert section_1.unique_letters('abcdef')
        assert not section_1.unique_letters('abcdefa')
        assert section_1.unique_letters_no_structs('abcdef')
        assert not section_1.unique_letters_no_structs('abcdefa')

    def test_section_1_2(self):
        assert section_1.check_permutation('abc', 'bca')
        assert not section_1.check_permutation('abc', 'bcd')
