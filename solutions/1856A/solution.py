n = int(input())
tests = []

for x in range(n):
    _ = input()
    tests.append(list(map(int, input().split())))

for test in tests:
    k = 0
    for i in range(len(test) - 1):
        if test[i] > test[i + 1] and test[i] > k:
            k = test[i]
    print(k)
