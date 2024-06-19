import sys
read = sys.stdin.readline

num_of_int, std_num = map(int, read().split())
num_list = filter(lambda i: i < std_num, map(int, read().split()))

print(*num_list)


'''
# 입력 문자열까지 출력
import sys
read = sys.stdin.readline

num_of_int, std_num = read().strip().split()
num_list = read().strip().split()

try:
    idx = num_list.index(std_num)
except ValueError:
    idx = -1

print(' '.join(num_list[:idx]))

# 출력만 하는 방식(정렬)
import sys
read = sys.stdin.readline

num_of_int, std_num = read().strip().split()
num_list = sorted(map(int, read().split()))
list_str = ' '.join(map(str, num_list))

print(list_str[:list_str.find(std_num) + 1])
'''