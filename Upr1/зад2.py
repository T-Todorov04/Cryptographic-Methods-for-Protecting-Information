import random
def TOTO():
    allNumbers = list(range(1, 50))

    myNumbers = []
    print(myNumbers)
    while True:
        myNumberInput = int(input("Въведете число: "))
        if myNumberInput in myNumbers:
            print("Въведете число, което не е вече избрано")
        elif myNumberInput not in allNumbers:
            print("Въведете число между 1 и 49")
        else:
            myNumbers.append(myNumberInput)
        if len(myNumbers) == 6:
            break
    print("Вашите числа са: ",myNumbers)


    TOTOnumbers = [random.randint(1, 50) for i in range(6)]

    guessedNumbers = []
    for num in myNumbers:
        if num in TOTOnumbers:
            guessedNumbers.append(num)

    print("Познахте ", len(guessedNumbers), " числа")

TOTO()