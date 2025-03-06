import tkinter
from tkinter import ttk, messagebox

screen = tkinter.Tk()
screen.title("Myapp")
screen.geometry("400x500")
screen.config(background="lightblue")

# lbl1 = tkinter.Label(text="Firstname:").pack()
# lbl2 = tkinter.Label(text="Lastname:").pack()

# lbl1 = tkinter.Label(text="Firstname:").place(x=0, y=0)
# lbl2 = tkinter.Label(text="Lastname:").place(x=0, y=30)

lbl1 = tkinter.Label(
    text="Firstname:", bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=0, column=0, sticky="w")
lbl2 = tkinter.Label(
    text="Lastname:", bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=1, column=0, sticky="w")


txt1 = tkinter.Entry(fg="red", font="Corbel 15 bold")
txt1.grid(row=0, column=1, sticky="w")
txt2 = tkinter.Entry(fg="red", font="Corbel 15 bold")
txt2.grid(row=1, column=1, sticky="w")

male = tkinter.Radiobutton(
    text="Male", value=0, bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=2, column=0, sticky="w")
female = tkinter.Radiobutton(
    text="Female", value=1, bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=2, column=1, sticky="w")


ch1 = tkinter.Checkbutton(
    text="Gujarati", bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=3, column=0, sticky="w")
ch2 = tkinter.Checkbutton(
    text="Hindi", bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=4, column=0, sticky="w")
ch3 = tkinter.Checkbutton(
    text="English", bg="lightblue", fg="red", font="Corbel 15 bold"
).grid(row=5, column=0, sticky="w")


city = ["Select City", "Rajkot", "Ahmedabad", "Baroda", "Surat", "Morbi", "Jamnagar"]
ttk.Combobox(values=city).grid(row=6, column=0, sticky="w")


def btnclick():
    # print("Button clicked!")
    # messagebox.showerror("Error!", "Something went wrong...")
    # messagebox.showinfo("Success", "Signup Successfully!")
    # messagebox.showwarning("Warning", "YOur disk is full!")
    print("Firstname:", txt1.get())
    print("Lastname:", txt2.get())


tkinter.Button(text="Submit", fg="red", font="Corbel 15 bold", command=btnclick).place(
    x=170, y=250
)

screen.mainloop()
