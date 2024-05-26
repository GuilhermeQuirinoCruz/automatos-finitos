import yaml

import os

class Test():
    def __init__(self, strings_accept, strings_reject) -> None:
        self.strings_accept = strings_accept
        self.strings_reject = strings_reject

def parse_yaml(path):
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
        test_data = yaml.safe_load(file)
    
    return Test(test_data.get('accept'), test_data.get('reject'))
        