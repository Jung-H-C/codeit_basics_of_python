# #alias 예
# x = [2, 3, 5, 7, 11]
# y = x
# y[2] = 4
# print(x)
# print(y)

#alias 아님
x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4
print(x)
print(y)