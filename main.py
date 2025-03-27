import sys
from stats import (
    get_book_text,
    get_num_words,
    get_char_count,
    order_char_count,
)


args = sys.argv


def main():
    file_path = args[1]
    book_text = get_book_text(file_path)
    amt_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    ordered_count = order_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{args[1]}'...")
    print("----------- Word Count ----------")
    print(f"Found {amt_words} total words")
    print("--------- Character Count -------")
    for item in ordered_count:
        print(item)
    print("============= END ===============")


if len(args) == 2:
    main()
    sys.exit(0)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
