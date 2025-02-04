import random

def make_computer_num():
    computer = random.sample(range(1, 9), 3)
    return computer

def player_input():
    get_num = list(map(int, input("숫자를 입력해주세요 : ")))
    return get_num

def check_input(get, com):
    ball, strike = 0, 0
    for i in range(0,3):
        if get[i] == com[i]:
            strike += 1
        elif get[i] in com:
            ball += 1
        else:
            continue
    if strike == 3:
        return "3스트라이크"
    elif ball + strike == 0:
        return "낫싱"
    elif ball == 0:
        return "{0}스트라이크".format(strike)
    elif strike == 0:
        return "{0}볼".format(ball)
    else:
        return "{0}볼 {1}스트라이크".format(ball, strike)
    
def loop_check(com):
    get = player_input()
    result_check_input = check_input(get, com)
    print(result_check_input)
    if result_check_input != "3스트라이크":
        loop_check(com)

def restart_baseball():
    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
    user_key = int(input())
    return user_key

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    restart = 1
    print("숫자 야구 게임을 시작합니다.")
    while restart == 1:
        computer = make_computer_num()
        print(computer)
        loop_check(computer)
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        restart = restart_baseball()

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
