import sys
read = sys.stdin.readline

read()
print([*map(int, read().split())].count(int(read())))