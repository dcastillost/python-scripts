import tkinter

#Functions
def click_button():
    print('Clicked!')
    my_label.config(text='Updated label')
    print(input.get())

#Create window
window = tkinter.Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)

#Label 
my_label = tkinter.Label(text='A label', font=('Arial', 24, 'bold'))
my_label.pack()

#Button
button = tkinter.Button(text='Click me', command = click_button)
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()

window.mainloop()