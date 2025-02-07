import random

def same_num_check(check_array):
    """
    리스트에서 중복된 숫자가 있는지 확인하는 함수.
    중복된 숫자가 있으면 1을 반환하고, 없으면 0을 반환.
    """
    for i in check_array:
        if check_array.count(i) != 1:
            return 1
    return 0

def validate_input(Data, Criteria):
    """
    사용자가 입력한 값을 검증하는 함수.
    - Data: 사용자가 입력한 값
    - Criteria: 예상하는 값의 조건 (정수 또는 리스트 형식()
    잘못된 값이 입력되면 ValueError를 발생시킴.
    """
    try:
        int(Data)  # Data가 int 형식인지 확인
    except ValueError as e:
        if "invalid literal for int()" in str(e):  # int로 변환할 수 없는 값일 경우
            raise ValueError("숫자만 입력해주세요.")  # 숫자가 아닌 값 입력시 예외 처리
        
    if type(Criteria) == int:  # Criteria가 int일 경우, player_input()에서 사용
        compare_array = list(map(int, Data))  # Data를 정수형 리스트로 변환

        # 플레이어가 입력한 값이 예상되는 값의 길이가 아닐 경우 예외 처리
        if (len(compare_array) != Criteria):
            raise ValueError("3개의 숫자를 입력해주세요.")
        
        # 중복된 숫자가 있을 경우 예외 처리
        if (same_num_check(compare_array) == 1):
            raise ValueError("숫자 중복 없이 입력해주세요.")
        
        # 1~9의 숫자가 아닌 0이 포함된 경우 예외 처리
        if (0 in compare_array):
            raise ValueError("1 ~ 9의 숫자만 입력해주세요.")
        
        return compare_array  # 입력이 정상이면 정수 리스트 변환
    
    elif type(Criteria) == list:  # Criteria가 list일 경우, restart_baseball()에서 사용
        # Data가 Criteria에 포함되지 않은 값일 경우 예외 처리
        if int(Data) not in Criteria:
            raise ValueError("숫자 1 또는 2만 입력해주세요.")

    
def make_computer_num():
    """
    컴퓨터가 랜덤으로 3개의 숫자를 생성하는 함수.
    1에서 9까지의 숫자 중에서 중복 없이 3개를 뽑음.
    """
    computer = random.sample(range(1, 10), 3)  # 1~9 사이에서 중복 없이 3개 숫자 선택
    return computer

def player_input():
    """
    플레이어에게 숫자 3개를 입력받는 함수.
    입력 값 검증 후 정상적인 값을 반환.
    """
    get_array = validate_input(input("숫자를 입력해주세요 : "), 3)  # 입력 값 검증
    return get_array

def check_input(get, com):
    """
    플레이어가 입력한 값과 컴퓨터가 생성한 값을 비교하여 결과를 출력하는 함수.
    - get: 플레이어가 입력한 숫자 리스트
    - com: 컴퓨터가 생성한 숫자 리스트
    결과에 따라 '스트라이크', '볼', '낫싱'을 반환.
    """
    ball, strike = 0, 0
    for i in range(0,3):
        if get[i] == com[i]:  # 숫자와 위치가 맞으면 스트라이크
            strike += 1
        elif get[i] in com:  # 숫자는 맞지만 위치가 다르면 볼
            ball += 1
        else:
            continue
    if strike == 3:
        return "3스트라이크"  # 3개의 숫자가 모두 맞으면 3스트라이크
    elif ball + strike == 0:
        return "낫싱"  # 맞는 숫자가 없으면 낫싱
    elif ball == 0:
        return "{0}스트라이크".format(strike)  # 볼은 없고 스트라이크만 있는 경우
    elif strike == 0:
        return "{0}볼".format(ball)  # 스트라이크는 없고 볼만 있는 경우
    else:
        return "{0}볼 {1}스트라이크".format(ball, strike)  # 볼과 스트라이크가 모두 있는 경우
    
def loop_check(com):
    """
    게임을 반복하여 진행하는 함수.
    플레이어가 3개의 숫자를 모두 맞힐 때까지 반복.
    """
    while True:
        get = player_input()  # 플레이어 입력 받기
        result_check_input = check_input(get, com)  # 입력한 값과 컴퓨터 값 비교
        print(result_check_input)  # 결과 출력
        if result_check_input == "3스트라이크":  # 3스트라이크면 게임 종료
            print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
            return 0  # 게임 종료

def restart_baseball():
    """
    게임 종료 후 '1'을 입력하면 게임을 새로 시작하고, '2'를 입력하면 종료하는 함수.
    """
    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
    restart_input = input()  # 플레이어 입력 받기
    validate_input(restart_input, [1, 2])  # 입력 값 검증
    return int(restart_input)
        

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("숫자 야구 게임을 시작합니다.")
    while True:
        com_num = make_computer_num()  # 컴퓨터가 생성한 숫자
        loop_check(com_num)  # 게임 진행
        restart = restart_baseball()  # 게임 재시작 여부 확인
        if restart == 1:  # 1을 입력하면 게임 재시작
            continue
        else:  # 2를 입력하면 게임 종료
            break

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
