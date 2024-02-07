import math

# Number of bits required
target_bits = 41

# Current number of bits
current_bits = 0

# Number of milliseconds in 1 year
milliseconds_in_year = 365 * 24 * 60 * 60 * 1000

# Counter for years
years = 1

# Iterate until the required number of bits is reached
while current_bits < target_bits:
    # int(2) = bin(10) = 2 bits. log2(2) = 1
    # int(3) = bin(11) = 2 bits. log2(3) = 1.584962500721156
    # int(4) = bin(100) = 3 bits. log2(4) = 2
    current_bits = (
        math.floor(math.log2(milliseconds_in_year * years)) + 1 if years > 0 else 0
    )
    years += 1

print("Number of years to reach", target_bits, "bits:", years)
