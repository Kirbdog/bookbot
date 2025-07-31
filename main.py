from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if sys.argv.__len__() < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    num_chars = count_words(book_text)
    sorted_text_info = sort_dict(count_characters(book_text))

    print('============ BOOKBOT ============\n'
        f'Analyzing book found at {book_path}...\n'
          '----------- Word Count ----------\n'
         f'Found {num_chars} total words\n'
          '--------- Character Count -------')

    for dict in range(0, sorted_text_info.__len__()):
        if sorted_text_info[dict]['char'].isalpha():
            print(f'{sorted_text_info[dict]['char']}: {sorted_text_info[dict]['num']}')
        else:
            dict += 1

main()
