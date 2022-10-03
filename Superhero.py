import Conditions

def quests(rolling):
    health = 2
    wealth = 1
    intelligence = 2
    confidence = 4
    message = ""
    winStreak = 0 
    questLvl = 1

    def unfoldPlan():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(intelligence,confidence,None,0,winStreak)
            return health,wealth,tup1[0],tup1[1],tup1[3],tup1[4]

    if questLvl == 1:
        tup1 = unfoldPlan()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        winStreak =tup1[5]
        questLvl = 2

    def prepareBattle():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(health,None,None,0,winStreak)
            return tup1[0],wealth,intelligence,confidence,tup1[3],tup1[4]

    if questLvl == 2:
        tup1 = prepareBattle()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = 3

    def fightVillain():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(intelligence,confidence,health,"fightingVillain",winStreak)
            return tup1[2],wealth,tup1[0],tup1[1],tup1[3],tup1[4]
    
    if questLvl == 3:
        tup1 = fightVillain()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = 4
    
    def DestroyPlan():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(wealth,None,None,11,winStreak)
            return health,tup1[0],intelligence,confidence,tup1[3],tup1[4]
    
    if questLvl == 4:
        tup1 = DestroyPlan()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = "game over"

    return health,wealth,intelligence,confidence,message
    