from tkinter import *
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import messagebox

root = Tk()
root.geometry("1130x700")

city_value = StringVar()
place_var = StringVar()
var = IntVar()
var_1 = StringVar()
var_2 = IntVar()
spin_days = StringVar()
spin_month = StringVar()
spin_year = StringVar()
time_hour = StringVar()
time_minute = StringVar()
coach_1 = StringVar()
coach_2 = StringVar()
captain_1 = StringVar()
captain_2 = StringVar()
noplayers_1 = StringVar()
noplayers_2 = StringVar()
run_1 = IntVar()
run_2 = IntVar()
team1_var_play = StringVar()
team2_var_play = StringVar()
team1_var_play1 = StringVar()
team2_var_play2 = StringVar()
x = 1
y = 1
l = 1
m = 1
li_1 = []
li_1_sub = []
li_2 = []
li_2_sub = []
li = []
list_matchdetails = []
list_locationdetails = []
list_teamdetails = []
li_toss = []
a_team1 = StringVar()
b_team2 = StringVar()
ampm_var = StringVar()
over_no = IntVar()


def error():
    messagebox.showinfo("info", "PLEASE COMPLETE THE PREVIOUS STEPS FIRST")


def error_3():
    messagebox.showinfo("info", "NO INFORMATION IS FOUND TO SAVE")


def error_2():
    messagebox.showinfo("COMPLETED", "YOU HAVE ALREADY COMPLETED THIS STEP")


def destroy():
    messagebox.showinfo("COMPLETED",
                        "YOU HAVE SUCCESSFULLY COMPLETED ALL THE STEPS AND YOUR DETAILS ARE SAVED IN AN EXCEL SHEET")
    root.destroy()


def check():
    CharButton_1 = Button(root, text="LOCATION DETAILS", font=('TimesNewRoman 15 bold'), width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", command=location_details)
    CharButton_1.grid(row=6, column=2, columnspan=2)


def check_1():
    CharButton_2 = Button(root, text="TEAM DETAILS", font=('TimesNewRoman 15 bold'), width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", command=team_details)
    CharButton_2.grid(row=10, column=2, columnspan=2)


def check_2():
    CharButton_3 = Button(root, text="PLAYER NAMES", font=('TimesNewRoman 15 bold'), width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", command=enter_names)
    CharButton_3.grid(row=14, column=2, columnspan=2)


def callback(input):
    if input.isdigit():
        return False

    elif input == "":
        return False

    else:
        return True


def save_destroy():
    global frame_3
    global can_1
    global can_2
    global a
    global b
    global li
    message = messagebox.askquestion("CONFIRMATION", "ARE YOU SURE YOU WANT TO SUBMIT")
    if message == "yes":
        b = b_team2.get()
        a = a_team1.get()
        c = var.get()
        d = over_no.get()
        if int(spin_days.get()) in range(0, 9):
            day_1 = "0" + spin_days.get()
        else:
            day_1 = spin_days.get()
        if int(spin_month.get()) in range(0, 9):
            month_1 = "0" + spin_month.get()
        else:
            month_1 = spin_month.get()
        date = day_1 + " / " + month_1 + " / " + spin_year.get()

        if int(time_minute.get()) in range(0, 9):
            time = time_hour.get() + " : " + "0" + time_minute.get() + " " + ampm_var.get()
        else:
            time = time_hour.get() + " : " + time_minute.get() + " " + ampm_var.get()

        if c == 0:
            messagebox.showerror("NO CHOICE MADE", "YOU FORGOT TO CHOOSE YOUR MATCH TYPE")
        elif d == 0:
            messagebox.showerror("NO CHOICE MADE", "YOU FORGOT TO CHOOSE TOTAL NUMBER OF OVERS")
        else:
            if c == 1:
                type_match = "ONE - DAY"
            elif c == 2:
                type_match = "T - 20"
            elif c == 3:
                type_match = "TEST MATCH"
            check_entry1 = callback(a)
            check_entry2 = callback(b)
            if check_entry1 == True:
                if check_entry2 == True:
                    if d != 0:
                        li.append(a)
                        li.append(b)

                        frame_3.grid_forget()
                        can_1.delete(can_text)
                        can_1.delete(can_arrow)
                        can_1.create_line(10, 35, 80, 35, arrow=LAST)
                        can_1.create_text(300, 35, text="YOU HAVE SUCCESSFULLY COMPLETED THIS STEP"
                                          , font=('Helvetica 13 bold'), fill="green")
                        img = Image.open("tick_2.png")
                        resizedImage = img.resize((30, 30), Image.ANTIALIAS)
                        CharPhoto = ImageTk.PhotoImage(image=resizedImage)
                        Can_tick = can_1.create_image(550, 35, image=CharPhoto)
                        can_1.image = CharPhoto

                        global can_arrow_2
                        global can_text_2
                        can_arrow_2 = can_2.create_line(10, 35, 100, 35, arrow=LAST)
                        can_text_2 = can_2.create_text(350, 35, text="CLICK ON THIS BUTTON TO FILL YOUR "
                                                                     "LOCATION DETAILS", font='Helvetica 13 bold')
                        list_matchdetails.append(type_match)
                        list_matchdetails.append(date)
                        list_matchdetails.append(time)
                        list_matchdetails.extend(li)
                        list_matchdetails.append(d)

                        entryButton_1 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                                               , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=error_3)
                        entryButton_1.grid(row=15, column=16, rowspan=3, columnspan=8)
                        CharButton = Button(root, text="MATCH DETAILS", font='TimesNewRoman 15 bold', width=20,
                                            pady=10, relief=RIDGE, borderwidth=5, command=error_2, bg="pink",
                                            fg="black")
                        CharButton.grid(row=2, column=2, columnspan=2)
                        check()
                    elif d == 0:
                        messagebox.showerror("ERROR", "YOU FORGOT TO SELECT TOTAL NUMBER OF OVERS ")
                else:
                    messagebox.showerror("WRONG TEAM NAME", "PLEASE ENTER A VALID TEAM NAME")
            else:
                messagebox.showerror("WRONG TEAM NAME", "PLEASE ENTER A VALID TEAM NAME")
    else:
        spin_days.set("1")
        spin_month.set("1")
        spin_year.set("2022")
        ampm_var.set("'please choose'")
        time_hour.set("0")
        time_minute.set("0")
        team_1_entry.delete(0, END)
        team_2_entry.delete(0, END)
        over_no.set(0)
        messagebox.showinfo("TRY AGAIN", "KINDLY REFILL YOUR DETAILS")


def match_details():
    global frame_3
    frame_3 = Frame(root, width=760, height=625)
    frame_3.grid(row=0, column=5, sticky=N, rowspan=20, columnspan=20)

    match_root = frame_3
    img = Image.open("shubhank_4.jfif")
    resizedImage = img.resize((760, 625), Image.ANTIALIAS)
    CharPhoto = ImageTk.PhotoImage(image=resizedImage)
    ChLabel = Label(frame_3, image=CharPhoto)
    ChLabel.img = CharPhoto
    ChLabel.grid(row=0, column=5, columnspan=20, rowspan=20, sticky=N)

    Label(match_root, text="MATCH DETAILS", padx=15, pady=15, bg="red", fg="WHITE", font='Algerian 20 bold', border=5,
          relief=RIDGE).grid(row=0, column=7, columnspan=15, rowspan=5, sticky=N)

    # RADIOBUTTONS : MATCH TYPE
    Label(match_root, text="MATCH TYPE", width=17, bg="ORANGE", fg="black", border=3,
          relief=RIDGE, font='Helvetica 15 bold').grid(row=3, column=5, columnspan=3, rowspan=2)
    Radiobutton(match_root, text="ONE - DAY", font='Helvetica 14 ', variable=var, value=1, fg="BLACK", bg="pink",
                relief=SUNKEN).grid(row=3, column=11, rowspan=2)
    Radiobutton(match_root, text="T-20", font='Helvetica 14 ', variable=var, value=2, fg="BLACK", bg="pink",
                relief=SUNKEN).grid(row=3, column=17, rowspan=2)
    Radiobutton(match_root, text="TEST CRICKET", font='Helvetica 14 ', variable=var, value=3, fg="BLACK", bg="pink",
                relief=SUNKEN).grid(row=3, column=22, rowspan=2)

    # DATE
    Label(match_root, text="DD", fg="BLACK", bg="pink", font='Helvetica 15 bold').grid(row=6, column=11, rowspan=2)
    Label(match_root, text="MM", fg="BLACK", bg="pink", font='Helvetica 15 bold').grid(row=6, column=17, rowspan=2)
    Label(match_root, text="YY", fg="BLACK", bg="pink", font='Helvetica 15 bold').grid(row=6, column=22, rowspan=2)
    Label(match_root, text="DATE OF MATCH", width=17, font='Helvetica 15 bold', bg="ORANGE"
          , fg="black", border=3, relief=RIDGE).grid(row=7, column=5, columnspan=3, rowspan=3)

    spin_days_1 = Spinbox(match_root, from_=1, to=31, font='Helvetica 10 ', textvariable=spin_days)
    spin_days_1.configure(width=5, font=1)
    spin_days_1.grid(row=7, column=11, rowspan=3)

    spin_month_1 = Spinbox(match_root, from_=1, to=12, font='Helvetica 10 ', textvariable=spin_month)
    spin_month_1.configure(width=5, font=1)
    spin_month_1.grid(row=7, column=17, rowspan=3)

    spin_year_1 = Spinbox(match_root, from_=2022, to=2300, font='Helvetica 10 ', textvariable=spin_year)
    spin_year_1.configure(width=5, font=1)
    spin_year_1.grid(row=7, column=22, rowspan=3)

    # TIME
    Label(match_root, text="TIME OF MATCH", bg="ORANGE", fg="black", width=17, border=3, relief=RIDGE
          , font=('Helvetica 15 bold')).grid(row=12, column=5, columnspan=3, rowspan=3)
    Label(match_root, text="HOURS", font='Helvetica 15 bold', fg="BLACK", bg="pink").grid(row=11, column=11, rowspan=2)
    Label(match_root, text="MINUTES", font='Helvetica 15 bold', fg="BLACK", bg="pink").grid(row=11, column=17,
                                                                                            rowspan=2)
    Label(match_root, text="AM / PM", font='Helvetica 15 bold', fg="BLACK", bg="pink").grid(row=11, column=22,
                                                                                            rowspan=2)
    time_hour_1 = Spinbox(match_root, from_=0, to=24, textvariable=time_hour)
    time_hour_1.configure(width=5, font=1)
    time_hour_1.grid(row=12, column=11, rowspan=3)
    time_minute_1 = Spinbox(match_root, from_=0, to=500, textvariable=time_minute)
    time_minute_1.configure(width=5, font=1)
    time_minute_1.grid(row=12, column=17, rowspan=3)

    li_ampm = ['AM', 'PM']
    drop_down_ampm = OptionMenu(match_root, ampm_var, *li_ampm)
    ampm_var.set("'Please Choose'")
    drop_down_ampm.config(width=13, font='Helvetica 10 bold')
    drop_down_ampm.grid(row=12, column=22, columnspan=2, rowspan=3)

    Label(match_root, text="NO. OF OVERS", bg="ORANGE", fg="black", width=17, border=3, relief=RIDGE
          , font='Helvetica 15 bold').grid(row=16, column=5, columnspan=3)

    over_1 = Spinbox(match_root, from_=0, to=60, textvariable=over_no)
    over_1.configure(width=10, font=1)
    over_1.grid(row=16, column=11)

    # TEAM DETAILS
    Label(match_root, text="NAME OF TEAMS", width=19, bg="ORANGE", fg="black", border=3, relief=RIDGE,
          font='Helvetica 15 bold').grid(row=18, column=5, columnspan=3)
    Label(match_root, text="TEAM I", fg="BLACK", font='Helvetica 14 bold', bg="pink").grid(row=18, column=11)
    Label(match_root, text="TEAM II", fg="BLACK", font='Helvetica 14 bold', bg="pink").grid(row=19, column=11)

    global team_1_entry
    team_1_entry = Entry(match_root, textvariable=a_team1)
    team_1_entry.configure(width=15, font='Helvetica 14 bold')
    team_1_entry.grid(row=18, column=14, columnspan=8)

    global team_2_entry
    team_2_entry = Entry(match_root, textvariable=b_team2)
    team_2_entry.configure(width=15, font='Helvetica 14 bold')
    team_2_entry.grid(row=19, column=14, columnspan=8)

    # BUTTONS
    entryButton_2 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                           , relief=RIDGE, borderwidth=5, command=save_destroy, bg="purple", fg="white")
    entryButton_2.grid(row=15, column=16, rowspan=3, columnspan=8)

    CharButton = Button(root, text="MATCH DETAILS", font='TimesNewRoman 15 bold', width=20,
                        pady=10, relief=RIDGE, borderwidth=5, bg="pink", fg="red")
    CharButton.grid(row=2, column=2, columnspan=2)


def location_1():
    global can_2
    global can_arrow_2
    global can_text_2
    global list_locationdetails
    global list_locationdetails_C
    global frame_4
    message_1 = messagebox.askquestion("CONFIRMATION", "ARE YOU SURE YOU WANT TO SUBMIT")
    if message_1 == "yes":
        if callback(value) == False:
            messagebox.showerror("WRONG VALUE ENTERED", "PLEASE ENTER A VALID ' CITY ' ENTRY")
        elif callback(value_1) == False:
            messagebox.showerror("WRONG VALUE ENTERED", "PLEASE ENTER A VALID ' VENUE ' ENTRY")
        else:
            list_locationdetails_C = list_locationdetails

            frame_4.grid_forget()

            can_2.delete(can_text_2)
            can_2.delete(can_arrow_2)
            can_arrow2 = can_2.create_line(10, 35, 80, 35, arrow=LAST)
            can_text2 = can_2.create_text(300, 35, text="YOU HAVE SUCCESSFULLY COMPLETED THIS STEP"
                                          , font='Helvetica 13 bold', fill="green")
            img_2 = Image.open("tick_2.png")
            resizedImage2 = img_2.resize((30, 30), Image.ANTIALIAS)
            CharPhoto2 = ImageTk.PhotoImage(image=resizedImage2)
            Can_tick2 = can_2.create_image(550, 35, image=CharPhoto2)
            can_2.image = CharPhoto2

            global can_arrow_3
            global can_text_3
            can_arrow_3 = can_3.create_line(10, 35, 100, 35, arrow=LAST)
            can_text_3 = can_3.create_text(350, 35, text="CLICK ON THIS BUTTON TO FILL YOUR TEAM DETAILS",
                                           font='Helvetica 13 bold')
            entryButton_1 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                                   , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=error_3)
            entryButton_1.grid(row=15, column=16, rowspan=3, columnspan=8)

            CharButton_1 = Button(root, text="LOCATION DETAILS", font='TimesNewRoman 15 bold', width=20, pady=10
                                  , relief=RIDGE, borderwidth=5, bg="pink", command=error_2)
            CharButton_1.grid(row=6, column=2, columnspan=2)

            check_1()

    else:
        global can_w
        global can_country
        global can_state
        global can_city
        global can_zipcode
        can_w.delete(can_country)
        can_w.delete(can_state)
        can_w.delete(can_city)
        can_w.delete(can_zipcode)

        global city_entry
        global place_entry
        city_entry.delete(0, END)
        place_entry.delete(0, END)
        list_locationdetails.clear()

        messagebox.showinfo("TRY AGAIN", "KINDLY REFILL YOUR DETAILS")


def full_location():
    global value
    global can_country
    global can_state
    global can_city
    global can_zipcode
    global value_1
    global list_locationdetails
    value = city_value.get()
    value_1 = place_var.get()

    check_value = callback(value)
    check_value_1 = callback(value_1)
    if check_value == True:
        if check_value_1 == True:
            try:
                geolocator = Nominatim(user_agent="MyApp")
                location = geolocator.geocode(value)
                s = location.latitude
                t = location.longitude

                x = str(s)
                y = str(t)

                location = geolocator.reverse(x + "," + y)
                address = location.raw['address']

                # traverse the data
                city = address.get('city', '')
                state = address.get('state', '')
                country = address.get('country', '')
                code = address.get('country_code')
                zipcode = address.get('postcode')

                if list(city) == []:
                    messagebox.showerror("NO CITY NAME FOUND", "VALUE ENTERED IS NOT A CITY, PLEASE TRY AGAIN.... ")
                    city_entry.delete(0, END)

                else:
                    can_country = can_w.create_text(270, 60, text=country.upper(), font='Helvetica 14 bold')
                    can_state = can_w.create_text(270, 120, text=state.upper(), font='Helvetica 14 bold')
                    can_city = can_w.create_text(270, 180, text=city.upper(), font='Helvetica 14 bold')
                    can_zipcode = can_w.create_text(270, 240, text=zipcode, font='Helvetica 14 bold')

                    entryButton_3 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                                           , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=location_1)
                    entryButton_3.grid(row=15, column=16, rowspan=3, columnspan=8)

                    list_locationdetails.append(value)
                    list_locationdetails.append(value_1)
                    list_locationdetails.append(country)
                    list_locationdetails.append(state)
                    list_locationdetails.append(city)
                    list_locationdetails.append(zipcode)
                    print(list_locationdetails)

            except AttributeError:
                messagebox.showerror("WRONG VALUE ENTERED", "PLEASE ENTER A VALID CITY NAME")
                city_entry.delete(0, END)

        else:
            messagebox.showerror("WRONG VALUE ENTERED", "PLEASE ENTER A VALID ' VENUE ' ENTRY")
    else:
        messagebox.showerror("WRONG VALUE ENTERED", "PLEASE ENTER A VALID ' CITY ' ENTRY")


def location_details():
    global frame_4
    frame_4 = Frame(root, width=760, height=625)
    frame_4.grid(row=0, column=5, sticky=N, rowspan=20, columnspan=20)

    location_root = frame_4

    img = Image.open("sarang.jpg")
    resizedImage = img.resize((760, 625), Image.ANTIALIAS)
    CharPhoto = ImageTk.PhotoImage(image=resizedImage)
    ChLabel = Label(frame_4, image=CharPhoto)
    ChLabel.img = CharPhoto
    ChLabel.grid(row=0, column=5, columnspan=20, rowspan=20, sticky=N)

    l1 = Label(location_root, text="LOCATION DETAILS", bg="BLUE", fg="WHITE", padx=15, pady=15, relief=RIDGE,
               font='Algerian 20 bold', border=4)
    l1.grid(row=0, column=7, columnspan=15, rowspan=5, sticky=N)

    # Label(location_root,text="").grid(row=1,column=12)
    Label(location_root, text="CITY", bg="LIGHT BLUE", fg="black", font='Helvetica 15 bold',
          padx=10, pady=10, relief=SUNKEN).grid(row=4, column=11, columnspan=3, rowspan=2)
    global city_entry
    city_entry = Entry(location_root, textvariable=city_value, font=1)
    city_entry.grid(row=4, column=17, rowspan=2)

    Label(location_root, text="VENUE", bg="LIGHT BLUE", fg="black", font='Helvetica 15 bold',
          padx=10, pady=10, relief=SUNKEN).grid(row=7, column=11, columnspan=3, rowspan=3)

    Button(location_root, text="ENTER LOCATION", bg="blue", fg="white", width=17, font='Times 13 bold', pady=5
           , command=full_location).grid(row=10, column=7, columnspan=15)
    global place_entry
    place_entry = Entry(location_root, textvariable=place_var, font=1)
    place_entry.grid(row=7, column=17, rowspan=3)
    global can_w
    can_w = Canvas(location_root, width=400, height=300, bg="white")
    cs_text = can_w.create_text(200, 20, text="* .............YOUR FULL LOCATION............. *",
                                font='Times 12 bold', fill="purple")
    can_w.create_text(128, 60, text="COUNTRY  :  ", font='Helvetica 14 bold')
    can_w.create_text(128, 120, text="STATE  :  ", font='Helvetica 14 bold')
    can_w.create_text(128, 180, text="CITY  :  ", font='Helvetica 14 bold')
    can_w.create_text(128, 240, text="CODE  :  ", font='Helvetica 14 bold')
    # can_w.configure(bg="pink")
    can_w.grid(row=12, column=7, columnspan=15, rowspan=7)

    entryButton_3 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                           , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=error_3)
    entryButton_3.grid(row=15, column=16, rowspan=3, columnspan=8)

    CharButton_1 = Button(root, text="LOCATION DETAILS", font='TimesNewRoman 15 bold', width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", fg="red")
    CharButton_1.grid(row=6, column=2, columnspan=2)


def entire():
    global li
    global li_toss
    global list_teamdetails
    global bat
    global bowl
    message_2 = messagebox.askquestion("CONFIRMATION", "ARE YOU SURE YOU WANT TO SUBMIT")
    if message_2 == "yes":
        coach_t1 = coach_1.get()
        coach_t2 = coach_2.get()
        captain_t1 = captain_1.get()
        captain_t2 = captain_2.get()
        if callback(coach_t1) == False:
            messagebox.showerror("WRONG INPUT", "PLEASE ENTER VALID COACH NAME")
            cap_1_entry_a.delete(0, END)
        elif callback(coach_t2) == False:
            messagebox.showerror("WRONG INPUT", "PLEASE ENTER VALID COACH NAME")
            cap_2_entry_b.delete(0, END)
        elif callback(captain_t1) == False:
            messagebox.showerror("WRONG INPUT", "PLEASE ENTER VALID CAPTAIN NAME")
            cap_1_entry.delete(0, END)
        elif callback(captain_t2) == False:
            messagebox.showerror("WRONG INPUT", "PLEASE ENTER VALID CAPTAIN NAME")
            cap_2_entry.delete(0, END)
        elif var_2.get() == 0:
            messagebox.showerror("NO CHOICE MADE", "YOU FORGOT TO ENTER THE CHOICE MADE BY TEAM WHICH WON THE TOSS")
        elif var_1.get() == "'SELECT'":
            messagebox.showerror("NO CHOICE MADE", "YOU FORGOT TO CHOOSE WHICH TEAM WON THE TOSS")
        else:
            list_teamdetails.append(coach_t1)
            list_teamdetails.append(coach_t2)
            list_teamdetails.append(captain_t1)
            list_teamdetails.append(captain_t2)
            print(list_teamdetails)

            if var_1.get() == li[0]:
                li_toss.append(var_1.get())
                if var_2.get() == 1:
                    bat = li[0]
                    bowl = li[1]
                    print(li[0], "CHOOSE TO BAT")
                    li_toss.append("BAT")
                else:
                    bat = li[1]
                    bowl = li[0]
                    print(li[0], "chose to ball")
                    li_toss.append("BOWL")
            elif var_1.get() == li[1]:
                li_toss.append(var_1.get())
                if var_2.get() == 1:
                    bat = li[1]
                    bowl = li[0]
                    print(li[1], "CHOOSE TO BAT")
                    li_toss.append("BAT")
                else:
                    bat = li[0]
                    bowl = li[1]
                    print(li[1], "chose to ball")
                    li_toss.append("BOWL")

            global frame_5
            frame_5.grid_forget()
            global can_3
            global can_arrow_3
            global can_text_3
            can_3.delete(can_text_3)
            can_3.delete(can_arrow_3)
            can_arrow3 = can_3.create_line(10, 35, 80, 35, arrow=LAST)
            can_text3 = can_3.create_text(300, 35, text="YOU HAVE SUCCESSFULLY COMPLETED THIS STEP"
                                          , font='Helvetica 13 bold', fill="green")
            img_3 = Image.open("tick_2.png")
            resizedImage3 = img_3.resize((30, 30), Image.ANTIALIAS)
            CharPhoto3 = ImageTk.PhotoImage(image=resizedImage3)
            Can_tick3 = can_3.create_image(550, 35, image=CharPhoto3)
            can_3.image = CharPhoto3

            global can_arrow_4
            global can_text_4
            can_arrow_4 = can_4.create_line(10, 35, 100, 35, arrow=LAST)
            can_text_4 = can_4.create_text(350, 35, text="CLICK ON THIS BUTTON TO FILL YOUR PLAYERS NAMES",
                                           font='Helvetica 13 bold')
            check_2()

            CharButton_2 = Button(root, text="TEAM DETAILS", font='TimesNewRoman 15 bold', width=20, pady=10
                                  , relief=RIDGE, borderwidth=5, bg="pink", command=error_2)
            CharButton_2.grid(row=10, column=2, columnspan=2)

            entryButton_1 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                                   , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=error_3)
            entryButton_1.grid(row=15, column=16, rowspan=3, columnspan=8)


    else:
        messagebox.showinfo("REFILL", "KINDLY FILL YOUR DETAILS AGAIN")
        cap_1_entry_a.delete(0, END)
        cap_2_entry_b.delete(0, END)
        cap_1_entry.delete(0, END)
        cap_2_entry.delete(0, END)
        var_1.set("'SELECT'")


def team_details():
    global frame_5
    global a
    global b
    global li
    frame_5 = Frame(root, width=760, height=625)
    frame_5.grid(row=0, column=5, sticky=N, rowspan=20, columnspan=20)

    team_root = frame_5

    img = Image.open("shubhank_4.jfif")
    resizedImage = img.resize((760, 625), Image.ANTIALIAS)
    # resizedImage_1 = img.resize((50,50), Image.ANTIALIAS)
    CharPhoto = ImageTk.PhotoImage(image=resizedImage)
    # Charphoto = ImageTk.PhotoImage(image=resizedImage_1)
    ChLabel = Label(frame_5, image=CharPhoto)
    ChLabel.img = CharPhoto
    ChLabel.grid(row=0, column=5, columnspan=20, rowspan=20, sticky=N)

    # TEAM DETAILS
    Label(team_root, text="TEAM DETAILS", padx=15, pady=15, bg="red", border=2, fg="black", relief=RIDGE,
          font='Algerian 20 bold').grid(row=0, column=7, columnspan=16, rowspan=5, sticky=N)

    name_can = Canvas(frame_5, width=285, height=50, bg="pink")
    name_can.create_text(142, 25, text=a, font='Helvetica 17 bold')
    name_can.configure(highlightthickness=0)
    name_can.grid(row=3, column=3, columnspan=11)

    name_can = Canvas(frame_5, width=285, height=50, bg="pink")
    name_can.create_text(142, 25, text=b, font='Helvetica 17 bold')
    name_can.configure(highlightthickness=0)
    name_can.grid(row=3, column=16, columnspan=8)

    Label(team_root, text="COACH NAME", fg="black", font='Helvetica 14 bold', bg="orange").grid(row=5, column=5,
                                                                                                rowspan=2, columnspan=5)
    Label(team_root, text="COACH NAME", fg="black", font='Helvetica 14 bold', bg="orange").grid(row=5, column=16,
                                                                                                rowspan=2,
                                                                                                columnspan=4)
    global cap_1_entry_a
    global cap_2_entry_b
    cap_1_entry_a = Entry(team_root, textvariable=coach_1, width=15, font='Times 13 ')
    cap_1_entry_a.grid(row=5, column=10, rowspan=2, columnspan=3)
    cap_2_entry_b = Entry(team_root, textvariable=coach_2, width=15, font='Times 13 ')
    cap_2_entry_b.grid(row=5, column=21, rowspan=2, columnspan=3)

    Label(team_root, text="CAPTAIN NAME", fg="black", bg="orange", font='Helvetica 14 bold').grid(row=7, column=5,
                                                                                                  rowspan=2,
                                                                                                  columnspan=5)
    Label(team_root, text="CAPTAIN NAME", fg="black", font='Helvetica 14 bold', bg="orange").grid(row=7, column=15,
                                                                                                  rowspan=2,
                                                                                                  columnspan=6)
    global cap_1_entry
    global cap_2_entry
    cap_1_entry = Entry(team_root, textvariable=captain_1, width=15, font='Times 13 ')
    cap_1_entry.grid(row=7, column=10, rowspan=2, columnspan=3)
    cap_2_entry = Entry(team_root, textvariable=captain_2, width=15, font='Times 13 ')
    cap_2_entry.grid(row=7, column=21, rowspan=2, columnspan=3)

    # TOSS WON BY WHICH TEAM
    Label(team_root, text="TOSS WON BY TEAM", padx=10, pady=10, bg="red", fg="white", font='Helvetica 15 bold',
          border=3, relief=SUNKEN).grid(row=11, column=7, rowspan=2, columnspan=7)
    toss_drop = OptionMenu(frame_5, var_1, *li)
    toss_drop.config(width=17, font='Helvetica 15 bold', bg="pink")
    var_1.set("'SELECT'")
    toss_drop.grid(row=11, column=13, columnspan=11, rowspan=2)

    # TEAM CHOSE TO
    Label(team_root, text="TEAM CHOSE TO", padx=10, pady=10, bg="red", fg="white", font='Helvetica 15 bold', border=3,
          relief=SUNKEN).grid(row=15, column=7, rowspan=2, columnspan=7)
    CHOICE_radio = Radiobutton(team_root, text="BAT", variable=var_2, value=1, font='Helvetica 14 ', bg="pink")
    CHOICE_radio.grid(row=15, column=13, columnspan=7, rowspan=2)
    CHOICE_radio_1 = Radiobutton(team_root, text="BOWL", variable=var_2, value=2, font='Helvetica 14 ', bg="pink")
    CHOICE_radio_1.grid(row=15, column=17, columnspan=7, rowspan=2)

    entryButton_5 = Button(root, width=12, pady=3, text="SAVE INFO", font='Helvetica 15 bold'
                           , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=entire)
    entryButton_5.grid(row=15, column=16, rowspan=3, columnspan=8)

    CharButton_2 = Button(root, text="TEAM DETAILS", font='TimesNewRoman 15 bold', width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", fg="red")
    CharButton_2.grid(row=10, column=2, columnspan=2)


def player_names():
    global li_1
    global li_2
    global li_1_sub
    global li_2_sub
    message_team = messagebox.askquestion("CONFIRMATION", "ARE YOU SURE YOU WANT TO SUBMIT")
    if message_team == "yes":
        global frame_7
        frame_7.grid_forget()

        global can_4
        global can_arrow_4
        global can_text_4
        can_4.delete(can_text_4)
        can_4.delete(can_arrow_4)
        can_arrow4 = can_4.create_line(10, 35, 80, 35, arrow=LAST)
        can_text4 = can_4.create_text(300, 35, text="YOU HAVE SUCCESSFULLY COMPLETED THIS STEP"
                                      , font=('Helvetica 13 bold'), fill="green")
        img_4 = Image.open("tick_2.png")
        resizedImage4 = img_4.resize((30, 30), Image.ANTIALIAS)
        CharPhoto4 = ImageTk.PhotoImage(image=resizedImage4)
        Can_tick4 = can_4.create_image(550, 35, image=CharPhoto4)
        can_4.image = CharPhoto4

        entryButton_4 = Button(root, width=12, pady=3, text="SUBMIT", font=('Helvetica 15 bold')
                               , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=destroy)
        entryButton_4.grid(row=15, column=16, rowspan=3, columnspan=8)

        CharButton_3 = Button(root, text="PLAYER NAMES", font=('TimesNewRoman 15 bold'), width=20, pady=10
                              , relief=RIDGE, borderwidth=5, bg="pink", fg="black", command=error_2)
        CharButton_3.grid(row=14, column=2, columnspan=2)
    else:
        messagebox.showinfo("TRY AGAIN", "KINDLY REFILL YOUR NAMES")
        li_1.clear()
        li_2.clear()
        li_1_sub.clear()
        li_2_sub.clear()


def team_1():
    global li_1
    global x
    global can_play
    global snno
    global team1_entry_play
    a_1 = team1_var_play.get()
    check = callback(a_1)
    if check == True:
        x = x + 1
        can_play.delete(snno)
        snno = can_play.create_text(20, 146, text=str(x), font=('Helvetica 20 bold'), fill="purple")
        li_1.append(a_1)
        team1_entry_play.delete(0, END)
    else:
        messagebox.showerror("WRONG INPUT", "INVALID ENTRY, PLEASE FILL AGAIN")
        team1_entry_play.delete(0, END)


def team_2():
    global li_2
    global l
    global can_play
    global snno_1
    global team2_entry_play
    b_2 = team2_var_play.get()
    check = callback(b_2)
    if check == True:
        can_play.delete(snno_1)
        l = l + 1
        snno_1 = can_play.create_text(445, 146, text=str(l), font=('Helvetica 20 bold'), fill="purple")
        li_2.append(b_2)
        team2_entry_play.delete(0, END)
    else:
        messagebox.showerror("WRONG INPUT", "INVALID ENTRY, PLEASE FILL AGAIN")
        team2_entry_play.delete(0, END)


def team_1_sub():
    global li_1_sub
    global y
    global c_play
    global snno_2
    global team1_entry_play1
    a_sub = team1_var_play1.get()
    check = callback(a_sub)
    if check == True:
        c_play.delete(snno_2)
        y = y + 1
        snno_2 = c_play.create_text(20, 146, text=str(y), font=('Helvetica 20 bold'), fill="purple")
        li_1_sub.append(a_sub)
        team1_entry_play1.delete(0, END)
    else:
        messagebox.showerror("WRONG INPUT", "INVALID ENTRY, PLEASE FILL AGAIN")
        team1_entry_play1.delete(0, END)


def team_2_sub():
    global li_2_sub
    global m
    global c_play
    global snno_3
    global team2_entry_play2
    b_sub = team2_var_play2.get()
    check = callback(b_sub)
    if check == True:
        c_play.delete(snno_3)
        m = m + 1
        snno_3 = c_play.create_text(445, 146, text=str(m), font=('Helvetica 20 bold'), fill="purple")
        li_2_sub.append(b_sub)
        team2_entry_play2.delete(0, END)
    else:
        messagebox.showerror("WRONG INPUT", "INVALID ENTRY, PLEASE FILL AGAIN")
        team2_entry_play2.delete(0, END)


def enter_names():
    global a
    global b
    global frame_7
    global can_play
    global c_play
    frame_7 = Frame(root, width=760, height=625)

    frame_7.grid(row=0, column=5, sticky=N, rowspan=20, columnspan=20)

    img = Image.open("shubhank_4.jfif")
    resizedImage = img.resize((760, 625), Image.ANTIALIAS)
    CharPhoto = ImageTk.PhotoImage(image=resizedImage)
    ChLabel = Label(frame_7, image=CharPhoto)
    ChLabel.img = CharPhoto
    ChLabel.grid(row=0, column=5, columnspan=20, rowspan=20, sticky=N)

    Label(frame_7, text="ENTER PLAYER NAMES", padx=15, pady=15, bg="purple"
          , border=2, fg="white", relief=SUNKEN, font=('Algerian 20 bold')).grid(row=0, column=7, columnspan=15,
                                                                                 sticky=N)
    global snno
    global snno_1
    can_play = Canvas(frame_7, width=750, height=265, bg="pink")
    snno = can_play.create_text(20, 146, text="1", font=('Helvetica 20 bold'), fill="purple")
    snno_1 = can_play.create_text(445, 146, text="1", font=('Helvetica 20 bold'), fill="purple")
    can_text_play_2 = can_play.create_text(350, 30, text="ENTER THE NAMES OF ' PLAYING ELEVEN ' HERE",
                                           font=('Helvetica 14 underline'))
    can_text_play = can_play.create_text(153, 80, text=a, font=('Helvetica 17 bold'))
    can_text_play_1 = can_play.create_text(577, 80, text=b, font=('Helvetica 17 bold'))
    can_play.grid(row=3, column=7, columnspan=14, rowspan=5)

    global team1_entry_play
    team1_entry_play = Entry(frame_7, textvariable=team1_var_play, font=('Times 14 '), width=20)
    team1_var_play.set("       'Player Name'")
    team1_entry_play.grid(row=5, column=8, columnspan=4, rowspan=2)

    global team2_entry_play
    team2_entry_play = Entry(frame_7, textvariable=team2_var_play, font=('Times 14 '), width=20)
    team2_var_play.set("       'Player Name'")
    team2_entry_play.grid(row=5, column=15, columnspan=7, rowspan=2)

    Button(frame_7, text="ENTER", bg="red", font=('Times 14 '), command=team_2).grid(row=6, column=15, columnspan=8,
                                                                                     rowspan=2)
    Button(frame_7, text="ENTER", bg="red", font=('Times 14 '), command=team_1).grid(row=6, column=6, columnspan=7,
                                                                                     rowspan=2)

    global snno_2
    global snno_3
    c_play = Canvas(frame_7, width=750, height=265, bg="pink")
    snno_2 = c_play.create_text(20, 146, text=str(y), font=('Helvetica 20 bold'), fill="purple")
    snno_3 = c_play.create_text(445, 146, text=str(m), font=('Helvetica 20 bold'), fill="purple")
    c_text_play_2 = c_play.create_text(350, 30, text="ENTER THE NAMES OF ' SUBSTITUTES ' HERE",
                                       font=('Helvetica 14 underline'))
    c_text_play = c_play.create_text(153, 80, text=a, font=('Helvetica 17 bold'))
    c_text_play_1 = c_play.create_text(577, 80, text=b, font=('Helvetica 17 bold'))
    c_play.grid(row=11, column=7, columnspan=14, rowspan=5)

    global team1_entry_play1
    team1_entry_play1 = Entry(frame_7, textvariable=team1_var_play1, font=('Times 14 '), width=20)
    team1_var_play1.set("       'Player Name'")
    team1_entry_play1.grid(row=13, column=8, columnspan=4, rowspan=2)

    global team2_entry_play2
    team2_entry_play2 = Entry(frame_7, textvariable=team2_var_play2, font=('Times 14 '), width=20)
    team2_var_play2.set("       'Player Name'")
    team2_entry_play2.grid(row=13, column=15, columnspan=7, rowspan=2)

    Button(frame_7, text="ENTER", bg="red", font=('Times 14 '), command=team_2_sub).grid(row=14, column=15,
                                                                                         columnspan=8,
                                                                                         rowspan=2)
    Button(frame_7, text="ENTER", bg="red", font=('Times 14 '), command=team_1_sub).grid(row=14, column=6, columnspan=7,
                                                                                         rowspan=2)

    entryButton_4 = Button(root, width=12, pady=3, text="SAVE INFO", font=('Helvetica 15 bold')
                           , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=player_names)
    entryButton_4.grid(row=15, column=16, rowspan=3, columnspan=8)

    CharButton_3 = Button(root, text="PLAYER NAMES", font=('TimesNewRoman 15 bold'), width=20, pady=10
                          , relief=RIDGE, borderwidth=5, bg="pink", fg="red")
    CharButton_3.grid(row=14, column=2, columnspan=2)


root.configure(bg="#cb6dcc")
root.title("FILL DETAILS")
Label(root, text="                                                         ", bg="#cb6dcc", font=5).grid(row=1,
                                                                                                          column=3)

img_root_1 = Image.open("image.png")
resizedImage_root_1 = img_root_1.resize((750, 350), Image.ANTIALIAS)
CharPhoto_root_1 = ImageTk.PhotoImage(image=resizedImage_root_1)
ChLabel_root_1 = Label(root, image=CharPhoto_root_1, borderwidth=0)
ChLabel_root_1.img = CharPhoto_root_1
ChLabel_root_1.configure(highlightthickness=0)
ChLabel_root_1.grid(row=0, column=0, rowspan=10, columnspan=8)

img_root = Image.open("image_op.png")
resizedImage_root = img_root.resize((750, 329), Image.ANTIALIAS)
CharPhoto_root = ImageTk.PhotoImage(image=resizedImage_root)
ChLabel_root = Label(root, image=CharPhoto_root, borderwidth=0)
ChLabel_root.img = CharPhoto_root
ChLabel_root.grid(row=8, column=0, rowspan=18, columnspan=10)

frame_1 = Frame(root, bg="black", width=10, height=700)
frame_1.grid(row=0, column=0, rowspan=20)

frame_2 = Frame(root, bg="black", width=10, height=700)
frame_2.grid(row=0, column=4, rowspan=18)

frame_8 = Frame(root, bg="pink", width=760, height=75)
frame_8.grid(row=0, column=5, sticky=S, rowspan=20, columnspan=20)

img = Image.open("redbg_1.jfif")
resizedimage = img.resize((760, 75), Image.ANTIALIAS)
CharPhoto = ImageTk.PhotoImage(image=resizedimage)
ChLabel = Label(frame_8, image=CharPhoto, relief=FLAT)
ChLabel.img = CharPhoto
ChLabel.grid(row=0, column=4, sticky=S, rowspan=20, columnspan=20)

CharButton = Button(root, text="MATCH DETAILS", font=('TimesNewRoman 15 bold'), width=20, pady=10
                    , relief=RIDGE, borderwidth=5, command=match_details, bg="pink", fg="black")
CharButton.grid(row=2, column=2, columnspan=2)

CharButton_1 = Button(root, text="LOCATION DETAILS", font=('TimesNewRoman 15 bold'), width=20, pady=10
                      , relief=RIDGE, borderwidth=5, bg="pink", fg="black", command=error)
CharButton_1.grid(row=6, column=2, columnspan=2)

CharButton_2 = Button(root, text="TEAM DETAILS", font=('TimesNewRoman 15 bold'), width=20, pady=10
                      , relief=RIDGE, borderwidth=5, bg="pink", fg="black", command=error)
CharButton_2.grid(row=10, column=2, columnspan=2)

CharButton_3 = Button(root, text="PLAYER NAMES", font=('TimesNewRoman 15 bold'), width=20, pady=10
                      , relief=RIDGE, borderwidth=5, bg="pink", fg="black", command=error)
CharButton_3.grid(row=14, column=2, columnspan=2)

entryButton_1 = Button(root, width=12, pady=3, text="SAVE INFO", font=('Helvetica 15 bold')
                       , relief=RIDGE, borderwidth=5, bg="purple", fg="white", command=error_3)
entryButton_1.grid(row=15, column=16, rowspan=3, columnspan=8)

frame_6 = Frame(root, width=760, height=625, bg="pink").grid(row=0, column=5, sticky=N, rowspan=20, columnspan=20)

can = Canvas(frame_6, width=600, height=70, bg="red")
can.create_text(300, 15, text="THIS IS YOUR WINDOW TO FILL ALL THE ", font=('Times 15 bold'), fill="black")
can.create_text(300, 45, text=" SPECIFIC DETAILS OF THE MATCH", font=('Times 15 bold'), fill="black")
can.configure(highlightthickness=0)
can.grid(row=0, column=5, columnspan=20, rowspan=2)

can_1 = Canvas(frame_6, width=595, height=70, bg="pink")
can_arrow = can_1.create_line(10, 35, 100, 35, arrow=LAST)
can_text = can_1.create_text(350, 35, text="CLICK ON THIS BUTTON TO FILL YOUR MATCH DETAILS",
                             font=('Helvetica 13 bold'))
can_1.configure(highlightthickness=0)
can_1.grid(row=2, column=5, columnspan=14)

can_2 = Canvas(frame_6, width=595, height=70, bg="pink")
can_2.configure(highlightthickness=0)
can_2.grid(row=6, column=5, columnspan=14)

can_3 = Canvas(frame_6, width=595, height=70, bg="pink")
can_3.configure(highlightthickness=0)
can_3.grid(row=10, column=5, columnspan=14)

can_4 = Canvas(frame_6, width=595, height=70, bg="pink")
can_4.configure(highlightthickness=0)
can_4.grid(row=14, column=5, columnspan=14)

root.mainloop()