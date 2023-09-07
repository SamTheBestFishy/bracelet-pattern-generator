import itertools as it

class state_tree:
    def __init__(self, pattern_array, string_count=None):
        self.pattern = pattern_array
        self.width = len(pattern_array[0])
        self.height = len(pattern_array)
        if string_count is None:
            self.string_count = 2*self.width
        else:
            self.string_count = string_count
        self.states = [[]]*self.height # TODO: define state as tuple of (string_sequence, row)
        self.dfs_stack = []
        self.parity = self.string_count % 2
        self.max_permutations = [range(0, self.string_count - self.parity, 2),range(1, self.string_count - 1, 2)]
        self.permutations = powerset(self.max_permutations)

    def powerset(x):
        return it.chain.from_iterable(it.combinations(x, r) for r in range(len(x)+1))

    def process_dfs_stack_item(self):
        #print("starting this function")
        if self.dfs_stack:
            string_sequence, row = self.dfs_stack.pop()
            # print(self.states)
            # print("before if", self.is_row_valid(string_sequence,row), string_sequence, self.states[row])
            if self.is_row_valid(string_sequence,row) and string_sequence not in self.states[row]:
                self.states[row].append(string_sequence)
                # print("before children", string_sequence)
                self.dfs_stack+=children(string_sequence,row)
        else:
            raise Exception("dfs_stack is empty, please add new root node to it")
    
    def is_row_valid(self, string_sequence, row):
        knots = self.pattern[row]

        parity_comparison = (row%2 != self.parity)
        preknots = [ string_sequence[i:i+2] for i in range(row_parity, self.string_count - parity_comparison, 2)]
        return all(knots[i] in preknots[i] for i in range(self.width-(parity_comparison-self.parity)))