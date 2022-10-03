#This game is created by Yatharth Jain
'''
    There are following variables used and their uses are listed:
    choice variable inputs a number from user, type is int
    attributeValues calls the Quests function and stores the values returned by it, it belongs to class tuple
    rolling is a variable which inputs any string character from the user and passes it to Quests function, passing this rolling varaible to increase user interaction

'''

import person
import Superhero
import Villain


def helloMes():
    print("Welcome to my adventure game: ")

def introduceCharacters():
    print("\n there are following characters in the game: ")
    print("1. An ordinary person")
    print("2. A hero")
    print("3. A villian")

    print("\n Every character has the following attributes: health,wealth,intelligence and confidence")
    print("The rules of this game are simple:")
    print("\n Critical Loss (e.g., 2 - 3): challenge is lost and the attribute that is based on is decreased") 
    print("Loss (e.g., 4-7): challenge is lost, no change in the character’s attributes") 
    print("Win (e.g., 8-10): challenge is won, no change in the character’s attributes") 
    print("Critical Win (e.g., 11-12): challenge is won and the attribute that is based on increases ")
    print("\n To win this game you must win atleast 3 quests or win 1 main quest")

def chooseCharacter():
    choice = int(input("\n To enter the game enter which character you want to choose, For example enter 1 for person: "))

    if choice == 1:
        
        print("Congratulations you choose to be an ordinary Person!")
        print("\n The First mission is to complete school and increase intelligence and confidence ")
        print("\n The next mission is to clear college and increase health and confidence ")
        print(f"\n Next is the time for the main quest to find a job if cleared confidence will be 4, intelligence will be 4 and wealth increased by 2 ")
        print("\n Finally it is time to solve a global problem, may it be global warming, greenhouse effect or protecting wildlife: remember it is a main quest too!")
        print(f"\n The health is 1, wealth is 1, intelligence is 2 and confidence is 1")
        rolling = input("\n Enter any character to start the game: \n ")

        attributeValues = person.quests(rolling)
        print(f"Your attributes after the game is completed are: health is {attributeValues[0]}, wealth is {attributeValues[1]} intelligence is {attributeValues[2]} and confidence is {attributeValues[3]} ")
        print(f"The final message is: {attributeValues[4]}")
    
    if choice == 2:
        print("Congratulations you choose to be a hero \n")
        print("Our hero like any other hero is on a journey to find himself and become stronger and wiser: \n")
        print("Ohh! but the story also has a villian more powerful than our hero, can you win quests and become strong enough to defeat the villian? \n")
        
        print("\n The First mission is to unfold the villian's plan and increase your intelligence and confidence")
        print("\n The next mission is to prepare for battle and increase your health ")
        print("\n Next is the time for the main quest to fight the villian, to increase confidence and intelligence ")
        print("\n Finally it is time for the main quest, to destroy villian's plan: remember it is a main quest and your wealth will be increased")

        print(f"\n The health is 2, wealth is 1, intelligence is 2 and confidence is 4")
        rolling = input("\n Enter any character to start the game: \n ")

        attributeValues = Superhero.quests(rolling)
        print(f"Your current attributes: health is {attributeValues[0]}, wealth is {attributeValues[1]} intelligence is {attributeValues[2]} and confidence is {attributeValues[3]} ")
        print(f"The final message is: {attributeValues[4]}")

    if choice == 3:
        print("Congratulations you choose to be a Villain \n")
        print("Our villain has a tragic back-story, as a child he was tortured and bullied badly on the streets and never had proper food and shelter, now he has risen to take revenge from this cruel world!")
        print("Could you become succesful in conquering the world or will the hero stop you, fate lies in your hands!")

        print("\n The First mission is to survive the cruel world as a child: ")
        print("\n The next mission is to construct a plan to conquer the world and increase your health and intelligence ")
        print("\n In the next quest you will have to stop the hero from spoiling your plan,confidence and intelligence would be increased after this quest")
        print("\n Finally it is time for the main quest, to rule this world and make changes in it according to you ")

        print(f"\n The health is 1, wealth is 0, intelligence is 0 and confidence is 1")# the villain has the least attributes amongst all characters because of his tragic childhood
        rolling = input("\n Enter any character to start the game: \n ")

        attributeValues = Villain.quests(rolling)
        print(f"Your current attributes: health is {attributeValues[0]}, wealth is {attributeValues[1]} intelligence is {attributeValues[2]} and confidence is {attributeValues[3]} ")
        print(f"The final message is: {attributeValues[4]}")

helloMes()
introduceCharacters()
chooseCharacter()
