n = int(input())
sols = []

for i in range(n):
    l = int(input())
    s = input()
    z = 0
    f = len(s)
    while (z < len(s)):
        if s[z] == 'B':
            z += 1
            break
        z += 1
    while (f > 0):
        if s[f - 1] == 'B':
            f -= 1
            break
        f -= 1
    sols.append(f + 1 - z + 1)

for sol in sols:
    print(sol)
