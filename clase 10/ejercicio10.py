import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="hola", bg="yellow",fg="blue")
label_saludo.pack(ipadx=50, ipady=50, expand=True) 
window.mainloop()