def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    print total

def purify(input):
    new_list = []
    for item in input:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

def product(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

def remove_duplicates(input):
    new_list = []
    for i in input:
        if i not in new_list:
            new_list.append(i)
    return new_list

def median(input):
    input = sorted(input)
    total = 0
    for i in input:
        total += 1
    median = total/2
    if total % 2 == 0:
        return (input[median]+input[median-1])/2.0
    else:
        return input[median]