"""
<문제>
겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성에 갔다 올 예정이다.
화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다.

@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

<입력>
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다. 입력으로 주어지는 수는 정수이거나 소수 첫째 자리까지 주어지며, 0 이상 100 이하이다. 연산자는 최대 3개 주어진다.

<출력>
각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.
"""

totalCase = int(input())

for i in range(1, totalCase+1):
    """
    print(eval(input().replace("@", "* 3").replace("%", "+5").replace("#", "-7")))
    이렇게 했더니 소수점 대응이 안 됨...
    내가 문제를 너무 날먹하려고 했음 ㅠㅠㅠ
    """
    elements = input().split(" ")
    result = float(elements.pop(0))
    for element in elements:
        if element == "@":
            result *= 3
        if element == "%":
            result += 5
        if element == "#":
            result -= 7
    print(f"{result:.2f}")