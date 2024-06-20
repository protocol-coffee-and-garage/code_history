import sys
read = sys.stdin.readline

def getQuadrant(x:int, y:int):
		if (x * y) > 0 and (x + y) > 0:
				return 1
		elif (x * y) < 0 and (x - y) < 0:
				return 2
		elif (x * y) > 0 and (x + y) < 0:
				return 3
		elif (x * y) < 0 and (x - y) > 0:
				return 4
		else:
				return 0

x, y = [int(read()) for _ in range(2)]
print(getQuadrant(x, y))

# 기존 답변
x2 = int(input())
y2 = int(input())
def quadrant(x, y):
		if (x * y > 0):
				if (x > -y):
						return 1
				else:
						return 3
		else:
				if (x < y):
						return 2
				else:
						return 4
print(quadrant(x2, y2))