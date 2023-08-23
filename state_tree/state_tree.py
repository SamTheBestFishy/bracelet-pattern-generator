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

    # TODO: adjust for offset or odd number of strings
    def check_validity(self, string_sequence, row):

        knots = self.pattern[row]

        if string_sequence % 2 == 1: #For bracelets with odd strings
            if row % 2 == 0:
                preknots = [ string_sequence[i:i+2] for i in range(0, self.strings-1, 2) ]
            else:
                preknots = [ string_sequence[i:i+2] for i in range(1, self.strings, 2) ]
        else:
            if row % 2 == 0:
                preknots = [ string_sequence[i:i+2] for i in range(0, self.strings, 2) ]
            else:
                preknots = [ string_sequence[i:i+2] for i in range(1, self.strings-1, 2) ]

        for i in range(self.width):
            if knots[i] not in preknots[i]:
                return False
        return True

