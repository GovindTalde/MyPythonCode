from tkinter import*
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("database")


conn = sqlite3.connect("address_book.db")

# create cursor
c = conn.cursor()

def update():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE adresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
                  })





    conn.commit()
    conn.close()



    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title("update record")


    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_box.get()
    
    c.execute("SELECT * FROM adresses WHERE oid = " + record_id)
    records = c.fetchall()

    
    #create global variables for
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

        

    
    #create a text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

   

    #create text box labels
    f_name_label = Label(editor, text = "first name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text = "last name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text = "address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text = "city")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text = "email id")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text =  "password")
    zipcode_label.grid(row=5, column=0)

    

    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    

    # create a save button
    save_btn = Button(editor, text="save record", command=update)
    save_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    

def delete():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    #delete a record
    c.execute("DELETE from adresses WHERE oid= " + delete_box.get())


    
    conn.commit()
    conn.close()


# create function for sbmit button
def submit():
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()

    #inserrt into table
    c.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
                })

    conn.commit()

    conn.close()


    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def querry():
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM adresses")
    records = c.fetchall()
    print(records)


    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
        
    querry_label = Label(root, text=print_records)
    querry_label.grid(row=12, column=0, columnspan=2)
    conn.commit()

    conn.close()


#create a text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)


#create text box labels
f_name_label = Label(root, text = "first name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text = "last name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text = "address")
address_label.grid(row=2, column=0)

city_label = Label(root, text = "city")
city_label.grid(row=3, column=0)

state_label = Label(root, text = "email id")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text =  "password")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text = "ID NO")
delete_box_label.grid(row=8, column=0)

# create submit buttons
submit_btn = Button(root, text="submit record", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# create a cuerry btn
querry_btn = Button(root, text="show button", command=querry)
querry_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# CRAETE A DELETE BUTTON
delete_btn = Button(root, text="delete", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# edit button
edit_btn = Button(root, text="edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()

conn.close()

root.mainloop()

