import random

def randomnumber():
   return random.sample(range(1, 10), 3)           

def nothing():
    return print("낫싱")

def onlystrike(x):
    return print("%d스트라이크"%x)

def onlyball(x):
    return print("%d볼"%x)

def ballandstrike(x,y) :
    return print("%d볼 %d스트라이크"%(x,y))

def gamestart():
    return print("숫자 야구 게임을 시작합니다")

def pick():
    return print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")

def main():
    print('숫자 야구 게임을 시작합니다')
    while 1:

        strike=0
        ball=0
        computer=randomnumber()




        while 1:
        
            computer1=computer.copy()
            
            strike=0
            ball=0
            
            a=input('숫자를 입력해주세요 :')
            
            if len(a) != 3:
                raise ValueError("3자리 숫자를 입력해주세요")
            
            if not a.isdigit():
                raise ValueError("숫자만 입력 가능합니다")
                    
            numbers = [int(x) for x in a]
            if len(set(numbers)) != 3:
                raise ValueError("중복되지 않은 숫자를 입력해주세요")
                
            if not all(1 <= x <= 9 for x in numbers):
                raise ValueError("1부터 9까지의 숫자만 입력 가능합니다")
                    
            user_numbers = numbers
            
            # 스트라이크 계산
            strike = sum(1 for i in range(3) if user_numbers[i] == computer[i])
            
            # 볼 계산
            ball = sum(1 for i in range(3) for j in range(3)
                      if i != j and user_numbers[i] == computer[j])

            computer=computer1  

            if ball==0 and strike ==0 :
                nothing()
            elif strike==3 :
                onlystrike(strike)
                print('게임 종료')
                break

            elif ball==0 :
                onlyball(ball)
            elif strike==0 :
                onlystrike(strike)
            elif ball!=0 and strike!=0 :
                ballandstrike(ball,strike)
        pick()
        press = input().strip()
        if press not in ['1', '2']:
            raise ValueError("1 또는 2만 입력 가능합니다")
        if press == '2':
             break

   
    
    
    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
