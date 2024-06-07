import os
import pathlib

class TXTParser:
    def parse_afd(self, path):
        full_path = os.path.join(os.getcwd(), path)
        with open(full_path, "r") as file:
            data = file.readlines()
        
        print(data)

    def parse_afn(self, path):
        pass

    def parse_afn_e(self, path):
        pass