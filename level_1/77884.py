# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 
# 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 
# return 하도록 solution 함수를 완성해주세요.

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 1
        for j in range(1, i + 1 // 2):
            if i % j == 0 :
                count+=1
        if count % 2 == 0 :
            answer += i
        else :
            answer -= i
    return answer




def solution1(left, right):
    answer = 0
    for i in range(left, right + 1):
        print(int(i ** 0.5), i ** 0.5)
        if int(i ** 0.5) == i ** 0.5: # 제곱수가 아닌 수의 약수들은 각자 곱해지는 쌍이 있으니까 무조건 약수의 개수가 짝수
            answer -= i
        else:
            answer += i
    return answer

print(solution1(24, 27))