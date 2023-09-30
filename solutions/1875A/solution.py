j = int(input())
tests = []

for i in range(j):
    tests.append((list(map(int, input().split())), list(map(int, input().split()))))


for abn, tools in tests:
    a, b, n = abn
    tools = list(map(lambda n: n if a >= 1 + n else a - 1, tools))
    print(sum([b, sum(tools)]))
