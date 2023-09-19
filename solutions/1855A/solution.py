import math

n = int(input())
tests = []

for x in range(n):
    students = [i + 1 for i in range(int(input()))]
    chairs = list(map(int, input().split()))
    tests.append((students, chairs))


def calc_identical(a, b):
    counter = 0
    for x, y in zip(a, b):
        if x == y:
            counter += 1
    return counter


for students, chairs in tests:
    print(math.ceil(calc_identical(students, chairs) / 2))
