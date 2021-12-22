# ****** QUESTION 2 *****

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.


#  ****** SOLUTION *****

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

# ****** SOLUTION ****

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

# arr = [6, 2, 1, 4, 3, 5, 5, 2, 6, 6, 19]

# print(sorted(set(arr))[-2])


# ****** QUESTION 4 *****

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


# n = int(input())
# arr = map(int, input().split())
# print(sorted(set(arr))[-2])


# arr = [2, 4, 5, 5, 7, 9, 12, 18, 90, 38, 64, 51, 83]

# maxnum = sorted(set(arr))[-1]

# minnum = sorted(set(arr))[0]

# print(sorted(set(arr)), maxnum, minnum)


n = int(input())
score_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(
    sorted([name for name, score in score_list if score == second_highest])))


# score_list = []
# for _ in range(int(input())):
#     score = float(input())
#     score_list.append(score)
# print(score_list)
