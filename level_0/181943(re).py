# 문자열 my_string, overwrite_string과 정수 s가 주어집니다.
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을
# 문자열 overwrite_string으로 바꾼 문자열을
# return 하는 solution 함수를 작성해 주세요.

# 입력
# my_string	overwrite_string	s	result
# "He11oWor1d"	"lloWorl"	    2	"HelloWorld"
# "Program29b8UYP"	"merS123"	7	"ProgrammerS123"


# 예제 1번의 my_string에서 인덱스 2부터 overwrite_string의 길이만큼에
# 해당하는 부분은 "11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.


def solution(my_string, overwrite_string, s):
    answer = ""

    # s가 my_string의 길이를 벗어나지 않는지 확인. 만약 벗어난다면, 즉 s + len(overwrite_string) > len(my_string)인 경우에는
    # my_string을 그대로 반환합니다.
    # 제약사항때문에 존하지 않아도 됨
    if s + len(overwrite_string) > len(my_string):
        answer = my_string

    # 그렇지 않은 경우에는 my_string의 s 인덱스부터 overwirte_string의 길이만큼을 overwrite_string으로 대체한 결과를 반환
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :]
    return answer


print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))
