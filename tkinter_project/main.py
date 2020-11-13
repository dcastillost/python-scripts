import tkinter

#Create window
window = tkinter.Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)

#Label 
my_label = tkinter.Label(text='A label', font=('Arial', 24, 'bold'))
my_label.pack()


window.mainloop()