n = int(input())
tests = []

for x in range(n):
    tests.append((int(input()), list(map(int, input().split()))))


def all_odd(array):
    for number in array:
        if is_even(number):
            return False
    return True


def all_even(array):
    for number in array:
        if not is_even(number):
            return False
    return True


def is_even(number):
    return True if not number % 2 else False


def same_parity(array1, array2):
    for a, b in zip(array1, array2):
        if a % 2 != b % 2:
            return False
    return True


for test in tests:
    array_len, array = test
    if sorted(array) == array or all_odd(array) or all_even(array):
        print("YES")
    else:
        if same_parity(sorted(array), array):
            print("YES")
        else:
            print("NO")
