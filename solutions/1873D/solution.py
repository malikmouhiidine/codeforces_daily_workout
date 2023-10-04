j = int(input())
tests = []

for i in range(j):
    tests.append((*list(map(int, input().split())), input()))

for test in tests:
    n, k, s = test
    m = 0
    i = 0
    while i < n:
        if s[i] == "B":
            m += 1
            i += k
        else:
            i += 1
    print(m)
