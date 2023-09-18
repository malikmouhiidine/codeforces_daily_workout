tests = []
ntests = int(input())

for i in range(ntests):
    tests.append(list(map(int, input().split())))

for n, k, x in tests:
    if k > x and k - x != 1 or n < k:
        print(-1)
        continue
    X = x if x != k else k - 1
    result = int(X * (n - k) + ((k * (k - 1)) / 2))
    if result >= 0:
        print(result)
    else:
        print(-1)
