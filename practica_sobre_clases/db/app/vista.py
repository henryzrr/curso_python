from tkinter import *
ventana = Tk()
ventana.title("GESTION DE EMPLEADOS")
ventana.geometry('400x400')
titulo = Label(ventana,text="GESTION DE EMPLEADOS",font=("Arial Bold",20))
titulo.grid(column=0,row=0)
btn = Button(ventana,text="Mostrar trabajadores")
btn.grid(column=0,row=1)
ventana.mainloop()
