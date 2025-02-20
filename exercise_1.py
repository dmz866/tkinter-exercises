from tkinter import *


app = Tk()
app.geometry('1020x630+0+0') #+0+0 defines start x and y position
app.resizable(0,0) #not resizable
app.title('My Title')
app.config(bg='burlywood')

#upper panel
upper_panel = Frame(app, bd=1, relief='flat') #bd border
upper_panel.pack(side=TOP)

title = Label(upper_panel, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 58), bg='burlywood')
title.grid(row=0, column=0)

#left panel
left_panel = Frame(app, bd=1, relief='flat')
left_panel.pack(side=LEFT)

#food panel
food_panel = LabelFrame(left_panel, text="Comida", bd=1, relief='flat', font=('Dosis', 19))
food_panel.pack(side=LEFT)

#beverages panel
beverages_panel = LabelFrame(left_panel, text="Bebidas", bd=1, relief='flat', font=('Dosis', 19))
beverages_panel.pack(side=LEFT)

#desserts panel
desserts_panel = LabelFrame(left_panel, text="Postres", bd=1, relief='flat', font=('Dosis', 19))
desserts_panel.pack(side=LEFT)

#costs panel
costs_panel = Frame(left_panel, bd=1, relief='flat')
costs_panel.pack(side=BOTTOM)


################################################

#right panel
right_panel = Frame(app, bd=1, relief='flat')
right_panel.pack(side=RIGHT)

#calculator panel
calculator_panel = Frame(right_panel, bd=1, relief='flat', bg='burlywood')
calculator_panel.pack()

#bill panel
bill_panel = Frame(right_panel, bd=1, relief='flat', bg='burlywood')
bill_panel.pack()

#buttons panel
buttons_panel = Frame(right_panel, bd=1, relief='flat', bg='burlywood')
buttons_panel.pack()


app.mainloop()