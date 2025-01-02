import random

def player_input() :

    player_number = input("숫자를 입력해주세요: ")
    if len(player_number) != 3 or not player_number.isdigit():
        raise ValueError("입력은 3자리 숫자여야 합니다.")

    elif len(set(player_number)) != 3:
        raise ValueError("입력 값의 각 자리는 서로 달라야 합니다.")
    return player_number


def game_comp(com_number, player_number) :
    strike, ball, index = 0, 0, 0

    for i in com_number :
        if int(player_number[index]) == i :
            strike += 1
        elif int(player_number[index]) in com_number :
            ball += 1
        index += 1
    return strike, ball

def game_print(com_number) :
    while True:
        number = player_input()
        strike, ball = game_comp(com_number, number)
        if strike==0 and ball==0:
            print("낫싱")
            continue
        elif strike == 3 :
            print(str(strike)+"스트라이크")
            print("게임 종료")
            break
        else:
            print(str(ball)+"볼", str(strike)+"스트라이크")
            continue
        
def main(): 
    while True :
        com_number = random.sample(range(1,10),3)
        print("숫자 야구 게임을 시작합니다.")
        game_print(com_number)


        result = input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
        if result == '1':
            main()
            return
        elif result == '2':
            print("게임을 종료합니다.")
            return
        else:
            raise ValueError("잘못된 입력입니다. 1 또는 2를 입력하세요.")
            
if __name__ == "__main__":
    main()