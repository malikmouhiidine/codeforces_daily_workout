n = int(input())
tests = []

for x in range(n):
    _ = input()
    tests.append(list(map(int, input().split())))

for test in tests:
    min_index = test.index(min(test))
    product = 1
    for i, n in enumerate(test):
        if i == min_index:
            product *= n + 1
        else:
            product *= n
    print(product)
