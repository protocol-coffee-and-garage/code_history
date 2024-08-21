from functools import reduce
import sys
read = sys.stdin.readline

s = int(read())
a_list = [*map(int, read().split())]
b_list = [*map(int, read().split())]

sorted_a_list = sorted(a_list)
sorted_b_list = sorted(b_list, reverse = True)

# v1
# print(sum(map(lambda a: a[0] * a[1], [*zip(sorted_a_list, sorted_b_list)])))

# v2
print(reduce(lambda a, b: a + b, [x * y for x, y in zip(sorted_a_list, sorted_b_list)]))