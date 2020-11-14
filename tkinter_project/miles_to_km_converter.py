from tkinter import *

window = Tk()

# Fundtions
def click_button():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text='{}'.format(km))

# Labels
miles_input = Entry(width=7)
miles_label = Label(text='Miles')
is_equal_label = Label(text='is equal to')
km_result_label = Label(text='0')
km_label = Label(text='Km')

#Button
calculate_button = Button(text='Convert', command=click_button)

# Positioning
miles_input.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
is_equal_label.grid(row=1, column=0)
km_result_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)



window.mainloop()