a, b, v = map(int, input().split())
h = 0
cnt = 0
while True:
    h += a
    cnt += 1
    if h >= v:
        break
    h -= b
print(cnt)