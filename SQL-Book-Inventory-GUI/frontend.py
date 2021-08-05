"""
A program that stores this book information:
1) Title
2) Author
3) Year
4) ISBN


User can: view all records, search, add entries, update entries, delete entries, and close the program
"""

from tkinter import *
import backend as back
import tkinter.messagebox
from tkinter.messagebox import askyesno

#### Front End View All ####
def view():
    lst1.delete(0,'end')
    for list in back.view_all():
        lst1.insert(END,list)


#### Front End Search Entry ####
def search():
    if (len(e1.get()) or len(e2.get()) or len(e3.get()) or len(e4.get())) >= 1:
        Title =  e1.get()
        Author = e2.get()
        Year = e3.get()
        ISBN = e4.get()
        lst1.delete(0,'end')
        for list in back.search(Title=Title,Author=Author,Year=Year,ISBN=ISBN):
            lst1.insert(END,list)
    else:
        return tkinter.messagebox.showinfo("Error",  "Please fill in one of the textboxes!")

### Front End Update Entry
def update():
    Title =  e1.get()
    Author = e2.get()
    Year = e3.get()
    ISBN = e4.get()
    if (len(Title)== 0 or len(Author)==0 or len(Year)==0 or len(ISBN)==0):
        return tkinter.messagebox.showinfo("Error",  "Please select an entry!")
    else: 
        id = index
        back.update(id=id,Title=Title,Author=Author,Year=Year,ISBN=ISBN)
        lst1.delete(0,'end')
        for list in back.view_all():
            lst1.insert(END,list)

    

#### Front End Add New Entry ####
def add():
    if (len(e1.get()) or len(e2.get()) or len(e3.get()) or len(e4.get())) == 0:
        return tkinter.messagebox.showinfo("Error",  "Please fill in all textboxes!")
    else:
        title = e1.get()
        author = e2.get()
        year = int(e3.get())
        isbn = int(e4.get())
        back.add_entry(title,author,year,isbn)
        lst1.delete(0,'end')
        for list in back.view_all():
            lst1.insert(END,list)
    
#### Front End Delete Entry ####
def delete():
    # Get Selected Item #
    value = lst1.get(lst1.curselection())
    print(value)
    # Ask for confirmation #
    confirmation = askyesno(title='Confirmation', message= "Are you sure you want to delete this item?")
    # Delete the Item
    if confirmation == TRUE:
        back.delete(id=value[0])
        lst1.delete(0,'end')
        for list in back.view_all():
            lst1.insert(END,list)
    else:
        return 

#### Update Textbox with highlighted entry in the listbox ####
def listboxitem(event):
    value = lst1.get(lst1.curselection())
    e1.delete(0,"end")
    e1.insert(END,value[1])
    e2.delete(0,"end")
    e2.insert(END,value[2])
    e3.delete(0,"end")
    e3.insert(END,value[3])
    e4.delete(0,"end")
    e4.insert(END,value[4])
    global index 
    index = value[0]


window = Tk() # Everything must go between this line and "window.mainloop()." Creates an empty tkinter window

#### Labels for 'Title', 'Author', 'Year', and 'ISBN' ####

# Title
l1 = Label(window, text = "Title")
l1.grid(row=0, column=0)

# Author
l2 = Label(window, text = "Author")
l2.grid(row=0, column=2)

# Year
l3 = Label(window, text = "Year")
l3.grid(row=1, column=0)

# ISBN

l4 = Label(window, text = "ISBN")
l4.grid(row=1, column=2)

#### Entry/Textboxes ####

title_value = StringVar() # Creating/Declaring the data type
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0,column=1)

author_value = StringVar()
e2 = Entry(window, textvariable=author_value)
e2.grid(row=0,column=3)

year_value = StringVar()
e3 = Entry(window, textvariable=year_value)
e3.grid(row=1,column=1)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1,column=3)


#### Buttons ####

b1 = Button(window, text = "View All", command = view)
b1.grid(row=3, column=3)

b2 = Button(window, text = "Search Entry", command = search)
b2.grid(row=4, column=3)

b3 = Button(window, text = "Add entry", command= add)
b3.grid(row=5, column=3)

b4 = Button(window, text = "Update", command=update)
b4.grid(row=6, column=3)

b5 = Button(window, text = "Delete", command = delete)
b5.grid(row=7, column=3)

b6 = Button(window, text = "Close", command= window.destroy)
b6.grid(row=8, column=3)


#### Listbox ####

lst1 = Listbox(window, height =10, width =21)
lst1.grid(row=3, column=1, rowspan=6, columnspan=3, pady=10, sticky='W')

# Populating the listbox
for list in back.view_all():
    lst1.insert(END,list)

# Adding text to textboxes from listbox
lst1.bind('<<ListboxSelect>>',listboxitem)

#### Scroll Bar ####
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

lst1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lst1.yview)

window.mainloop() # Everything must go between this line and "window = tk()". This makes sure to keep the main window open

#print(value)
#print(view())