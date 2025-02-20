from statistics import variance
from tkinter import *

def save():
    global title_test
    title_test.set('Save!')

def on_check():
    pos = 0
    for e in food_fields:
        if food_var[pos].get() == 1:
            food_fields[pos].config(state='normal')
        pos +=1



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


################################################

food_list = ['Pollo', 'Carne', 'Pescado', 'Pizza']
food_var = []
food_fields = []
food_texts = []

c = 0
for f in food_list:
    food_var.append('')
    food_var[c] = IntVar() #creates an int variable
    cb = Checkbutton(food_panel, text=f.title(), font=('Dosis', 19), onvalue=1, offvalue=0, variable=food_var[c], command=on_check) #variable=food_var[c] => bind the checkbox to a variable
    cb.grid(row=c, column=0, sticky=W)

    #Food fields
    food_fields.append('')
    food_texts.append('')
    food_texts[c]= StringVar()
    food_texts[c].set('0')

    food_fields[c] = Entry(food_panel, font=('Dosis', 19), bd=1, width=6, state=DISABLED, textvariable=food_texts[c])
    food_fields[c].grid(row=c, column=1)
    c += 1


###############################################


food_text_var = ''
food_cost = Label(costs_panel, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
food_cost.grid(row=2, column=0)

title_test = StringVar()
title_test.set('Shi')
title_test = Entry(costs_panel,  font=('Dosis', 12, 'bold'), bg='azure4', fg='white', textvariable=title_test)
title_test.grid(row=3, column=0)


food_cost_text = Entry(costs_panel, font=('Dosis', 19), bd=1, width=6, state='readonly', textvariable=food_text_var)
food_cost_text.grid(row=0, column=1)

###############################################
b = Button(buttons_panel, text='Guardar', fg='white',font=('Dosis', 19), bd=1, width=9)
b.grid(row=0,column=0)
b.config(command=lambda: save)


app.mainloop()