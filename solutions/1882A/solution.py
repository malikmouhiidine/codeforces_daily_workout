n = int(input())
tests = []


def no_one_repeat(array1, array2):
    for a, b in zip(array1, array2):
        if a == b:
            return False
    return True


for x in range(n):
    _ = input()
    tests.append(list(map(int, input().split())))

for a in tests:
    b = []
    b.append(1 if a[0] != 1 else 2)
    a.pop(0)
    for i in a:
        b.append(b[-1] + 1 if b[-1] + 1 != i else i + 1)
    print(b[-1])
