import sys
read = sys.stdin.readline

num = int(read())
print('\n'.join([f'{"*" * (idx + 1)}'.rjust(num, ' ') for idx in range(num)]))