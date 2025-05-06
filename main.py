import sys
from stats import word_count
from stats import character_count
from stats import sorted_dictionary
from stats import printing_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(sys.argv[1]))

filepath, wordcount = word_count(sys.argv[1])
character_dict = character_count(sys.argv[1])
dictnum_pair = sorted_dictionary(character_dict)
printing_dict(dictnum_pair, filepath, wordcount)