from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_characters_count(book_text)
    print(f"{num_words} number of words found in the document")
    print(num_chars)

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
    characters_count_object = Counter(lowered_text)
    characters_count = dict(characters_count_object)
    return characters_count
    
main()