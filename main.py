import random
try:
    dice = random.randint(1, 6)
    userInput = int(input("Make your guess for a 6 int dice: "))
    if dice == userInput:
        print("You are right! The dice was ", dice)
    elif dice != userInput:
        print("Not lucky today? The dice was ", dice)
    pass
except Exception as e:
    print(e)
