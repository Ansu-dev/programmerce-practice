# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.


def solution(numbers):
    answer = sum(i for i in range(10) if i not in numbers)
    return answer


print(solution([1, 3, 5, 7]))


# 0~9 의 합산인 45에서 배열안에 중복되지 않은 숫자들의 합을 빼면 답
def solution(numbers):
    return 45 - sum(numbers)
