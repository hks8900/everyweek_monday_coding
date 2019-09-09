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
# print(x[3:4])
z = []
zz = []
result = []
num = 1
if len(x) >  len(y):  # 입력 된 것 중 길이 긴 값으로 "0" 리스트 생성
    for i in range(0, len(x)):
        result.append(0)
else:
    for i in range(0, len(y)):
        result.append(0)

for i in range(0, len(result)): # 각 자리 비교하여 큰 값 입력
    t = x[(len(x) - (i + 1)):(len(x) - i)]
    r = y[(len(y) - (i + 1)):(len(y) - i)]
    if t >= r:
        z.append(t)
    else:
        z.append(r)

for i in z:
    result[-num]=i # append로 바뀐 순서 역순 정렬
    num += 1

print("{}".format(y))
print("+{}".format(x))
print("---------")
print(result)   # 합 계산 완료!
print("""-----------------------------------------------------------------------""")


x2 = []
y2 = []
for i in y:
    y2.append(i)
yy = y2
for i in x:
    x2.append(i)
xy = x2
pre = 0
for i in range(0, len(result)):
    xx = x[(len(x) - (i + 1)):(len(x) - i)]
    rr = y[(len(y) - (i + 1)):(len(y) - i)]

    if xx <= rr:
        yy.pop(-(i + 1), )
        rt = xy(-(i + 1), )
        yy[-(i+1):len(yy)] =
        if i != 0:
            yy.append(0)
            yy2 = list(map(int, yy))
            print(yy2)
    print("xxyy",yy)

print("yy",yy2)


#yy2 = list(map(int,yy))
# xr=yy2*(10**i)



