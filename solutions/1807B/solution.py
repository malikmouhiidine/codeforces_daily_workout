t = int(input())
sols = []

for w in range(t):
    _ = input()
    candies = input().split()
    candies = list(map(int, candies))

    if sum([num for num in candies if num % 2 != 1]) > sum([num for num in candies if num % 2 == 1]):
        sols.append("YES")
    else:
        sols.append("NO")

for sol in sols:
    print(sol)
