def creator(check_num, origin_num):
    devide_sum = check_num + sum(list(map(int, str(check_num))))
    if origin_num == devide_sum:
        return True

# 1. N입력받기
N = int(input())
for i in range(N):
    if creator(i, N) == True:
        print(i)
        exit()
print(0)
#2. 생성자 확인 함수 만들기