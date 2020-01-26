from tkinter import *
from tkinter import ttk
from BMI_Class import BMI_Class
from tkinter import messagebox

def SubmitClicked():
    weightNum =  float(weight_box.get())
    heightNum = float(height_box.get())
    messagebox.showinfo('BMI CHART', "Your BMI was successfully calculated")
    BMI_Chart.add_BMI(weightNum, heightNum)

window = Tk()
window.title("BMI Chart")
window.geometry("500x500")

BMI_Chart = BMI_Class()


weight_label = Label(window, text='Enter your Weight(LBS): ')
weight_label.grid(column=0, row=0)
weight_box = Entry(window, width = 10)
weight_box.grid(column = 1, row = 0)


height_label = Label(window, text='Enter your Height(IN): ')
height_label.grid(column=0, row=1)
height_box = Entry(window, width = 10)
height_box.grid(column = 1, row = 1)


submit_button = Button(window, text = "Submit", command = SubmitClicked)
submit_button.grid(column = 0, row = 5)



window.mainloop()