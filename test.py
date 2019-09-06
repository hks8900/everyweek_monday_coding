"""
Lunar(Dismal) Arithmetic 라는 어떤 연산이 있습니다. 이 연산에서 덧셈「+」은 각 자릿수를 비교해서 큰 수를 취합니다.
5 + 3 = 5
13 + 6 = 16

   169
 + 248
 ------
   269

-----------------------구분 경계선-------------------------------------------

그리고 곱셈「×」은 각 자릿수를 비교해서 작은 수를 취합니다.
5 × 3 = 3
13 × 6 = 13

     169
   × 248
   ------
     168 #각 자리 별 곱 표현이네.. ㄱ-;; 1의 자리 비교 값
    144  # 2번째 자리 비교값./ 248중 4랑 169를 하나씩 비교해서 올리는 방식이군; 순간 문제 잘못 된 줄 알았네
 + 122
 --------
   12468
Lunar Arithmetic를 수행하는 계산기를 만들어봅시다.
http://codingdojang.com/scode/673?answer_mode=hide
"""
x = input("1.수 입력")
y = input("2.수 입력")
#print(x[3:4])

for j in range(0,len(y)):
    for i in range(0,len(x)):
        t = x[(len(x)-(i+1)):(len(x)-i)] #
        """
        t 에 수 입력1234 하는 경우 아래와 같이 나온다.
                    4
                    3
                    2
                    1
        """
        test = x[(len(x)-(i+1)):(len(x))]
        print(test)
        """
        test 수 입력1234
            4
            34
            234
            1234
        """
        x = input("1.수 입력")
        y = input("2.수 입력")
        # print(x[3:4])
        z = []

        for i in range(0, len(x)):
            t = x[(len(x) - (i + 1)):(len(x) - i)]
            r = y[(len(y) - (i + 1)):(len(y) - i)]
            if t >= r:
                z.append(t)
                z[-1]
                print(z)

        for i in range(0, len(x)):
            test = x[(len(x) - (i + 1)):(len(x))]
            print(test)
