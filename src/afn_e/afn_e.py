class AFNEState:
    def __init__(self, name, types) -> None:
        self.name = name
        self.types = types
        self.transitions = {}

class AFN_E:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet
        self.states = {}
        self.start_state = ''
    
    def add_state(self, name, types):
        new_state = AFNEState(name, types)
        self.states.update({name : new_state})

        if 'start' in types:
            self.start_state = name
    
    def add_transition_to_state(self, state, symbol, next_states):
        self.states.get(state).transitions.update({symbol : next_states})

    def add_empty_transitions(self, current_states):
        state_queue = set(current_states)

        while len(state_queue) > 0:
            next_states = self.states.get(state_queue.pop()).transitions.get('ε')
            if next_states:
                for state in next_states:
                    if state not in current_states:
                        current_states.add(state)
                        state_queue.add(state)
        
        return current_states

    def proccess_string(self, string, print_info):
        if print_info:
            print(f'Processing string {string}')
        
        current_states = set([self.start_state])
        self.add_empty_transitions(current_states)

        return

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
            
            if 'accept' in state.types:
                if print_info:
                    print('String accepted')
                    print(f'{state.name} is final')
                
                return True
        
        if print_info:
            print('String rejected')
            print('There are no final states')
        
        return False