# week3_.py
import sys
read = sys.stdin.readline

s, p = map(int, read().split())
keys = read().strip()
a, c, g, t = map(int, read().split())

# 시간 초과
'''
result = 0
for idx1 in range(s - p + 1):
    idx2 = idx1 + p
    key = keys[idx1:idx2]
    if (key.count('A') >= a and key.count('C') >= c and key.count('G') >= g and key.count('T') >= t):
        result += 1
'''

result = 0
key = keys[:p]
cnt_dict = dict(zip(['A', 'C', 'G', 'T'], [key.count('A'), key.count('C'), key.count('G'), key.count('T')]))
for idx2 in range(p, s + 1):
    if (cnt_dict['A'] >= a and cnt_dict['C'] >= c and cnt_dict['G'] >= g and cnt_dict['T'] >= t):
        result += 1
    cnt_dict[keys[idx2 - p]] -= 1
    if idx2 < s:
        cnt_dict[keys[idx2]] += 1

print(result)