import random as rand
def getNumber():
    input1 = int(input("Guess next number : "))
    return input1
def getRandomNumber():
    return rand.randint(0,100)
def checkNumberFromImputAndReturnTip(randomNumber, userInputNumber):
    if(randomNumber > userInputNumber):
        print("Za mała liczba")
        return 0
    else:
        if(randomNumber<userInputNumber):
            print("Za duza liczba")
            return 0
        else:
            print("Brawo mój przyjacielu")
            return 1
if __name__ == "__main__":
    randomNumber = getRandomNumber()
    userInput = getNumber()
    while(checkNumberFromImputAndReturnTip(randomNumber,userInput)==0):
        userInput = getNumber()
