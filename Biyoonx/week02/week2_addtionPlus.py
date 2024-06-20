import sys
read = sys.stdin.readline

num_line = int(read())

for idx in range(num_line):
    print(f'Case #{idx + 1}: {sum(map(int, read().split()))}')