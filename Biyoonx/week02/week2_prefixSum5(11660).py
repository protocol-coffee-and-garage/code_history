import sys
read = sys.stdin.readline

import sys
read = sys.stdin.readline

n, cnt = map(int, read().split())
sub_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for line in range(n):
    for idx, num in enumerate([*map(int, read().split())]):
        sub_sum[line + 1][idx + 1] = sub_sum[line + 1][idx] + num
    print(sub_sum[line])
print(sub_sum[-1])

for _ in range(cnt):
    x1, y1, x2, y2 = map(int, read().split())
    sum = 0
    for y in range(y1, y2 + 1):
        sum += sub_sum[x2][y] - sub_sum[x1 - 1][y]
    print(sum)