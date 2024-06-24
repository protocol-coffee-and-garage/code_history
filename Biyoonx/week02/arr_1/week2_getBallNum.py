import sys
read = sys.stdin.readline

num_of_basket, loop_num = map(int, read().split())
basket_list = [0] * num_of_basket

def put_ball(start, end, ball_num):
		basket_list[start - 1:end] = [ball_num] * (end - start + 1)

for i in range(loop_num):
		s, e, b = map(int, read().split())
		put_ball(s, e, b)

print(' '.join(map(str, basket_list)))