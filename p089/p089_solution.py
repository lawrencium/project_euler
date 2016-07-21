from p089.roman import compress
from util.filereader import read_file
from util.solutiontimer import time_function


def main():
    roman_numerals = read_file('p089_roman.txt')

    characters_saved = 0
    for roman_numeral in roman_numerals:
        original_number_characters = len(roman_numeral)

        compressed_result = compress(roman_numeral)
        new_number_characters = len(compressed_result)

        characters_saved += original_number_characters - new_number_characters

    print 'After compression, {} characters were saved when converting each Roman numeral into its minimal form.'.format(
        characters_saved)


if __name__ == '__main__':
    time_function(main)
