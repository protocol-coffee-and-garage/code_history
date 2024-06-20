import sys
read = sys.stdin.readline

num_line = int(read())
num_set = sorted({int(read()) for _ in range(num_line)})
for num in num_set:
    print(num)