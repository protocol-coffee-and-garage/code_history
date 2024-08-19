import sys
read = sys.stdin.readline

n, k = map(int, read().split())
x_list = [*map(int, read().split())]
x_list.sort(reverse = True)

print(x_list[k - 1])
