import sys
read = sys.stdin.readline

n = int(read())
n_list = [int(read()) for _ in range(n)]

# 시간 초과
'''
stack = [*range(1, n + 1)]
stack_sequence = []
top = -1

for item in n_list:
		idx = stack.index(item)
		if idx < top:
				stack_sequence.clear()
				stack_sequence.append('NO')
				break
		if top < idx:
				stack_sequence.extend(['+'] * (idx - top))
		stack_sequence.append('-')
		stack.remove(item)
		top = idx - 1

print('\n'.join(stack_sequence))
'''

top = 0
stack_list = [*range(1, n + 1)]
target_stack = []
result = []
for item in n_list:
		top = top if top < n else (n - 1)
		if item >= stack_list[top]:
				while top < n and item >= stack_list[top]:
						target_stack.append(stack_list[top])
						result.append('+')
						top += 1
				result.append('-')
				target_stack.pop()
		else: # item < stack_list[top]
				target = target_stack.pop()
				result.append('-')
				if target > item:
						result.clear()
						result.append('NO')
						break

print('\n'.join(result))