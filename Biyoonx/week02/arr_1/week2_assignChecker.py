import sys
read = sys.stdin.readline

assign_mem_list = [int(read()) for _ in range(28)]

lazy_mem_list = []
for idx in range(1, 31):
    if idx not in assign_mem_list:
        print(idx)

'''
assign_mem_list = [0] * 30
for _ in range(28):
    num = int(read())
    assign_mem_list[num - 1] = num

nope = [str(idx + 1) for idx, val in enumerate(assign_mem_list) if val == 0]

print('\n'.join(nope))
'''