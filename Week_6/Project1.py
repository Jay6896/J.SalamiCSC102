import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

def first():     
    window = tk.Toplevel(root) 
    window.title("Adekunle Gold Delivery Service") 
    window.geometry("300x200")

    label_1 = tk.Label(window, text=f"\nYour Total fee is N5,000") 
    label_1.pack()

    root.mainloop()

def second():     
    window = tk.Toplevel(root) 
    window.title("Adekunle Gold Delivery Service") 
    window.geometry("300x200")

    label_1 = tk.Label(window, text=f"\nYour Total fee is N10,000") 
    label_1.pack()

    root.mainloop()

def submit():
    size = int(size_entry.get())
    location = location_entry.get()

    if size >= 10  and location == "IBEJU":
         first()
    elif size >= 10 and location == "EPE":
         second()



entrance = msgbox.askyesno("Adekunle Gold Delivery Service", "Welcome to Adekunle Gold Delivery Service! \n\nWould you like to deliver any items?")
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

    location_label = tk.Label(root, text="What location do you want me to deliver to? \nFor now, we only deliver to Ibeju-Lekki and Epe \n") 
    location_label.pack()

    location_label2 = tk.Label(root, text="Input your location \n(TYPE IBEJU or EPE and in all caps)") 
    location_label2.pack()

    location_entry = tk.Entry(root) 
    location_entry.pack()


    submit_button= tk.Button(root, text="Submit", command=submit) 
    submit_button.pack()

    root.mainloop()

else:
    root = tk.Tk()
    root.title("Adekunle Gold Delivery Service")
    root.geometry("400x200")
    root.destroy()
        


