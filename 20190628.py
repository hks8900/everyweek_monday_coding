"""
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어
    d(91) = 9 + 1 + 91 = 101
이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를
인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
"""
r = []
l = []
ll = []
n = 0
f = 0
t = 0
k = 0
we = 0
while t < 5000: # 임시로 50 설정
    l.append(0)
    r.append(t)
    t += 1  # l 리스트 값 0으로 채워서 미리 칸 만듬. range out 에러 예방.
print(t)

while n < 5000:

    for ii in str(n): # 제네레이터 값 생성
        i = int(ii)
        #print(i)
        s = f + i
        #print("s",s)
        f = s
        #print("f", f)
        d = n + s
        #print(d)
        l[n] = d
    d = 0
    f = 0
    n += 1

for j in l: # ee는 제네 총함
    ee=k + j
    k= ee
for jj in r: # 1 ~ 5000 값 총함
    qw = we + jj
    we = qw

print("list",format(l)) # 각 리스트 값 확인. 제네 값
print("list",format(r)) # 1~5000

te = list(set(r) - set(l)) # 겁색해보니 집합으로 변환 하여 차 집합 구함. 셀프 넘버 값
te.sort()
print(te)

g = 0
for h in te:
    result = g + h
    g = result
print("셀프 넘버값",result) # 셀프 넘버 값 총 합
