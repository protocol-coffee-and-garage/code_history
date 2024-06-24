import sys
read = sys.stdin.readline

num_of_basket, change_cnt = map(int, read().split())
basket_list = [idx + 1 for idx in range(num_of_basket)]

for _ in range(change_cnt):
		idx1, idx2 = map(int, read().split())
		basket_list[idx1 - 1], basket_list[idx2 - 1] = basket_list[idx2 - 1], basket_list[idx1 - 1]

print(' '.join(map(str, basket_list)))