T = int(input())

for _ in range(T):
    m = int(input())
    r = 0
    q = m // 25
    r = m % 25
    d = r // 10
    r = r % 10
    n = r // 5
    r = r % 5
    print(f"{q} {d} {n} {r}")
