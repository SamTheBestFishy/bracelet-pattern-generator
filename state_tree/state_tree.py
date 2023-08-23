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
        # for i in len(knots):
        #     if knots[i] not in preknots[i]:
        #         return False
        # return True
        # # return all(knots[i] in preknots[i] for i in len(knots))
    

    # TODO: better name for this method, fill out else statement
    def check_state(self):
        if self.dfs_stack:
            string_sequence, row = self.dfs_stack.pop()
            if self.is_valid(string_sequence,row) and string_sequence not in self.states[row]:
                self.states[row].append(string_sequence)
                self.dfs_stack.append(children(string_sequence,row))
        else:
            raise Exception("dfs_stack is empty, please add to it")
        

# TODO: define permutations (a permutation is list of indices that tells which strings to swap)
#       eg, the permutation [0,1,3,2] means keep the first two strings the same, but swap the last 2
def children(string_seq, row):
    children = set()
    for permutation in permutations:
        children.add((permute(string_seq,permutation),row+1))
    return list(children)

def permute(string_seq, permutation):
    output = string_seq
    for i in len(string_seq):
        output[i] = string_seq[permutation[i]]
    return output