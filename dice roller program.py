import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
print('you have a maximum number of 5 dice rolls')
NumberOfSides=int(input('pick a number between 2 and 6,how many sides the dice has'))
while NumberOfSides>6 or NumberOfSides<2:
    NumberOfSides=int(input('pick a number between 1 and 6,how many sides the dice has'))

NumberOfRolls=int(input('how many rolls do you want to roll?'))
while NumberOfRolls>5 or NumberOfRolls<1:
    NumberOfRolls=int(input('pick a number between 1 and 5,how many rolls do you want to roll'))

for roll in range(0,NumberOfRolls):
    DiceFace=random.randint(1,NumberOfSides)
    for line in dice_art[DiceFace]:
        print(line)