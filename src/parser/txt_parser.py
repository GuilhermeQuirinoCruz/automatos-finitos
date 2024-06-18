import os

import afd.afd as AFD
import afn.afn as AFN

class TXTParser:
    def extract_data(self, path):
        full_path = os.path.join(os.getcwd(), path)
        with open(full_path, 'r') as file:
            data = list(map(str.strip, file.readlines()))
        
        return data
    
    def parse_afd(self, path):
        data = self.extract_data(path)
        
        alphabet = data[0].split(' ')
        afd = AFD.AFD(alphabet)

        for state in data[1].split():
            afd.add_state(state)
        
        transition_amount = int(data[2])
        for i in range(transition_amount):
            (state, symbol, next_state) = data[3 + i].split()
            afd.add_transition_to_state(state, symbol, next_state)
        
        afd.set_start_state(data[3 + transition_amount])
        for state in data[4 + transition_amount].split():
            afd.set_state_as_final(state)

        test_strings = data[6 + transition_amount:]
        
        return afd, test_strings

    def parse_afn(self, path):
        data = self.extract_data(path)

        alphabet = data[0].split(' ')
        afn = AFN.AFN(alphabet)

        for state in data[1].split():
            afn.add_state(state)
        
        transition_amount = int(data[2])
        for i in range(transition_amount):
            (state, symbol, next_state) = data[3 + i].split()
            afn.add_transition_to_state(state, symbol, next_state)
        
        afn.set_start_state(data[3 + transition_amount])
        for state in data[4 + transition_amount].split():
            afn.set_state_as_final(state)

        test_strings = data[6 + transition_amount:]
        
        return afn, test_strings

    def parse_afn_e(self, path):
        pass