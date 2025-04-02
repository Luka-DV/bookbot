import sys
from stats import count_book_words
from stats import count_book_characters
from stats import sort_char_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(file_path, word_count, sort_char_dict):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_object in sort_char_dict:
        if char_object["character"].isalpha():
            print(f"{char_object["character"]}: {char_object["count"]}")
    print("============= END ===============")
    
def main(file_path):
    #print(get_book_text("books/frankenstein.txt"))
    #file_path = "books/frankenstein.txt"

    book_string = get_book_text(file_path)

    word_count = count_book_words(book_string) 
    print(f"{word_count} words found in the document")

    char_counts_dict = count_book_characters(book_string)
    print(char_counts_dict)

    sorted_char_counts = sort_char_dict(char_counts_dict)

    print_report(file_path, word_count, sorted_char_counts)


main(file_path)
