import Conditions

def quests(rolling):
    health = 1
    wealth = 0
    intelligence = 0
    confidence = 1
    message = ""
    winStreak = 0
    questLvl = 1

    def SurviveThisWorld():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(intelligence,confidence,None,"0V",winStreak)
            return health,wealth,tup1[0],tup1[1],tup1[3],tup1[4]

    if questLvl == 1:
        # we are not checking if he survived the world or not that is default won
        health = 2
        wealth = 3
        intelligence = 2
        confidence = 4
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = 2

    def constructAPlan():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(health,intelligence,None,"0V",winStreak)
            return tup1[0],wealth,tup1[1],confidence,tup1[3],tup1[4]

    if questLvl == 2:
        tup1 = constructAPlan()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = 3

    def stopHero():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(intelligence,confidence,health,"1V",winStreak)
            return health,wealth,tup1[0],tup1[1],tup1[4],tup1[5]
    
    if questLvl == 3:
        tup1 = stopHero()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        dice = tup1[5]
        questLvl = 4
    
    def ruleTheWorld():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(health,wealth,intelligence,"11V",winStreak)
            return tup1[1],tup1[1],tup1[2],confidence,tup1[4],tup1[5]
    
    if questLvl == 4:
        tup1 = ruleTheWorld()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = "max"
        message = tup1[4]
        winStreak = tup1[5]
        questLvl = "game over"

    return health,wealth,intelligence,confidence,message,dice
    