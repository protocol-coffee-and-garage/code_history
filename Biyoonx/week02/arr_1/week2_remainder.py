import sys
read = sys.stdin.readline

num_list = {int(read()) % 42 for _ in range(10)}
print(len(num_list))