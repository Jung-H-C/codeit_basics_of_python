# function declaration
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if (some_list[i] == value):
            return True
        i = i + 1
    return False



#테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

print(7 in primes)
print(12 in primes)