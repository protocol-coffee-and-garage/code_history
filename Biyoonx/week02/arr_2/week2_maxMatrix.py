import sys
read = sys.stdin.readline

num_list = [list(map(int, read().split())) for _ in range(9)]

# 초기값을 -1(또는 -Inf)가 아니라 0으로 했을 때 최댓값 인덱스가 초기화되지 않는 문제가 있음
max_num = -1
max_row, max_col = 0, 0
for idx in range(9):
		row_max = max(num_list[idx])
		if (max_num < row_max):
				max_num = row_max
				max_row, max_col = (idx + 1), (num_list[idx].index(row_max) + 1)

print(max_num)
print(max_row, max_col)