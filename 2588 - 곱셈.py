a = int(input())
b = int(input())

third_of_b = b % 10 # ex: 365를 10으로 나눈 나머지는 '5'
second_of_b = (b // 10) % 10 #ex: 365를 10으로 정수 나눗셈 하면 36, 36을 10으로 나눈 나머지는 6
first_of_b = b // 100 #ex: 365를 100으로 정수 나눗셈 하면 3

firstLineToPrint = a * third_of_b
secondLineToPrint = a * second_of_b
thirdLineToPrint = a * first_of_b
fourthLineToPrint = firstLineToPrint + secondLineToPrint*10 + thirdLineToPrint*100

print(firstLineToPrint)
print(secondLineToPrint)
print(thirdLineToPrint)
print(fourthLineToPrint)