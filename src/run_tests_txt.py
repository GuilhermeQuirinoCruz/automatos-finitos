# import src.parser.txt_parser as TxtParser
import parser.txt_parser as TXTParser

def main():
    txt_parser = TXTParser.TXTParser()
    txt_parser.parse_afd('tests/afd/teste_1.txt')

if __name__ == "__main__":
    main()