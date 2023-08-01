# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n):
    # 문자열을 뒤집음
    answer = [int(i) for i in reversed(str(n))]
    return answer


print(solution(12345))


def digit_reverse(n):
    # 숫자를 문자열로 변경후 뒤집음다음 다시 숫자로 변경
    # 해당 숫자를 배열화
    return list(map(int, reversed(str(n))))
