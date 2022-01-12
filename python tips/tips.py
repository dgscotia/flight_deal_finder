import pandas as pd
import sys

# 1. Iterate with enumerate

" THE OLD WAY USING RANGE(LEN()) "
data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

" INSTEAD USE ENUMERATE "
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

# 2. Use list comprehension instead of for loops
" OLD WAY "
squares = []
for i in range(10):
    squares.append(i * i)

" NEW WAY "
squares = [i * i for i in range(10)]

# 3 Sort iterables with built-in sort method
data = [3, 5, 1, 10, 9]
sorted_data = sorted(data, reverse=False)
print(sorted_data)

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]
sorted_data = sorted(data, key=lambda x: x["age"])

# 4. Store unique values with sets
my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]
# sets have no duplicats
my_set = set(my_list)  # removes the duplicates from your list

# 5. Save memory with generators
new_list = [i for i in range(10000)]
print(sum(my_list))  # possible but long
# use generator comprehension
my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(new_list), "bytes")
print(sys.getsizeof(my_gen), "bytes")

# 6. Define default values in dict with .get() and .setdefault()
my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", default=0)

new_count = my_dict.setdefault("count", 0)  # count key is now available

# 7. Count hashable objects with collections.Counter
from collections import Counter

another_list = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9, 9]
counter = Counter(my_list)  # creates a dict that counts the items, ordered largest to smallest
print(counter[10])
most_common = counter.most_common(2)  # second most common item

# 8. Format strings with f-strings
i = 10
print(f"{i} squared is {i * i}")

# 9. Concatenate strings with .join()
list_of_strings = ["hello", "from", "beyond"]
new_string = " ".join(list_of_strings)

# 10. Merge dictionaries with {**d1, **d2}
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "Paris"}

merged_d = {**d1, **d2}

# 10. Simplify f statement with if x in [a,b,c]
colors = ["red", "green", "blue"]
c = "red"
""" BAD WAY """
if c=="red" or c=="green" or c=="blue":
    print("is primary color")

""" GOOD WAY """
if c in colors:
    print("is primary color")