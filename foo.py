# Checks whether x is divisible by k.
def is_divisible_by_k(x, k):
  return x%k == 0

# Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)

integers = [] # tuples () cannot be appended, only lists [] can
for i in range(1001): # python numbers are not inclusive
  if is_divisible_by_k(i, 2) or is_divisible_by_k(i, 3) or is_divisible_by_k(i, 7):
    integers.append(i)

# Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
total = sum(integers)
print(total)
