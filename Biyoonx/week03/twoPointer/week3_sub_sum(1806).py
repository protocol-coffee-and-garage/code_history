import sys
read = sys.stdin.readline

n, s = map(int, read().split())
elem_list = list(map(int, read().split()))

idx1 = 0
idx2 = 0 # 부분합이 첫번째 원소만인 경우도 포함시킬 것
sub_sum = elem_list[idx1]
result = float("inf")
while idx1 < n and idx2 < n:
		if (sub_sum >= s):
				result = min(result, idx2 - idx1 + 1)
				sub_sum -= elem_list[idx1]
				idx1 += 1
		else: # sub_sum < s
				idx2 += 1
				if idx2 < n:
						sub_sum += elem_list[idx2]

print(result if result != float("inf") else 0)