from stats import get_book_text , get_num_words , get_num_char , get_char_count , order_char_count
import sys 

args = sys.argv

def main():
    filePath = args[1]
    bookText = get_book_text(filePath)
    amtWords = get_num_words(bookText)
    charCount = get_char_count(bookText)
    orderedCount = order_char_count(charCount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{args[1]}'...")
    print("----------- Word Count ----------")
    print(f"Found {amtWords} total words")
    print("--------- Character Count -------")
    for item in orderedCount:
        print(item)
    print("============= END ===============")
    

#if len(args) != 2:
    #print(f"Usage: python3 main.py <{args[1]}>\n")
    #sys.exit(1)
    #print('this is working')
#else:
    #main()

if len(args) == 2:
    main()
    sys.exit(0)
else:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

