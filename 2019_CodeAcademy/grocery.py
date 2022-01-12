prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
total = 0

for key in prices:
    subtotal = prices[key] * stock[key]
    print("Subtotal for %s is " % key + str(subtotal) + ".")
    total += subtotal

print("Total stock value is " + str(total) + ".")
