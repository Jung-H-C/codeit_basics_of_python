wage = 5
exchange_rate = 1142.16

print("{}시간에 {}달러 벌었습니다.".format(1, wage * 1))
print("{}시간에 {}달러 벌었습니다.".format(5, wage * 5))
print("{}시간에 {}원 벌었습니다.".format(1, wage * 1 * exchange_rate))
print("{}시간에 {:.1f}원 벌었습니다.".format(5, wage * 5 * exchange_rate))

# 불린(Boolean)

print(True and True)
print(True and False)
print(not True)
print(not False)

print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)

# type 함수
# 자료형 확인에 용이

print(type(3)) # <class 'int'>
print(type(3.0)) # <class 'float'>
print(type("3")) # <class 'str'>

def hello():
    print("Hello world!")


print(type(hello)) # <class 'function'>