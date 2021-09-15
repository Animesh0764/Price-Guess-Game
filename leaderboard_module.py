from tkinter import * 
import tkinter.font as Font
from PIL import ImageTk, Image
import scores as sc

def leader_board():

    leadb=Tk()
    leadb.title('Details')
    leadb.iconbitmap('images/profile.ico')

    bg_img = PhotoImage(file='images/lb_mod.png')
    #creating a canvas
    canva = Canvas(leadb, width=960, height=540)
    canva.pack(fill='both', expand=True)
    canva.create_image(0,0, image=bg_img, anchor='nw')

    import mysql.connector as mycon
    con=mycon.connect(host="localhost", user='root', passwd='ashu$123', database='project')
    cur=con.cursor()
    if con.is_connected():
        
        f=('Montserrat-Medium', 25)

        #create labels for participant
        canva.create_text(305, 113, text="Enter your name", font=f, fill='white')
        canva.create_text(305, 163, text="Enter your age", font=f, fill='white')
        canva.create_text(269, 213, text="Enter your date of birth", font=f, fill='white')
        canva.create_text(305, 263, text="Enter your class", font=f, fill='white')
        canva.create_text(305, 313, text="Enter your section", font=f, fill='white')

        def clear_entry_box():
            name_entry.delete(0, END)
            age_entry.delete(0, END)
            dob_entry.delete(0, END)
            class_entry.delete(0, END)
            section_entry.delete(0, END)

        #command for submission
        def submission():
            insertion = "insert into leaderboard (participant, age, dob, class, section) values (%s, %s, %s, %s, %s)"
            values = (name_entry.get(), age_entry.get(), dob_entry.get(), class_entry.get(), section_entry.get())
            cur.execute(insertion, values)
            con.commit()

            clear_entry_box()

        #create entry for users
        name_entry = Entry(leadb, font=('montserrat-medium',20))
        
        age_entry = Entry(leadb, font=('montserrat-medium',20))
        
        dob_entry = Entry(leadb, font=('montserrat-medium',20))
    
        class_entry = Entry(leadb, font=('montserrat-medium',20))

        section_entry = Entry(leadb, font=('montserrat-medium',20))
        
        def submitted_scores():
            leadb.destroy()
            sc.open_scores()

        #BUTTON creation
        submit_entries = Button(leadb, text='Submit the entries', width=17, font=('Dobkin Script', 20), fg='#ff0f63', command=submission)
        scores = Button(leadb, text='See the scores', width=17, font=('Dobkin Script', 20), fg='#ff0f63', command=submitted_scores)
        

        canva.create_window(520, 100, anchor='nw', window=name_entry)
        canva.create_window(520, 150, anchor='nw', window=age_entry)
        canva.create_window(520, 200, anchor='nw', window=dob_entry)
        canva.create_window(520, 250, anchor='nw', window=class_entry)
        canva.create_window(520, 300, anchor='nw', window=section_entry)
        canva.create_window(346, 405, anchor='nw', window=submit_entries)
        canva.create_window(346, 465, anchor='nw', window=scores)

    leadb.geometry('960x540')
    leadb.mainloop()



if __name__ == '__main__':
    leader_board()
    print('function name is:', __name__)