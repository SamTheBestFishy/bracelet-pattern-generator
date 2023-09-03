import itertools as it

class parity_handler:
    def __init__(self, strings):
        self.parity = len(strings) % 2




# TODO: define state as tuple of (string_sequence, row)
class state_tree:
    def __init__(self, pattern_array, strings=None):
        self.pattern = pattern_array
        self.width = len(pattern_array[0])
        self.height = len(pattern_array)
        if strings is None:
            self.strings = 2*self.width
        else:
            self.strings = strings
        self.states = [[]]*self.height
        self.dfs_stack = []

    # TODO: try to parallelize the checking
    def is_valid(self, string_sequence, row):

        knots = self.pattern[row]

        if self.strings % 2 == 1 and row % 2 == 0: #For bracelets with odd strings
            preknots = [ string_sequence[i:i+2] for i in range(0, self.strings-1, 2) ]
        elif self.strings % 2 == 1 and row % 2 == 1:
            preknots = [ string_sequence[i:i+2] for i in range(1, self.strings, 2) ]
        elif self.strings % 2 == 0 and row % 2 == 0:
            preknots = [ string_sequence[i:i+2] for i in range(0, self.strings, 2) ]
        elif self.strings % 2 == 0 and row % 2 == 1:
            preknots = [ string_sequence[i:i+2] for i in range(1, self.strings-1, 2) ]
        else: # This should never happen
            raise Exception("self.strings or row is not an integer")

        # TODO: even strings, odd row case        
        for i in range(self.width):
            if knots[i] not in preknots[i]:
                return False
        return True
    

    # TODO: try to parallelize the checking
    def check_validity_faster_maybe(self, string_sequence, row):
        knots = self.pattern[row]
        preknots = [ string_sequence[i:i+2] for i in range(row%2, self.strings-(row+self.strings)%2, 2) ]
        return all(knots[i] in preknots[i] for i in range(self.width-(row*(self.strings+1))%2))
        
        # knots = self.pattern[row]
        # if row%2 == 1 and self.strings%2 == 0:
        #   knots.pop()
        # preknots = [ string_sequence[i:i+2] for i in range(row%2, self.strings-(row+self.strings)%2, 2) ]
        # # return all(knots[i] in preknots[i] for i in len(knots))


    # science has gone too far - don't use this please
    def is_valid_oneliner(self, string_sequence, row):
        return all(self.pattern[row][i] in [ string_sequence[i:i+2] for i in range(row%2, self.strings-(row+self.strings)%2, 2) ][i] for i in range(self.width-(row*(self.strings+1))%2))
    

    # TODO: better name for this method, fill out else statement, add terminate condition on reaching height
    def process_dfs_stack_item(self):
        print("starting this function")
        if self.dfs_stack:
            print(self.dfs_stack)
            string_sequence, row = self.dfs_stack.pop()
            print(self.states)
            print("before if", self.is_valid(string_sequence,row), string_sequence, self.states[row])
            if self.is_valid(string_sequence,row) and string_sequence not in self.states[row]:
                self.states[row].append(string_sequence)
                print("before children", string_sequence)
                self.dfs_stack+=children(string_sequence,row)
        else:
            raise Exception("dfs_stack is empty, please add new root node to it")
        

# TODO: a permutation is list of indices that tells which strings to swap
#       eg, the permutation [1,5] means swap strings at index 1 and 2, as well as strings at index 5 and 6
# TODO: calculate max_permutation based on parity of self.strings and row
def children(string_sequence, row):
    print("inside children", string_sequence)
    children = set()
    max_permutation = calculate_max_permutation()
    permutations = powerset_2(max_permutation)
    print(permutations)
    for permutation in permutations: 
        print("inside for", permutation)
        children.add((permute(string_sequence,permutation),row+1))
    return list(children)

# TODO: figure out new way to do this without loop
def permute(string_sequence, permutation):
    print("inside permute", permutation)
    output = string_sequence
    for i in permutation:
        print(i)
        output = string_sequence[:i] + string_sequence[i:i+1] + string_sequence[i+2:]
        print("output", output)
    return output

def calculate_max_permutation(length, row):
    max_permutation = []

    # Check the parity of self.strings and row
    if self.strings % 2 == 0:
        # For even self.strings, there is no need to adjust max_permutation
        pass
    elif row % 2 == 1:
        # For odd self.strings and odd row, adjust max_permutation to exclude the last string
        max_permutation = [i for i in range(self.strings - 1)]
    else:
        # For odd self.strings and even row, no adjustment is needed
        max_permutation = [i for i in range(self.strings)]

    return max_permutation


# TODO: figure out which powerset function is faster
def powerset(x):
    return it.chain.from_iterable(it.combinations(x, r) for r in range(len(x)+1))

def powerset_2(x):
    for sl in it.product(*[[[], [i]] for i in x]):
        yield {j for i in sl for j in i}


