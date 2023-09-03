import unittest
from state_tree import state_tree
from state_tree import powerset
import itertools as it

class TestStateTree(unittest.TestCase):

    def setUp(self):
        # Create an instance of state_tree with a sample pattern
        pattern_array = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['A', 'D', 'F']
        ]
        strings = 6
        self.tree = state_tree(pattern_array, strings)

    def test_is_valid(self):
        # Test cases for is_valid method
        self.assertTrue(self.tree.is_valid("ADBECF", 0))
        self.assertFalse(self.tree.is_valid("ABCDEF", 0))
        # Add more test cases here

    def test_check_validity_faster_maybe(self):
        # Test check_validity_faster_maybe method using self.tree
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

    # def test_process_dfs_stack_item_invalid(self):
    #     # Add an invalid item to the dfs_stack and test its processing
    #     self.tree.dfs_stack = [("XYZ", 0)]  # Replace with appropriate item
    #     self.tree.process_dfs_stack_item()

    #     # Add your assertions here to check if the states and dfs_stack were not updated
    #     self.assertEqual(len(self.tree.states[0]), 0)
    #     self.assertEqual(len(self.tree.dfs_stack), 0)
    #     # Add more assertions as needed

    # # Add more test methods for other scenarios if needed
    def test_powerset(self):
        # Test the powerset function with a simple input
        input_set = {1, 2, 3}
        expected_result = set(it.chain.from_iterable(it.combinations(input_set, r) for r in range(len(input_set)+1)))

        result = set(powerset(input_set))
        print(result, expected_result)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()