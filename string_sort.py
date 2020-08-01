# input: string of words seperated by space
# output: string of words order alphabetically

def sort_word_list(full_string):
    list_of_words = full_string.split()
    list_of_words.sort(key=str.lower)
    # sorted_list_of_words = sorted(list_of_words, key=str.lower)
    print(list_of_words)