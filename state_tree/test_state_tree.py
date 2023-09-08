import unittest
from state_tree import state_tree
from state_tree import powerset
import itertools as it

class TestIsValids(unittest.TestCase):

    def setUp(self):
        # Create an instance of state_tree with a sample pattern
        pattern_array = [
            ['A', 'B', 'C'],
            ['D', 'E'],
            ['A', 'D', 'F']
        ]
        strings_even = 6
        self.tree = state_tree(pattern_array, strings_even)

        pattern_array_odd = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['B', 'D', 'G']
        ]

        strings_odd = 7
        self.tree_odd = state_tree(pattern_array_odd, strings_odd)


    def test_is_valid(self):
        # Test cases for is_valid method
        self.assertTrue(self.tree.is_valid("ADBECF", 0))
        self.assertFalse(self.tree.is_valid("ABCDEF", 0))
        # Add more test cases here

    def test_check_validity_faster_maybe(self):

        self.assertTrue(self.tree.check_validity_faster_maybe("ADBECF", 0))
        self.assertFalse(self.tree.check_validity_faster_maybe("ABCDEF", 0))
        self.assertTrue(self.tree.check_validity_faster_maybe("ADBECF", 1))
        self.assertFalse(self.tree.check_validity_faster_maybe("ABCDEF", 1))
        self.assertTrue(self.tree.check_validity_faster_maybe("ABDEFC", 2))
        self.assertFalse(self.tree.check_validity_faster_maybe("ADBECF", 2))

        self.assertTrue(self.tree_odd.check_validity_faster_maybe("ADBECGF", 0))
        self.assertFalse(self.tree_odd.check_validity_faster_maybe("ABCDEFG", 0))
        self.assertTrue(self.tree_odd.check_validity_faster_maybe("ADBECGF", 1))
        self.assertFalse(self.tree_odd.check_validity_faster_maybe("ABCDEFG", 1))
        self.assertTrue(self.tree_odd.check_validity_faster_maybe("ABDEFGC", 2))
        self.assertFalse(self.tree_odd.check_validity_faster_maybe("ADBECFG", 2))        


    def test_is_row_valid(self):
        self.assertTrue(self.tree.is_row_valid("ADBECF", 0))
        self.assertFalse(self.tree.is_row_valid("ABCDEF", 0))
        self.assertTrue(self.tree.is_row_valid("ADBECF", 1))
        self.assertFalse(self.tree.is_row_valid("ABCDEF", 1))
        self.assertTrue(self.tree.is_row_valid("ABDEFC", 2))
        self.assertFalse(self.tree.is_row_valid("ADBECF", 2))

        self.assertTrue(self.tree_odd.is_row_valid("ADBECGF", 0))
        self.assertFalse(self.tree_odd.is_row_valid("ABCDEFG", 0))
        self.assertTrue(self.tree_odd.is_row_valid("ADBECGF", 1))
        self.assertFalse(self.tree_odd.is_row_valid("ABCDEFG", 1))
        self.assertTrue(self.tree_odd.is_row_valid("ABDEFGC", 2))
        self.assertFalse(self.tree_odd.is_row_valid("ADBECFG", 2))     


class TestItemProcessor(unittest.TestCase):

    def test(self):
        pass

    def test_process_dfs_stack_item_valid(self):
        # Add an item to the dfs_stack and test its processing
        self.tree.dfs_stack = [("DABECF", 0)]  # Replace with appropriate item
        print("value of self.tree.dfs_stack", self.tree.dfs_stack)
        self.tree.process_dfs_stack_item()
        print("value of self.tree.states", self.tree.states, ", value of self.tree.dfs_stack", self.tree.dfs_stack)

        # Add your assertions here to check if the states and dfs_stack were updated as expected
        self.assertEqual(len(self.tree.states[0]), 1)
        # self.assertEqual(len(self.tree.dfs_stack), 0)
        # Add more assertions as needed

    def test_process_dfs_stack_item_invalid(self):
        # Add an invalid item to the dfs_stack and test its processing
        self.tree.dfs_stack = [("XYZ", 0)]  # Replace with appropriate item
        self.tree.process_dfs_stack_item()

        # Add your assertions here to check if the states and dfs_stack were not updated
        self.assertEqual(len(self.tree.states[0]), 0)
        self.assertEqual(len(self.tree.dfs_stack), 0)
        # Add more assertions as needed

    # Add more test methods for other scenarios if needed
    def test_powerset(self):
        # Test the powerset function with a simple input
        input_set = {1, 2, 3}
        expected_result = set(it.chain.from_iterable(it.combinations(input_set, r) for r in range(len(input_set)+1)))

        result = set(powerset(input_set))
        print(result, expected_result)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    # Create test suites
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestIsValids)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(TestItemProcessor)


    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run specific test suites
    runner.run(suite1)
    # runner.run(suite2)