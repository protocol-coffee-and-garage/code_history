import sys
read = sys.stdin.readline

n = int(read())
num_list = [int(read()) for _ in range(n)]

for _ in range(n):
    for i in range(1, n):
        if num_list[i - 1] > num_list[i]:
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]

print('\n'.join(map(str, num_list)))