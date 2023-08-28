N = int(input())
d = [0] * (N+1)

for i in range(3, N+1):
    if i%3==0:.
        d[i] =  min(i//3, i//5+i%5//3)
    elif i%5==0:
        d[i] = min(i//5, i//3+i%3//5)
    else:
        d[i] = -1

print(d[N])