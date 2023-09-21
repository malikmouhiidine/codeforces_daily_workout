n = int(input())
tests = []

for x in range(n):
    tests.append(input())

for test in tests:
    if test == "abc" or test == "acb" or test == "bac" or test == "cba":
        print("YES")
    else:
        print("NO")
