"""
    10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
    1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
    http://codingdojang.com/scode/350?answer_mode=hide
"""
five = 0
f = []
i=0
i2 = 0
result = 0
while five < 995: # 1000미만의 값 1000넣으면 1000이 포함됨;; 분명 부등호 < 이건데;;? 뭐지;;
    three = 3 * i
    five = 5 * i
    f.append(three) # append 3과 5의 배수를 한번에 넣는다.
    f.append(five)
    i += 1

for i in f:
    result = i2 + i # 합산
    i2 = i
print(result)
print(f)


