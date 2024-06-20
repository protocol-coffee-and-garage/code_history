import sys
read = sys.stdin.readline

num = int(read())
print('\n'.join([f'{num} * {n + 1} = {num * (n + 1)}' for n in range(9)]))