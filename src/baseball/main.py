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
    
    
    
    
    
    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
