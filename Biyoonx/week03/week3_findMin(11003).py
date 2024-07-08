import sys
read = sys.stdin.readline

n, l = map(int, read().split())
a_list = [*map(int, read().split())]
# 어려워....모르겟어....
result = []
min_num = float("inf")
for idx2 in range(n):
    target = a_list[(idx2 - l) if idx2 >= l else 0:idx2 + 1]
    target_min = min(target)
    min_num = min(target_min, min_num) if target_min  > 0 else min_num
    result.append(str(min_num))

print(' '.join(result))
