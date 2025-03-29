print("Welcome to the Izfin Technology Annual Tax Revenue (ATR) Calculator")
print("Please Input your years of experience here at Izfin and your age to receive your ATR")

userExp = int(input("\nEnter your years of experience"))
userAge = int(input("Now Enter your age"))

if userExp > 25 and userAge >= 55:
    print("Your Annual Tax Revenue (ATR) is: N5,600,000")
elif userExp > 20 and userAge >= 45:
    print("Your Annual Tax Revenue (ATR) is: N4,480,000")
elif userExp > 10 and userAge >= 35:
    print("Your Annual Tax Revenue (ATR) is: N1,500,000")
elif userExp < 10 and userAge <= 35:
    print("Your Annual Tax Revenue (ATR) is: N550,000")
else:
    print("You do not qualify for an Annual Tax Revenue")
