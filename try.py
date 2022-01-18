from datetime import datetime

# time = datetime.strptime(input(), "%H:%M")

# print("%s:%s" % (time.hour, time.minute))


# now = datetime.now()  # current date and time
# year = now.strftime("%Y")
# print(year)

# month = now.strftime("%m")
# print(month)

# day = now.strftime("%d")
# print(day)

# time = now.strftime("%H:%M:%S")
# print(" + (str(time) + ")

# date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(date)


# import json
# List = ["A", "B"]
# print json.dumps(List)
# ["A", "B"]


# sale = {input(): int(input())}
# print(sale)


# def work(shift) -> str:
#     sale = {input(): int(input())}
#     shift("make")
#     return sale


def process_shifts(path_to_csv):
    """

    :param path_to_csv: The path to the work_shift.csv
    :type string:
    :return: A dictionary with time as key (string) with format %H:%M
        (e.g. "18:00") and cost as value (Number)
    For example, it should be something like :
    {
        "17:00": 50,
        "22:00: 40,
    }
    In other words, for the hour beginning at 17:00, labour cost was
    50 pounds
    :rtype dict:
    """
    hour, minutes = (int(input()) for _ in range(2))
    now = datetime(2022, 1, 12, hour, minutes)
    time = now.strftime('%H:%M')
    return {time: int(input())}


print(process_shifts("path_to_csv"))


def process_sales(path_to_csv):
    """

    :param path_to_csv: The path to the transactions.csv
    :type string:
    :return: A dictionary with time (string) with format %H:%M as key and
    sales as value (string),
    and corresponding value with format %H:%M (e.g. "18:00"),
    and type float)
    For example, it should be something like :
    {
        "17:00": 250,
        "22:00": 0,
    },
    This means, for the hour beginning at 17:00, the sales were 250 dollars
    and for the hour beginning at 22:00, the sales were 0.

    :rtype dict:
    """
    hour, minutes = (int(input()) for _ in range(2))
    now = datetime(2022, 1, 12, hour, minutes)
    time = now.strftime('%H:%M')
    return {time: float(input())}


print(process_sales('path_to_csv'))


def compute_percentage(shifts, sales):
    """

    :param shifts:
    :type shifts: dict
    :param sales:
    :type sales: dict
    :return: A dictionary with time as key (string) with format %H:%M and
    percentage of labour cost per sales as value (float),
    If the sales are null, then return -cost instead of percentage
    For example, it should be something like :
    {
        "17:00": 20,
        "22:00": -40,
    }
    :rtype: dict
    """
    hour, minutes = (int(input()) for _ in range(2))
    now = datetime(2022, 1, 12, hour, minutes)
    percent_time = now.strftime('%H:%M')

    shifts = shifts.get(time)
    sales = sales.get(time)
    percentage = shifts // sales * 100
    if sales <= 0:
        percentage == -sales

    return {percent_time: float(percentage)}


def best_and_worst_hour(percentages):
    """

    Args:
    percentages: output of compute_percentage
    Return: list of strings, the first element should be the best hour,
    the second (and last) element should be the worst hour. Hour are
    represented by string with format %H:%M
    e.g. ["18:00", "20:00"]

    """
    sorted_keys = sorted(percentages, key=percentages.get)
    hours_worked = sorted_keys.reverse()
    return hours_worked
