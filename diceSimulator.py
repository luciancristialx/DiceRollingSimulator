import random
print("This is a DICE SIMULATOR")

number: int
userInput = input("Press y to roll the dice!\n")

while userInput == "y":
    number = random.randint(1, 6)
    if number == 1:
        print('-----------')
        print('|         |')
        print('|    0    |')
        print('|         |')
        print('-----------')
    elif number == 2:
        print('-----------')
        print('|         |')
        print('| 0     0 |')
        print('|         |')
        print('-----------')
    elif number == 3:
        print('-----------')
        print('| 0       |')
        print('|    0    |')
        print('|       0 |')
        print('-----------')
    elif number == 4:
        print('-----------')
        print('|  0   0  |')
        print('|         |')
        print('|  0   0  |')
        print('-----------')
    elif number == 5:
        print('-----------')
        print('|  0   0  |')
        print('|    0    |')
        print('|  0   0  |')
        print('-----------')
    elif number == 6:
        print('-----------')
        print('| 0  0  0 |')
        print('|         |')
        print('| 0  0  0 |')
        print('-----------')
    userInput=input("Roll again? Press y: ")

