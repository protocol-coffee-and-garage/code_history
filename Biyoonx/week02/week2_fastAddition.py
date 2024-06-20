import sys
read = sys.stdin.readline

num_line = int(read())
for _ in range(num_line):
    print(sum(map(int, read().split())))