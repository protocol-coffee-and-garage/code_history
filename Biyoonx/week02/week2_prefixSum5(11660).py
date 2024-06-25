import sys
read = sys.stdin.readline

# 시간 초과
'''
n, cnt = map(int, read().split())
sub_sum = [[0 for _ in range(n)] for _ in range(n)]

for line in range(n):
	  for idx, num in enumerate([*map(int, read().split())]):
 		    sub_sum[line][idx] = num + (sub_sum[line][idx - 1] if idx != 0 else 0)

for _ in range(cnt):
    x1, y1, x2, y2 = map(int, read().split())
    sum = 0
    for x in range(x1, x2 + 1):
        sum += (sub_sum[x - 1][y2 - 1] - (sub_sum[x - 1][y1 - 2] if y1 > 1 else 0))
    print(sum)
'''

# 파이썬에서 리스트는 일반적인 배열처럼 값을 저장하는 구조가 아니라 참조를 저장하는 형태. [0] * n으로 배열을 초기화하는 방식은 값을 얕은 복사하여 리스트를 중첩할 때는 얕은 복사의 문제가 발생. 1차원 배열일때 [0] * n 방식이 얕은 복사라도 문제가 되지 않는 이유는 숫자나 문자열(+튜플)은 "불변 객체"이므로 값이 변경될 수 없어 참조 공유가 문제되지 않음. 1차원 배열이어도 딕셔너리, 집합과 같은 가변객체를 저장할 경우 문제가 될 수 있음

n, cnt = map(int, read().split())
sub_sum = [[0] * n for _ in range(n)]

for row in range(n):
		num_line = [*map(int, read().split())]
		for col in range(n):
				sub_sum[row][col] = (sub_sum[row][col - 1] if col != 0 else 0) + (sub_sum[row - 1][col] if row != 0 else 0) + num_line[col] - (sub_sum[row - 1][col - 1] if col != 0 and row != 0 else 0)

for _ in range(cnt):
    x1, y1, x2, y2 = map(int, read().split())
    range_sum = sub_sum[x2 - 1][y2 - 1] - (sub_sum[x1 - 2][y2 - 1] if x1 > 1 else 0) - (sub_sum[x2 - 1][y1 - 2] if y1 > 1 else 0) + (sub_sum[x1 - 2][y1 - 2] if x1 > 1 and y1 > 1 else 0)
    print(range_sum)

# 풀이
'''
n, m = map(int, read().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
		origin_row = [0] + [int(x) for x in read().split()]
		A.append(origin_row)

for i in range(1, n + 1):
		for j in range(1, n + 1):
				D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
		x1, y1, x2, y2 = map(int, read().split())
		result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
		print(result)
'''