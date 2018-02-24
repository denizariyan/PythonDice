import random
try:
    dice = random.randint(1, 6)
    endFlag = 1
    while endFlag:
        userInput = int(input("Make your guess for a 6 int dice: "))
        if dice == userInput:
            print("You are right! The dice was ", dice)
            endFlag = 0
        elif dice != userInput:
                    if dice < userInput:
                            print("Thats a bit high I see. Try again")
                    else:
                            print("Thats a bit too low. Try again")
                    pass
        pass
except Exception as e:
    print(e)
