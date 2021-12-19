# def check(n):
#     if n % 2 != 0:
#         print(" weired")
#     elif n % 2 == 0:
#         n >= 2 and n <= 5
#     print("not Weired")
#     elif n % 2 == 0:
#         n >= 6 and n <= 20
#     print("weired")
#     else:
#     print("pass")


# check(10)

# list comprehensions

# list comprehensions are used for creating a new list from existing iterables like tupels, strings, arrays list etc.

# a  list comprehension is made of
# 1. an expresion,
# 2. for element in old list
# 3. if condition

# a list comprehension has more time and space efficiency than loops   , it has fewer lines of code, it transforms iterative statement into a formula

# names = ['Sarah', 'Mike', 'Solomon', 'Siege', 'Harry', 'Simon']

# new_names = [x for x in names if len(x) <= 4]
# print(new_names)

# s_names = [x + ' staff member' for x in names if 'S' in x]

# print(s_names)


# for n in range(1, int(input()) + 1):
#     print(n, end='')


# ***** ADVANCED LIST COMPREHENSION *****

# x, y, z, n = (int(input()) for _ in range(4))

# print([[i, j, k] for i in range(x) for j in range(y)
#       for k in range(z) if i + j + k != n-1])

x, y, z, n = (int(input()) for _ in range(4))
print([[i, j, k] for i in range(x) for j in range(y)
      for k in range(z) if i + j + k != n-1])


# def multiply(n) -> int:
#     for i in range(1, 13):
#         result = n * i
#         print('{} * {} = {}'.format(n, i, result))


# multiply(2)


# n = int(input())
# a = [int(x) for x in input().split()]
# largest = secondlargest = -100
# for x in a:
#     if x > largest:
#         tmp = largest
#         largest = x
#         secondlargest = tmp
#     elif x > secondlargest and x != largest:
#         secondlargest = x
# print(secondlargest)
