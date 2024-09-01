#TASK 4
#Rock Paper Scissors Game

d=['paper','scissor','rock']
import random
while True:
    e=0
    f=0
    
    a=int(input("1.start , 2.exit"))
    if a==1:
        for i in range(0,5):
            s=int(input("1. paper , 2.rock , 3.scissor"))
            if s==1:
                u='paper'
            elif s==2:
                u='rock'
            elif s==3:
                u='scissor'
                
            c=random.choice(d)
            if c==u:
                print("Game Draw")
                print("computer value",c)
                print("user value",u)
                
            elif (c=='paper' and u=='scissor') or (c=='rock' and u=='paper') or (c=='scissor' and u=='rock'):
                print("user Game Win")
                print("computer value",c)
                print("user value",u)
                e=e+1
                
            else:
                print("Computer Win")
                print("computer value",c)
                print("user value",u)
                f=f+1
                
        if e==f:
            print("Game Draw")
        elif e>f:
            print("user win",e)
        elif f>e:
            print("computer win",f)
          
    else:
        break
    
    
            