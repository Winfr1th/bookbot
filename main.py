from stats import get_num_words, char_counts, sort_char
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read() 
        num = get_num_words(file_contents)
        sorted_char = sort_char(char_counts(file_contents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for char in sorted_char:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']} ")
        else:
            continue
    print("============= END ===============")
    return f""
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    print(get_book_text(sys.argv[1]))
    

main()
