# import src.parser.txt_parser as TxtParser
import parser.txt_parser as TXTParser

def test_automaton(automaton, test_strings):
    for string in test_strings:
        print('Aceita' if automaton.proccess_string(string, print_info=False) else 'Rejeita')

def test_afd():
    print('Testing AFD')

    txt_parser = TXTParser.TXTParser()
    (afd, test_strings) = txt_parser.parse_afd('src/tests/afd/teste_2.txt')
    test_automaton(afd, test_strings)

def test_afn():
    print('Testing AFN')

    txt_parser = TXTParser.TXTParser()
    (afn, test_strings) = txt_parser.parse_afn('src/tests/afn/teste_2.txt')
    test_automaton(afn, test_strings)

def main():
    # test_afd()
    test_afn()

if __name__ == "__main__":
    main()