
'''

1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
http://codingdojang.com/scode/408?answer_mode=hide

'''
S = [1, 3, 4, 8, 13, 17, 20]
dt = []
def qr():
    for i in range(len(S)):
        r = S[i]
        for j in range(len(S)):
            r2 = S[j]
            qw = r2 - r
            if qw > 0:
                dt.append(qw)
                dt.sort()

                if dt[0] == qw:
                    print(r)
                    print("결과값{}".format(qw))
                    print(r, r2)

qr()

