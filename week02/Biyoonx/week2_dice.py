import sys
read = sys.stdin.readline

def getReward(x:int, y:int, z:int):
		# type = 0
		# eyes = 0
		if (x == y == z):
				type = 1
				eyes = x
		elif (x == y or y == z or z == x):
				type = 2
				eyes = x if (x == z) else y
		else:
				type = 3
				eyes = max(x, y, z)
    
		return {
    		1: lambda a: 10000 + a * 1000,
        2: lambda a: 1000 + a * 100,
        3: lambda a: a * 100
    }.get(type)(eyes)

a, b, c = map(int, read().split())
print(getReward(a, b, c))