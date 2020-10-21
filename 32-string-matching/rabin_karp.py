def rabin_karp(T, P, d, q):
    n = len(T)
    m = len(P)
    h = 1
    for _ in range(m-1):
        h = h * d % q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + int(P[i])) % q
        t = (d*t + int(T[i])) % q
    for s in range(n-m+1):
        if p == t:
            if P == T[s:s+m]:
                print(f"match at {s}")
        if s < n-m:
            t = (d*(t-int(T[s])*h)+int(T[s+m])) % q


if __name__ == '__main__':
    tt = '314159265'
    pp = '159'
    rabin_karp(tt, pp, 10, 13000)
