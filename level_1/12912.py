# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.


def solution(a, b):
    # a,b의 숫자 비교를 먼저 해줌
    _a = b if a > b else a
    _b = a if a > b else b
    answer = sum(i for i in range(_a, _b + 1))
    return answer


print(solution(5, 3))


def adder(a, b):
    # a가 b보다 클경우
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
