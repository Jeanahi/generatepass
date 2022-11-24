from tkinter import *
import random 

def generatePass():
    new_label=Label(root,text="hello").pack()


root = Tk()

root.title("Generador de Password")

root.geometry("500x500")

root.resizable(0,0)


my_button=Button(root, text="Generar",font="arial 15 bold ",command=generatePass).pack() 
my_label=Label(root,text="").pack()
exit_button=Button(root, text="Salir", font="arial 15 bold",command=root.destroy).pack()



root.mainloop()