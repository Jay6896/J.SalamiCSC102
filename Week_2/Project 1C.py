# PSEUDOCODE FOR AGE SWAPPING
# INPUT name1
# INPUT age1
# INPUT name2
# INPUT age2
# PRINT name1, age1, name2, age2
# LIST ageContainer[]
# APPEND age1 to ageContainer[]
# APPEND age2 to ageContainer[]
# SET age1 to ageContainer[1]
# SET age2 to ageContainer[0]
# PRINT name1, age1, name2, age2

print("Hello user, I would like you to input 2 names for me with their corresponding ages.")

name1 = input("Input first name")
age1 = int(input("Input first names age (In numbers only)"))
name2 = input("Input second name")
age2 = int(input("Input second names age (In numbers only)"))
ageContainer = []


ageContainer.append(age1)
ageContainer.append(age2)
print("Okay so " + str(name1) + " is " + str(age1) + " years old and " + str(name2) + " is " + str(age2) + " years old ")
print("I shall swap their ages... \n\n")

age1 = ageContainer[1]
age2 = ageContainer[0]

print("Now that the ages have been swapped, \n" + str(name1) + " is " + str(age1) + " years old and " + str(name2) + " is " + str(age2) + " years old ")