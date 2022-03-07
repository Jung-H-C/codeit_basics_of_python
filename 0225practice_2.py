# append del insert 배우기!
numbers = []

print(len(numbers))

numbers.append(10)
numbers.append(10)
numbers.append(10)
numbers.append(10)
numbers.append(10)
# .append -> list에 요소 추가
print(len(numbers))
print(numbers)

numbers.append(8)
print(len(numbers))

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)

del numbers[3]
# 요소 지우기 -> 3번쨰 요소가 삭제됨
print(numbers)

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)

numbers.insert(4, 37)
# 요소 추가하기 -> [4] 자리에 37 삽입
print(numbers)