import sys
read = sys.stdin.readline

num_list = [int(read()) for _ in range(9)]
max_num = max(num_list)

print(max_num)
print(num_list.index(max_num) + 1)