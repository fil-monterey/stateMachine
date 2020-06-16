class StateMachine:
    def __init__(self, state, transitions):
        self.state = state
        self.transitions = transitions

    def is_accepted(self, state_machine, input_string):
        self.input_string = list(self.transitions)
        self.state_machine = state_machine
        for i in range(0, len(self.input_string)):
            if self.input_string[i] == 'a':
                self.state_machine = 'S1'
            elif self.input_string[i] == 'b':
                self.state_machine = 'S2'
            else:
                return False
        return True


S1 = StateMachine(0, 'abab')
print(S1.is_accepted('S1', 'abab'))

