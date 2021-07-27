def duplicated_letters(word):
    wordl = []
    for i in range(len(word)):
        if word.count(word[i]) != 1:
            if word[i] not in wordl:
                wordl.append(word[i])
    return wordl
print(duplicated_letters('banana'))