# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#
# for i in numbers:  # i 는 각 요소를 보관하는 변수
#     print(i)

# for number in range(100):  # parameter 1: 0~99
#     print(number)

# for number in range(3, 11): # parameter 2: 3~10
#     print(number)

# for number in range(0, 100, 2):
#     print(number)

# range 장점
#  간편함
#  깔끔함
#  메모리 효율성


# for i in range(11):
#     print("2^{} = {}".format(i, 2 ** i))

# 구구단 예제 만들기
# for i in range(1,10):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, i * j))

# 피타고라스 삼조 practice
# for a in range(1, 400):
#     for b in range(a, 400):
#         c = 400 - a - b
#
#         if a ** 2 + b ** 2 == c ** 2:
#             print(a * b * c)
#

# 리스트 원소 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for a in range(int(len(numbers) / 2)):
    tmp = numbers[a]
    numbers[a] = numbers[len(numbers) - 1 - a]
    numbers[len(numbers) - 1 - a] = tmp

print("뒤집어진 리스트: " + str(numbers))






















