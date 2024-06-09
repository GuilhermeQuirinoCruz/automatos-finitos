# import src.parser.txt_parser as TxtParser
import parser.txt_parser as TXTParser

def main():
    txt_parser = TXTParser.TXTParser()
    (afd, test_strings) = txt_parser.parse_afd('src/tests/afd/teste_2.txt')

    for string in test_strings:
        print('Aceita' if afd.proccess_string(string) else 'Rejeita')

if __name__ == "__main__":
    main()