from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    print(get_book_text('books/frankenstein.txt'))
    book_text = get_book_text('books/frankenstein.txt')
    print(f'{count_words(book_text)} words found in the document')
    num_chars = count_characters(book_text)
    print(f'The number of each character in the book is {num_chars}')

main()
