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
        l=[]
        computer=randomnumber()




        while 1:
        
            computer1=computer.copy()
            
            strike=0
            ball=0
            l=[]
            a=input('숫자를 입력해주세요 :')
            
            if len(a) !=3 :
                raise ValueError
                    
            for r in range(len(a)) :
                l.append(int(a[r]))
            
            for i in range(len(computer)-1,-1,-1) :
                if computer[i] == l[i] :
                    strike+=1
                    computer.pop(i)
                    l.pop(i)
                    
                    
            
            for k in range(len(l)) :
                if l[k] in computer :
                    ball+=1
            
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
        press=input()
        if press!='1':
            break

   
    
    
    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
