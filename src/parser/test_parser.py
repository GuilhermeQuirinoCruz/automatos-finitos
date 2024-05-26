import yaml

import os

class Test():
    def __init__(self, strings_accept, strings_reject) -> None:
        self.strings_accept = strings_accept
        self.strings_reject = strings_reject
    
    def proccess_strings(self, afd, verbose, strings, expected):
        expected_string = 'accept' if expected else 'reject'
        for string in strings:
            if verbose > 0:
                print(f'Processing string {string}')
                print(f'Expected result: {expected_string}')
            
            if afd.proccess_string(string, print_info=(verbose > 1)) != expected:
                if verbose > 0:
                    print(f'Unexpected result: {'rejected' if expected else 'accepted'}')
                
                return False
            else:
                if verbose > 0:
                    print(f'Result: {expected_string}ed')

    def test_afd(self, afd, verbose=0):
        if not self.proccess_strings(afd, verbose, self.strings_accept, True):
            return False

        if verbose > 0:
            print("")
        
        if not self.proccess_strings(afd, verbose, self.strings_reject, False):
            return False

        return True

def parse_yaml(path):
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
        test_data = yaml.safe_load(file)
    
    return Test(test_data.get('accept'), test_data.get('reject'))
        