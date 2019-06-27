"""
완전수 구하기
자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14
// 1,2,4,7,14는 각각 28의 약수

입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.
출처 - http://codingdojang.com/scode/539?answer_mode=hide
"""
l=[]
m=0
while True:
    n = int(input("완전수 구하자"))
    for i in range(1, n):
        # print("i",i)
        b = n % i # 약수 구하기
        if b == 0:
            l.append(i) # 약수의 리스트
            sum = m + i # 동적 데이터 관리 때 쓰던 방법이 이렇게?!!
            m = sum     # 총 합 구하기
            # print("sum",sum)
    if sum == n: #입력 값과 총합이 같은 경우
        print("완전수 입니다.")
        print("약수 {}, 완전수 {}".format(l, sum)) # 리스트 값과 총 합 프린트
        print(n, sum, l)
    else: # 그외 처리
        print("이거 실수 했는데;;")
        print(n, sum, l)
    del l[:] # 반복 입력을 위한 값 초기화 작업
    n = 0
    m = 0
    continue