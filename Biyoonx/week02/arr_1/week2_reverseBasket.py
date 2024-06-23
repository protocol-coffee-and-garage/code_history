import sys
read = sys.stdin.readline

num_of_basket, reverse_num = map(int, read().split())
basket_list = [idx + 1 for idx in range(num_of_basket)]

for _ in range(reverse_num):
		idx1, idx2 = map(int, read().split())
		basket_list[idx1 - 1:idx2] = reversed(basket_list[idx1 - 1:idx2])

print(' '.join(map(str, basket_list)))