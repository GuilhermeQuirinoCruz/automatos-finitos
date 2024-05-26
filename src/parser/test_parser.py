import yaml

import os

class Test():
    def __init__(self, strings_accept, strings_reject) -> None:
        self.strings_accept = strings_accept
        self.strings_reject = strings_reject
    
    def test_afd(self, afd, verbose=0):
        for accept in self.strings_accept:
            if verbose > 0:
                print(f'Processing string {accept}, should accept')
            
            if not afd.proccess_string(accept, print_info=(verbose > 1)):
                if verbose > 0:
                    print('Incorrectly rejected string')
                
                return False
        
        for reject in self.strings_reject:
            if verbose > 0:
                print(f'Processing string {reject}, should reject')
            
            if afd.proccess_string(reject, print_info=(verbose > 1)):
                if verbose > 0:
                    print('Incorrectly accepted string')
                
                return False

        return True

def parse_yaml(path):
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
        test_data = yaml.safe_load(file)
    
    return Test(test_data.get('accept'), test_data.get('reject'))
        