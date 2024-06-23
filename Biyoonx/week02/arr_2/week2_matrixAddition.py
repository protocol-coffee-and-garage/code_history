import sys
read = sys.stdin.readline

num_of_line, num_of_elem = map(int, read().split())

arr1 = [list(map(int, read().split())) for _ in range(num_of_line)]
arr2 = [list(map(int, read().split())) for _ in range(num_of_line)]

'''
# 얕은 복사
# result = [[0] * num_of_elem] * num_of_line
# 깊은 복사
result = [[0 for _ in range(num_of_elem)] for _ in range(num_of_line)]
result_str = []
idx1, idx2 = 0, 0
while idx1 < num_of_line:
		result[idx1][idx2] = str(arr1[idx1][idx2] + arr2[idx1][idx2])
		idx2 += 1
		if idx2 == num_of_elem:
				result_str.append(' '.join(result[idx1]))
				idx1 += 1
				idx2 = 0

print('\n'.join(result_str))
'''

for num1, num2 in zip(arr1, arr2):
		print(' '.join(str(num1[idx] + num2[idx]) for idx in range(len(num1))))