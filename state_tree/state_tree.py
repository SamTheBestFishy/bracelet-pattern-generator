import itertools as it


# TODO: define state as tuple of (string_seq, row)
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
    def is_valid_oneliner(self, string_seq, row):
        return all(self.pattern[row][i] in [ string_seq[i:i+2] for i in range(row%2, self.strings-(row+self.strings)%2, 2) ][i] for i in range(self.width-(row*(self.strings+1))%2))
    

    # TODO: better name for this method, fill out else statement, add terminate condition on reaching height
    def advance_dfs_stack(self):
        if self.dfs_stack:
            string_sequence, row = self.dfs_stack.pop()
            if self.is_valid(string_sequence,row) and string_sequence not in self.states[row]:
                self.states[row].append(string_sequence)
                self.dfs_stack+=children(string_sequence,row)
        else:
            raise Exception("dfs_stack is empty, please add new root node to it")
        

# TODO: a permutation is list of indices that tells which strings to swap
#       eg, the permutation [1,5] means swap strings at index 1 and 2, as well as strings at index 5 and 6
# TODO: calculate max_permutation based on parity of self.strings and row
def children(string_seq, row):
    children = set()
    max_permutation = []
    permutations = powerset(max_permutation)
    for permutation in permutations: 
        children.add((permute(string_seq,permutation),row+1))
    return list(children)

# TODO: figure out new way to do this without loop
def permute(string_seq, permutation):
    output = string_seq
    for i in permutation:
        output = string_seq[:i] + string_seq[i:i+1] + string_seq[i+2:]
    return output

# TODO: figure out which powerset function is faster
def powerset(x):
    return it.chain.from_iterable(it.combinations(x, r) for r in range(len(x)+1))

def powerset_2(x):
    for sl in it.product(*[[[], [i]] for i in x]):
        yield {j for i in sl for j in i}