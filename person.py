#We are defining functions for each individual quests in this package
'''health,wealth,intelligence,confidence are all attributes type of all these variables is int
    message is a string type variable which will take the final win or loose message from Conditions package and pass it to the app.py package for the user to see
    To run this program we will be calling the quests funcntion in app.py package and quests will run goesSchool,goesCollege and other functions one by one
    each time a function/quest is completed the value of questLvl will be updated and so will be the value of attributes.
    Therefore questLvl is a variable whose value is int and changes to string at the end when the game is over
    win condition for person will be: if player wins sub quests which are goesSchool and goesCollege and a main quest(that means atleast 3 quests in total) or if the player only wins a main quest like FindsJob or SolvesAGlobalProblem 
'''

import Conditions
def quests(rolling):
    health = 1
    wealth = 1
    intelligence = 2 
    confidence = 1
    message = ""
    questLvl = 1 
    winStreak = 0

    def goesSchool():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(intelligence,confidence,None,0,winStreak)
            return health,wealth,tup1[0],tup1[1],tup1[3],tup1[4]
    
    if questLvl == 1:
        tup1 = goesSchool()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        questLvl = 2
        winStreak = tup1[5]

    def goesCollege():
        if(type(rolling) == str ):

        #taking parameter from the previous equation #p is intelligence and q is confidence
            tup1 = Conditions.challengeCompleted(health,confidence,None,0,winStreak)
            return tup1[0],wealth,intelligence,tup1[1],tup1[3],tup1[4]

    if questLvl == 2:
        tup1 = goesCollege()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        questLvl = 3
        winStreak = tup1[5]

    def FindsJob():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(wealth,intelligence,confidence,1,winStreak)
            return health,tup1[0],tup1[1],tup1[2],tup1[3],tup1[4]

    if questLvl == 3:
        tup1 = FindsJob()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        questLvl = 4
        winStreak = tup1[5]

    def SolvesAGlobalProblem():
        if(type(rolling) == str ):
            tup1 = Conditions.challengeCompleted(wealth,intelligence,confidence,11,winStreak)
            return health,tup1[0],tup1[1],tup1[2],tup1[3],tup1[4]

    if questLvl == 4:
        tup1 = SolvesAGlobalProblem()
        health = tup1[0]
        wealth = tup1[1]
        intelligence = tup1[2]
        confidence = tup1[3]
        message = tup1[4]
        questLvl = "game over"
        winStreak = tup1[5]

    return health,wealth,intelligence,confidence,message
    