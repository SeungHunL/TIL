def get_secret_word(lst):
    word = ''
    for i in range(len(lst)):
        word += chr(lst[i])
    return word
get_secret_word([83, 115, 65, 102, 89])