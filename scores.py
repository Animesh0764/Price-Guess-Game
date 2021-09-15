from tkinter import *
import tkinter.font as Font
from PIL import ImageTk, Image

def open_scores():
    leaderboard = Tk()
    leaderboard.title('Leaderboard')
    leaderboard.iconbitmap('images/leader.ico')

    bg = ImageTk.PhotoImage(file='images/leader.png')

    leaderboard_canvas = Canvas(leaderboard , width=1920, height=1080)
    leaderboard_canvas.grid(row=0, column=0)
    leaderboard_canvas.create_image(0,0, image=bg, anchor='nw')
    leaderboard_canvas.create_text(960, 80, text='Leaderboard', font=('Blockletter', 75), fill='#ff3087')

    def resize(w):
        global bg_2, new_bg, background_img
        bg_2 = Image.open('images/leader.png')
        new_bg = bg_2.resize((w.width, w.height), Image.ANTIALIAS)
        background_img = ImageTk.PhotoImage(new_bg)
        leaderboard_canvas.create_image(0,0, image=background_img, anchor='nw')


    leaderboard_canvas.create_text(590, 271, text='S.no', font=('Montserrat-Medium', 45), fill='#000dff')
    leaderboard_canvas.create_text(970, 271, text='Participant', font=('Montserrat-Medium', 45), fill='#000dff')
    leaderboard_canvas.create_text(1350, 271, text='Points', font=('Montserrat-Medium', 45), fill='#000dff')

    import mysql.connector as mycon
    con = mycon.connect(host="localhost", user='root', passwd='ashu$123', database='project')
    cur = con.cursor()

    #displaying serial number
    cur.execute("select Sno from leaderboard")
    data = cur.fetchall()
    c=560
    r=300
    for row in data:
        leaderboard_canvas.create_text(c, r, text=row, font=('Montserrat-Medium', 35), fill='Black', anchor='nw')
        r+=60

    #displaying participant name
    cur.execute("select Participant from leaderboard")
    name = cur.fetchall()

    c2=960
    r2=360
    for part in name:
        leaderboard_canvas.create_text(c2, r2, text=part[0], font=('Montserrat-Medium', 35), fill='Black')
        r2+=60

    #displaying points
    cur.execute("select Points from leaderboard")
    name = cur.fetchall()

    c3=1360
    r3=360
    for part in name:
        leaderboard_canvas.create_text(c3, r3, text=part, font=('Montserrat-Medium', 35), fill='Black')
        r3+=60

    leaderboard.geometry('960x540')
    leaderboard.mainloop()


if __name__ == '__main__':
    open_scores()
    print('function name is:', __name__)