import sys
read = sys.stdin.readline

sum_paid, count_paid = [int(read()) for _ in range(2)]
paid_list = [list(map(int, read().split())) for _ in range(count_paid)]
is_same = sum_paid == sum(product[0] * product[1] for product in paid_list)

print({True: 'Yes', False: 'No'}.get(is_same))