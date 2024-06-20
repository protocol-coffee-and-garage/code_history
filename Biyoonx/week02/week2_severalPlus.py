import sys
read = sys.stdin.readline

num_line = int(read())
print('\n'.join([f'{sum(map(int, read().split()))}' for _ in range(num_line)]))