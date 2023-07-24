# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
# apple pen
# applepen

str1, str2 = input().strip().split(" ")

_result = str1 + str2
print(_result.replace(" ", ""))

# strip 양쪽의 모든 공백을 제거(Js에서 trim() 가 유사)
print(input().strip().replace(" ", ""))
