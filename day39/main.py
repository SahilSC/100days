#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from day39.notification_manager import NotificationManager
# from day39.data_manager import DataManager
# from day39.flight_search import FlightSearch
# from day39.flight_data import FlightData

import random

# while True:
#     i = random.randint(12, 19)
#     ans = i ** 3
#     x=input(f"{i}^3=")
#     cnt = 0
#     while int(x) != ans and cnt != 1:
#         cnt += 1
#         x = input("Try again: ")
#     if int(x) != ans:
#         print(f"ans: {ans}")

# while True:
#     i = random.randint(1,9)
#     ans = round(i**(1/2),2)
#     x=input(f"sqrt({i})=")
#     cnt = 0
#     while float(x) != ans and cnt != 1:
#         cnt += 1
#         x = input("Try again: ")
#     if float(x) != ans:
#         print(f"ans: {ans}")

# cnter = 10
# ##ls = [17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29]
# ls = [17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29]
# while cnter!=0:
#     i = random.choice(ls)
#     ans = i ** 2
#     x=input(f"{i}^2=")
#     cnt = 0
#     while int(x) != ans and cnt != 1:
#         cnt += 1
#         x = input("Try again: ")
#     if int(x) != ans:
#         print(f"ans: {ans}")
#     cnt+=1

# while True:
#     b = random.randint(1,9)*100
#     c = random.randint(1, 31)
#     i = b+c
#     ans = i**2
#     x=input(f"{i}**2=")
#     cnt = 0
#     while float(x) != ans and cnt != 1:
#         cnt += 1
#         x = input("Try again: ")
#     if float(x) != ans:
#         print(f"ans: {ans}")

ls = [18, 22, 23, 24, 26, 28, 29]
while True:
    ans = random.choice(ls)
    i = ans ** 2
    x=input(f"sqrt({i})=")
    cnt = 0
    while int(x) != ans and cnt != 1:
        cnt += 1
        x = input("Try again: ")
    if int(x) != ans:
        print(f"ans: {ans}")

