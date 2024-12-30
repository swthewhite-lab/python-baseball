import random

def player_input() :
    while True :
        player_number = input("3자리 숫자를 입력하세요: ")
        if len(player_number) != 3 or not player_number.isdigit():
            print("입력은 3자리 숫자여야 합니다.")
            continue
        elif len(set(player_number)) != 3:
            print("입력 값의 각 자리는 서로 달라야 합니다.")
            continue
        break
    return player_number


def game_comp(player_number) :
    strike, ball, index = 0, 0, 0
  
    for i in com_number :
        if int(player_number[index]) == i :
            strike += 1
        elif int(player_number[index]) in com_number :
            ball += 1
        index += 1
    return strike, ball


def game_print() :
    while True:
        number = player_input()
        strike, ball = game_comp(number)
        print(strike, "스트라이크", " / ", ball, "볼")

        if strike == 3 :
            print("축하합니다! 숫자를 모두 맞추셨습니다.")
            break
        else:
            continue
        
    
while True :
    com_number = random.sample(range(1,10),3)
    print("숫자 야구 게임을 시작합니다.")
    game_print()
  
    while True:
        result = input("게임을 다시 시작하려면 1, 완전히 종료하려면 2를 입력하세요: ")
        if result == '1':
            print("게임을 다시 시작합니다.")
            break  # 이곳에서 안쪽 while 문을 종료하고 게임을 다시 시작
        elif result == '2':
            print("게임을 종료합니다.")
            exit()  # 프로그램을 종료
        else:
            print("잘못된 입력입니다. 1 또는 2를 입력하세요.")