class AFNState:
    def __init__(self, name) -> None:
        self.name = name
        self.is_final = False
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
    
    def add_state(self, name):
        new_state = AFNState(name)
        self.states.update({name : new_state})
    
    def add_transition_to_state(self, state, symbol, next_state):
        next_states = self.states.get(state).transitions.get(symbol) or set()
        if len(next_states) > 0:
            next_states.add(next_state)
        else:
            self.states.get(state).transitions.update({symbol : next_states})
    
    def set_start_state(self, state):
        self.start_state = state
    
    def set_state_as_final(self, state):
        self.states.get(state).is_final = True
    
    def proccess_string(self, string, print_info=False):
        if print_info:
            print(f'Processing string {string}')
        
        current_states = [self.states.get(self.start_state)]

        for symbol in string:
            if print_info:
                print(f'Current states: {current_states}')
                print(f'Reading symbol: {symbol}')

            next_states = set()
            
            for state in current_states:
                if print_info:
                    print(f'Checking state: {state.name}')
                
                for next_state in state.transitions.get(symbol) or []:
                    if print_info:
                        print(f'Transition found to: {next_state}')
                    
                    next_states.add(next_state)
            
            if print_info:
                print(f'Next states: {next_states}')
            
            if not next_states:
                if print_info:
                    print('String rejected')
                    print('There are no valid transitions')
                
                return False

            current_states.clear()
            for state in next_states:
                current_states.append(self.states.get(state))
        
        if print_info:
            print('Finished proccessing string')
            print('Checking for final states')

        for state in current_states:
            if print_info:
                print(f'Checking if {state.name} is final')
            
            if state.is_final:
                if print_info:
                    print('String accepted')
                    print(f'{state.name} is final')
                
                return True
        
        if print_info:
            print('String rejected')
            print('There are no final states')
        
        return False

