# type conversion, type casting

print(int(3.8)) # 3

print(float(3)) # 3.0

print(int("2") + int("5")) # 7

print(float("1.1") + float("2.5")) # 3.6

print(str(2) + str(5))  # 25

age = 7
print("제 나이는 " + str(age) + "살입니다.") # fine

# 문자열과 정수는 연결시킬 수 없음

# formatting

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "입니다.")
print("오늘은 2019년 10월 29일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day + 1))

print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠")) # 순서바꾸기 가능!

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
# f -> float, .2 -> 소숫점 둘째자리 반올림
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))
# 정수표현 -> :.0f