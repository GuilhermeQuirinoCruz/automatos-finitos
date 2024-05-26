import yaml

import os
from collections import Counter

import afd.afd as AFD
import afn.afn as AFN

# https://gist.github.com/pypt/94d747fe5180851196eb
# https://stackoverflow.com/questions/44904290/getting-duplicate-keys-in-yaml-using-python
class PreserveDuplicatesLoader(yaml.loader.Loader):
    def construct_mapping(loader, node, deep=False):
        keys = [loader.construct_object(node, deep=deep) for node, _ in node.value]
        vals = [loader.construct_object(node, deep=deep) for _, node in node.value]
        key_count = Counter(keys)
        data = {}
        for key, val in zip(keys, vals):
            if key_count[key] > 1:
                if key not in data:
                    data[key] = []
                data[key].append(val)
            else:
                data[key] = val
        return data

class YAMLParser():
    def parse_afd(self, path):
        with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
            # afd_data = yaml.load(file, Loader=PreserveDuplicatesLoader)
            afd_data = yaml.safe_load(file)
        
        afd = AFD.AFD(afd_data['alphabet'])
        for state in afd_data['states']:
            afd.add_state(state['name'], tuple(state.get('types') or ['none']))

            for transition in state['transitions']:
                afd.add_transition_to_state(state['name'], transition['symbol'], transition['next_state'])

        return afd
    
    def parse_afn(self, path):
        with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
            afn_data = yaml.safe_load(file)
        
        afn = AFN.AFN(afn_data['alphabet'])
        for state in afn_data['states']:
            afn.add_state(state['name'], tuple(state.get('types') or ['none']))

            for transition in state['transitions']:
                afn.add_transition_to_state(state['name'], transition['symbol'], transition['next_states'])

        return afn