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
# 이취코 단순하게 푸는 해설
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

######################################################################
# 이취코 효율적으로 푸는 법
count = int(num / (rep + 1)) * rep  # 얘만큼 수열이 반복됨! (first + first + ... + second) + (first + first + ... + second) ...
count += num % ( rep + 1 )  # 나누어떨어지지 않으면 반복하고 남은만큼이 요만큼

result = 0
result += count * first  # count만큼 가장 큰 수 반복하니까 그만큼 곱해서 더해줌
result += (num - count) * second  # 전체에서 count를 뺀 거만큼 second를 더해줌

print(result)