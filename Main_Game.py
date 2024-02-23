import random 
import moves
import Termmon
import Ai
#var
FirstRivBAiTM=[]
FirstRivBAiT=[]
StaterMove=[]
Starter=[]
####
def RivBattle_p():
    global Starter
    global StaterMove
    global FirstRivBAiT
    movea = input('What Move Will You Use: ')
    if movea == StaterMove[4]:  
        chancerolla = random.randint(0, 100)
        if chancerolla == StaterMove[2] or chancerolla < StaterMove[2]:
            FirstRivBAiT[1] -= StaterMove[1]  
            if FirstRivBAiT[1] <= 0:  
                print('You Won')
            else:
                Ai.Firstrivbattle()
        else:
            print('Move Failed')
            Ai.Firstrivbattle()
    else:
        print('That\'s Not A Move!!!')
        RivBattle_p()

  
name=input('''                                ---------------------------------
                                [ hi whould you like a tutorail ]
                                [type down below]
                                -----------------
                               <''') 

if name == 'yes':
  print('''                                ------------------------------
                                [well lets get the basics down]
                                [we use termmon to have term fights]
                                [so both players send out ther termmon ]
                                [then you fight with a turend based fight systeam]
                                [and thats it]
                                --------------''')
  wait = input('')


opt = input('''                                ------------------
                                [select a termmmon]
                                [to be you starter]
                                [looper,stringer,varbolt]
                                -----------------
                                <''')
if opt == 'looper':
    Starter = Termmon.looper
    StaterMove = moves.False_Blast
    FirstRivBAiT = Termmon.varbolt  
    FirstRivBAiTM = moves.Data_Creat
elif opt == 'stringer':
    Starter = Termmon.stringer
    StaterMove = moves.Repeat_That
    FirstRivBAiT = Termmon.looper  
    FirstRivBAiTM = moves.False_Blast
elif opt == 'varbolt':
    Starter = Termmon.varbolt
    StaterMove = moves.Data_Creat
    FirstRivBAiT = Termmon.stringer  
    FirstRivBAiTM = moves.Repeat_That
  
print('You Chose',Starter[0],'Now You Can Start Your Journey!!!!')
riv = input('''                                --------------------------------
                                [Stop Right Their Im your Rival]
                                [Harold]
                                [Fight me]
                                ----------
                                <''')
if riv == 'yes':
  print('You Sent Out'+Starter[0])
  RivBattle_p()
