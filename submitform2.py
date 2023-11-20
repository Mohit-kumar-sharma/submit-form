from tkinter import *
root=Tk()

root.geometry("600x300")
Label(root,text="Welcome to Hindustan Travel",font="comlcsanses 13 bold",pady=15).grid(row=0,column=3)
def famous():
    print("welcome to Hindustan travel")
    print(f"{Namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()}")
    with open("record.txt","a") as f:
        f.write(f"{Namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()}\n")
Name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency number")
paymentmode = Label(root, text="Paymentmode")

Name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

Namevalue= StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=Namevalue)
phoenentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyvalueentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

nameentry.grid(row=1,column=3)
phoenentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyvalueentry.grid(row=4,column=3)
paymentmodeentry.grid (row=5,column=3)

#foodservice=Checkbutton("text=want to prebook your ticket",variable=foodservicevalue)
#foodservice.gr
# id(row=6,column=3)

Button=Button(root,text="submit",command=famous)
Button.grid(row=6,column=3)

root.mainloop()