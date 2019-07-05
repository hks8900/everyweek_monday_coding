n = []
ii = 4

listnum = [1,2,5,4,3]
listnum.sort()
for i in listnum:
    n.append(0)
print(n)

for i in listnum:
    n[ii] = i
    print(n)
    ii -= 1
    print(ii)
    
print(listnum)