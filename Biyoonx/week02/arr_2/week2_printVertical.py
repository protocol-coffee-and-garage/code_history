from itertools import zip_longest
import sys
read = sys.stdin.readline

str_list = [''.join(read().strip().split()) for _ in range(5)]

result = ''
for a in zip_longest(*str_list):
		result += ''.join(map(lambda x: x if x is not None else '', a))

print(result)