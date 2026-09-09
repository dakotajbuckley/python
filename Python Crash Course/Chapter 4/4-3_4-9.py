# 4.3
for value in range(1,21):
    print(value)

# 4.4 
numbers = [value for value in range(1, 1000001)]
# for number in numbers:
#     print(numbers)

# 4.5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6
odd_nums = [value for value in range(1, 21, 2)]
for value in odd_nums:
    print(value)

# 4.7
multiples = [value for value in range(3, 31, 3)]
for value in multiples:
    print(value)

# 4.8
cubes = [value**3 for value in range(1,11)]
for value in cubes:
    print(value)