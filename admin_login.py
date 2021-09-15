from tkinter import *
from tkinter import font 
from tkinter.font import Font
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import admin_mode as admin

def admin_login():
    #start
    root = Tk()
    root.title("Admin Page")
    root.iconbitmap('images/admin icon.ico')
    root.geometry('1200x800')

    #canvas and graphics
    bg = Image.open('images/login.png')
    resized_image = bg.resize((1200, 800), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    admin_can = Canvas(root, width=1920, height=1080)
    admin_can.pack(fill='both', expand=True)

    admin_can.create_image(0,0, image=new_image, anchor='nw')

    admin_can.create_line(460, 200, 460, 600, width = 10, fill = '#15ff00')

    user_entry = Entry(root, font=('montserrat-medium',15), width=20, fg='#336d92', bd = 2)
    user_entry_window = admin_can.create_window(710, 308, anchor='nw', window=user_entry)
    pass_entry = Entry(root, font=('montserrat-medium',15), width=20, fg='#336d92', show = '•', bd = 2)
    pass_entry_window = admin_can.create_window(710, 408, anchor='nw', window=pass_entry)

    admin_can.create_text(590, 320, text = 'Username: ', font=('Montserrat-Medium', 25), fill='#0004ff')
    admin_can.create_text(590, 320, text = 'Username: ', font=('Montserrat-Medium', 26), fill='white')
    admin_can.create_text(590, 420, text = 'Password: ', font=('Montserrat-Medium', 25), fill='#0004ff')
    admin_can.create_text(590, 420, text = 'Password: ', font=('Montserrat-Medium', 26), fill='white')

    def clear_fields():
        user_entry.delete(0, END)
        pass_entry.delete(0, END)

    def proceed():
        if user_entry.get() == 'admin' and pass_entry.get() == '12345':
            welcome = messagebox.showinfo("Correct", "Welcome boss!!")
            btn1.after(5000, root.destroy())
            admin.admin_page()
        else:
            caution = messagebox.showwarning("Error!!", "Wrong credentials. Try again")
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

    btn1 = Button(root, text='Login', width=15, font=('Dobkin Script', 17), command = proceed)
    btn1.configure(activebackground = "#33B5E5", relief = RAISED)
    btn2 = Button(root, text='Clear', width=15, font=('Dobkin Script', 17), command = clear_fields)
    btn2.configure(activebackground = "#33B5E5", relief = RAISED)

    btn1_window = admin_can.create_window(560, 500, anchor='nw', window=btn1)
    btn2_window = admin_can.create_window(780, 500, anchor='nw', window=btn2)


    root.mainloop()