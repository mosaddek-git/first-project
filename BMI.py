import tkinter as tk

def calculate():
    weight= float(entry_weight.get())
    height= float(entry_height.get())
    height=height/100
    bmi =weight/(height**2)
    bmi_result.config(text="Your BMI : {:.2f}".format(bmi))



window =tk.Tk()
window.title("BMI CALCULATOR")
window.geometry("350x400")
window.resizable(0,0)
window.configure(bg='#333333')


#create the label
label_weight=tk.Label(window, text="Weight(Kg):",font=("Rockwell",15, "bold"))
label_weight.pack(pady=10)

entry_weight=tk.Entry(window,font=("Rockwell",15))
entry_weight.pack()

label_height=tk.Label(window, text="Height:",font=("Rockwell",15, "bold"))
label_height.pack(pady=15)

entry_height=tk.Entry(window,font=("Rockwell",15))
entry_height.pack()

#create a frame for calculate button
frame=tk.Frame(window)
frame.pack(pady=30)

calculate_button=tk.Button(frame,text="Calculate",font=("Rockwell",15, "bold"), command=calculate)
calculate_button.grid(row=0, column=0)

clear_button=tk.Button(frame,text="Clear",font=("Rockwell",15, "bold"))
clear_button.grid(row=0,column=1)

#create label for result
bmi_result=tk.Label(window,text="",font=("Rockwell",15))
bmi_result.pack()

status=tk.Label(window, text="", font=("Rockwell",15))
status.pack()



window.mainloop()