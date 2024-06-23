import sys
read = sys.stdin.readline

num_of_score = int(read())
score_list = [*map(int, read().split())]
max_score = max(score_list)

for idx, score in enumerate(score_list):
		score_list[idx] = (score / max_score) * 100

print(sum(score_list) / num_of_score)

# 풀이
num_of_score2 = int(read())
score_list2 = [*map(int, read().split())]

print(sum(score_list2) * 100 / max(score_list) / num_of_score2)