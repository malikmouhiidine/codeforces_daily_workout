n = int(input())

tests = []

for x in range(n):
    _ = input()
    tests.append(list(map(int, input().split())))

for test in tests:
    if not ((sum(test) / 2) % 1):
        print("YES")
    else:
        print("NO")
