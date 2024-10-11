def count_words(file):
    file_as_array = file.split()
    
    return len(file_as_array)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print(count_words(file_contents))
    
    # print(file_contents)
