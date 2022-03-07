# # function declaration
# def in_list(some_list, value):
#     i = 0
#     while i < len(some_list):
#         if (some_list[i] == value):
#             return True
#         i = i + 1
#     return False
#
#
#
# #테스트
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# print(in_list(primes, 7))
# print(in_list(primes, 12))
#
# print(7 in primes)
# print(12 in primes)

# 리스트 안의 리스트

# grades = [[62,75,77], [78,81,86], [85,91,89]]
#
# print(grades[0])
# print(grades[1])
# print(grades[2])
# print(grades[0][0])
#
# print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)

# sort 메소드

# numbers = [5, 3, 7, 1]
# numbers.sort()
# print(numbers)
#
# numbers = [5, 3, 7, 1]
# print(sorted(numbers))

numbers = [5, 3, 7, 1]

numbers.reverse()
print(numbers)

friends = ["규호", "지훈", "재용", "주호"]
# print(friends.index("규호"))
# print(friends.index("지훈"))
# print(friends.index("재용"))
print(friends.index("주호"))


print(friends)
friends.remove("지훈") # list.remove() : 해당 리스트의 요소를 지움
print("지웠습니다.")
print(friends)
print(friends.index("주호"))