admitted = []
not_admitted = []

def computer_science(name, score, interview):
    if score >= 250 and interview == "y":
        print("Congratulations! You meet the requirements for Computer Science")
        admitted.append(name)
    else:
        print("Sorry, you do not meet the requirements for Computer Science")
        not_admitted.append(name)

def mass_communication(name, score, interview):
    if score >= 230 and interview == "y":
        print("Congratulations! You meet the requirements for Mass Communication")
        admitted.append(name)
    else:
        print("Sorry, you do not meet the requirements for Mass Communication")
        not_admitted.append(name)


print("Hello and welcome to the admissions center \nAs of now only Computer Science and Mass Communication is available")
input1 = int(input("Which course do you want to offer? \ninput 1 for Computer Science and 2 for Mass Communication"))

if input1 == 1:
    name = input("What is your name")
    score = int(input("What was your JAMB score?"))
    interview = input("Did you pass your interview? \nType y or n")
    computer_science(name, score, interview)

elif input1 == 2:
    name = input("What is your name")
    score = int(input("What was your JAMB score?"))
    interview = input("Did you pass your interview? \nType y or n")
    mass_communication(name, score, interview)

else:
    print("Invalid input")


print(f"Admitted Students - {admitted} \nNot-Admitted Students - {not_admitted}")