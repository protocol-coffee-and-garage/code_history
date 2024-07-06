import sys
read = sys.stdin.readline

n = int(read())
n_list = list(map(int, read().split()))
m = int(read())
m_list = list(map(int, read().split()))

cnt = dict.fromkeys(set(n_list), 0)
for item in n_list:
		if (item in cnt):
				cnt[item] += 1

result = []
for item in m_list:
		if (item in cnt):
				result.append(str(cnt.get(item)))
		else:
				result.append('0')

print(' '.join(result))