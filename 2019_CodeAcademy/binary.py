print 0b1,     # 1
print 0b10,    # 2
print 0b11,    # 3
print 0b100,   # 4
print 0b101,   # 5
print 0b110,   # 6
print 0b111,   # 7
print 0b1000,  # 8
print 0b1001,  # 9
print 0b1010   # 10


print 0b1, 0b10, 0b11, 0b100, 0b101, 0b110, 0b111, 0b1000, 0b1001, 0b1010, 0b1100, 0b1101, 0b1110, 0b1111, 0b10000

print 0b10000, 0b10001, 0b10010, 0b10011, 0b10100, 0b10101, 0b10110, 0b10111, 0b11000, 0b11001, 0b11010, 0b11011, 0b11100, 0b11101, 0b11110, 0b11111, 0b100000

# BIN FUNCTION - CONVERT INTEGER TO BINARY STRING
print bin(0),
print bin(1),
print bin(2),
print bin(4),
print bin(8),
print bin(16),
print bin(32),
print bin(64),
print bin(128),
print bin(256),
print bin(512),
print bin(1024)

print int("11001001",2)

print "\n"

#BITWISE OPERATORS
# SHIFT LEFT (MULTIPLY BY 2) AND SHIFT RIGHT (DIVIDE BY 2)
print 5 >> 4
print 5 << 1
print "\n"

# AND: Compares two numbers (A and B) and returns a number with the bits present in both A and B.
print 42 & 15, # Returns the number 10 (0b1010)
print bin(0b101010 & 0b1111) # Now in binary, returns number of 0b1010.

# OR: Compares two numbers (A and B) and returns a number with the bits present in either A or B.
print 42 | 15, # Returns the number 47 (0b101111)
print bin(0b101010 | 0b1111) # Now in binary, returns number of 0b101111.

# XOR: Compares two numbers (A and B) and returns a number with the bits present in either A or B, but not both.
print 42 ^ 15, # Returns the number 32 (0b10101)
print bin(0b101010 ^ 0b1111) # Now in binary, returns the number 0b100101.

# NOT: "Flips" all the bits in a single number. Equivalent to adding a digit and turning negative.
print bin(42),
print bin(~42)

# BIT MASK
num = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"

def check_bit4(input):
    mask = 0b1000
    if mask & input > 7:
        return "on"
    else:
        return "off"

print check_bit4(0b1000)

# Use Bit mask tu turn on a bit, or to make sure it is on
a = 0b110 # 6
mask = 0b1 # 1
desired = a | mask # 7 OR 0b111
print desired

# Use XOR to flip bits.
a - 0b110 # 6
mask = 0b111 # 7
desired = a ^ mask # 1 OR 0b1 [0b001]

# Use SHIFT to slide the masks into place
a = 0b101 # 10th bit mask
mask = (0b1 << 9) # one less than 10. Don't want to write whole bit, but slide over single bit 9 places to reach 10th bit.
desired = a ^ mask

def flip_bit(number, n):
  return bin(number ^ (0b1 << (n - 1)))