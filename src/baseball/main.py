import random
import sys
def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """

    print("숫자 야구 게임을 시작합니다.")
    def game_start():
        ran_numbers = random.sample(range(1, 10), 3)

        def player_input(player_number) :
                
            if len(player_number) != 3 or not player_number.isdigit():
                raise ValueError("입력은 3자리 숫자여야 합니다.")
            
            if len(set(player_number)) != 3:
                raise ValueError("입력 값의 각 자리는 서로 달라야 합니다.")
                
            return True

        def num_comparison(player_number,com_number) :
            strike, ball = 0, 0
        
            for i in range(3) :
                if player_number[i] == com_number[i] :
                    strike += 1
                elif player_number[i] in com_number :
                    ball += 1

            if strike == 0 and ball == 0:
                return "낫싱"
            else:
                return f"{strike}스트라이크, {ball}볼"
        
        while True:
            user_input = input("3자리 숫자를 입력하세요: ")

            player_input(user_input)
                
            result = num_comparison(user_input, list(map(str, ran_numbers)))
            print(result)

            if result == "3스트라이크":
                print("축하합니다! 숫자를 모두 맞추셨습니다.")
                break

    while True :
        game_start()  
        
        while True:
            complete = input("게임을 다시 시작하려면 1, 완전히 종료하려면 2를 입력하세요: ")
            if complete == '1':
                print("게임을 다시 시작합니다.")
                break 
            elif complete == '2':
                print("게임을 종료합니다.")
                return 
            else:
                print("잘못된 입력입니다. 1 또는 2를 입력하세요.")
                continue


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()