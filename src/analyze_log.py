# import csv
import re


def analyze_log(path_to_file):
    if not re.search('csv$', path_to_file):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as file:
            print(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
