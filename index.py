from tkinter import * 
import tkinter.font as Font
from PIL import ImageTk, Image
import game_page_mod as gamep
import admin_login as ad

window=Tk()
window.title('Login Page')
window.iconbitmap('images/login.ico')
window.geometry('1200x800')

#putting the background image
bground = ImageTk.PhotoImage(file='images/bg2.png')

#creating a canvas
canvas1 = Canvas(window, width=1920, height=1080)
canvas1.pack(fill='both', expand=True)
canvas1.create_image(0,0, image=bground, anchor='nw')
canvas1.create_text(960, 175, text='The Price\nis Right!!!', font=('Shockwave', 100), fill='#33ffa3')

#resizing window
def resize(w):
    global bg_2, new_bg, background_img
    bg_2 = Image.open('images/bg2.png')
    new_bg=bg_2.resize((w.width, w.height), Image.ANTIALIAS)
    background_img = ImageTk.PhotoImage(new_bg)
    canvas1.create_image(0,0, image=background_img, anchor='nw')

#destroy window
def new_window():
    btn4.after(2000, window.destroy())
    gamep.game_page()

def destroy_window():
    btn3.after(2000, window.destroy())

def start_admin_page():
    btn5.after(2000, window.destroy())
    ad.admin_login()

btn3=Button(window, text='Exit', command=destroy_window, width=10, font=('Dobkin Script', 28))
btn4=Button(window, text='Start', command=new_window, width=10, font=('Dobkin Script', 28))
btn5=Button(window, text='Admin Mode', command=start_admin_page, width=10, font=('Dobkin Script', 28))

btn4_window = canvas1.create_window(850, 520, anchor='nw', window=btn4)#placing of buttons
btn3_window = canvas1.create_window(850, 610, anchor='nw', window=btn3)#placing of buttons
btn3_window = canvas1.create_window(850, 700, anchor='nw', window=btn5)#placing of buttons 

#End
window.mainloop()