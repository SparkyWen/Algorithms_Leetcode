import sys
def parse_floor(s):
    if not s:
        raise ValueError("cant be null")
    if s[0] =='F':
        body = s[1:]
        if body.endswith("A"):
            return int(body[:-1]) + 1
        else:
            return int(body)
    elif s[0] == 'B':
        return 1 - int(s[1:])
    else:
        raise ValueError("invalid floor")

def to_label(h):
    if h <=0:
        return f"B{1 - h}"
    if h == 4:
        return "F3A"
    return f"F{h}"

def main():
    data = sys.stdin.read().strip().split()
    if not data: return
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        start = next(it)
        delta = int(next(it))
        h = parse_floor(start) + delta
        out.append(to_label(h))
    print("\n".join(out))

if __name__ == "__main__":
    main()