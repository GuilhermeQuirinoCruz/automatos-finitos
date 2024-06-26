class AFDState:
    def __init__(self, name) -> None:
        self.name = name
        self.is_final = False
        self.transitions = {}

class AFD:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet
        self.states = {}
        self.start_state = ''
    
    def add_state(self, name):
        new_state = AFDState(name)
        self.states.update({name : new_state})

    def add_transition_to_state(self, state, symbol, next_state):
        self.states.get(state).transitions.update({symbol : next_state})
    
    def set_start_state(self, state):
        self.start_state = state

    def set_state_as_final(self, state):
        self.states.get(state).is_final = True

    def proccess_string(self, string, print_info=False):
        if print_info:
            print(f'Processing string {string}')
        
        current_state = self.start_state

        for symbol in string:
            if print_info:
                print(f'Current state: {current_state}')
                print(f'Reading symbol: {symbol}')
            
            next_state = self.states.get(current_state).transitions.get(symbol)
            if not next_state:
                if print_info:
                    print('Transition not found')
                
                return False
            
            if print_info:
                print(f'Transitioning to state: {next_state}')

            current_state = next_state

        string_accepted = self.states.get(current_state).is_final
        if print_info:
            print('String accepted' if string_accepted else 'String rejected')
        
        return string_accepted