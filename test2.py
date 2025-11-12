import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)

    ni = lambda: int(next(it))
    T = ni()
    out = []

    for _ in range(T):
        n = ni()
        arr = [ni() for _ in range(n)]
        out.append(str(sum(arr)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()