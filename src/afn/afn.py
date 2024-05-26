class AFNState:
    def __init__(self, name, types) -> None:
        self.name = name
        self.types = types
        self.transitions = {}

class AFN:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet
        self.states = {}
        self.start_state = ''
    
    def add_state(self, name, types):
        new_state = AFNState(name, types)
        self.states.update({name : new_state})

        if 'start' in types:
            self.start_state = name
    
    def add_transition_to_state(self, state, symbol, next_states):
        self.states.get(state).transitions.update({symbol : next_states})