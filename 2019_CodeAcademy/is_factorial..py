def factorial(x):
    total = 1
    if x < 0 or x - int(x) != 0:
        print "Not a positive integer."
    else:
        x_int = x
        while x_int > 0:
           total = total * x_int
           x_int -= 1
    print total

factorial(4)
factorial(-1)
factorial(10)
factorial(1)
