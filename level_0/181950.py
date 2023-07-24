# 문자열과 숫자가 입력됨
# 문자열을 입력받은 숫자만큼 연속해서 출력하면됨

a, b = input().strip().split(" ")
b = int(b)


_result = ""
for i in range(0, b):
    _result += a

print(_result)


# 다른사람 풀이
print(a * b)
