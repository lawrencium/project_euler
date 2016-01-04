import unittest

from assertpy import assert_that

from p51.primetrie import PrimeDigitTrie, PrimeLeafNode, PrimeIndexNode, InsertInformation

__author__ = 'lawrencechen'


class PrimeDigitTrieInitializationTest(unittest.TestCase):
    def test_prime_tree_has_leaf_node_root_if_levels_is_one(self):
        assert_that(PrimeDigitTrie(1)._root).is_type_of(PrimeLeafNode)

    def test_prime_tree_has_index_node_root_if_levels_is_greater_than_one(self):
        assert_that(PrimeDigitTrie(2)._root).is_type_of(PrimeIndexNode)


class PrimeDigitTrieInsertTest(unittest.TestCase):
    def setUp(self):
        self.tree = PrimeDigitTrie(3)

    def test_tree_throws_exception_on_insert_if_inserting_negative_number(self):
        with self.assertRaises(Exception):
            self.tree.insert(-10)

    def test_tree_throws_exception_on_insert_if_digits_in_number_to_insert_does_not_equal_levels(self):
        with self.assertRaises(Exception):
            self.tree.insert(10)


# noinspection PyStatementEffect
class PrimeLeafNodeInsertTest(unittest.TestCase):
    def setUp(self):
        self.insert_information = InsertInformation(9, '')
        self.asterisk_insert = InsertInformation(9, '9')
        self.node = PrimeLeafNode()

    def test_node_inserts_new_digit_to_digits_with_value_one_if_digit_not_in_digits_table(self):
        information = self.node.insert(self.insert_information)
        assert_that(information.count).is_equal_to(1)

    def test_return_correct_smallest_value_on_single_insert(self):
        information = self.node.insert(self.insert_information)
        assert_that(information).has_smallest_value(9)

    def test_node_increments_value_by_one_if_digit_already_in_table(self):
        self.node.insert(self.insert_information)
        second_insert = InsertInformation(19, '')
        second_insert.next_digit  # skip the first digit to insert at leaf level
        information = self.node.insert(second_insert)
        assert_that(information.count).is_equal_to(2)

    def test_return_correct_smallest_value_on_multiple_inserts_to_same_pattern(self):
        self.node.insert(self.insert_information)
        second_insert = InsertInformation(19, '')
        second_insert.next_digit  # skip the first digit to insert at leaf level
        information = self.node.insert(second_insert)
        assert_that(information.smallest_value).is_equal_to(9)

    def test_node_returns_asterisk_value_count_if_it_is_larger(self):
        first_insert = InsertInformation(19, '9')
        first_insert.next_digit  # skip the first digit to insert at leaf level
        self.node.insert(first_insert)
        information = self.node.insert(self.insert_information)
        assert_that(information.count).is_equal_to(2)

    def test_node_returns_value_associated_with_larger_count_on_insert_asterisk(self):
        first_insert = InsertInformation(19, '9')
        first_insert.next_digit  # skip the first digit to insert at leaf level
        self.node.insert(first_insert)
        information = self.node.insert(self.insert_information)
        assert_that(information.smallest_value).is_equal_to(19)
