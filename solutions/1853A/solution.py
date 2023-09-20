import math

n = int(input())
tests = []

for x in range(n):
    tests.append((int(input()), list(map(int, input().split()))))

for array_len, array in tests:
    if sorted(array) != array:
        print(0)
        continue
    lowest_diff = float("inf")
    lowest_diff_idx = -1
    for i in range(array_len - 1):
        #   print(array[i + 1] - array[i])
        if array[i + 1] - array[i] <= lowest_diff:
            lowest_diff = array[i + 1] - array[i]
            lowest_diff_idx = i + 1
    # print(lowest_diff, lowest_diff_idx, array, array_len)
    print(math.ceil((array[lowest_diff_idx] - array[lowest_diff_idx - 1] + 1) / 2))
