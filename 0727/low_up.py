def low_and_up(word):
    nword = ''
    if word[0].islower() == 0:
        nword += word[0]
        for i in range(1, len(word)):
            if i%2 == 1: 
                nword += word[i].lower() 
            if i%2 != 1: 
                nword += word[i].upper()
    else:
        nword += word[0]
        for i in range(1, len(word)):
            if i%2 == 1: 
                nword += word[i].upper() 
            if i%2 != 1: 
                nword += word[i].lower()
    return nword
print(low_and_up('BANana'))