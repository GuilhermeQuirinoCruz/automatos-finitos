import parser.yaml_parser as YAMLParser
import parser.test_parser as TestParser

import afd.afd as AFD
import afn
import afn_e

def test_yaml_parser_afd():
    print('> Testing the YAML parser for AFDs')
    parser = YAMLParser.YAMLParser()
    afd = parser.parse_afd('../../tests/afd/aa-bb.yaml')
    afd.proccess_string('ababab', print_info=True)

def test_yaml_test_parser():
    print('> Testing the YAML parser for tests')
    test = TestParser.parse_yaml('../../tests/strings/str-aa-bb.yaml')
    print(test.strings_accept)
    print(test.strings_reject)

def test_afd():
    print('> Testing both YAML parsers(AFDs and tests) and processing strings with the AFD')
    parser = YAMLParser.YAMLParser()
    afd = parser.parse_afd('../../tests/afd/aa-bb.yaml')
    test = TestParser.parse_yaml('../../tests/strings/str-aa-bb.yaml')

    print(test.test_afd(afd, 2))

def run_all_tests():
    test_yaml_parser_afd()
    print('')

    test_yaml_test_parser()
    print('')

    test_afd()

def main():
    test_afd()

if __name__ == "__main__":
    main()
