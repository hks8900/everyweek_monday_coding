"""
n개의 의자에 n명의 사람이 각각 앉아 있다. 이들의 자리를 재배치 하려고 할때,
한 사람도 처음 앉았던 자리에 다시 앉지 않도록 자리를 재배치하는 경우의 수를 X(n)이라고 하자.
n (0 < n <=10)을 입력받아 X(n)을 출력하는 프로그램을 작성하라.
http://codingdojang.com/scode/671?answer_mode=hide

입력예1: 2
출력예1: X(2) = 1

입력예2: 3
출력예2: X(3) = 2

입력예3: 4
출력예3: X(4) = 9
"""
import random
x = input("자리 입력")
for i in x:
    ram = random.randint(0,11) #랜덤 함수 이용
    if x == ram: # 같은 자리 못 앉게 설정
        continue
    else:
        print("X({}) = {}".format(x,ram))

