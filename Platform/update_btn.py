from tkinter import *
import pandas
from update_fn import data_update
from database_importing import dict_create


def main():
    di = dict_create()
    def update_data():
        txt.delete('end')
        can = str(entry1.get())
        cus = str(entry2.get())
        stall = str(entry3.get())
        dish = str(entry4.get())
        price = str(entry5.get())
        veg = str(entry6.get())
        hal = str(entry7.get())
        ope = str(entry8.get())
        clo = str(entry9.get())
        tra = str(entry10.get())
        rat = str(entry11.get())
        di_type = str(entry12.get())
        benchmark = True
    

        
        if veg.strip().upper() != "TRUE" and veg.strip().upper() != "FALSE":
            txt.insert(0.0, "\n Please enter a valid entry for Vegetarian")
            benchmark = False
        if hal.strip().upper() != "TRUE" and hal.strip().upper() != "FALSE":
            txt.insert(0.0, " \n Please enter a valid entry for Halal")
            benchmark = False
        if can.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Canteen")
            benchmark = False
        if cus.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Cuisine")
            benchmark = False
        if stall.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Stall")
            benchmark = False
        if dish.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Dish")
            benchmark = False
        try:
            price_int = int(price)
        except ValueError:
            txt.insert(0.0, "\n Please enter a valid Integral Price for rating between 1 and 5")
            benchmark = False    
        if ope.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Opening time")
            benchmark = False
        if clo.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for Closing Time")
            benchmark = False

        if tra.strip().upper() != "LOW" and tra.strip().upper() != "MEDIUM" and tra.strip().upper() != "HIGH":
            txt.insert(0.0, "\n Please enter a valid entry for Traffic - Low, Medium, High")
            benchmark = False
        try:
            rat_int = int(rat.strip())
            if rat_int<1 or rat_int>5:
                txt.insert(0.0, "\n Please enter a valid entry for rating between 1 and 5")
                benchmark = False
        except ValueError:
            txt.insert(0.0, "\n Please enter a valid integral rating for rating between 1 and 5")
            benchmark = False
        if di_type.strip() == "":
            txt.insert(0.0, "\n Please enter a valid entry for dish type")
            benchmark = False

        if benchmark == True:
            di[len(di)] = {"Canteen": can.upper(), "Cuisine": cus.upper(), "Stall": stall.upper(),
                           "Dish" : dish.upper(), "Price": price_int, "Vegetarian": veg.upper(),
                           "Halal": hal.upper(), "Opening time": ope, "Closing time":clo,
                           "Traffic": tra.upper(), "Rating": rat_int, "Dish type": di_type.upper() }
            rest = data_update(di)
            txt.insert(0.0, rest)
    def quit_tk():
        root.destroy()
        from intro import mainfile
        mainfile()
    root = Tk()
    root.geometry ("900x700")

    background_image = PhotoImage(file = "images/Webp.net-resizeimage.png")
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas = Canvas(root, bg = 'white', height=100, width=70)

    title_line = Label(canvas, text = "Update a new value")
    line1 = Label(canvas, text = "Canteen")
    line2 = Label(canvas, text = "Cuisine type")
    line3 = Label(canvas, text = "Stall Name")
    line4 = Label(canvas, text = "Dish Name")
    line5 = Label(canvas, text = "Price")
    line6 = Label(canvas, text = "Vegetarian? 'True' or 'False'")
    line7 = Label(canvas, text = "Halal? 'True' or 'False'")
    line8 = Label(canvas, text = "Opening time:")
    line9 = Label(canvas, text = "Closing Time")
    line10 = Label(canvas, text = "Traffic at Peak Hours")
    line11 = Label(canvas, text = "Rating out of 5")
    line12 = Label(canvas, text = "Dish type")

    entry1 = Entry(canvas)
    entry2 = Entry(canvas)
    entry3 = Entry(canvas)
    entry4 = Entry(canvas)
    entry5 = Entry(canvas)
    entry6 = Entry(canvas)
    entry7 = Entry(canvas)
    entry8 = Entry(canvas)
    entry9 = Entry(canvas)
    entry10 = Entry(canvas)
    entry11 = Entry(canvas)
    entry12 = Entry(canvas)

    title_line.grid(row=1, column=1, columnspan=2)
    line1.grid (row=2, column=1)
    line2.grid (row=3, column=1)
    line3.grid (row=4, column=1)
    line4.grid (row=5, column=1)
    line5.grid (row=6, column=1)
    line6.grid (row=7, column=1)
    line7.grid (row=8, column=1)
    line8.grid (row=9, column=1)
    line9.grid (row=10, column=1)
    line10.grid (row=11, column=1)
    line11.grid (row=12, column=1)
    line12.grid (row=13, column=1)

    entry1.grid (row=2, column=2)
    entry2.grid (row=3, column=2)
    entry3.grid (row=4, column=2)
    entry4.grid (row=5, column=2)
    entry5.grid (row=6, column=2)
    entry6.grid (row=7, column=2)
    entry7.grid (row=8, column=2)
    entry8.grid (row=9, column=2)
    entry9.grid (row=10, column=2)
    entry10.grid (row=11, column=2)
    entry11.grid (row=12, column=2)
    entry12.grid (row=13, column=2)

    btn = Button(canvas, text="Search", bg ="green", fg="black", command=update_data).grid(row=14, column=2)
    btn2 = Button(canvas, text="Quit", bg ="green", fg="black", command= quit_tk).grid(row=15, column=2)    
   
    txt = Text(canvas, width=70, height=10, wrap=WORD)
    txt.grid(row=16, column=1, columnspan=2, sticky=W)

    canvas.place(x=200, y=150, anchor=NW)
    root.mainloop()


