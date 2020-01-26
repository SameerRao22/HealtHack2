from tkinter import *
from tkinter import ttk
from BMI_Class import BMI_Class
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

window = Tk()
window.title("BMI Chart")
window.geometry("500x500")

BMI_Chart = BMI_Class()

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

canvas = FigureCanvasTkAgg(f, window)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas._tkcanvas.pack()

window.mainloop()