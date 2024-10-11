def count_words(file):
    file_as_array = file.split()
    
    num_words = len(file_as_array)
    
    return num_words

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print(count_words(file_contents))
    
    # print(file_contents)
