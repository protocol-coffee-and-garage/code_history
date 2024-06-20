import sys
read = sys.stdin.readline

# num_of_int = int(read())
read()
num_list = [*map(int, read().split())]

print(min(num_list), max(num_list))