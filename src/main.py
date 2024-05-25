import parser.yaml_parser as YAMLParser

import afd.afd as AFD
import afn
import afn_e

def test_afd():
    new_afd = AFD.AFD(['a', 'b'])
    new_afd.add_state('q0', 'start')
    new_afd.add_transition_to_state('q0', 'a', 'q1')
    new_afd.add_transition_to_state('q0', 'b', 'q2')

    new_afd.add_state('q1')
    new_afd.add_transition_to_state('q1', 'a', 'qf')
    new_afd.add_transition_to_state('q1', 'b', 'q2')

    new_afd.add_state('q2')
    new_afd.add_transition_to_state('q2', 'a', 'q1')
    new_afd.add_transition_to_state('q2', 'b', 'qf')

    new_afd.add_state('qf', 'accept')
    new_afd.add_transition_to_state('qf', 'a', 'qf')
    new_afd.add_transition_to_state('qf', 'b', 'qf')

    new_afd.proccess_string('aabbaa', print_info=True)
    new_afd.proccess_string('ababa', print_info=True)

def test_yaml_parser_afd():
    parser = YAMLParser.YAMLParser()
    # afd = parser.parse_afd('test.yaml')
    afd = parser.parse_afd('../../tests/examples/ex1.yaml')

test_yaml_parser_afd()