import sys
read = sys.stdin.readline

n = int(read())
a_list = [*map(int, read().split())]

# 시간 초과
'''
def nge(std, nums):
		if not nums:
				return '-1'
		for n in nums:
				if n > std:
						return f'{n}'
		return '-1'

result = []
for idx, a in enumerate(a_list):
		result.append(nge(a, a_list[idx + 1:]))

print(' '.join(result))
'''

result = ['-1'] * n
stack = []

for idx in range(n):
		while stack and a_list[stack[-1]] < a_list[idx]:
				result[stack.pop()] = f'{a_list[idx]}'
		stack.append(idx)

print(' '.join(result))