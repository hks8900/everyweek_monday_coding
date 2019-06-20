"""
양수 k 가 주어지면 k 길이의 이진법 숫자를 모두 프린트하시오.
단, 연속으로 1이 있으면 안됩니다.

input:5
output: 00000 00001 00010 00100 00101 01000 01001 01010 10000 10001 10010 10100
"""
number=8
nt=[]
i=0
while i < 8:
    print(i)
    nt.append(0)
    i = i + 1
    print(nt)
'''

내가 시도 했던 코드. 추후 수정해볼까.. 생각중
l=(str(list(range(1,15))))

print(l)
a=[]
j=0
d=[]
for i in l:
   j=j+1
   a.insert(j,i)

   print(a)

'''
