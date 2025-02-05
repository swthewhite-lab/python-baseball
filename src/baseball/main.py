import random

def same_num_check(check_array):    # list에서 중복되는 수를 인식하는 기능 함수
    for i in check_array:
        if check_array.count(i) != 1:
            return 0
    return 1

def validate_input(compare_array, want_len):    # 잘못된 값을 입력한 경우 ValueError가 발생하여 프로그램을 종료하는 기능 함수
    if (len(compare_array) != want_len) or (0 in compare_array) or (same_num_check(compare_array) == 0):    # 플레이어가 입력한 값이 예상되는 값의 길이가 아니거나, 0이 포함되거나, 중복되는 수가 입력되어도 예외 처리
        raise ValueError
    
def make_computer_num():    # random 모듈을 사용하여 임의의 수 생성하는 함수 (요구사항)
    computer = random.sample(range(1, 10), 3)    # basecode
    return computer

def player_input(): # 플레이어에게 3개의 숫자 입력 받는 기능 함수
    get_array = list(map(int, input("숫자를 입력해주세요 : ")))
    validate_input(get_array, 3)
    return get_array

def check_input(get, com):  # 플레이어가 입력한 숫자에 대한 결과를 출력하는 함수
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
    
def loop_check(com):    # 1에서 3까지의 과정을 반복해 3개의 숫자를 모두 맞히면 게임이 종료되는 기능 함수
    get = player_input()
    result_check_input = check_input(get, com)
    print(result_check_input)
    if result_check_input == "3스트라이크": # check_input()의 결과가 "3스트라이크"일 경우 게임을 종료하고, 아닐 경우 다시 loop_check() 수해
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        return 0
    else:
        loop_check(com)

def restart_baseball(): # 게임 종료 후 '1' 입력시 다시 시작, '2' 입력시 완전히 종료하는 기능 함수
    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
    user_key = int(input())
    if user_key in [1, 2]:
        return user_key
    else:    # 잘못된 값을 입력할 경우 'ValueError'를 발생
        raise ValueError

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("숫자 야구 게임을 시작합니다.")
    while True:
        com_num = make_computer_num()
        loop_check(com_num)
        restart = restart_baseball()
        if restart == 1:
            continue
        else:
            break

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
