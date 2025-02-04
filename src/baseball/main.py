import random

def make_computer_num():
    computer = random.sample(range(1, 9), 3)
    return computer

def player_input():
    get_num = list(map(int, input("숫자를 입력해주세요 : ")))
    return get_num

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("숫자 야구 게임을 시작합니다.")
    computer = make_computer_num()
    print(computer)
    get = player_input()
    print(get)

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
