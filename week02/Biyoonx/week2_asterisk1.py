import sys
read =sys.stdin.readline

print('\n'.join([f'{"*" * (idx + 1)}' for idx in range(int(read()))]))