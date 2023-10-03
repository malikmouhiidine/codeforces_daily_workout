j = int(input())
solutions = []

for i in range(j):
    y = int(input())
    players = []
    for x in range(y):
        players.append(list(map(int, input().split())))
    polycarp = players[0]
    players.pop(0)
    pw, pe = polycarp
    if (
        len(list(filter(lambda player: player[0] >= pw and player[1] >= pe, players)))
        > 0
    ):
        solutions.append(-1)
        continue
    solutions.append(pw)

for solution in solutions:
    print(solution)
