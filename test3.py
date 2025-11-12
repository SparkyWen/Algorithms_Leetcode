# import sys
# data = sys.stdin.buffer.read().strip().split()
# print(type(data))
# it = iter(data)


import sys
raw = sys.stdin.buffer.read()
non_empty = [ln for ln in raw.splitlines() if ln.strip()]
for _ in range(len(non_empty)):
    print(non_empty)

