def count_words(file):
    file_as_array = file.split()
    num_words = 0

    for word in file_as_array:
        num_words += 1
    return num_words

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print(count_words(file_contents))
    
    # print(file_contents)
