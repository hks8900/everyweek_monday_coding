"""
Zigzag Array
Spiral Array 문제를 보고 비슷한 문제를 만들어봤습니다.
http://codingdojang.com/scode/266
자연수 N을 입력받아서 다음과 같은 NxN 매트릭스를 출력하는 프로그램을 작성하라

출처
http://codingdojang.com/scode/666?answer_mode=hide
<입력예1>
자연수 N을 입력하시오(0<N) : 3
<출력예1>
1 3 4
2 5 8
6 7 9

<입력예2>
자연수 N을 입력하시오(0<N) : 5
<출력예2>
1 3 4 10 11
2 5 9 12 19
6 8 13 18 20
7 14 17 21 24
15 16 22 23 25
"""
import random
p = []
x = int(input("자연수 N 입력하면 N*N 매트릭스 출력됨"))
n = x**2
""" # 중복된 랜덤 값이 3행으로 나타난다. 그로 인해 ㅈㅈ 이건 답이 아니다.
for j in range(0,x):
    for i in range(0,x):
        y = random.randint(1,n)
        p.append(y)
    print(p)
    p = []
"""
num = []
for t in range(1,n+1):
    num.append(t)
print(num) # 해결책 1.  num list를 만들어서 채워놓는다.

for j in range(0,x):
    y = random.sample(num,x) # num에서 x 개수 만큼 랜덤 선정
    # 2. 랜덤 샘플링 방법으로 숫자 선정!
    print(y)
    for e in y:
        num.remove(e) # 3. remove 이용하여 선정된 숫자를  numlist에서 삭제 한다.
        # 4. 사용된 리스트 값이 삭제되어 중복이 발생 할 수 없다.

print(num) # 남은 값 확인 []






