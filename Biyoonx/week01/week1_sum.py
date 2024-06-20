import sys
read = sys.stdin.readline

num_list = [*map(int, read().split())]
print(sum(num_list))

# 기존 답변
a, b, c = list(map(int, input().split()))
print(a + b + c)