def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if (some_list[i] == value):
            return True
        i += 1
    return False


hello = [1, 2, 3, 4, 5, 20]

print(in_list(hello, 3))
print(in_list(hello, 6))

hello.reverse()

print(hello)

print(hello.index(20))

# list.index(int) -> int의 index를 반환함

# list.remove(value) -> list에서 첫번째로 value의 값을 갖고 있는 원소를 삭제함

fruits = ["딸기", "당근", "파인애플", "수박", "메론", "수박"]

fruits.remove("수박")

print(fruits)