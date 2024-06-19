import sys
from functools import reduce
read = sys.stdin.readline

print(reduce(lambda x, y: x + y, range(int(read()) + 1)))