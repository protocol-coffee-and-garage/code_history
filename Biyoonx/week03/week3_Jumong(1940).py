import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
materials = [*map(int, read().split())]

# 합이 가장 큰 값부터 비교 >> 시간 초과
'''
materials.sort()
idx1 = 0
idx2 = n - 1
result = 0
while idx1 < n:
		sub_sum = materials[idx1] + materials[idx2]
		if (sub_sum == m):
				idx1 += 1
				idx2 = n - 1
				result += 1
		elif (sub_sum > m and idx1 + 1 < idx2):
				idx2 -= 1
		else:
				idx1 += 1
print(result)
'''

# 두 값의 합이니까 목표값에서 현재 포인터의 값을 뺀 값이랑 짝일 것
result = 0
for idx in range(n):
		sub = m - materials[idx]
		result += materials.count(sub)
print(result // 2)