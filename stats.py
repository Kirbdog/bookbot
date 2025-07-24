def count_words(text_to_count):
    split_words = text_to_count.split()
    num_words = len(split_words)
    return num_words

def count_characters(book_text):
    character_dict = {}
    book_text = book_text.lower()
    character_list = list(book_text)
    for char in character_list:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict
