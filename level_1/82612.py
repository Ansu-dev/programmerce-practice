# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 
# 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 제한사항
# 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수


def solution(price, money, count):
    answer = 0

    amount = 0
    for i in range(1, count + 1):
        amount += price * i

    if amount > money:
        answer = amount - money
    return answer




# 이 함수는 주어진 가격(price), 소지금(money), 및 횟수(count)를 기반으로, 특정 물건을 count 번만큼 구매할 때 부족한 금액을 계산하는 함수입니다. 함수 내부를 살펴보겠습니다.

# price * (count + 1) * count // 2:

# count는 구매 횟수를 나타냅니다.
# (count + 1) * count는 구매한 물건의 총 갯수를 나타냅니다. (1번째 구매 + 2번째 구매 + ... + count 번째 구매)
# price는 각 물건의 가격을 나타냅니다.
# 따라서 이 부분은 총 비용을 나타냅니다.
# price * (count + 1) * count // 2 - money:

# 앞서 계산한 총 비용에서 소지금(money)을 뺀 값입니다.
# 이 값이 0보다 크면 소지금이 충분하고, 0 이하라면 부족한 금액을 나타냅니다.
# max(0, price * (count + 1) * count // 2 - money):

# 위에서 계산한 부족한 금액이 음수일 경우, 음수를 0으로 만듭니다. 왜냐하면 부족한 금액이 음수일 때는 부족하지 않고, 충분한 금액을 가지고 있기 때문입니다.
# 따라서 이 함수는 구매하려는 물건의 가격(price), 현재 소지금(money), 및 구매 횟수(count)를 입력받아, 부족한 금액을 계산하고 이를 반환합니다. 반환값이 0 이하인 경우에는 소지금이 부족하지 않으며, 양수인 경우에는 부족한 금액을 나타냅니다.

def solution(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)


print(solution(3,20,4))