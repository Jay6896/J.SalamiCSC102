import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

class Delivery:

    def first(self, root, size_entry, location_entry):     
        window = tk.Toplevel(root) 
        window.title("Adekunle Gold Delivery Service") 
        window.geometry("300x200")

        label_1 = tk.Label(window, text=f"\nYour Total fee is N2,000") 
        label_1.pack()

        root.mainloop()

    def second(self, root, size_entry, location_entry):     
        window = tk.Toplevel(root) 
        window.title("Adekunle Gold Delivery Service") 
        window.geometry("300x200")

        label_1 = tk.Label(window, text=f"\nYour Total fee is N1,500") 
        label_1.pack()

        root.mainloop()

    def third(self, root, size_entry, location_entry):     
        window = tk.Toplevel(root) 
        window.title("Adekunle Gold Delivery Service") 
        window.geometry("300x200")

        label_1 = tk.Label(window, text=f"\nYour Total fee is N5,000") 
        label_1.pack()

        root.mainloop()

    def fourth(self, root, size_entry, location_entry):     
        window = tk.Toplevel(root) 
        window.title("Adekunle Gold Delivery Service") 
        window.geometry("300x200")

        label_1 = tk.Label(window, text=f"\nYour Total fee is N4,000") 
        label_1.pack()

        root.mainloop()

    def last(self, root, size_entry, location_entry):     
        window = tk.Toplevel(root) 
        window.title("Adekunle Gold Delivery Service") 
        window.geometry("300x200")

        label_1 = tk.Label(window, text=f"\nSorry, we dont ship to your location") 
        label_1.pack()

        root.mainloop()

    def submit(self, root, size_entry, location_entry):
        size = int(size_entry.get())
        location = location_entry.get()

        if size >= 10  and location == "PAU":
             self.first(root, size_entry, location_entry)
        elif size < 10 and location == "PAU":
             self.second(root, size_entry, location_entry)
        if size >= 10  and location == "EPE":
             self.third(root, size_entry, location_entry)
        elif size < 10 and location == "EPE":
             self.fourth(root, size_entry, location_entry)
        else:
             self.last(root, size_entry, location_entry)
            



entrance = msgbox.askyesno("Adekunle Gold Delivery Service", "Welcome to Adekunle Gold Delivery Service! \n\nWould you like to deliver any items?")
entrance = Delivery()
if entrance:
    root = tk.Tk()
    root.title("Adekunle Gold Delivery Service")
    root.geometry("400x300")

    root.lift()
    root.attributes('-topmost', True)

    size_label = tk.Label(root, text="What is the size of the item you are delivering? \n And where do you want to deliver to? \n") 
    size_label.pack()

    size_label2 = tk.Label(root, text="Input the size in Kg \n(TYPE THE NUMBERS ONLY, DO NOT PUT KG)") 
    size_label2.pack()

    size_entry = tk.Entry(root) 
    size_entry.pack()

    location_label = tk.Label(root, text="What location do you want me to deliver to? \nFor now, we only deliver to PAU and Epe \n") 
    location_label.pack()

    location_label2 = tk.Label(root, text="Input your location \n(TYPE PAU or EPE and in all caps)") 
    location_label2.pack()

    location_entry = tk.Entry(root) 
    location_entry.pack()


    submit_button= tk.Button(root, text="Submit", command=lambda: entrance.submit(root, size_entry, location_entry)) 
    submit_button.pack()

    root.mainloop()

else:
    root = tk.Tk()
    root.title("Adekunle Gold Delivery Service")
    root.geometry("400x200")
    root.destroy()
        


