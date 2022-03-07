#indexing, list slicing

my_num = 7
my_str = "Hello!"

numbers = [2, 3, 5, 7, 11, 13]
#list

names = ["윤수", "혜린", "태호", "상혁"]

print(names)
print(numbers)


#indexing : list에서 각 요소(index)를 받아 오는것

#for example...
print(names[0])
print(names[1])
print(names[2])

print(numbers[1] + numbers[3])
# 10
print(names[0] + names[1])
# 윤수혜린

num_1 = numbers[1]
num_2 = numbers[3]

print(num_1 + num_2)

print(numbers[-5])
print(numbers[-6])
# 인덱스가 6개인경우 -6~5까지 접근가능

# 리스트 슬라이싱 (list slicing)

print(numbers[0:4])
# [0] 부터 4개 즉 [3]까지..

print(names[0:2])

print(numbers[:3])
# 처음부터 3개 즉 [2]까지..

new_list = numbers[:3] # [2, 3, 5]
print(new_list[2])

# 요소 값 update
print(numbers)
numbers[0] = 7
print(numbers)
# success

numbers[0] = numbers[0] + numbers[1]
print(numbers)