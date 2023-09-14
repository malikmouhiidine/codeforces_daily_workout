# link: https://codeforces.com/problemset/problem/1859/A
# difficulty: 800

tests_n = int(input())
a_rrays = []


def is_divisor(n, array):
    for x in array:
        if not (x / n) % 1:
            return True
    return False


def is_divided(n, array):
    for x in array:
        if not (n / x) % 1:
            return True
    return False


for i in range(tests_n):
    _ = int(input())
    a_rrays.append(list(map(int, input().split())))

for a in a_rrays:
    a = sorted(a)
    b = []
    c = []

    for n in a:
        if not len(b):
            b.append(n)
        elif not len(c) and not is_divisor(n, b):
            c.append(n)
        elif not is_divided(n, c):
            b.append(n)
        elif not is_divisor(n, b):
            c.append(n)

    if len(b) and len(c):
        print(len(b), len(c))
        print(*b)
        print(*c)
    else:
        print("-1")