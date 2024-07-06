import sys
read = sys.stdin.readline

# 시간 초과
'''
n = int(read())
a_list = list(map(int, read().split()))
m = int(read())
m_list = list(map(int, read().split()))

result = []
for idx1 in range(m):
		for idx2 in range(n):
				if (a_list[idx2] == m_list[idx1]):
						result.append('1')
		if (len(result) == idx1):
				result.append('0')

print('\n'.join(result))
'''

n = int(read())
a_dict = dict.fromkeys(map(int, read().split()), True)
m = int(read())
m_list = list(map(int, read().split()))

for item in m_list:
		print(int(item in a_dict))