# ctrl+/ = comment


# x = 2
# while x <= 100:
#     print(x)
#     x += 2


# i = 100
#
# while (i % 23 != 0):
#     i += 1
#
#
# print(i)

# 학점 계산기
#
# def print_grade(midterm_score, final_score):
#     total = midterm_score + final_score
#
#     if (total >= 90):
#         print("A")
#     elif (total >= 80):
#         print("B")
#     elif (total >= 70):
#         print("C")
#     elif (total >= 60):
#         print("D")
#     else:
#         print("F")
#
# #test
#
# print_grade(40, 45)
# print_grade(20, 35)
# print_grade(30, 32)
# print_grade(50, 45)

# 100이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력:

# i = 1
#
# while (i <= 100):
#     if (i % 8 == 0 and i % 12 != 0):
#         print(i)
#     i += 1


# 1000보다 작은 자연수 중 2또는 3의 배수의 합을 출력하시오

# i = 1
# count = 0
# while (i < 1000):
#     if (i % 2 == 0):
#         count = count + i
#     elif (i % 3 == 0):
#         count = count + i
#
#     i += 1
#
# print(count)
#

# 120의 약수를 모두 출력하고 개수를 출력하는 program을 짜시오.

i = 1
count = 0

while (i <= 120):
    if (120 % i == 0):
        count += 1
        print(i)

    i += 1

print("120의 약수는 총 "+str(count)+"개입니다.")