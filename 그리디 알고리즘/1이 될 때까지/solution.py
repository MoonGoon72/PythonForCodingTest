n, k = map(int, input().split(' '))
n1, k1 = n, k
result = 0

while n >= k:
    if n % k == 0:
        n = n // k
        result += 1
    else:
        n -= 1
        result += 1
print(result)

###########################################
result = 0
while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1 씩 빼기
    target = (n1 // k1) * k1  ## 몫을 구하고 다시 곱한 값을
    result += (n1 - target)  ## 기존값으로 빼면 나누어떨어질때까지 1씩 빼는 효과가 나온다.
    n1 = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n1 < k1:
        break
    # K로 나누기
    result += 1
    n1 //= k1

result += (n1 - 1)
print(result)