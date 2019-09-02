"""
대각선 길이 구하기

직각삼각형의 밑변이 x, 높이가 y일 때 남은 변(대각선)의 길이를 구하는 함수를 만들어주세요.

ps. 요즘 대각선계산기 어플이 인기가 있는 걸 보고 한번 직접 만들어보는 것도 좋다고 생각해서 문제를 만들어 올립니다.
http://codingdojang.com/scode/672?answer_mode=hide
"""

result = 0
x = int(input ("x의 길이 입력"))
y = int(input ("y의 길이 입력"))

result = x**2 + y**2 # 제곱 표현 방법 : 숫자**2 <- 2제곱이다.
result = result ** 0.5 # 루트 표현 방법 : 숫자**0.5 <- 루트.
print(result)

# 제곱은 (x + y ) ** 2 또는 math.pow(( x + y), 제곱횟수)
#
# 루트는 (x + y ) ** 0.5 또는 math.sqrt(x + y) 를 이용한다. 이건 모르면 개고생이네.