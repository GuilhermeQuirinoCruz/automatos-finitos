class AFDState:
    def __init__(self, name, types) -> None:
        self.name = name
        self.types = types
        self.transitions = {}

class AFD:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet
        self.states = {}
        self.start_state = ''
    
    def add_state(self, name, types=('none')):
        new_state = AFDState(name, types)
        self.states.update({name : new_state})

        if type == 'start':
            self.start_state = name

    def add_transition_to_state(self, state, symbol, next_state):
        self.states.get(state).transitions.update({symbol : next_state})

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

        accept_string = self.states.get(current_state).type == 'accept'
        if print_info:
            print('String accepted' if accept_string else 'String rejected')
        
        return accept_string