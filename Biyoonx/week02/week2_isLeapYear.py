import sys
read = sys.stdin.readline

year = int(read())
def isLeapYear(num:int):
    return (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)

print(int(isLeapYear(year)))

# 기존 답변
year2  = int(input())
def isLeapYear2(year):
		leapCond1 = (year % 4 == 0) and (year % 100 != 0)
		leapCond2 = (year % 400 == 0)
		if (leapCond1 or leapCond2):
				return 1
		else:
				return 0
print(isLeapYear(year2))