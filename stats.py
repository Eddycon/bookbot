def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        split_contents = file_contents.split()
        word_count = 0
        for word in split_contents:
            word_count += 1
    print(f"{word_count} words found in the document")
    return filepath, word_count

def character_count(filepath):
    character_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        lowercase_contents = file_contents.lower()
    for character in lowercase_contents:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sorted_dictionary(character_dict):
    dictnum_pairlist = []

    for char in character_dict:
        char_dict = {}
        char_num = {}
        char_dictnum = {}
        char_dict["char"] = char
        char_num["num"] = character_dict[char]
        for key in char_dict:
            char_dictnum[key] = char_dict[key]
        for key in char_num:
            char_dictnum[key] = char_num[key]
        dictnum_pairlist.append(char_dictnum)

    dictnum_pairlist.sort(reverse=True, key=sort_on)
    return dictnum_pairlist

def printing_dict(dictnum_pairlist, filepath, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in dictnum_pairlist:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

'''
Easier solution, could also optimise passing of functions - very clunky just now:

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
'''