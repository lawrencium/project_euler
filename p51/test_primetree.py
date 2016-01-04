import unittest

from assertpy import assert_that

from p51.primetrie import PrimeDigitTrie, PrimeLeafNode, PrimeIndexNode

__author__ = 'lawrencechen'


class PrimeDigitTrieInitializationTest(unittest.TestCase):
    def test_prime_tree_has_leaf_node_root_if_levels_is_one(self):
        assert_that(PrimeDigitTrie(1)._root).is_type_of(PrimeLeafNode)

    def test_prime_tree_has_index_node_root_if_levels_is_greater_than_one(self):
        assert_that(PrimeDigitTrie(2)._root).is_type_of(PrimeIndexNode)
