"""
골드바흐의 추측(Goldbach's conjecture)은 오래전부터 알려진 정수론의 미해결 문제로,
2보다 큰 모든 짝수는 두 개의 소수(Prime number)의 합으로 표시할 수 있다는 것이다.
이때 하나의 소수를 두 번 사용하는 것은 허용한다.
2보다 큰 짝수 n을 입력 받으면, n=p1+p2 를 만족하는 소수 p1,p2의 페어를 모두 출력하는 프로그램을 작성하시오.

입력예1: n=26
출력예1: [[3, 23], [7, 19], [13, 13]]

입력예2: n=48
출력예2 [[5, 43], [7, 41], [11, 37], [17, 31], [19, 29]]
"""
a = []
num = int(input("숫자 입력"))
l = num % 2
y=range(num)

if num >= 2 and l == 0:
    for i in range(num):
        for j in range(num):
            result = i + j
            if num == result and 1 == j % 2 and 1 == i % 2:
                a.append([i, j])
                print(a)
                continue
else:
    print("2보다 큰 짝수 입력하세요.")



