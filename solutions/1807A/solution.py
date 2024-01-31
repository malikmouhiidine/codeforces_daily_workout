i = int(input())
sol = []

for n in range(i):
    s = input().split()
    a, b, c = list(map(int, s))
    if a + b == c:
        sol.append("+")
    else:
        sol.append("-")

for s in sol:
    print(s)
