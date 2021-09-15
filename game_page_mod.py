from scores import open_scores
from tkinter import *
from tkinter import font 
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import messagebox
from pygame import mixer
from random import *
points = 0
c = 0


def game_page():
    #start
    root=Tk()
    root.title("Game Area")
    root.iconbitmap('images/icon.ico')
    root.geometry('1200x800')

    #root.resizable(width=False, height=False)

    f = Font(family='Shockwave', size=75)
    f2 = Font(family='Montserrat Medium', size=20)


    #canvas and image
    bg = ImageTk.PhotoImage(file='images/game_wall.png')

    can1 = Canvas(root, width=1920, height=1080, highlightthickness = 0)
    can1.pack(fill='both', expand=True)

    can1.create_image(0,0, image=bg, anchor='nw')


    #the game
    l1 = []

    img1 = Image.open('images/game photos/alexa.png')
    resized_image1 = img1.resize((960, 540), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(resized_image1)

    img2 = Image.open('images/game photos/apple watch.png')
    resized_image2 = img2.resize((960, 540), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(resized_image2)

    img3 = Image.open('images/game photos/banana.png')
    resized_image3 = img3.resize((960, 540), Image.ANTIALIAS)
    new_image3 = ImageTk.PhotoImage(resized_image3)

    img4 = Image.open('images/game photos/bike.png')
    resized_image4 = img4.resize((960, 540), Image.ANTIALIAS)
    new_image4 = ImageTk.PhotoImage(resized_image4)

    img5 = Image.open('images/game photos/btc.png')
    resized_image5 = img5.resize((960, 540), Image.ANTIALIAS)
    new_image5 = ImageTk.PhotoImage(resized_image5)

    img6 = Image.open('images/game photos/buggati.png')
    resized_image6 = img6.resize((960, 540), Image.ANTIALIAS)
    new_image6 = ImageTk.PhotoImage(resized_image6)

    img7 = Image.open('images/game photos/charger.png')
    resized_image7 = img7.resize((960, 540), Image.ANTIALIAS)
    new_image7 = ImageTk.PhotoImage(resized_image7)

    img8 = Image.open('images/game photos/diamond.png')
    resized_image8 = img8.resize((960, 540), Image.ANTIALIAS)
    new_image8 = ImageTk.PhotoImage(resized_image8)

    img9 = Image.open('images/game photos/eth.png')
    resized_image9 = img9.resize((960, 540), Image.ANTIALIAS)
    new_image9 = ImageTk.PhotoImage(resized_image9)

    img10 = Image.open('images/game photos/ferrari.png')
    resized_image10 = img10.resize((960, 540), Image.ANTIALIAS)
    new_image10 = ImageTk.PhotoImage(resized_image10)

    img11 = Image.open('images/game photos/gaming pc.png')
    resized_image11 = img11.resize((960, 540), Image.ANTIALIAS)
    new_image11 = ImageTk.PhotoImage(resized_image11)

    img12 = Image.open('images/game photos/google home.png')
    resized_image12 = img12.resize((960, 540), Image.ANTIALIAS)
    new_image12 = ImageTk.PhotoImage(resized_image12)

    img13 = Image.open('images/game photos/jeep.png')
    resized_image13 = img13.resize((960, 540), Image.ANTIALIAS)
    new_image13 = ImageTk.PhotoImage(resized_image13)

    img14 = Image.open('images/game photos/lambo.png')
    resized_image14 = img14.resize((960, 540), Image.ANTIALIAS)
    new_image14 = ImageTk.PhotoImage(resized_image14)

    img15 = Image.open('images/game photos/mansion.png')
    resized_image15 = img15.resize((960, 540), Image.ANTIALIAS)
    new_image15 = ImageTk.PhotoImage(resized_image15)

    img16 = Image.open('images/game photos/powerbank.png')
    resized_image16 = img16.resize((960, 540), Image.ANTIALIAS)
    new_image16 = ImageTk.PhotoImage(resized_image16)

    img17 = Image.open('images/game photos/ps5.png')
    resized_image17 = img17.resize((960, 540), Image.ANTIALIAS)
    new_image17 = ImageTk.PhotoImage(resized_image17)

    img18 = Image.open('images/game photos/rtx 3090.png')
    resized_image18 = img18.resize((960, 540), Image.ANTIALIAS)
    new_image18 = ImageTk.PhotoImage(resized_image18)

    img19 = Image.open('images/game photos/switch.png')
    resized_image19 = img19.resize((960, 540), Image.ANTIALIAS)
    new_image19 = ImageTk.PhotoImage(resized_image19)

    img20 = Image.open('images/game photos/tv.png')
    resized_image20 = img20.resize((960, 540), Image.ANTIALIAS)
    new_image20 = ImageTk.PhotoImage(resized_image20)

    img21 = Image.open('images/game photos/vr.png')
    resized_image21 = img21.resize((960, 540), Image.ANTIALIAS)
    new_image21 = ImageTk.PhotoImage(resized_image21)

    img22 = Image.open('images/game photos/webcam.png')
    resized_image22 = img22.resize((960, 540), Image.ANTIALIAS)
    new_image22 = ImageTk.PhotoImage(resized_image22)

    img23 = Image.open('images/game photos/xbox.png')
    resized_image23 = img23.resize((960, 540), Image.ANTIALIAS)
    new_image23 = ImageTk.PhotoImage(resized_image23)

    global count, image_list, image_name_list, image_price_list

    image_name_list = ['Alexa', 'Apple Watch', 'Banana', 'Bike', 'Bitcoin', 'Buggati',
    'iPhone Charger', 'Diamond', 'Ethereum', 'Ferrari', 'Gaming PC', 'Google Home',
    'Jeep', 'Lambo', 'Mansion', 'Powerbank', 'PS5', 'RTX 3090',
    'Nintendo Switch', 'TV', 'VR', 'Webcam', 'Xbox']

    image_list = [new_image1, new_image2, new_image3, new_image4, new_image5, new_image6,
    new_image7, new_image8, new_image9, new_image10, new_image11, new_image12, new_image13, new_image14,
    new_image15, new_image16, new_image17, new_image18, new_image19, new_image20, new_image21, new_image22, new_image23]

    image_price_list = ['30', '400', '5', '45000', '1900000', '200', '4000000', '2000', '350000', '800', '50', '500000',
    '100000', '4000000', '100', '999', '1899', '400', '250', '150', '45', '700', '456']

    count = -1
    points_display = can1.create_text(70, 20, text = 'Points: 0', font = ('Montserrat', 18), fill = 'white')

    def images():
        global guess

        #price box
        guess = Entry(root, font=('montserrat-medium',20), width=35, fg='#336d92', bd=3)
        guess_win = can1.create_window(610,790, anchor='nw', window=guess)
        can1.create_image(450, 210, image = image_list[0], anchor ='nw')
        can1.create_text(960, 700, text= image_name_list[0], font=('Montserrat-Medium', 40), fill='#fcec03')

        def next():
            global guess, count
            if count == 23:
                can1.create_image(450, 210, image = image_list[0], anchor ='nw')
                can1.create_text(960, 700, text= image_name_list[0], font=('Montserrat-Medium', 40), fill='#fcec03')
                messagebox.showinfo("Completed", "Your points: "+str(points))
                root.after(5000, open_scores())

            else:
                can1.create_image(450, 210, image = image_list[count+1], anchor ='nw')
                can1.create_text(960, 700, text= image_name_list[count+1], font=('Montserrat-Medium', 40), fill='#fcec03')
                count += 1

            root.after(10000, next)
        next()
    images()

    def answer():
        global points, c

        if c == 0:
            if guess.get() == image_price_list[0]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct0')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct0')
            elif guess.get() != image_price_list[0]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[0], font = f2, fill = '#ff0000', tags = 'wrong0')
                root.after(2500, can1.delete, 'wrong0')
                c += 1
        elif c == 1:
            if guess.get() == image_price_list[1]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct1')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct1')
            elif guess.get() != image_price_list[1]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[1], font = f2, fill = '#ff0000', tags = 'wrong1')
                c += 1
                root.after(2500, can1.delete, 'wrong1')
        elif c == 2:
            if guess.get() == image_price_list[2]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct2')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct2')
            elif guess.get() != image_price_list[2]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[2], font = f2, fill = '#ff0000', tags = 'wrong2')
                c += 1
                root.after(2500, can1.delete, 'wrong2')
        elif c == 3:
            if guess.get() == image_price_list[3]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct3')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct3')
            elif guess.get() != image_price_list[3]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[3], font = f2, fill = '#ff0000', tags = 'wrong3')
                c += 1
                root.after(2500, can1.delete, 'wrong3')
        elif c == 4:
            if guess.get() == image_price_list[4]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct4')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct4')
            elif guess.get() != image_price_list[4]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[4], font = f2, fill = '#ff0000', tags = 'wrong4')
                c += 1
                root.after(2500, can1.delete, 'wrong4')
        elif c == 5:
            if guess.get() == image_price_list[5]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct5')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct5')
            elif guess.get() != image_price_list[5]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[5], font = f2, fill = '#ff0000', tags = 'wrong5')
                c += 1
                root.after(2500, can1.delete, 'wrong5')
        elif c == 6:
            if guess.get() == image_price_list[6]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct6')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct6')
            elif guess.get() != image_price_list[6]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[6], font = f2, fill = '#ff0000', tags = 'wrong6')
                c += 1
                root.after(2500, can1.delete, 'wrong6')
        elif c == 7:
            if guess.get() == image_price_list[7]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct7')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct7')
            elif guess.get() != image_price_list[7]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[7], font = f2, fill = '#ff0000', tags = 'wrong7')
                c += 1
                root.after(2500, can1.delete, 'wrong7')
        elif c == 8:
            if guess.get() == image_price_list[8]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct8')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct8')
            elif guess.get() != image_price_list[8]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[8], font = f2, fill = '#ff0000', tags = 'correct8')
                c += 1
                root.after(2500, can1.delete, 'wrong8')
        elif c == 9:
            if guess.get() == image_price_list[9]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct9')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct9')
            elif guess.get() != image_price_list[9]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[9], font = f2, fill = '#ff0000', tags = 'wrong9')
                c += 1
                root.after(2500, can1.delete, 'wrong9')
        elif c == 10:
            if guess.get() == image_price_list[10]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct10')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct10')
            elif guess.get() != image_price_list[10]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[10], font = f2, fill = '#ff0000', tags = 'wrong10')
                c += 1
                root.after(2500, can1.delete, 'wrong10')
        elif c == 11:
            if guess.get() == image_price_list[11]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct11')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct11')
            elif guess.get() != image_price_list[11]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[11], font = f2, fill = '#ff0000', tags = 'wrong11')
                c += 1
                root.after(2500, can1.delete, 'wrong11')
        elif c == 12:
            if guess.get() == image_price_list[12]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct12')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct12')
            elif guess.get() != image_price_list[12]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[12], font = f2, fill = '#ff0000', tags = 'wrong12')
                c += 1
                root.after(2500, can1.delete, 'wrong12')
        elif c == 13:
            if guess.get() == image_price_list[13]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct13')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct13')
            elif guess.get() != image_price_list[13]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[13], font = f2, fill = '#ff0000', tags = 'wrong13')
                c += 1
                root.after(2500, can1.delete, 'wrong13')
        elif c == 14:
            if guess.get() == image_price_list[14]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct14')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct14')
            elif guess.get() != image_price_list[14]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[14], font = f2, fill = '#ff0000', tags = 'wrong14')
                c += 1
                root.after(2500, can1.delete, 'wrong14')
        elif c == 15:
            if guess.get() == image_price_list[15]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct15')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct15')
            elif guess.get() != image_price_list[15]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[15], font = f2, fill = '#ff0000', tags = 'wrong15')
                c += 1
                root.after(2500, can1.delete, 'wrong15')
        elif c == 16:
            if guess.get() == image_price_list[16]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct16')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct16')
            elif guess.get() != image_price_list[16]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[16], font = f2, fill = '#ff0000', tags = 'wrong16')
                c += 1
                root.after(2500, can1.delete, 'wrong16')
        elif c == 17:
            if guess.get() == image_price_list[17]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct17')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct17')
            elif guess.get() != image_price_list[17]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[17], font = f2, fill = '#ff0000', tags = 'wrong17')
                c += 1
                root.after(2500, can1.delete, 'wrong17')
        elif c == 18:
            if guess.get() == image_price_list[18]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct18')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct18')
            elif guess.get() != image_price_list[18]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[18], font = f2, fill = '#ff0000', tags = 'wrong18')
                c += 1
                root.after(2500, can1.delete, 'wrong18')
        elif c == 19:
            if guess.get() == image_price_list[19]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct19')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct19')
            elif guess.get() != image_price_list[19]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[19], font = f2, fill = '#ff0000', tags = 'wrong19')
                c += 1
                root.after(2500, can1.delete, 'wrong19')
        elif c == 20:
            if guess.get() == image_price_list[20]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct20')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct20')
            elif guess.get() != image_price_list[20]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[20], font = f2, fill = '#ff0000', tags = 'wrong20')
                c += 1
                root.after(2500, can1.delete, 'wrong20')
        elif c == 21:
            if guess.get() == image_price_list[21]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct21')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct21')
            elif guess.get() != image_price_list[21]:
                can1.create_text(960, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[21], font = f2, fill = '#ff0000', tags = 'wrong21')
                c += 1
                root.after(2500, can1.delete, 'wrong21')
        elif c == 22:
            if guess.get() == image_price_list[22]:
                can1.create_text(960, 770, text = 'Correct✔️', font = f2, fill = '#22ad10', tags = 'correct22')
                points += 1
                c += 1
                can1.itemconfig(points_display, text = 'Points: '+str(points))
                root.after(2500, can1.delete, 'correct22')
            elif guess.get() != image_price_list[22]:
                can1.create_text(930, 770, text = 'Wrong❌ '+'Correct: '+image_price_list[22], font = f2, fill = '#ff0000', tags = 'wrong22')
                c += 1
                root.after(2500, can1.delete, 'wrong22')

        guess.delete(0, END)
    btn1=Button(root, text='Submit', command=answer, width=10, font=('Dobkin Script', 22))

    #leaderboard
    import scores as sc

    def leader_board():
        global points

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
                insertion = "insert into leaderboard (participant, points, age, dob, class, section) values (%s, %s, %s, %s, %s, %s)"
                values = (name_entry.get(), points, age_entry.get(), dob_entry.get(), class_entry.get(), section_entry.get())
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

    def detail_window_opens():
        btn2.after(7000, root.destroy())
        leader_board()
    btn2=Button(root, text='End', width=10, font=('Dobkin Script', 22), command=detail_window_opens)

    #def image_delete():
        #btn1.configure(itm_img.destroy())

    def destroy_game():
        btn_destroy.after(2000, root.destroy())

    btn_destroy=Button(root, text='Exit', command=destroy_game, width=10, font=('Dobkin Script', 22))
    btn_destroy_window = can1.create_window(1050, 850, anchor='nw', window=btn_destroy)
    btn1_window = can1.create_window(650, 850, anchor='nw', window=btn1)#placing of buttons
    btn2_window = can1.create_window(850, 850, anchor='nw', window=btn2)#placing of buttons


    #resize the window
    def resize(w):
        global bg1, resized, new_bg
        bg1 = Image.open('images/game_wall.png')
        resized=bg1.resize((w.width, w.height), Image.ANTIALIAS)
        new_bg = ImageTk.PhotoImage(resized)
        can1.create_text(960, 80, text='You got this!!!👍', font=f, fill='#29ff34')


    root.bind('<Configure>', resize)

    #music in background
    mixer.init()
    mixer.music.load("audio/alert.mp3")
    mixer.music.play(50)

    def play():
        mixer.music.unpause()
        play1=Button(root,text='Play',command=play,state=DISABLED, font=('Dobkin Script', 15))
        can1.create_window(1825, 4, anchor='nw', window=play1)#placing of buttons 
        stop1=Button(root,text='Stop',command=stop, font=('Dobkin Script', 15))
        can1.create_window(1875, 4, anchor='nw', window=stop1)#placing of buttons
    def stop():
        mixer.music.pause()
        play1=Button(root,text='Play',command=play, font=('Dobkin Script', 15))
        can1.create_window(1825, 4, anchor='nw', window=play1)#placing of buttons 
        stop1=Button(root,text='Stop',command=stop,state=DISABLED, font=('Dobkin Script', 15))
        can1.create_window(1875, 4, anchor='nw', window=stop1)#placing of buttons

    play1=Button(root,text='Play',command=play,state=DISABLED, font=('Dobkin Script', 15))
    can1.create_window(1825, 4, anchor='nw', window=play1)#placing of buttons 
    stop1=Button(root,text='Stop',command=stop, font=('Dobkin Script', 15))
    can1.create_window(1875, 4, anchor='nw', window=stop1)#placing of buttons

    def sound(x):
        mixer.music.set_volume(vol.get())

    vol=Scale(root,from_=1,to=0, orient='vertical', command=sound , resolution='0.05', font=(8))
    can1.create_window(1845, 55, anchor='nw', window=vol) 

    #End
    root.mainloop()