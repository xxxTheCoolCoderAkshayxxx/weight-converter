from tkinter import *
import tkinter.font as f
root = Tk()
root.title("weight converter")
root.geometry("350x250")
root.config(background="white")

def conversion():
    ounces=ouncesBox.get()
    if(ounces.replace('.','',1).isdigit()):
        errorMessage.grid_forget()
        pounds = (float(ounces)/16)
        answerLabel.config(text="weight in pounds: "+str(pounds))
    else:
        errorMessage.grid(row=1,column=1)

head = Label(root,text="Ounces -> Pounds",font=f.Font(size=20),fg="black")
head.pack()

#creating frame
frame=Frame(root)
frame.pack(pady=20)

label1 = Label(frame,text="Enter the weight in ounces: ",font=f.Font(size=10),fg="blue")
label1.grid(row=0,column=0)

ouncesBox = Entry(frame)
ouncesBox.grid(row=0,column=1)

errorMessage = Label(frame,text="Please enter the valid input",font=f.Font(size=8),fg="black")

answerLabel = Label(frame,font=f.Font(size=12))
answerLabel.grid(row=2,column=0,columnspan=2,pady=10)

convert = Button(frame,text="Convert",width=30,fg="black",bg="white",bd=0,padx=20,pady=10,command=conversion)
convert.grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()

