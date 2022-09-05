import random
import time
import sys
import copy




def forest():
    lines_forest=[]
    sword=0
    fight1=0
    armour_and_boots=0
    lines_forest.append('you have obtained a "Blunt sword"....')#0
    lines_forest.append('are you sure(YES/NO')#1
    lines_forest.append('thats a bad decision')#2
    lines_forest.append('oh!! a wild monster has appeared, what would you like to do?(RUN or Fight)')#3
    lines_forest.append('Pew pew pew pew pew pew pew pew HAYAAAAA')#4
    lines_forest.append('nice you have defeated the forest monster')#5
    lines_forest.append('an leather armour and leather boots have been droped by the monster, do you want to pick it up?(YES or NO)')#6
    lines_forest.append('you lost the battle and lost your humanity')#7
    lines_forest.append('i dont think thats going to be an option')#8
    lines_forest.append('you have to fight with your life on the line')#9
    lines_forest.append('whak whak whak whak slap slap whak THUD')#10
    

    c=[1,2,3,4,5,6,7,8,9,10]
    chance1=random.choice(c)
    l=[1,2]
    luck=random.choice(l)

    print('you found a mystery box it might contain something usefull.\npress any number(1-2) to test your luck!!....')
    i=int(input('number>>'))
    if i==luck:
        print(lines_forest[0])
        time.sleep(1)
        sword=1
    else:
        print('bad luck, nothing was found')
        time.sleep(1)
        sword=0



    print(lines_forest[3])
    r2=input().lower()
    r4=''
    if sword==1:
        if r2=='fight':
            if chance1<=8:
                
                print(lines_forest[4])
                time.sleep(0.5)
                
                print(lines_forest[5])
                time.sleep(0.5)
                
                print(lines_forest[6])
                r4=input().lower()
                fight1=1
            else:
                
                print(lines_forest[7])

        else:
            
            print(lines_forest[8])
            time.sleep(0.5)
            
            print(lines_forest[9])
            time.sleep(0.5)
            if chance1<=8:
                print(lines_forest[4])
                time.sleep(0.5)
                print(lines_forest[5])
                time.sleep(0.5)
                print(lines_forest[6])
                r4=input().lower()
                fight1=1
            else:
                print(lines_forest[7])
    else:
        if r2=='fight':
            if chance1<=4:
                print(lines_forest[10])
                time.sleep(0.5)
                print(lines_forest[5])
                time.sleep(0.5)
                print(lines_forest[6])
                r4=input().lower()
                fight1=1
            else:
                print(lines_forest[7])
        else:
            print(lines_forest[8])
            time.sleep(0.5)
            print(lines_forest[9])
            time.sleep(0.5)
            if chance1<=4:
                print(lines_forest[10])
                time.sleep(0.5)
                print(lines_forest[5])
                time.sleep(0.5)
                print(lines_forest[6])
                r4=input().lower()
                fight1=1
            else:
                print(lines_forest[7])
    
    if r4=='yes':
        armour_and_boots=1
    l1=[armour_and_boots,sword,fight1]
    return l1



def gatemonster(lst):
    if lst==None:
        return
    armour_and_boots, sword, fight1 = lst[0],lst[1], lst[2]

    if fight1==1:
        fight2=0
        c=[1,2,3,4,5,6,7,8,9,10]
        cimage1=copy.deepcopy(c)
        cimage2=copy.deepcopy(c)
        cimage3=copy.deepcopy(c)
        cimage4=copy.deepcopy(c)
        chances_0=[]
        chances_sah=[]
        chances_s=[]
        chances_ah=[]
        new_equipment=0
        for i in range(8):
            cloop=random.choice(cimage1)
            chances_sah.append(cloop)
            cimage1.remove(cloop)

        for i in range(7):
            cloop=random.choice(cimage2)
            chances_s.append(cloop)
            cimage2.remove(cloop)

        for i in range(6):
            cloop=random.choice(cimage3)
            chances_ah.append(cloop)
            cimage3.remove(cloop)

        
        for i in range(4):
            cloop=random.choice(cimage4)
            chances_0.append(cloop)
            cimage4.remove(cloop)

        hit_sah=0
        hit_s=0
        hit_ah=0
        hit_0=0

        lines_gate=[]
        lines_gate.append('a new set of equipment has been droped, do you want to pick it up(Y/N)')#0
        lines_gate.append('not a good choice.., do yoy wish to reconsider?(Y/N)')#1
        
        print('entering the village........')
        time.sleep(1)
        
        print('a gate keeper is watching your village entrance, you have to kill it to proceed further')
        if sword==1 and armour_and_boots==1:
            print('you have armour, boots and sword so this should be an easy task for you')
            print('you get five chances to hit the monster, you have to hit the monster 2 times')
            print('8 out of the 10 numbers can hit the gate keeper')
            print('enter 5 numbers one by one')
            for i in range(5):
                hitnum=int(input('number>>'))
                if hitnum in chances_sah:
                    print('Hit!!')
                    hit_sah=hit_sah+1
                    if hit_sah==2:
                        print('you have defeated the monster')
                        fight2=1
                        break
                else:
                    print('miss')
            if hit_sah<2:
                print('you have lost the battle')
            else:
                print(lines_gate[0])
                if input().lower()=='y':
                        new_equipment=1
                else:
                    print(lines_gate[1])
                    if input().lower()=='y':
                        print(lines_gate[0])
                        if input().lower()=='y':
                            new_equipment=1
                        else:
                            print('Ok, good luck to your grave')
                    else:
                        print('Ok, good luck to your grave')
        if sword==1 and armour_and_boots==0:
            print('you only have sword so this should be a difficult task for you')
            print('you get five chances to hit the monster, you have to hit the monster 2 times')
            print('7 out of the 10 numbers can hit the gate keeper')
            print('enter 5 numbers one by one')
            for i in range(5):
                hitnum=int(input('number>>'))
                if hitnum in chances_s:
                    print('Hit!!')
                    hit_s=hit_s+1
                    if hit_s==2:
                        print('you have defeated the monster')
                        fight2=1
                        break
                else:
                    print('miss')
            if hit_s<2:
                print('you have lost the battle')
            else:
                print(lines_gate[0])
                if input().lower()=='y':
                        new_equipment=1
                else:
                    print(lines_gate[1])
                    if input().lower()=='y':
                        print(lines_gate[0])
                        if input().lower()=='y':
                            new_equipment=1
                        else:
                            print('Ok, good luck to your grave')
                    else:
                        print('Ok, good luck to your grave')
            
        if sword==0 and armour_and_boots==1:
            print('you only have an armour and boots so this should be a difficult task for you')
            print('you get five chances to hit the monster, you have to hit the monster 2 times')
            print('6 out of the 10 numbers can hit the gate keeper')
            print('enter 5 numbers one by one')
            for i in range(5):
                hitnum=int(input('number>>'))
                if hitnum in chances_ah:
                    print('Hit!!')
                    hit_ah=hit_ah+1
                    if hit_ah==2:
                        print('you have defeated the monster')
                        fight2=1
                        break
                else:
                    print('miss')
            if hit_ah<2:
                print('you have lost the battle')
            else:
                print(lines_gate[0])
                if input().lower()=='y':
                        new_equipment=1
                else:
                    print(lines_gate[1])
                    if input().lower()=='y':
                        print(lines_gate[0])
                        if input().lower()=='y':
                            new_equipment=1
                        else:
                            print('Ok, good luck to your grave')
                    else:
                        print('Ok, good luck to your grave')
            

        if sword==0 and armour_and_boots==0:
            print('you dont have any equipment so this should be an impossibel task for you')
            print('you get five chances to hit the monster, you have to hit the monster 2 times')
            print('4 out of the 10 numbers can hit the gate keeper')
            print('enter 5 numbers one by one')
            for i in range(5):
                hitnum=int(input('number>>'))
                if hitnum in chances_0:
                    print('Hit!!')
                    hit_0=hit_0+1
                    if hit_0==2:
                        print('you have defeated the monster')
                        fight2=1
                        break
                else:
                    print('miss')
            if hit_0<2:
                print('you have lost the battle')
            else:
                print(lines_gate[0])
                if input().lower()=='y':
                        new_equipment=1
                else:
                    print(lines_gate[1])
                    if input().lower()=='y':
                        print(lines_gate[0])
                        if input().lower()=='y':
                            new_equipment=1
                        else:
                            print('Ok, good luck to your grave')
                    else:
                        print('Ok, good luck to your grave')
       

    
        l2=[sword,armour_and_boots,new_equipment,fight2,fight1]
        return l2
    


def boss(lst):
    if lst == None:
        return
    sword,armour_and_boots,new_equipment, fight2, fight1=lst[0],lst[1],lst[2],lst[3],lst[4]
    if fight2==1:
            fight3=0
            print('entering the boss den....')
            time.sleep(1)
            c=[1,2,3,4,5,6,7,8,9,10]
            cbimage1=copy.deepcopy(c)
            cbimage2=copy.deepcopy(c)
            cbimage3=copy.deepcopy(c)
            chance_sah={}
            chance_ne={}
            chance_a_s={}

            
            
            bosshealth=3

            if new_equipment==1:

                for i in range(3):
                    cloop=random.choice(cbimage2)
                    chance_ne[cloop]=2
                    cbimage2.remove(cloop) 
                for i in range(5):
                    cloop=random.choice(cbimage2)
                    chance_ne[cloop]=1
                    cbimage2.remove(cloop)
                print('because you have the better equipment, i think you can take on the boss')
                print('some of your attacks will do normal damage of 1 and some will do critical damage of 2 hits')
                print('you will have 4 chances to attack and for the monster t be defeated you need to do 3 hits of any manner')

                for i in range(4):
                    hit=int(input(('number>>')))
                    if hit in chance_ne.keys():
                        if chance_ne[hit]==1:
                            print('normal hit - 1')
                            bosshealth=bosshealth-1
                            if bosshealth==0:
                                print('you have defeated the boss')
                                fight3=1
                                break
                        else:
                            print('critical hit - 2')
                            bosshealth=bosshealth-2
                            if bosshealth<1:
                                print('you have defeated the boss')
                                fight3=1
                                break
                    else:
                        print('Miss')
                    
                if bosshealth>0:
                    print('you have been defeated by the boss')
            
            elif sword==1 and armour_and_boots==1 and new_equipment==0:


                for i in range(2):
                    cloop=random.choice(cbimage3)
                    chance_sah[cloop]=2
                    cbimage3.remove(cloop) 
                for i in range(4):
                    cloop=random.choice(cbimage3)
                    chance_sah[cloop]=1
                    cbimage3.remove(cloop)
                print('as you didnt have better equipment you might not be able to kill the boss')
                print('some of your attacks will do normal damage of 1 and some will do critical damage of 2 hits')
                print('you will have 4 chances to attack and for the monster t be defeated you need to do 3 hits of any manner')

                for i in range(4):
                    hit=int(input(('number>>')))
                    if hit in chance_sah.keys():
                        if chance_sah[hit]==1:
                            print('normal hit - 1')
                            bosshealth=bosshealth-1
                            if bosshealth==0:
                                print('you have defeated the boss')
                                fight3=1
                                break
                        else:
                            print('critical hit - 2')
                            bosshealth=bosshealth-2
                            if bosshealth<1:
                                print('you have defeated the boss')
                                fight3=1
                                break
                    else:
                        print('Miss')

                if bosshealth>0:
                    print('you have been defeated by the boss')               

            elif (sword==1 and armour_and_boots==0) or (sword==0 and armour_and_boots==1):




                for i in range(2):
                    cloop=random.choice(cbimage1)
                    chance_a_s[cloop]=2
                    cbimage1.remove(cloop) 
                for i in range(2):
                    cloop=random.choice(cbimage1)
                    chance_a_s[cloop]=1
                    cbimage1.remove(cloop)

                print('as you dont have good equipment you might not be able to kill the boss')
                print('some of your attacks will do normal damage of 1 and some will do critical damage of 2 hits')
                print('you will have 4 chances to attack and for the monster t be defeated you need to do 3 hits of any manner')
                for i in range(4):
                        hit=int(input(('number>>')))
                        if hit in chance_a_s.keys():
                            if chance_a_s[hit]==1:
                                print('normal hit - 1')
                                bosshealth=bosshealth-1
                                if bosshealth==0:
                                    print('you have defeated the boss')
                                    fight3=1
                                    break
                            else:
                                print('critical hit - 2')
                                bosshealth=bosshealth-2
                                if bosshealth<1:
                                    print('you have defeated the boss')
                                    fight3=1
                                    break
                        else:
                            print('Miss')

                if bosshealth>0:
                        print('you have been defeated by the boss')  

                        
            elif sword==0 and armour_and_boots==0:
                    print('you have the worst equipment possible, u are going to kill yourself if you fight')
                    if input(print('do you still want to fight(Y/N)')).lower()=='y':
                        print('you died')
                    else:
                        print('you lived but you .......................................... ')
                        fight3=2
            if fight3==1:
                print('you have freed the village from the orcs, and now its time for you to vanish into the woods')
                print('thank you for playing the game')
            elif fight3==2:
                print('it was not in your hands to free the village')
                print('thank you for playing the game')
            




if input(' do you want to start the game?(Y/N)').lower()=='y':
    print("once upon a time there was a peacefull village with lush green farms then all of that had to come to an end.")
    time.sleep(0.4)
    print('one day they were attacked and taken over by Orc army')
    time.sleep(0.4)
    print('when there was no hope a silent hero apeared..........')
    time.sleep(0.4)
    i1=input('enter your characaters name')
    print('entering outer forest....')
    boss(gatemonster(forest()))
else:
    print('thank you for not playing the game XD')
            