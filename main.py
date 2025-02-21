from stats import count_words, count_chars, sorted_dict_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    chars_dict = count_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    for char in chars_dict:
        if char.isalpha():
            print(f"{char}: {chars_dict[char]}")

    print("============= END ===============")


main()
