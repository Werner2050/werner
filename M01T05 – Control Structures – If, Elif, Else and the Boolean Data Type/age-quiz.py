# if, elif and else statements will be used to enable a variety of responses deermined by the data the user enters

age = int(input("What is your age: "))

if age > 100:
    print("Sorry you'are dead.")
elif age > 65:
    print("Enjoy your retirement.")
elif age > 40:
    print("You are over the hill.") 
elif age > 21:
    print("Age is but a number.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 13:
    print("Age is but a number.")
else:
    print("You qualify for kiddies discount.")
