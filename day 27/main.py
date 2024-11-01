import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=50,height=30)
window.config(padx=20,pady=20)

def Milestokm():
    miles = miles_input.get()
    km = float(miles)*1.689
    kilo_output.config(text=km)

miles_input = tkinter.Entry()
miles_input.grid(column = 1,row = 0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column = 2,row = 0)

is_equal_to = tkinter.Label(text="is equal to ")
is_equal_to.grid(column = 0,row=1)

kilo_output = tkinter.Label(text="0")
kilo_output.grid(column = 1,row = 1)

kilo_label = tkinter.Label(text="Km")
kilo_label.grid(column = 2,row = 1)

calculate_button = tkinter.Button(text="Calculate",command=Milestokm)
calculate_button.grid(column = 1,row = 2)

window.mainloop()