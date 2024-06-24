import sys
read = sys.stdin.readline

n, cnt = map(int, read().split())
sub_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for line in range(n):
    for idx, num in enumerate([*map(int, read().split())]):
        # 여기 인덱스가 문제 같음
        sub_sum[line][idx] = sub_sum[line][idx - 1] if (line != 0 and idx > 1) else 0 + num
for line in range(n + 1):
    print(sub_sum[line])

for _ in range(cnt):
    x1, y1, x2, y2 = map(int, read().split())
    sum = 0
    for y in range(y1, y2 + 1):
        print(y, x2, y, x1-1)
        print(sub_sum[y][x2], sub_sum[y][x1 - 1])
        sum += (sub_sum[y][x2] - sub_sum[y][x1 - 1])
		
    print(sum)