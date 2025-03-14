from stats import get_num_words
from stats import get_char_count_dictionary
from stats import get_sorted_dictionary
import sys

def get_book_text(filepath: str) -> str:
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Could not read file."

def print_book(num_words,sorted_char_dictionary):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_dictionary:
        print(f"{char}: {sorted_char_dictionary[char]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        filepath = sys.argv[1]
        # print(f"File path = {filepath}")
        book_contents = get_book_text(filepath)
        num_words = get_num_words(book_contents)
        print(f"Found {num_words} total words")
        unsorted_char_dictionary = get_char_count_dictionary(book_contents)
        # print(unsorted_char_dictionary)
        sorted_char_dictionary = get_sorted_dictionary(unsorted_char_dictionary)
        # print(sorted_char_dictionary)
        print_book(num_words,sorted_char_dictionary)
  
if __name__ == "__main__":
    main()
