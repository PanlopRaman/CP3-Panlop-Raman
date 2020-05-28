from tkinter import *
import math
def LeftClick (event):
#labelResult.configure(text = float(textBoxW.get())/math.pow(float(textBoxH.get())/100,2))
    BMI = float(textBoxW.get())/math.pow(float(textBoxH.get())/100,2)
    print(BMI)
    if BMI > 30:
        labelResult.configure(text="อ้วนมาก")
        print(BMI)
    elif BMI >= 25.0:
        labelResult.configure(text="อ้วน")
    elif BMI >= 23.0:
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ")
    else:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
#Height
labelHeight = Label(MainWindow,text = "ส่วนสูง (Cm.)")
labelHeight.grid(row=0, column=0)
textBoxH = Entry(MainWindow)
textBoxH.grid(row=0, column=1)
#wWeight
labelWeight = Label(MainWindow, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxW = Entry(MainWindow)
textBoxW.grid(row=1, column=1)
#Cal
CalBotton = Button(MainWindow, text = "คำนวณค่า")
CalBotton.bind('<Button-1>', LeftClick)
CalBotton.grid(row=2, column= 0)
#Result
labelResult = Label(MainWindow, text= "BMI")
labelResult.grid(row=2, column= 1)
MainWindow.mainloop()
