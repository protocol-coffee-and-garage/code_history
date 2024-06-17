import sys
read = sys.stdin.readline

score_var1 = int(read())
def score(num:int):
    grade_table = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}
    if num // 10 in grade_table:
        return grade_table.get(num // 10)
    else:
        return 'F'
print(score(score_var1))

# 기존 답변
score_var2 = int(input())
def grade(score):
		if (90 <= score <= 100):
				return 'A'
		elif (80 <= score <= 89):
				return 'B'
		elif (70 <= score <= 79):
				return 'C'
		elif (60 <= score <= 69):
				return 'D'
		else:
				return 'F'
print(grade(score_var2))