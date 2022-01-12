def anti_vowel(text):
    str(text)
    print text
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in text:
        if i not in vowels:
            new_string += i
    return new_string

anti_vowel('Taking Out All the Vowels!')