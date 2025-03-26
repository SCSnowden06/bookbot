from stats import get_book_text , get_num_words , get_num_char , get_char_count , order_char_count

def main():
    filePath = "books/frankenstein.txt"
    bookText = get_book_text(filePath)
    amtWords = get_num_words(bookText)
    charCount = get_char_count(bookText)
    orderedCount = order_char_count(charCount)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {amtWords} total words")
    print("--------- Character Count -------")
    for item in orderedCount:
        print(item)
    print("============= END ===============")

main()


