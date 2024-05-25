class AFDState:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.transitions = {}

class AFD:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet
        self.states = {}
    
    def add_state(self, name, type='none'):
        new_state = AFDState(name, type)
        self.states.update({name : new_state})

    def add_transition_to_state(self, state, symbol, next_state):
        self.states.get(state).transitions.update({symbol : next_state})