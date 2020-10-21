def naive(t, p):
    n = len(t)
    m = len(p)
    for s in range(n-m):
        if p == t[s:s+m]:
            print(f"match at {s}")


if __name__ == '__main__':
    T = "hello world"
    P = " wo"
    naive(T, P)
