import lotteri
from tkinter import *
from tkinter import messagebox

#skapar objekt av klassen lotteri
lotter = lotteri.lotteri()

root = Tk()
#sätter titel på fönster
root.title("Lotteri")
root.geometry("380x300")

#skapar labels
label_antal = Label(root, text="Antal Lotter: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

#skapar textfält
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

# updateralistbox function
def update_list_box(antal_lotter):
    #tömmer listbox
    listbox.delete(0, END)
    #lägger till nya vinster
    listbox.insert(1, "Grattis du vann detta: ")

    try:
        #typomvandlar
        int_antal_lotter = int(antal_lotter)

        i=0
    
        if(int_antal_lotter <= 5):

            while i<int_antal_lotter:
                vinst = lotter.get_vinst()
                listbox.insert((i+2), vinst)
                i = i+1

        else:
            messagebox.showinfo("Max 3 lotter!")
    except:
        messagebox.showinfo("Endast siffror tillåtet!")




def clickSlumpaButton():
    antal_lott = textbox_antal.get()
    #tömmer textbox
    textbox_antal.delete(0, END)
    update_list_box(antal_lott)

button_slumpa = Button(text="Tur Knapp!", command=clickSlumpaButton)
button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=13)



#skapar listbox
listbox = Listbox(root, height=4, width=30, bg="blue", activestyle="dotbox", font="Helvetica", fg="red")
listbox.grid(row=2, column=0, columnspan=2, padx=14, pady=15)

 
root.mainloop()