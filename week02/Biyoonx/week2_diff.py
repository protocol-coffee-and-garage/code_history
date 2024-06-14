import sys
from functools import reduce
read = sys.stdin.readline

num_list = list(map(int, read().split()))
def diff(*num):
    diff_num = reduce(lambda a, b : a - b, map(int, num))
    if diff_num == 0:
        return '=='
    elif diff_num > 0:
        return '>'
    elif diff_num < 0:
        return '<'
    else:
        raise ValueError()

print(diff(*num_list))

# 기존 답변
a, b = list(map(int, input().split()))
def compareNums(a, b):
    if (a > b):
        return '>'
    elif (a < b):
        return '<'
    elif (a == b):
        return '=='

print(compareNums(a, b))