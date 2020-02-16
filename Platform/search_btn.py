from tkinter import *
import math
import fire

def search():
        def search_data():
                txt.delete('end')
                veg_check = dft_val1.get()
                dishes = fire.getVacancies(veg_check)
                if (dishes==[]):
                        dishes="\nNo Vacancies/Buses in this route\n\n"
                txt.insert(0.0,dishes)


        def quit_tk():
                root.destroy()
                from intro import mainfile
                mainfile()

        root = Tk()
        root.geometry ("800x600")

        background_image = PhotoImage(file=("images/hack3.gif"))
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        canvas = Canvas(root, bg = 'white', height=100, width=70) 

        title_line = Label(canvas, text = "Search")
        
        true_false_veg = ["Red","Green", "Blue", "Brown"]

        dft_val1 = StringVar(root)
        dft_val1.set(true_false_veg[0])
        line4 = Label(canvas, text = "Select Campus Loop")
        entry4 = OptionMenu(canvas, dft_val1, *true_false_veg)
        
        title_line.grid(row=50, column=1, columnspan=2)
        line4.grid (row=52, column=1)
        entry4.grid (row=52, column=2)

        #quitbtn = Button(root, image="exitbtn.png", command=root.quit).grid(row=4, column=0)

            
        btn = Button(canvas, text="Search", bg ="green", fg="black", command= search_data).grid(row=54, column=2)
        btn2 = Button(canvas, text="Quit", bg ="green", fg="black", command= quit_tk).grid(row=55, column=2)    
        txt = Text(canvas, width=70, height=10, wrap=WORD)
        txt.grid(row=55, column=1, columnspan=2, sticky=W)

        canvas.place(x=200, y=200, anchor=NW)
        root.mainloop()

