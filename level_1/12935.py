# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수,
# solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.


def solution(arr):
    min_value = min(arr)
    answer = [i for i in arr if i != min_value] if len(arr) > 1 else [-1]
    # 가장 작은수를 찾아 삭제
    # 빈배열 검증후 빈배열의 경우 -1로 채워넣어줌
    return answer


print(solution([4]))
