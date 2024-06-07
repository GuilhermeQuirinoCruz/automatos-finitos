import src.parser.yaml_parser as YAMLParser
import src.parser.test_parser as TestParser

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

    print(test.test_fsm(afd, 2))

def run_all_afd_tests():
    test_yaml_parser_afd()
    print('')

    test_yaml_test_parser()
    print('')

    test_afd()

def test_yaml_parser_afn():
    print('> Testing the YAML parser for AFNs')
    parser = YAMLParser.YAMLParser()
    afn = parser.parse_afn('../../tests/afn/aa-bb.yaml')

def test_afn():
    print('> Testing the AFN')
    parser = YAMLParser.YAMLParser()
    afn = parser.parse_afn('../../tests/afn/aa-bb.yaml')

    test = TestParser.parse_yaml('../../tests/strings/str-aa-bb.yaml')
    print(test.test_fsm(afn, 2))

def main():
    test_afn()

if __name__ == "__main__":
    main()
