import sys
read = sys.stdin.readline

s = int(read())
a_list = [*map(int, read().split())]
b_list = list(map(lambda (i, v): (int(v), i), enumerate(read().split())))
print(b_list)