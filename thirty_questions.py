# ****** QUESTION 2 *****

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.


#  ****** SOLUTION 2*****

# meal_cost = float(input())
# tip_percent, tax_percent = (int(input().strip()) for _ in range(2))
# tip = meal_cost * tip_percent / 100
# tax = meal_cost * tax_percent / 100
# total = round(meal_cost + tip + tax)
# print('the total meal cost is ' + str(total) + ' dollars')


# ****** QUESTION 3 *****

# Task
# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# ****** SOLUTION 3 ****

# def check(n) -> int:
#     if n % 2 != 0:
#         print('Weird')
#     elif n in range(2, 6):
#         print('Not weird')
#     elif n <= 20:
#         print('Weird')
#     else:
#         print(' Not Wired')


# check(42)

# ************* EXTRA************

# To get the second highest in a list without repetition of any array element

# arr = [6, 2, 1, 4, 3, 5, 5, 2, 6, 6, 19]

# print(sorted(set(arr))[-2])


# ****** QUESTION 4 *****

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


# n = int(input())
# arr = map(int, input().split())
# print(sorted(set(arr))[-2])


# n = int(input())
# score_list = []
# for _ in range(int(input())):
#     score_list.append([input(), float(input())])
# second_highest = sorted(list(set([score for name, score in score_list])))[1]
# print('\n'.join([a for a, b in sorted(score_list) if b == second_highest]))


# score_list = []
# for _ in range(int(input())):
#     score = float(input())
#     score_list.append(score)
# print(score_list)


# *********EXTRA************

# arr =[] print the list element without duplicate, the highest and lowest number in the list.

# arr = [2, 4, 5, 5, 7, 9, 12, 18, 90, 38, 64, 51, 83]

# maxnum = sorted(set(arr))[-1]

# minnum = sorted(set(arr))[0]

# print(sorted(set(arr)), maxnum, minnum)

# ****** QUESTION 5 *****

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# ****** SOLUTION 5 *****

# N = int(input())
# L = []
# for _ in range(N):
#     args = input().strip().split(" ")
#     if args[0] == "append":
#         L.append(int(args[1]))
#         print(L)
#     elif args[0] == "insert":
#         L.insert(int(args[1]), int(args[2]))
#     elif args[0] == "remove":
#         L.remove()
#     elif args[0] == "sort":
#         L.sort()
#     elif args[0] == "pop":
#         L.pop()
#     elif args[0] == "pop":
#         L.pop()
#     elif args[0] == "print":
#         print(L)

# ****** QUESTION 6 *****

# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# n = int(input())
# integer_list = map(int, input().split())
# t = tuple(integer_list)
# print(hash(t))


# ****** QUESTION 7 *****
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# string line: a string of space-separated words
# Returns
# string: the resulting string

# def spilt_and_join(line) -> str:
#     x = line.split(" ")
#     x = '-'.join(x)
#     return x
#     print(x)


# spilt_and_join('this is a string')


# ****** QUESTION 8 *****

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2


# ****** SOLUTION 8 *****


def swap_case(s):
    return " ".join([i.lower() if i.isupper() else i.upper for i in s])


s = input()
result = swap_case(s)
print(result)
