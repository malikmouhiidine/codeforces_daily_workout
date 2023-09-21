n = int(input())
tests = []

for x in range(n):
    tests.append([list(input()) for i in range(10)])

for test in tests:
    points = 0
    for y in range(10):
        for x in range(10):
            if test[y][x] == "X":
                if 4 <= y and y <= 5 and 4 <= x and x <= 5:
                    points += 5
                elif 3 <= y and y <= 6 and 3 <= x and x <= 6:
                    points += 4
                elif 2 <= y and y <= 7 and 2 <= x and x <= 7:
                    points += 3
                elif 1 <= y and y <= 8 and 1 <= x and x <= 8:
                    points += 2
                else:
                    points += 1
    print(points)
