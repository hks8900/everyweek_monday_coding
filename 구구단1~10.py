i=0
k=0
while i < 10:
    i = i + 1
    print("{}단".format(i))
    for k  in range(0,10):
        s=i * k
        #print(s)
        print("구구단{}x{}={}".format(i,k,s))
        k=k+1

