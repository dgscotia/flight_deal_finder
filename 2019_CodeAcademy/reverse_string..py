def reverse(text):
    text_fwd = str(text)
    new_string = ''
    for i in range(len(text_fwd), 0, -1):
        new_string += text_fwd[i-1]
    return new_string

reverse('duncan')