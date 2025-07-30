from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text('books/frankenstein.txt')
    
    num_chars = count_words(book_text)
    sorted_text_info = sort_dict(count_characters(book_text))

    print('============ BOOKBOT ============\n'
          'Analyzing book found at books/frankenstein.txt...\n'
          '----------- Word Count ----------\n'
         f'Found {num_chars} total words\n'
          '--------- Character Count -------')

    for dict in range(0, sorted_text_info.__len__()):
        if sorted_text_info[dict]['char'].isalpha():
            print(f'{sorted_text_info[dict]['char']}: {sorted_text_info[dict]['num']}')
        else:
            dict += 1

main()
