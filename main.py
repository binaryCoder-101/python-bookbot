def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    characters_count = get_characters_count(book_text)
    characters_count_sorted_list = characters_count_dict_to_sorted_list(characters_count)
    print_book_report(num_words, characters_count_sorted_list)

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_characters_count(text):
    lowered_text = text.lower()
    characters_count = {}
    for character in lowered_text:
        if character.isalpha():
            if character in characters_count:
                characters_count[character] += 1
            else:
                characters_count[character] = 1
    
    return characters_count

def characters_count_dict_to_sorted_list(characters_count):
    characters_count_sorted_list = []
    for key in characters_count:
        characters_count_sorted_list.append({"char" : key, "count" : characters_count[key]})
    characters_count_sorted_list.sort(key=key_for_sort, reverse=True)
    return characters_count_sorted_list

def key_for_sort(dict):
    return dict["count"]

def print_book_report(num_words, characters_count_sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for dict in characters_count_sorted_list:
        print(f"The '{dict['char']}' character was found {dict['count']} times")
    print("--- End report ---")

main()
