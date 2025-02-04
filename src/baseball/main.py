import random

def main():
    while True :
        computer = generateNum()

        print("숫자 야구 게임을 시작합니다.")
        while(True) :
            print("숫자를 입력해주세요 : ", end='')
            user = input()
            checkInput(user)

            if (calculate(user, computer)) :
                break

        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
        select = input()
        if select == "1" :
            continue
        elif select == "2" :
            break
        else :
            raise ValueError

def generateNum() :
    num = random.sample(range(1,10), 3)
    computer = "".join(map(str, num))
    return computer

def checkInput(user) :
    if not user.isdigit() :
        raise ValueError

    num = int(user)
    if num < 100 or num > 999 :
        raise ValueError

    check = list(user)
    if len(set(check)) != 3 :
        raise ValueError

    return True

def calculate(user, computer) :
    strike = sum(1 for i in range(3) if user[i] == computer[i])
    ball = sum(1 for b in user if b in computer) - strike
    
    return format(strike, ball)

def format(strike, ball) :
    if strike == 3 :
        print("3스트라이크")
        return True
    
    output = []
    if ball > 0 :
        output.append(f"{ball}볼")
    if strike > 0 :
        output.append(f"{strike}스트라이크")

    print(" ".join(output) if output else "낫싱")
    return False

if __name__ == "__main__":
    main()