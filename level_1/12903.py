# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.


def solution(s):
    answer = ""
    _len = len(s)
    if _len % 2 == 0:
        answer = s[_len // 2 - 1] + s[_len // 2]
    else:
        answer = s[_len // 2]
    return answer


print(solution("qwer"))


def string_middle(str):
    return str[(len(str) - 1) // 2 : len(str) // 2 + 1]
