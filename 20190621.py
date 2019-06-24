"""
Bulls and Cows라는 간단한 게임을 프로그램으로 만들어보자.
<게임 규칙>
먼저 컴퓨터가 0부터 9까지의 숫자중 4개를 중복없이 배열한 문자열을 랜덤하게 생성한다.
플레이어는 생성된 문자열을 예상하여 1턴에 1번씩 입력할 수 있다.
컴퓨터는 플레이어가 입력한 문자열을 정답과 비교하여 값과 위치가 모두 맞는 숫자의 갯수를 'Bulls'
위치는 틀렸지만 값은 맞는 숫자의 갯수를 'Cows'로 카운트하여 매턴마다
사용자의 입력에 대해 Bulls와 Cows값을 알려준다.
플레이어는 10턴 안에 정답을 맞춰야한다.

<세부 사항>
판정의 출력형식은 (Bulls값)B(Cows값)C 로 한다. ex) 답이 1234일때 0124를 입력하면 1B2C 를 출력
판정을 출력할때마다 사용자가 입력한 횟수N(=현재 턴수)을 함께 출력한다. ex>판정: 1B2C, 입력한 횟수: 2
형식에 맞지 않는 잘못된 입력(ex>2211, a1bc, 209111 등)을 한 경우는 에러 메시지를 출력하고 N은 변하지 않는다.
단 이미 입력했던 값을 다시 입력하는것은 괜찮다.
플레이어가 정답을 맞추면, "정답입니다. 총 입력한 횟수: N"를 출력한다.
10턴이 지나도 정답을 맞추지 못하면 정답을 공개하고 Game Over 메시지를 출력한다.
플레이어가 정답을 맞추거나 Game Over가 되면, 다시 처음부터 게임을 시작할지 종료할지 물어본다.
이때 플레이어가 1을 입력하면 처음부터 게임을 다시 시작하고 0을 입력하면 게임을 종료한다(그 외의 입력에는 에러를 출력하고 다시 물어본다)

"""
import random
i = 0
l = []
L = []
turn = 0
result = []
while turn < 11:
    answer = input("Bulls and Cows! 4자리의 숫자를 입력하세요.")  # input 은 문자 값으로 입력 받는다.
    # L=",".join(answer)
    try:
        for W in answer:  # 문자로 받은 값을 썰어서 예 1234 이면 '1','2','3','4' 나옴
            a = int(W)  # int 로 1,2,3,4로 나오게 만든다.
            L.append(a)  # L은 리스트 형식으로 append 를 이용해서 하나씩 순서대로 1->2->3->4 들어가고
        print(L)  # [1,2,3,4]가 나온다. 젠장 뻘짓 오지게 했으니 안까먹겠네.
        print(len(L))
        if L != 0:
            while i < 4:
                r = random.randrange(0, 10)
                l.append(r)
                i = i + 1
            print(l)

        for w in range(len(l)):  # l의 길이만큼 반복하여 l과 L의 리스트 값 비교
            if l[w] == L[w]:
                result.insert(w, "C")  # 정답
            else:
                result.insert(w, "B")  # 오답
    except ValueError:
        print("숫자 4자리 입력하세요.1현재 턴 {}".format(turn))
        turn = turn - 1
        pass
    except IndexError:
        print("4자리 입력하세요.2현재 턴 {}".format(turn))
        turn = turn - 1
        pass
    if 4 < len(L):
        print("값이 많습니다. 5현재 턴 {}".format(turn))
        turn = turn - 1
        pass

    elif turn < 0:
        turn = 0  # 턴이 마이너스 값이 되지 않도록 마지막에 조정.

    elif turn == 10:
        a = input("GAMEOVER 재시도는 1번 0번은 종료")
        if a == '1':
            del L[:], result[:]
            turn = 0
            continue
        elif a == '0':
            break
        else:
            print("잘못입력하였습니다.")

    elif result[:] == ['C', 'C', 'C', 'C']:
        turn = 10
        a = input("문제해결 재시도는 1번 0번은 종료")
        if a == '1':
            del L[:], result[:]
            turn = 0
            continue
        elif a == '0':
            break
        else:
            print("잘못입력하였습니다.")
    print("결과: {} 현재 턴:{}".format(result, turn))
    turn = turn + 1
    del L[:], result[:]  # list 값 초기화

# 코드가 전체적으로 정리가 더 필요할거 같은데, 지금 실력으로 어떻게 접근해야 하나 싶다.
