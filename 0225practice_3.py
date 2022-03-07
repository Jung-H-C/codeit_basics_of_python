# sorted, sort함수
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

new_list = sorted(numbers)
print(new_list)

new_list = sorted(numbers, reverse=True)
# 반대로 정렬하기
print(new_list)
print(numbers)

# sorted 함수는 기존 리스트를 전혀 건드리지 않ㅇ므

print(numbers.sort())
# sort()함수는 아무것도 return 하지 않음 numbers리스트 자체를 sort함
print(numbers)

numbers.sort(reverse=True)

print(numbers)

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르", "아이아이아"]

i = 0

while i < len(greetings):
    print(greetings[i])
    i += 1


def fa_to_ce(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]

i = 0
celsius = []
print(celsius)

while i < len(temperature_list):
    celsius.append(round(fa_to_ce(temperature_list[i]), 1))
    i += 1

print(celsius)
print(len(celsius))

# round(float, int) -> float를 int개의 소숫점 자리에서 반올림