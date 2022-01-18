# for i in range(1, int(input())):

#     print((10 ** (i) // 9) * i)

n = int(input())
name_number = [input().split() for _ in range(n)]
phone_book = {k: v for k, v in name_number}
print(phone_book)
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print('%s=%s' % (name, phone_book[name]))
#         else:
#             print('not found')
#     except:
#         break
