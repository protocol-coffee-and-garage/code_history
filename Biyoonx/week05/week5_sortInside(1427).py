import sys
read = sys.stdin.readline

n = sorted(read().strip(), reverse=True)

print(''.join(n))
# 혹은 오름차순으로 그냥 정렬하되 문자열 순서를 뒤집어도 될 듯

# 선택 정렬(내림차순이니까 최댓값이 처음으로 와야함)
'''
n = list(read().strip())

for idx in range(len(n)):
		max_idx = idx
		for i in range(idx + 1, len(n)):
				if n[i] > n[max_idx]:
						max_idx = i
		n[idx], n[max_idx] = n[max_idx], n[idx]
  
print(''.join(n))
'''