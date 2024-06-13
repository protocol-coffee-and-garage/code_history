import sys
read = sys.stdin.readline
num_list = [*map(int, read().split())] # num_list = list(map(int, read().split()))
print(num_list[0] + sum(-num_list[idx + 1] for idx in range(len(num_list[1:]))))

# 기존 답변
a, b = list(map(int, input().split()))
print(a - b)