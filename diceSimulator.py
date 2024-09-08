import random
print("Welcome to dice simulator!!")
game_is_on = True
try:
    while game_is_on:
        sides = int(input("  Enter the number of sides: "))
        if sides < 1:
            raise ValueError("Number of sides should be postive")
        
        rolls = int(input("  Enter no of rolls: "))
        if rolls < 1:
            raise ValueError("Number of roll should be positive")

        rolling=[]

        for i in range(rolls):
            dice = random.randint(1, sides)
            rolling.append(dice)

        print(f"Resuts:{rolling}")
        roll_again = input("Do you want roll again(yes/no): ").strip().lower()
        if roll_again == "no":
            game_is_on = False  
except ValueError as e:
    print(f"error:{e}.Please enter a valid number")         
        

