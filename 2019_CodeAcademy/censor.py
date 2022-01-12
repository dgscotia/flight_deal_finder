def censor(text, word):
    if str(word) in text:
        total = 0
        for i in word:
            total += 1
        count = total * '*'
    text = text.replace(word, count)
    return text

censor('Finding Duncan Duncan', 'Duncan')