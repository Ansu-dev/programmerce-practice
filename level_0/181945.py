# 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
# abcde

# a
# b
# c
# d
# e

str = input()

# _result = ""
# for char in str:
#     _result += char + "\n"

# print(_result)

# 다른사람 풀이
print("\n".join(str))  # 각 문자사이에 \n를 삽입한다.
