import math

n = int(input())

tests = [list(map(int, input().split())) for x in range(n)]

for test in tests:
    a, b, c = test
    if a + math.ceil(c / 2) > b + math.floor(c / 2):
        print("First")
    else:
        print("Second")
