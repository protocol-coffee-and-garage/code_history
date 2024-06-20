import sys
read = sys.stdin.readline

num_line = int(read())
for idx in range(num_line):
    a, b = map(int, read().split())
    print(f'Case #{idx + 1}: {a} + {b} = {a + b}')