T = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

width = 0
for k in range(100):
    for l in range(100):
        if arr[k][l] == 1:
            width += 1

print(width)