import random

class Employee:


    def check_employee(self, name):
        employee_names = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

        if name not in employee_names:
            self.refuse_access(name)
        else:
            self.take_attendance(name)


    def take_attendance(self, name):
        print(name, "you have successfully taken your attendance for today!")
        self.assign_task(name)



    def assign_task(self, name):
        tasks = ["Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"]
        print(name , "is now", random.choice(tasks))



    def refuse_access(self, name):
        print(name, "is not currently employed under Mrs Jane")


userinput = input("Input your name here")
user = Employee()
user.check_employee(userinput)