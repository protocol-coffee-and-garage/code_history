import sys
read = sys.stdin.readline
def product(*num):
    if len(num) == 1:
        return num[0]
    return num[0] * product(*num[1:])

num_list = [*map(int, read().split())]

print(product(*num_list))

# 기존 작성 내용
a, b = list(map(int, input().split()))
print(a * b)
