import random
import Main_Game
import moves
import Termmon



def Firstrivbattle():
    chancerollt = random.randint(0,100)
    if chancerollt == Main_Game.FirstRivBAiTM[2] or chancerollt < Main_Game.FirstRivBAiTM[2]:
        print('Harold Used'+ Main_Game.FirstRivBAiTM[4])
        Main_Game.Starter[1] -= Main_Game.FirstRivBAiTM[1]
        if Main_Game.Starter[1] <= 0:
           print('You Lose')
        else:
         print('You Did',Main_Game.FirstRivBAiTM[1],'Dmg To' + Main_Game.Starter[0])
         Main_Game.RivBattle_p()