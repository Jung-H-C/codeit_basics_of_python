# list와 문자열 대조!!
# alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# alphabet_string = 'ABCDEFGH'
#
# print(alphabet_list[0])
# print(alphabet_list[2])
#
# print(alphabet_string[0])
# print(alphabet_string[2])
#
# #list slicing
# print(alphabet_list[0:5]) # [0]부터 [4]까지
# print(alphabet_list[4:]) # [4]부터
# print(alphabet_list[:4]) # [3]까지

#string slicing
# print(alphabet_string[0:5])

# list랑 str 모두 +로 concatenate 가능
# list랑 str 모두 len으로 길이 확인 가능

#문자열 리스트 차이
# numbers = [1, 2, 3, 4]
# numbers[0] = 5
# print(numbers)

# BUT, 문자열은 수정이 불가능 합니다!
# 문자열 더하는것은 얼마든지 가능합니다!

# name = 'Jung' + 'HyeonCheol'
# print(name)

# def sum_digit(num):
#     Num = str(num)
#     sum = 0
#     for i in Num:
#         sum = sum + int(i)
#     return sum
#
#
# sum = 0
# for i in range(1, 1001):
#     sum = sum + sum_digit(i)
#
# print(sum)

#주민등록번호 가리기

def mask_security_number(security_number):
    new_number = security_number[:-4] + "****"
    return new_number

print(mask_security_number("990312-1067726"))
print(mask_security_number("9903121067726"))
