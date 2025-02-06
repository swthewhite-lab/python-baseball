def main():
    import random

    def randnumber():
        return random.sample(range(1, 10), 3)  
    while True:
        arr = randnumber()

        while True:
            try:
                num = int(input())  # 메시지 없이 입력받음
                if num < 100 or num > 999:  # 3자리 숫자가 아닐 경우
                    raise ValueError("3자리 숫자를 입력해야 합니다.")
            except ValueError:
                raise ValueError(("잘못된 입력입니다"))


            num_arr = [(num // 100), ((num // 10) % 10), (num % 10)]  

            strike_Cnt = 0
            ball_Cnt = 0

            for x in range(3):
                for y in range(3):
                    if arr[x] == num_arr[y]:
                        if x == y:
                            strike_Cnt += 1
                        else:
                            ball_Cnt += 1

            if strike_Cnt == 3:
                print("3스트라이크")
                print("게임 종료")
                break  # 정답을 맞추면 게임 종료
            elif strike_Cnt == 0 and ball_Cnt == 0:
                print("낫싱")
            elif strike_Cnt == 1 and ball_Cnt == 1:
                print("1볼 1스트라이크")
            elif ball_Cnt == 3:
                print("3볼")
            else:
                continue  # 지정된 출력 패턴이 아닌 경우 무시하고 다시 입력받음

        menu = input()  # 입력 메시지 없이 입력받음
        if menu != '1':  # 1이 아니면 게임 종료
            break

if __name__ == "__main__":
    main()