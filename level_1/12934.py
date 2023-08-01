# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.


def solution(n):
    answer = -1
    # 제곱근을 구하는데 정수라면 +1 제곱을 구하고
    for i in range(1, n // 2 + 1):
        if i * i == n:
            answer = (i + 1) * (i + 1)
            break
    # 아니라면 -1
    if n == 1:
        answer = (n + 1) * (n + 1)
    return answer


print(solution(1))


def nextSqure(n):
    sqrt = n ** (1 / 2)  # 제곱근

    if sqrt % 1 == 0:  # 1도 포함하는 조건
        return (sqrt + 1) ** 2  # 제곱
    return -1
