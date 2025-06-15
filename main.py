import sys
from sys import argv
from stats import get_word_count, get_num_of_characters, format_dict

def main():
    args = sys.argv
    check_command_args(args)
    book_path = args[1]
    book_contents = get_book_text(book_path)
    book_word_count = get_word_count(book_contents)
    number_of_characters = get_num_of_characters(book_contents)
    sorted_characters = format_dict(number_of_characters)
    print_report(book_path, book_word_count, sorted_characters)

def check_command_args(command_args):
    if len(command_args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(book_path, book_word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print(f"--------- Character Count -------")
    for character in sorted_characters:
        if character['char'].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

main()