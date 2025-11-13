# import sys
# data = sys.stdin.buffer.read().strip().split()
# print(type(data))
# it = iter(data)


# 手写求和
import sys
raw = sys.stdin.buffer.read().strip().split()
it = iter(raw)

ni = lambda:int(next(it))
sum = 0

for _ in range(len(raw)):
    n = ni()
    sum += n
print(sum)

