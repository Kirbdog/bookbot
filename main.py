def num_letters(file):
    char_count = {}
    for char in file:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1

    return char_count

def count_words(file):
    file_as_array = file.split()
    return len(file_as_array)


with open("books/frankenstein.txt") as f:
    file_contents = f.read()


