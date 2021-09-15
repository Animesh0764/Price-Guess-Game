from tkinter import *
from tkinter import font 
from tkinter.font import Font
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk

def admin_page():
    #start
    root = Tk()
    root.title("Admin Page")
    root.iconbitmap('images/admin icon.ico')
    root.geometry('1200x800')

    #canvas and graphics
    bg = ImageTk.PhotoImage(file='images/admin.png')

    admin_canvas = Canvas(root, width=1920, height=1080)
    admin_canvas.pack(fill='both', expand=True)

    admin_canvas.create_image(0,0, image=bg, anchor='nw')

    #resizing the window
    def resize(w):
        global bg1, resized, new_bg
        bg1 = Image.open('images/admin.png')
        resized=bg1.resize((w.width, w.height), Image.ANTIALIAS)
        new_bg = ImageTk.PhotoImage(resized)
        admin_canvas.create_image(0,0, image=new_bg, anchor='nw')
        #admin_canvas.create_text(960, 80, text='You got this!!!👍', font=f, fill='white')


    root.bind('<Configure>', resize)

    #importing mysql
    import mysql.connector as mycon
    con = mycon.connect(host="localhost", user='root', passwd='ashu$123', database='project')
    cur = con.cursor()

    def delete_window():
        #start
        root = Tk()
        root.title("Delete Page")
        root.iconbitmap('images/admin icon.ico')
        root.geometry('1200x800')

        #canvas and graphics
        bg = ImageTk.PhotoImage(file='images/admin.png')

        delete_canvas = Canvas(root, width=1920, height=1080)
        delete_canvas.pack(fill='both', expand=True)

        delete_canvas.create_image(0,0, image=bg, anchor='nw')

        import mysql.connector as mycon
        con = mycon.connect(host="localhost", user='root', passwd='ashu$123', database='project')
        cur = con.cursor()

        #adding treeview
        tree = ttk.Treeview(root)
        tree['show'] = 'headings'

        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure('Treeview',
        font = ('Montserrat', 12),
        background = '#7d7972',
        foreground = '#e6e6e6',
        rowheight = 25,
        fieldbackground = '#7d7972')

        style.configure('Treeview.Heading', font = ('Blockletter', 12))

        style.map('Treeview', background = [('selected','#34d13e')])

        cur.execute("select * from leaderboard order by Sno")
        tree['columns'] = ('Sno', 'Participant', 'Points', 'Age', 'DOB', 'Class', 'Section')
        tree.column('Sno', width=50, minwidth = 50, anchor='c')
        tree.column('Participant', width=150, minwidth = 150, anchor='c')
        tree.column('Points', width=150, minwidth = 150, anchor='c')
        tree.column('Age', width=150, minwidth = 150, anchor='c')
        tree.column('DOB', width=150, minwidth = 150, anchor='c')
        tree.column('Class', width=150, minwidth = 150, anchor='c')
        tree.column('Section', width=150, minwidth = 150, anchor='c')

        tree.heading('Sno', text='Sno', anchor='c')
        tree.heading('Participant', text='Participant', anchor='c')
        tree.heading('Points', text='Points', anchor='c')
        tree.heading('Age', text='Age', anchor='c')
        tree.heading('DOB', text='DOB', anchor='c')
        tree.heading('Class', text='Class', anchor='c')
        tree.heading('Section', text='Section', anchor='c')

        i = 0
        for row in cur:
            tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1

        tree_win = delete_canvas.create_window(450, 300, anchor='nw', window = tree)

        #resizing the window
        def resize(w):
            global bg1, resized, new_bg
            bg1 = Image.open('images/admin.png')
            resized=bg1.resize((w.width, w.height), Image.ANTIALIAS)
            new_bg = ImageTk.PhotoImage(resized)
            delete_canvas.create_image(0,0, image=new_bg, anchor='nw')
            #admin_canvas.create_text(960, 80, text='You got this!!!👍', font=f, fill='white')


        root.bind('<Configure>', resize)
        #deletion of a record
        def delete_record():
            cur.execute("select Sno from leaderboard")
            data = cur.fetchall()
            flag = False
            for entry in data:
                if rec.get() in entry:
                    flag == True
                    break
            if flag == False:
                messagebox.showerror('Error', "No such record found!!")
            elif flag == True:
                cur.execute("DELETE FROM leaderboard WHERE Sno = "+rec.get())

                rec.delete(0, END)

                con.commit()

        def backtoadmin():
            backtoadmin_btn.after(2000, root.destroy())
            admin_page()

        #create text box for searching record
        rec = Entry(root, font=('montserrat-medium',20), width=35, fg='#336d92', bd=3)
        rec_win = delete_canvas.create_window(600, 600, anchor='nw', window = rec)
        rec.insert(0, 'Enter value')

        #create delete button
        del_btn = Button(root, text='Delete', width=10, font = ('Dobkin Script', 15), command = delete_record)
        del_btn_window = delete_canvas.create_window(750, 700, anchor='nw', window=del_btn)#placing of buttons
        backtoadmin_btn = Button(root, text='Back to Admin', font = ('Dobkin Script', 15), width=10, command = backtoadmin)
        backtoadmin_btn_window = delete_canvas.create_window(950, 700, anchor='nw', window=backtoadmin_btn)#placing of buttons
        #end
        root.mainloop()

    def update_window():
        #start
        root = Tk()
        root.title("Update Page")
        root.iconbitmap('images/admin icon.ico')
        root.geometry('1200x800')

        #canvas and graphics
        bg = ImageTk.PhotoImage(file='images/admin.png')

        update_canvas = Canvas(root, width=1920, height=1080)
        update_canvas.pack(fill='both', expand=True)

        tree = ttk.Treeview(root)
        tree['show'] = 'headings'

        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure('Treeview',
        font = ('Montserrat', 12),
        background = '#7d7972',
        foreground = '#e6e6e6',
        rowheight = 25,
        fieldbackground = '#7d7972')

        style.configure('Treeview.Heading', font = ('Blockletter', 12))

        style.map('Treeview', background = [('selected','#34d13e')])

        cur.execute("select * from leaderboard")
        tree['columns'] = ('Sno', 'Participant', 'Points', 'Age', 'DOB', 'Class', 'Section')
        tree.column('Sno', width=50, minwidth = 50, anchor='c')
        tree.column('Participant', width=150, minwidth = 150, anchor='c')
        tree.column('Points', width=150, minwidth = 150, anchor='c')
        tree.column('Age', width=150, minwidth = 150, anchor='c')
        tree.column('DOB', width=150, minwidth = 150, anchor='c')
        tree.column('Class', width=150, minwidth = 150, anchor='c')
        tree.column('Section', width=150, minwidth = 150, anchor='c')

        tree.heading('Sno', text='Sno', anchor='c')
        tree.heading('Participant', text='Participant', anchor='c')
        tree.heading('Points', text='Points', anchor='c')
        tree.heading('Age', text='Age', anchor='c')
        tree.heading('DOB', text='DOB', anchor='c')
        tree.heading('Class', text='Class', anchor='c')
        tree.heading('Section', text='Section', anchor='c')

        i = 0
        for row in cur:
            tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1

        tree_win = update_canvas.create_window(450, 300, anchor='nw', window = tree)

        update_canvas.create_image(0,0, image=bg, anchor='nw')

        #defining the entry boxes
        e0 = Entry(root, width=25, font = ('Montserrat Medium', 10))
        e0_win = update_canvas.create_window(60000, 60000, anchor='nw', window = e0)
        e1 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e1_win = update_canvas.create_window(530, 600, anchor='nw', window = e1)
        e2 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e2_win = update_canvas.create_window(800, 600, anchor='nw', window = e2)
        e3 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e3_win = update_canvas.create_window(1070, 600, anchor='nw', window = e3)
        e4 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e4_win = update_canvas.create_window(530, 650, anchor='nw', window = e4)
        e5 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e5_win = update_canvas.create_window(800, 650, anchor='nw', window = e5)
        e6 = Entry(root, width=20, font = ('Montserrat Medium', 15))
        e6_win = update_canvas.create_window(1070, 650, anchor='nw', window = e6)

        def select_rec():
            global values
            #importing mysql
            import mysql.connector as mycon
            con = mycon.connect(host="localhost", user='root', passwd='ashu$123', database='project')
            cur = con.cursor()

            e0.delete(0, END)
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)

            selected = tree.focus()
            values = tree.item(selected, 'values')

            e0.insert(0, values[0])
            e1.insert(0, values[1])
            e2.insert(0, values[2])
            e3.insert(0, values[3])
            e4.insert(0, values[4])
            e5.insert(0, values[5])
            e6.insert(0, values[6])

        def update_record():

            cur.execute(("""UPDATE leaderboard
            SET Participant=%s, Points=%s, Age=%s, DOB=%s, Class=%s, Section=%s
            WHERE Sno=%s"""),(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), values[0]))

            con.commit()

            selected = tree.focus()
            tree.item(selected, text='', values=(e0.get(), e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))

            e0.delete(0, END)
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)

        #resizing the window
        def resize(w):
            global bg1, resized, new_bg
            bg1 = Image.open('images/admin.png')
            resized=bg1.resize((w.width, w.height), Image.ANTIALIAS)
            new_bg = ImageTk.PhotoImage(resized)
            update_canvas.create_image(0,0, image=new_bg, anchor='nw')
            #update_canvas.create_text(960, 80, text='You got this!!!👍', font=f, fill='white')


        root.bind('<Configure>', resize)

        def backtoadmin():
            backtoadmin_btn.after(2000, root.destroy())
            admin_page()

        backtoadmin_btn = Button(root, text='Back to Admin', font = ('Dobkin Script', 18), width=10, command = backtoadmin)
        backtoadmin_btn_window = update_canvas.create_window(1050, 700, anchor='nw', window=backtoadmin_btn)#placing of buttons
        select_btn = Button(root, text='Select', width=10, font = ('Dobkin Script', 18), command = select_rec)
        select_btn_window = update_canvas.create_window(650, 700, anchor='nw', window=select_btn)#placing of buttons
        update_btn = Button(root, text='Update', width=10, font = ('Dobkin Script', 18), command = update_record)
        update_btn_window = update_canvas.create_window(850, 700, anchor='nw', window=update_btn)#placing of buttons
        #end
        root.mainloop()


    admin_canvas.create_text(100, 100, text = 'Welcome to the admin mode!!', font=('Shockwave', 80), fill = 'white')
    admin_canvas.create_text(100, 120, text = 'Where would you like to proceed', font=('Shockwave', 80), fill = 'white')

    def new_win_del():
        btn1.after(2000, root.destroy())
        delete_window()

    def new_update_del():
        btn2.after(2000, root.destroy())
        update_window()

    btn1=Button(root, text='Delete Records', command=new_win_del, width=15, font=('Montserrat', 28))
    btn2=Button(root, text='Update Records', command=new_update_del, width=15, font=('Montserrat', 28))

    btn1_window = admin_canvas.create_window(650, 750, anchor='nw', window=btn1)#placing of buttons
    btn2_window = admin_canvas.create_window(1060, 750, anchor='nw', window=btn2)#placing of buttons

    #end
    root.mainloop()

if __name__ == '__main__':
    admin_page()
    print('function name is:', __name__)