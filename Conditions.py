import random

def challengeCompleted(att1,att2,att3,isMain,winStreak):
    dice = random.randint(1,6) + random.randint(1,6)
    
    def questCompleted(att1,att2,att3,isMain):
        message = ""
        newStreak = 0
        if(dice==2 or dice==3):
            outcome = 1

        if(dice>=4 and dice<=7):
            outcome = 2

        if(dice>=8 and dice<=10):
            outcome = 3

        if(dice>=10):
            outcome = 4

        if(outcome == 1):
            message = ("Oops you loose and it is a critical loss!, attributes decreased by 1 ")
            att1 -= 1 
            att2 -= 1 

        if(outcome == 2):
            message = ("it is a loss but attributes remain same ")
        
        if(outcome == 3):
            message = ("it is a win but attributes remain same ")
            newStreak = winStreak + 1
            
        if(outcome == 4):
            if isMain == 1 or isMain == 11 or isMain =="1V":
                att1 = 4
                att3 = 4
                att2 += 2
                newStreak = winStreak + 1

            #if Villain won the last quest his attributes will be max
            
            elif isMain == "11V":
                att1 = "max"
                att2 = "max"
                att3 = "max"

            else:
                message =("Congrats you won and it is a critical win!, attributes increased by 1 ")     
                att1 += 1 
                att2 += 1
                newStreak = winStreak + 1 
        
        if isMain == 11 or isMain == 1:
            def isWin():
                
                if isMain =="0V" or isMain =="1V" or isMain =="11V":
                    #different win condition for Villian
                    if(winStreak >= 2):
                        message =("Congrats you won the game: ")
                    elif(isMain == 1 or isMain == 11) and outcome == 4 :
                        message =("Congrats you cleared the main quest and you won the game ")
                    else:
                        message =("Sorry you loose! ")
                    return message

                if(winStreak >= 3):
                    message =("Congrats you won the game: ")
                elif(isMain == 1 or isMain == 11) and outcome == 4 :
                    message =("Congrats you cleared the main quest and you won the game ")
                else:
                    message =("Sorry you loose! ")
                return message
                

            message = isWin()
        
        #Special if block for superhero 
        if isMain == "fightingVillain":
            if (att1 >= 3 and att2 >= 3) and att3 >= 3:
                #if hero's attributes are more than a threshold he wins 
                message = "Congratulations you defeated the villian: "
                return message

        return att1,att2,att3,message,newStreak

    returnQuestCompl = questCompleted(att1,att2,att3,isMain)
    return returnQuestCompl[0],returnQuestCompl[1],returnQuestCompl[2],returnQuestCompl[3],returnQuestCompl[4]



         
       