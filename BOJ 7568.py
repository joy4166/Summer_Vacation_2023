N = int(input())

people_list = []
score_list = []
for _ in range(N):
    score_list.append(1)
for _ in range(N):
    people_list.append(list(map(int, input().split(" "))))

for i in range(N):
    for k in range(i+1, N):
        if people_list[i][0] > people_list[k][0] and people_list[i][1] > people_list[k][1]:
            score_list[k] += 1
        elif people_list[i][0] < people_list[k][0] and people_list[i][1] < people_list[k][1]:
            score_list[i] += 1
        else:
            continue
for i in score_list:
    print(i, end=" ")