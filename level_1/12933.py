# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.
def solution(n):
    answer = sorted(
        map(int, str(n)), reverse=True
    )  # reverse=True로 내림차순 정렬, sorted로 하면 자동으로 배열로 반환되어 list를 쓰지않아도 됨
    return int("".join(map(str, answer)))


print(solution(118372))
