# N, M, K 를 공백으로 구분하여 입력받음
index, num, rep = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받음
arr = list(map(int, input().split()))
# 연속으로 더할 수 있는 횟수를 구별해주기 위한 변수
a = int(0)
sum = 0
# 내림차순으로 정렬
arr.sort(reverse=True)
for _ in range(num):  # 더하는 횟수를 반복문으로 구현
    if a < rep:  # 최대 연속반복횟수가 아니면 가장 큰 수 더해줌
        sum = sum + arr[0]
        a = a + 1
    else:  # 최대 연속반복횟수를 채우면 그 다음수를 더해주고 횟수 리셋함
        sum = sum + arr[1]
        a = 0
print(sum)

#####################################################################
# 이취코 해설
arr.sort()
# 가장 큰 수와 그 다음 수만 필요함!
first = arr[index - 1]
second = arr[index - 2]

result = 0

while True:
    for i in range(rep): # 가장 큰 수를 rep(최대 반복 횟수)번 더하기
        if num == 0: # num이 0이라면 반복문 탈출
            break
        result += first
        num -= 1 # 더할때마다 1 씩 빼기
    if num == 0: # num이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한번씩 더하기
    num -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안