import sys
read = sys.stdin.readline

n, k = map(int, read().split())
t_list = list(map(int, read().split()))

sub_sum = sum(t_list[0:k])
sub_sum2 = sub_sum
for idx in range(n - k):
		sub_sum2 = sub_sum2 - t_list[idx] + t_list[idx + k]
		if sub_sum < sub_sum2:
				sub_sum = sub_sum2

print(sub_sum)