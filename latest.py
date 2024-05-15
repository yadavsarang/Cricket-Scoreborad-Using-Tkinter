from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DETAILS_FILE import li_bowl, li_bat, bat_main, bowl_main, toss_won, toss_chose, over_entry

li_bowlers_name = []
li_over_number = []
li_over_runs = []
li_over_out = []
li_over_wide = []
li_over_noball = []

li_batsman_name = []
li_runs_scored = []
li_ball_played = []
li_mode_of_dismayal = []

bat_main = "INDIA"
bowl_main = "PAKISATAN"
toss_won = "INDIA"
toss_chose = "BAT"
# over_entry = 3
# START MATCH

def start_match_1():
    Button(board_root, text="WIDE / NO BALL", bg="orange", fg="black", padx=20, pady=20, font='Helvetica 15 bold',
           command=wide_no_ball).grid(row=14, column=2, columnspan=6)
    Button(board_root, text="SUBMIT ENTERIES", bg="VIOLET", fg="black", padx=15, pady=20, font='Helvetica 15 bold',
           command=submit_enteries).grid(row=22, column=7, columnspan=3, rowspan=8)
    Button(board_root, text="WICKET", bg="RED", fg="white", padx=20, pady=20, font='Helvetica 15 bold',
           command=wicket).grid(row=14, column=7, columnspan=3)


def start_match():
    if play1_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE COMPLETE THE PLAYER SELECTION")
    elif play2_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE COMPLETE THE PLAYER SELECTION")
    else:
        global first_inn
        run_1.set(0)
        run_2.set(0)
        global c2_lights
        canvas_lights.delete(c2_lights)
        c2_lights = canvas_lights.create_text(90, 100, text="'0'", font='Ebrima 15 bold')

        global c3_lights
        canvas_lights.delete(c3_lights)
        c3_lights = canvas_lights.create_text(400, 100, text="'0'", font='Ebrima 15 bold')

        first_inn = Label(board_root, text="FIRST INNINGS", font='Times 20 bold')
        first_inn.place(x=665, y=70)
        global t1
        global rec
        global rec_2
        global t2
        canvas_2.delete(t1)
        rec = canvas_2.create_rectangle(50, 10, 725, 50)
        #rec_2 = canvas_2.create_rectangle(825, 10, 1473, 50)
        t1 = canvas_2.create_text(390, 30,
                                  text="THE MATCH IS HELD BETWEEN " + ' " ' + bat_main + " AND " + bowl_main + ' " ',
                                  font=('Times 17 bold'))
        t2 = canvas_2.create_text(1150, 30, text=toss_won + " HAS WON THE TOSS AND HAS CHOOSED TO " + toss_chose,
                                  font=('Times 17 bold'))
        start_match_1()


def end_start_match():
    if play1_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE COMPLETE THE PLAYER SELECTION")
    elif play2_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE COMPLETE THE PLAYER SELECTION")
    else:
        global first_inn
        run_1.set(0)
        run_2.set(0)
        global c2_lights
        canvas_lights.delete(c2_lights)
        c2_lights = canvas_lights.create_text(90, 100, text="'0'", font=('Ebrima 15 bold'))

        global c3_lights
        canvas_lights.delete(c3_lights)
        c3_lights = canvas_lights.create_text(400, 100, text="'0'", font=('Ebrima 15 bold'))

        first_inn.configure(text="SECOND INNINGS")

        global t1
        global t2
        #global rec_2
        canvas_2.delete(t1)
        canvas_2.delete(t2)
        #canvas_2.delete(rec_2)
        canvas_2.create_rectangle(50, 10, 725, 50)
        #rec_2 = canvas_2.create_rectangle(785, 10, 1513, 50)
        canvas_2.create_text(390, 30,
                             text="THE MATCH IS HELD BETWEEN " + ' " ' + bat_main + " AND " + bowl_main + ' " ',
                             font=('Times 17 bold'))
        canvas_2.create_text(1150, 30, text="FIRST INNINGS ARE OVER AND " + bat_main + " IS NOW " + "BOWLING",
                             font=('Times 17 bold'))
        start_match_1()


def error():
    run_1.set(0)
    run_2.set(0)
    messagebox.showerror("ERROR", "PLEASE COMPLETE THE PLAYER SELECTION")


def out_1_error():
    messagebox.showerror("ERROR", "PLEASE CLICK ON 'START MATCH' TO START THE BOARD")


def error_1():
    messagebox.showerror("ERROR", "PLEASE SELECT THE BOWLER'S NAME FOR THE OVER")
    play1_var.set("'SELECT'")
    play2_var.set("'SELECT'")


def error_2():
    messagebox.showerror("ERROR", "PLEASE SELECT THE PLAYER I NAME FIRST")
    play2_var.set("'SELECT'")


def not_out():
    global x
    messagebox.showinfo("INFO", "YOU CANNOT CHANGE YOUR PLAYER NAME UNTIL THE PLAYER IS OUT")
    play1_var.set(x)


def not_out_1():
    global x_1
    messagebox.showinfo("INFO", "YOU CANNOT CHANGE YOUR PLAYER NAME UNTIL THE PLAYER IS OUT")
    play2_var.set(x_1)


def act_over():
    global x_2
    messagebox.showinfo("INFO", "YOU CANNOT CHANGE YOUR BOWLER NAME UNTIL THE OVER IS COMPLETED")
    bowler_var.set(x_2)


# NAME AND BUTTONS
def start_name():
    global y
    global x
    a_name = play1_var.get()
    # li_batsman_name.append(a_name)
    x = a_name.split(" ")
    y = x[0]
    global c2_lights_1
    canvas_lights.delete(c2_lights_1)
    c2_lights_1 = canvas_lights.create_text(90, 70, text=y + " " + "'0'", font=('Ebrima 15 bold'))

    b = play1_var.get()
    empty_list.append(b)
    li_bat.remove(b)

    drop_play_var = OptionMenu(board_root, play1_var, *li_bat)
    drop_play_var.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    drop_play_var.grid(row=18, column=1, columnspan=2)
    drop_play_var_2 = OptionMenu(board_root, play2_var, *li_bat)
    drop_play_var_2.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    drop_play_var_2.grid(row=20, column=1, columnspan=2)


def start_1_name():
    global y_1
    global x_1
    b_name = play2_var.get()
    #li_batsman_name.append(b_name)
    x_1 = b_name.split(" ")
    y_1 = x_1[0]
    global c2_lights_2
    canvas_lights.delete(c2_lights_2)
    c2_lights_2 = canvas_lights.create_text(400, 70, text=y_1 + " " + "'0'", font=('Ebrima 15 bold'))

    b = play2_var.get()
    empty_list.append(b)
    li_bat.remove(b)

    drop_play_var = OptionMenu(board_root, play1_var, *li_bat)
    drop_play_var.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    drop_play_var.grid(row=18, column=1, columnspan=2)
    drop_play_var_2 = OptionMenu(board_root, play2_var, *li_bat)
    drop_play_var_2.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    drop_play_var_2.grid(row=20, column=1, columnspan=2)


def start_2_name():
    global bowl_name_1
    global x_2
    global c1_lights
    bowl_name_1 = bowler_var.get()
    li_bowlers_name.append(bowl_name_1)
    x_2 = bowl_name_1.split(" ")
    y_2 = x_2[0]
    canvas_lights.delete(c1_lights)
    c1_lights = canvas_lights.create_text(242, 20, text=y_2 + " WILL BE BOWLING FOR THIS OVER"
                                          , font=('Consolas 15 bold'), fill="blue")


def end_start():
    if play1_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play1_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_name()
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=end_start_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out,
               font=('Helvetica 10 bold')).grid(row=18, column=3)


def start():
    if play1_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play1_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_name()
        play2_var.set("'SELECT'")
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=start_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out,
               font=('Helvetica 10 bold')).grid(row=18, column=3)


def name():
    if play1_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play1_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_name()
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out,
               font=('Helvetica 10 bold')).grid(row=18, column=3)


def end_start_1():
    if play2_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play2_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_1_name()
        Button(board_root, text="START MATCH", bg="VIOLET", fg="black", padx=15, pady=20, font=('Helvetica 15 bold'),
               command=end_start_match).grid(row=22, column=7, columnspan=3, rowspan=8)

        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)


def start_1():
    if play2_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play2_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_1_name()
        Button(board_root, text="START MATCH", bg="VIOLET", fg="black", padx=15, pady=20, font=('Helvetica 15 bold'),
               command=start_match).grid(row=22, column=7, columnspan=3, rowspan=8)
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)


def name_1():
    if play2_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    elif play2_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BATSMAN NAME")
    else:
        start_1_name()
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=not_out_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)


def end_start_2():
    if bowler_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BOWLER NAME")
        bowler_var.set("'SELECT'")
    else:
        start_2_name()
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=end_start,
               font=('Helvetica 10 bold')).grid(row=18, column=3)
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=error_2,
               font=('Helvetica 10 bold')).grid(row=20, column=3)
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=act_over,
               font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)


def start_2():
    if bowler_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BOWLER NAME")
        bowler_var.set("'SELECT'")
    else:
        start_2_name()
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=start,
               font=('Helvetica 10 bold')).grid(row=18, column=3)
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=error_2,
               font=('Helvetica 10 bold')).grid(row=20, column=3)
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=act_over,
               font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)


def name_2():
    if bowler_var.get() == "'SELECT'":
        messagebox.showerror("ERROR", "PLEASE SELECT THE BOWLER NAME")
        bowler_var.set("'SELECT'")
    else:
        start_2_name()
        Button(board_root, text="OK", width=5, bg="violet", fg="black", command=act_over,
               font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)


# WICKET
def main():
    global li_bat
    global count
    global count_over
    global wide_over
    global no_over
    global c
    count = count + 1
    count_over = count_over + 1
    global bowl
    global c_wicket
    canvas_lights.delete(c_wicket)
    c_wicket = canvas_lights.create_text(285, 200, text=str(count_over), font=('Ebrima 20 bold'))
    global canvas_wickets
    canvas.delete(canvas_wickets)
    canvas_wickets = canvas.create_text(343, 70, text=str(count), fill="black", font=('Helvetica 70 bold'))
    global ball_total
    global ball_stop
    global ball
    ball_stop = over_entry * 6
    ball_total = ball_total + 1
    ball = ball + 1
    global over
    if ball == 6:
        li_over_number.append(over)
        ball = 0
        over = over + 1
    bowl = str(over) + "." + str(ball)

    global canvas_overs
    canvas.delete(canvas_overs)
    canvas_overs = canvas.create_text(250, 190, text=bowl, fill="black", font=('Helvetica 70 bold'))
    if over != 0:
        if bowl == str(over) + "." + "0":
            messagebox.showinfo("OVER COMPLETE!!", "OVER IS COMPLETE")
            Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name_2,
                   font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)
            li_over_out.append(count_over)
            count_over = 0
            canvas_lights.delete(c_wicket)
            c_wicket = canvas_lights.create_text(285, 200, text=str(count_over), font=('Ebrima 20 bold'))
            global wide_over
            li_over_wide.append(wide_over)
            wide_over = 0
            global no_over
            li_over_noball.append(no_over)
            no_over = 0

            global c_runs
            canvas_lights.delete(c_runs)
            c_runs = canvas_lights.create_text(215, 200, text=str(c), font=('Ebrima 20 bold'))
            li_over_runs.append(c)
            c = 0

    func_1()

    if ball_total == ball_stop:
        if first_inn.cget("text") == "SECOND INNINGS":
            end_match()
        else:
            end()
    elif count == 10:
        if first_inn.cget("text") == "SECOND INNINGS":
            end_match()
        else:
            end()

def checking_1():
    global li_bowl
    global ball_opener_count
    global ball_non_count
    global out
    if diss_2.get() == 1:
        out = m
        li_batsman_name.append(out)
        global c2_lights_1
        global opener_sum
        canvas_lights.delete(c2_lights_1)
        c2_lights_1 = canvas_lights.create_text(90, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
        li_runs_scored.append(opener_sum)
        opener_sum = 0
        global c2_lights
        canvas_lights.delete(c2_lights)
        c2_lights = canvas_lights.create_text(90, 100, text="'balls played'", font=('Ebrima 15 bold'))
        play1_var.set("'PLAYER NAME'")
        li_ball_played.append(ball_opener_count)
        ball_opener_count = 0
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name,
               font=('Helvetica 10 bold')).grid(
            row=18, column=3)
        run_1.set(0)
    elif diss_2.get() == 2:
        out = n
        li_batsman_name.append(out)
        global c2_lights_2
        canvas_lights.delete(c2_lights_2)
        c2_lights_2 = canvas_lights.create_text(400, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
        global non_striker_sum
        li_runs_scored.append(non_striker_sum)
        non_striker_sum = 0
        play2_var.set("'PLAYER NAME'")
        li_ball_played.append(ball_non_count)
        ball_non_count = 0
        global c3_lights
        canvas_lights.delete(c3_lights)
        c3_lights = canvas_lights.create_text(400, 100, text="'balls played'", font=('Ebrima 15 bold'))
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name_1,
               font=('Helvetica 10 bold')).grid(row=20, column=3)
        run_2.set(0)


j_2 = 0
j_3 = 0


def run_destroy():
    global out
    global first_inn
    global end_bat_1
    if first_inn.cget("text") == "SECOND INNINGS":
        for i in range(len(end_bat_1)):
            if diss_3.get() == i:
                s = end_bat_1[i]

    else:
        for i in range(len(li_bowl)):
            if diss_3.get() == i:
                s = li_bowl[i]

    global f_4
    f_4.grid_forget()
    root_out.destroy()
    main()


def run_out():
    global li_bowl
    global j_2
    global j_3
    global f_4
    global first_inn
    global end_bat_1
    if first_inn.cget("text") == "SECOND INNINGS":
        checking_1()
        b = "#ffaec8"
        f_4 = Frame(f_3, width=400, height=430, bg=b)
        f_4.grid()
        Label(f_4, text="BY WHICH PLAYER :", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
        d = len(end_bat_1) // 2 + 1
        for i in range(d):
            na = end_bat_1[i].split(" ")
            r = Radiobutton(f_4, text=na[0], font='Helvetica 12 bold', variable=diss_3, value=i, fg="BLACK",
                            bg="orange", relief=FLAT)
            r.place(x=50, y=90 + j_2)
            j_2 = j_2 + 50
        c = len(end_bat_1) - d
        for i in range(c):
            na_1 = end_bat_1[d].split(" ")
            r2 = Radiobutton(f_4, text=na_1[0], font='Helvetica 12 bold', variable=diss_3, value=d, fg="BLACK",
                             bg="orange", relief=FLAT)
            r2.place(x=250, y=90 + j_3)
            j_3 = j_3 + 50
            d = d + 1
        Button(f_4, text="SUBMIT", font="Times 15 bold", bg="red", command=run_destroy).place(x=250, y=370)
        j_2 = 0
        j_3 = 0
    else:
        checking_1()
        b = "#ffaec8"
        f_4 = Frame(f_3, width=400, height=430, bg=b)
        f_4.grid()
        Label(f_4, text="BY WHICH PLAYER :", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
        d = len(li_bowl) // 2 + 1
        for i in range(d):
            na = li_bowl[i].split(" ")
            r = Radiobutton(f_4, text=na[0], font='Helvetica 12 bold', variable=diss_3, value=i, fg="BLACK",
                            bg="orange", relief=FLAT)
            r.place(x=50, y=90 + j_2)
            j_2 = j_2 + 50
        c = len(li_bowl) - d
        for i in range(c):
            na_1 = li_bowl[d].split(" ")
            r2 = Radiobutton(f_4, text=na_1[0], font='Helvetica 12 bold', variable=diss_3, value=d, fg="BLACK",
                             bg="orange", relief=FLAT)
            r2.place(x=250, y=90 + j_3)
            j_3 = j_3 + 50
            d = d + 1
        Button(f_4, text="SUBMIT", font="Times 15 bold", bg="red", command=run_destroy).place(x=250, y=370)
        j_2 = 0
        j_3 = 0


def other_d():
    global f_2
    f_2.grid_forget()
    root_out.destroy()
    main()


def other_out():
    global f_1
    f_1.grid_forget()
    checking_1()
    b = "#ffaec8"
    global f_2
    f_2 = Frame(root_out, width=400, height=430, bg=b)
    f_2.grid()
    Label(f_2, text="PLEASE SPECIFY :", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
    Entry(f_2, textvariable=others, width=20, font="Times 20 bold").place(x=70, y=100)
    c = Canvas(f_2, width=50, height=50, bg=b)
    c.create_line(5, 20, 50, 20, arrow=LAST)
    c.configure(highlightthickness=0)
    c.place(x=10, y=100)
    Button(f_2, text="SUBMIT", font="Times 15 bold", bg="red", command=other_d).place(x=250, y=170)


def checking_2():
    global l1_get
    global l2_get
    global m
    global ball_non_count
    global ball_opener_count
    if "*" in l1_get:
        m = play1_var.get()
        li_batsman_name.append(m)
        global c2_lights_1
        global opener_sum
        canvas_lights.delete(c2_lights_1)
        c2_lights_1 = canvas_lights.create_text(90, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
        li_runs_scored.append(opener_sum)
        opener_sum = 0
        global c2_lights
        canvas_lights.delete(c2_lights)
        c2_lights = canvas_lights.create_text(90, 100, text="'balls played'", font=('Ebrima 15 bold'))
        play1_var.set("'PLAYER NAME'")
        li_ball_played.append(ball_opener_count)
        ball_opener_count = 0
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name,
               font=('Helvetica 10 bold')).grid(row=18, column=3)
        run_1.set(0)
    if "*" in l2_get:
        m = play2_var.get()
        li_batsman_name.append(m)
        global c2_lights_2
        canvas_lights.delete(c2_lights_2)
        c2_lights_2 = canvas_lights.create_text(400, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
        global non_striker_sum
        li_runs_scored.append(non_striker_sum)
        non_striker_sum = 0
        play2_var.set("'PLAYER NAME'")
        li_ball_played.append(ball_non_count)
        ball_non_count = 0
        global c3_lights
        canvas_lights.delete(c3_lights)
        c3_lights = canvas_lights.create_text(400, 100, text="'balls played'", font=('Ebrima 15 bold'))
        Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name_1,font=('Helvetica 10 bold')).grid(row=20, column=3)
        run_2.set(0)


def caught():
    global first_inn
    if first_inn.cget("text") == "SECOND INNINGS":
        global end_bat_1
        for i in range(len(end_bat_1)):
            if diss_2.get() == i:
                s = end_bat_1[i]

    else:
        global li_bowl
        for i in range(len(li_bowl)):
            if diss_2.get() == i:
                s = li_bowl[i]

    global f_1
    f_1.grid_forget()
    root_out.destroy()
    main()


count = 0
empty_list = []
j = 0
j_1 = 0
count_over = 0


def out_mode():
    global j
    global j_1
    global f
    global f_1
    global root_out
    global f_3
    global li_bowl

    b = "#ffaec8"
    mode = diss_1.get()
    if mode == 1:
        checking_2()
        root_out.destroy()
        main()

    elif mode == 2:
        global first_inn
        if first_inn.cget("text") == "SECOND INNINGS":
            global end_bat_1
            checking_2()
            f_1 = Frame(f, width=400, height=430, bg=b)
            f_1.grid()
            Label(f_1, text="BY WHICH PLAYER :", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
            d = len(end_bat_1) // 2 + 1
            for i in range(d):
                na = end_bat_1[i].split(" ")
                r = Radiobutton(f_1, text=na[0], font='Helvetica 12 bold', variable=diss_2, value=i, fg="BLACK",
                                bg="orange", relief=FLAT)
                r.place(x=50, y=90 + j)
                j = j + 50
            c = len(end_bat_1) - d
            for i in range(c):
                na_1 = end_bat_1[d].split(" ")
                r2 = Radiobutton(f_1, text=na_1[0], font='Helvetica 12 bold', variable=diss_2, value=d, fg="BLACK",
                                 bg="orange", relief=FLAT)
                r2.place(x=250, y=90 + j_1)
                j_1 = j_1 + 50
                d = d + 1
            Button(f_1, text="SUBMIT", font="Times 15 bold", bg="red", command=caught).place(x=270, y=370)
            j_1 = 0
            j = 0
        else:
            checking_2()
            # f.grid_forget()
            f_1 = Frame(f, width=400, height=430, bg=b)
            f_1.grid()
            Label(f_1, text="BY WHICH PLAYER :", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
            d = len(li_bowl) // 2 + 1
            for i in range(d):
                na = li_bowl[i].split(" ")
                r = Radiobutton(f_1, text=na[0], font='Helvetica 12 bold', variable=diss_2, value=i, fg="BLACK",
                                bg="orange", relief=FLAT)
                r.place(x=50, y=90 + j)
                j = j + 50
            c = len(li_bowl) - d
            for i in range(c):
                na_1 = li_bowl[d].split(" ")
                r2 = Radiobutton(f_1, text=na_1[0], font='Helvetica 12 bold', variable=diss_2, value=d, fg="BLACK",
                                 bg="orange", relief=FLAT)
                r2.place(x=250, y=90 + j_1)
                j_1 = j_1 + 50
                d = d + 1
            Button(f_1, text="SUBMIT", font="Times 15 bold", bg="red", command=caught).place(x=270, y=370)
            j_1 = 0
            j = 0

    elif mode == 3:
        global m
        global n
        f_3 = Frame(f, width=400, height=430, bg=b)
        f_3.grid()
        Label(f_3, text="WHICH BATSMAN ?", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
        m = play1_var.get()
        n = play2_var.get()

        Radiobutton(f_3, text=m, font='Helvetica 12 bold', variable=diss_2, value=1, fg="BLACK", bg="orange",
                    relief=FLAT).place(x=50, y=90)
        Radiobutton(f_3, text=n, font='Helvetica 12 bold', variable=diss_2, value=2, fg="BLACK", bg="orange",
                    relief=FLAT).place(x=250, y=90)
        Button(f_3, text="SUBMIT", font="Times 15 bold", bg="red", command=run_out).place(x=250, y=160)

    elif mode == 4:
        checking_2()
        root_out.destroy()
        main()

    elif mode == 5:
        root_out.destroy()
        main()

    elif mode == 6:
        f.grid_forget()
        f_1 = Frame(root_out, width=400, height=430, bg=b)
        f_1.grid()
        Label(f_1, text="WHICH BATSMAN ?", font="Times 20 bold", bg="violet", relief=SOLID).place(x=70, y=10)
        m = play1_var.get()
        n = play2_var.get()

        r_bat = Radiobutton(f_1, text=m, font='Helvetica 12 bold', variable=diss_2, value=1, fg="BLACK", bg="orange",
                            relief=FLAT).place(x=50, y=90)
        r_bat = Radiobutton(f_1, text=n, font='Helvetica 12 bold', variable=diss_2, value=2, fg="BLACK", bg="orange",
                            relief=FLAT).place(x=250, y=90)
        Button(f_1, text="SUBMIT", font="Times 15 bold", bg="red", command=other_out).place(x=250, y=160)


def wicket():
    if play1_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "YOU HAVE NOT SELECTED YOUR PLAYER NAME")
    elif play2_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "YOU HAVE NOT SELECTED YOUR PLAYER NAME")
    else:
        global f
        global root_out
        root_out = Toplevel(board_root)
        root_out.geometry("700x430")
        b = "#ffaec8"
        root_out.configure(bg=b)
        root_out.title("WICKET")
        a = "orange"
        img_3 = Image.open("wicket.png")
        resizedImage3 = img_3.resize((320, 430), Image.ANTIALIAS)
        CharPhoto3 = ImageTk.PhotoImage(image=resizedImage3, master=board_root)
        f = Frame(root_out, width=400, height=430, bg=b)
        f.grid()
        Label(f, text="MODE OF DISSMISAL", font="Times 20 bold", bg=b, relief=SOLID).place(x=70, y=10)

        r1 = Radiobutton(f, text="BOWLED", font='Helvetica 14 bold', variable=diss_1, value=1, fg="BLACK", bg=a,
                         relief=FLAT)
        r1.place(x=50, y=70)

        r2 = Radiobutton(f, text="CAUGHT", font='Helvetica 14 bold', variable=diss_1, value=2, fg="BLACK", bg=a,
                         relief=FLAT)
        r2.place(x=250, y=70)

        r3 = Radiobutton(f, text="RUN OUT", font='Helvetica 14 bold', variable=diss_1, value=3, fg="BLACK", bg=a,
                         relief=FLAT)
        r3.place(x=50, y=170)

        r4 = Radiobutton(f, text="LBW", font='Helvetica 14 bold', variable=diss_1, value=4, fg="BLACK", bg=a,
                         relief=FLAT)
        r4.place(x=250, y=170)

        r5 = Radiobutton(f, text="STUMPED", font='Helvetica 14 bold', variable=diss_1, value=5, fg="BLACK", bg=a,
                         relief=FLAT)
        r5.place(x=50, y=270)

        r6 = Radiobutton(f, text="OTHERS", font='Helvetica 14 bold', variable=diss_1, value=6, fg="BLACK", bg=a,
                         relief=FLAT)
        r6.place(x=250, y=270)

        can_out = Canvas(root_out, width=300, height=400, bg=b)
        can_tick3 = can_out.create_image(150, 210, image=CharPhoto3)
        can_out.configure(highlightthickness=0)

        can_out.place(x=400, y=10)
        Button(f, text="SUBMIT", font="Times 15 bold", bg="red", command=out_mode).place(x=150, y=370)


        root_out.mainloop()
a = 0


def board():
    global opener
    global non_striker
    sum_runs_1 = opener + non_striker
    # wickets = str(2)
    global a
    a = a + sum_runs_1
    a = str(a)
    global canvas_runs
    canvas.delete(canvas_runs)
    canvas_runs = canvas.create_text(160, 70, text=a, fill="black", font=('Helvetica 70 bold'))
    over_runs()
    a = int(a)


c = 0
def over_runs():
    global opener
    global non_striker
    global sum_runs_over
    global bowl
    sum_runs_over = opener + non_striker
    global c
    c = c + sum_runs_over
    #c = str(c)
    # over_no = str(s1.get())
    # ball_no = str(s2.get())
    # bowl = over_no + "." + ball_no
    global canvas_overs
    canvas.delete(canvas_overs)
    canvas_overs = canvas.create_text(250, 190, text=bowl, fill="black", font=('Helvetica 70 bold'))
    global l_1
    global l_2
    # if over != 0:
    #     if str(over) + "." + "0" == bowl:
    #     # global c_runs
    #         # canvas_lights.delete(c_runs)
    #         # c_runs = canvas_lights.create_text(215, 200, text=str(c), font=('Ebrima 20 bold'))
    #         # li_over_runs.append(c)
    #         # c = 0

    #c = int(c)


wide_over = 0
def wide():
    global bowl
    messagebox.showinfo("WIDE", "THE BOWL WAS WIDE BALL, THE BATTING TEAM IS AWARDED WITH ONE EXTRA RUN")
    global wide_over
    global a
    a = a + 1
    global c
    c = c + 1
    global canvas_runs
    wide_over = wide_over + 1
    canvas.delete(canvas_runs)
    canvas_runs = canvas.create_text(160, 70, text=a, fill="black", font=('Helvetica 70 bold'))
    global wn_root
    wn_root.destroy()


no_over = 0
def noBall():
    global a
    messagebox.showinfo("NO BALL", "THE BOWL WAS ' NO BALL ', THE BATTING TEAM IS AWARDED WITH A FREE HIT")
    a = a + 1
    global c
    c = c + 1
    global canvas_runs
    canvas.delete(canvas_runs)
    canvas_runs = canvas.create_text(160, 70, text=a, fill="black", font=('Helvetica 70 bold'))
    global c6_lights
    canvas_lights.delete(c6_lights)
    global no_over
    no_over = no_over + 1
    global wn_root
    wn_root.destroy()


def wide_no_ball():
    global wn_root
    wn_root = Toplevel(board_root)
    wn_root.geometry("790x500")
    wn_root.configure(bg="#ffaec8")
    wn_root.title("Wide AND No Ball")

    label_1 = Label(wn_root, text="TYPE OF BALL", font="Times 20 bold", bg="red", relief=SOLID, pady=10, padx=10)
    label_1.place(x=290, y=20)

    label_2 = Label(wn_root, text="Wide Ball", font="Times 15 bold", bg="orange")
    label_2.place(x=153, y=125)

    label_3 = Label(wn_root, text="No Ball", font="Times 15 bold", bg="orange")
    label_3.place(x=570, y=125)

    img_root_1 = Image.open("wideball.jpg")
    resizedImage_root_1 = img_root_1.resize((300, 300), Image.ANTIALIAS)
    CharPhoto_root_1 = ImageTk.PhotoImage(image=resizedImage_root_1, master=board_root)
    a_1 = Button(wn_root, image=CharPhoto_root_1, command=wide)
    a_1.image = img_root_1
    a_1.grid(row=30, column=1, padx=(40, 0), pady=(180, 0))

    img_root_2 = Image.open("noball.jpg")
    resizedImage_root_2 = img_root_2.resize((300, 300), Image.ANTIALIAS)
    CharPhoto_root_2 = ImageTk.PhotoImage(image=resizedImage_root_2, master=board_root)

    a_2 = Button(wn_root, text="No Ball", image=CharPhoto_root_2, command=noBall)
    a_2.grid(row=30, column=10, padx=(100, 0), pady=(180, 0))

    wn_root.mainloop()


def over_strike():
    global l1
    global l2
    global l1_get
    global l2_get
    global over
    global bowl
    global z_3
    if over != 0:
        if bowl == str(over) + "." + "0":
            if "*" in l1_get:
                l1 = Label(board_root, text="PLAYER I   ", fg="black", font=('Ebrima 14 bold'))
                l2 = Label(board_root, text="PLAYER II *", fg="black", font=('Ebrima 14 bold'))
            if "*" in l2_get:
                l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
                l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
            l1_get = l1.cget("text")
            l2_get = l2.cget("text")


ball_stop_1 = -1


def check_entry():
    global l1_get
    global l2_get
    global opener
    global non_striker
    global bowl
    global ball
    global over
    global ball_total
    global li_over_me
    global l1
    global l2
    global canvas_lights
    global ball_stop
    global count
    global ball_stop_1
    global first_inn
    ball_stop = over_entry * 6
    ball_total = ball_total + 1
    ball = ball + 1

    if ball == 6:
        ball = 0
        li_over_number.append(over)
        over = over + 1
    bowl = str(over) + "." + str(ball)

    if "*" in l1_get:
        if non_striker != 0:
            global ball_opener_count
            ball_opener_count = ball_opener_count - 1
            global c2_lights
            canvas_lights.delete(c2_lights)
            c2_lights = canvas_lights.create_text(90, 100, text="( " + str(ball_opener_count) + " )",
                                                  font=('Ebrima 15 bold'))
            messagebox.showerror("WRONG ENTRY FILLED", "PLEASE FILL THE ENTRY OF THE PLAYER ON STRIKE")
            non_striker = 0
            if bowl == "0.0":
                ball = 0
                bowl = str(over) + "." + str(ball)
            elif bowl == "0.1":
                ball = ball - 1
                bowl = str(over) + "." + str(ball)
            elif bowl == str(over) + "." + "1":
                if "*" in l1_get:
                    l1 = Label(board_root, text="PLAYER I   ", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II *", fg="black", font=('Ebrima 14 bold'))
                if "*" in l2_get:
                    l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
                l1_get = l1.cget("text")
                l2_get = l2.cget("text")
                ball = ball - 1
                bowl = str(over) + "." + str(ball)
            elif bowl == str(over) + "." + "0":
                t = over - 1
                bowl = str(t) + "." + "5"
                ball = 5
                over = over - 1

            else:
                ball = ball - 1
                bowl = str(over) + "." + str(ball)
            ball_total = ball_total - 1

    if "*" in l2_get:
        if opener != 0:
            global ball_non_count
            ball_non_count = ball_non_count - 1
            global c3_lights
            canvas_lights.delete(c3_lights)
            c3_lights = canvas_lights.create_text(400, 100, text="( " + str(ball_non_count) + " )",
                                                  font=('Ebrima 15 bold'))

            messagebox.showerror("WRONG ENTRY FILLED", "PLEASE FILL THE ENTRY OF THE PLAYER ON STRIKE")
            opener = 0
            if bowl == "0.0":
                ball = 0
                bowl = str(over) + "." + str(ball)
            elif bowl == "0.1":
                ball = ball - 1
                bowl = str(over) + "." + str(ball)
            elif bowl == str(over) + "." + "1":

                if "*" in l1_get:
                    l1 = Label(board_root, text="PLAYER I   ", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II *", fg="black", font=('Ebrima 14 bold'))
                if "*" in l2_get:
                    l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
                l1_get = l1.cget("text")
                l2_get = l2.cget("text")
                ball = ball - 1
                bowl = str(over) + "." + str(ball)
            elif bowl == str(over) + "." + "0":
                t = over - 1
                bowl = str(t) + "." + "5"
                ball = 5
                over = over - 1
            else:
                ball = ball - 1
                bowl = str(over) + "." + str(ball)

            ball_total = ball_total - 1

    if over != 0:
        if bowl == str(over) + "." + "0":
            messagebox.showinfo("OVER COMPLETE!!", "OVER IS COMPLETE")
            Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=name_2,
                   font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)
            global count_over
            global c_wicket
            li_over_out.append(count_over)
            count_over = 0
            canvas_lights.delete(c_wicket)
            c_wicket = canvas_lights.create_text(285, 200, text=str(count_over), font=('Ebrima 20 bold'))
            global wide_over
            li_over_wide.append(wide_over)
            wide_over = 0
            global no_over
            li_over_noball.append(no_over)
            no_over = 0
            global c_runs
            global c
            canvas_lights.delete(c_runs)
            c_runs = canvas_lights.create_text(215, 200, text=str(c), font=('Ebrima 20 bold'))
            li_over_runs.append(c)
            c = 0

    func_1()


ball = 0
over = 0
li = []
li_over_me = []
ball_total = 0
#over_entry = 3


def func_1():
    global li
    global over
    global ball
    global ball_total
    global li_over
    global bowl
    # ball_stop = over_entry * 6
    c = str(ball_total)
    for i in range(len(c)):
        c_1 = c[i]
        li.append(c_1)
    if len(li) == 1:
        l4_ball.configure(text=li[0])
        li.remove(c_1)
    elif len(li) == 2:
        l3_ball.configure(text=li[0])
        l4_ball.configure(text=li[1])
        li.clear()
    elif len(li) == 3:
        l2_ball.configure(text=li[0])
        l3_ball.configure(text=li[1])
        l4_ball.configure(text=li[2])
        li.clear()
    elif len(li) == 4:
        l1_ball.configure(text=li[0])
        l2_ball.configure(text=li[1])
        l3_ball.configure(text=li[2])
        l4_ball.configure(text=li[3])
        li.clear()

    c_ov = str(over)
    for i in range(len(c_ov)):
        c_o = c_ov[i]
        li_over_me.append(c_o)
    if len(li_over_me) == 1:
        l3_ov.configure(text=li_over_me[0])
        li_over_me.remove(c_o)
    elif len(li_over_me) == 2:
        l2_ov.configure(text=li_over_me[0])
        l3_ov.configure(text=li_over_me[1])
        li_over_me.clear()
    elif len(li_over_me) == 3:
        l1_ov.configure(text=li_over_me[0])
        l2_ov.configure(text=li_over_me[1])
        l3_ov.configure(text=li_over_me[2])
        li_over_me.clear()


opener_sum = 0
non_striker_sum = 0
ball_opener_count = 0
ball_non_count = 0


def submit_enteries():
    global ball_total
    global ball_stop
    global ball_stop_1
    global count
    ball_stop = over_entry * 6
    if play1_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "YOU HAVE NOT SELECTED YOUR PLAYER NAME")
    elif play2_var.get() == "'PLAYER NAME'":
        messagebox.showerror("ERROR", "YOU HAVE NOT SELECTED YOUR PLAYER NAME")

    else:
        global bowl

        global l1_get
        global l2_get

        global opener
        global non_striker

        global l1
        global l2

        global over
        global canvas_lights

        opener = run_1.get()
        non_striker = run_2.get()
        global first_inn

        if "*" in l1_get:
            global ball_opener_count
            ball_opener_count = ball_opener_count + 1
            global c2_lights
            canvas_lights.delete(c2_lights)
            c2_lights = canvas_lights.create_text(90, 100, text="( " + str(ball_opener_count) + " )",
                                                  font=('Ebrima 15 bold'))
        elif "*" in l2_get:
            global ball_non_count
            ball_non_count = ball_non_count + 1
            global c3_lights
            canvas_lights.delete(c3_lights)
            c3_lights = canvas_lights.create_text(400, 100, text="( " + str(ball_non_count) + " )",
                                                  font=('Ebrima 15 bold'))

        check_entry()

        if ball_total == ball_stop:
            if first_inn.cget("text") == "SECOND INNINGS":
                end_match()
            else:
                end()
        elif count == 10:
            if first_inn.cget("text") == "SECOND INNINGS":
                end_match()
            else:
                end()
        else:
            if opener == 0 and non_striker == 0:
                l1_get = l1.cget("text")
                l2_get = l2.cget("text")
                over_strike()
                l1.grid(row=18, column=0)
                l2.grid(row=20, column=0)

            global opener_sum
            opener_sum = opener + opener_sum

            global non_striker_sum
            non_striker_sum = non_striker + non_striker_sum

            if opener != 0:
                if opener % 2 == 0:
                    l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
                elif opener % 2 != 0:
                    l1 = Label(board_root, text="PLAYER I   ", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II *", fg="black", font=('Ebrima 14 bold'))
                l1_get = l1.cget("text")
                l2_get = l2.cget("text")
                over_strike()
                l1.grid(row=18, column=0)
                l2.grid(row=20, column=0)

            if non_striker != 0:
                if non_striker % 2 == 0:
                    l1 = Label(board_root, text="PLAYER I   ", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II *", fg="black", font=('Ebrima 14 bold'))
                elif non_striker % 2 != 0:
                    l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
                    l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
                l1_get = l1.cget("text")
                l2_get = l2.cget("text")
                over_strike()
                l1.grid(row=18, column=0)
                l2.grid(row=20, column=0)

            board()
            if over != 0:
                global a

                run_rate = (a / ball_total) * 6
                f = round(run_rate, 2)
                global c_lights
                canvas_lights.delete(c_lights)
                c_lights = canvas_lights.create_text(120, 300, text=str(f), font=('Courier 20 bold'), fill="blue")

                global c_lights_1
                canvas_lights.delete(c_lights_1)
                projected_score = f * (over_entry)
                g = round(projected_score)
                c_lights_1 = canvas_lights.create_text(360, 300, text=str(g), font=('Courier 20 bold'), fill="blue")

            global y
            global c2_lights_1
            canvas_lights.delete(c2_lights_1)
            c2_lights_1 = canvas_lights.create_text(90, 70, text=y + " " + "'" + str(opener_sum) + "'",
                                                    font=('Ebrima 15 bold'))
            global y_1
            global c2_lights_2
            canvas_lights.delete(c2_lights_2)
            c2_lights_2 = canvas_lights.create_text(400, 70, text=y_1 + " " + "'" + str(non_striker_sum) + "'",
                                                    font=('Ebrima 15 bold'))
            run_1.set(0)
            run_2.set(0)


def end():
    global opener_sum
    global non_striker_sum
    global opener_sum
    global non_striker_sum
    global ball_opener_count
    global ball_non_count
    messagebox.showinfo("INNINGS",
                        "YOUR ' FIRST INNINGS ' ARE OVER, YOUR ENTRIES ARE SUCCESSFULLY STORED, THE BOARD IS READY FOR ' SECOND INNINGS ' , JUST SELECT YOUR PLAYER NAMES")
    global bat_team_l
    global bowl_team_l
    global li_bowl
    global li_bat
    global bat_main
    global bowl_main
    global first_inn
    first_inn.configure(text="SECOND INNINGS")
    bat_team_l.configure(text=bowl_main)
    bowl_team_l.configure(text=bat_main)

    if play1_var.get() != "'PLAYER NAME'":
        li_batsman_name.append(play1_var.get())
        li_ball_played.append(ball_opener_count)

    if play2_var.get() != "'PLAYER NAME'":
        li_batsman_name.append(play2_var.get())
        li_ball_played.append(ball_non_count)

    if play1_var.get() != "'PLAYER NAME'":
        li_runs_scored.append(opener_sum)
    if play2_var.get() != "'PLAYER NAME'":
        li_runs_scored.append(non_striker_sum)

    drop_play_var = OptionMenu(board_root, play1_var, *li_bowl)
    drop_play_var.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    play1_var.set("'PLAYER NAME'")
    drop_play_var.grid(row=18, column=1, columnspan=2)
    drop_play_var_2 = OptionMenu(board_root, play2_var, *li_bowl)
    drop_play_var_2.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    play2_var.set("'PLAYER NAME'")
    drop_play_var_2.grid(row=20, column=1, columnspan=2)

    global end_bat_1
    end_bat_1 = li_bat + empty_list
    drop_down_bowl = OptionMenu(board_root, bowler_var, *end_bat_1)
    drop_down_bowl.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
    bowler_var.set("'PLAYER NAME'")
    drop_down_bowl.grid(row=10, column=1, columnspan=2, rowspan=2)
    # end_bat_1 = m_bowl
    li_bat = li_bowl

    l1_ov.configure(text="0")
    l2_ov.configure(text="0")
    l3_ov.configure(text="0")

    l1_ball.configure(text="0")
    l2_ball.configure(text="0")
    l3_ball.configure(text="0")
    l4_ball.configure(text="0")

    global t1
    global t2
    global rec
    canvas_2.delete(t1)
    canvas_2.delete(t2)
    canvas_2.delete(rec)

    t1 = canvas_2.create_text(760, 30,
                              text="YOUR FIRST INNINGS ARE OVER , PLEASE CONTINUE BY SELECTING YOUR PLAYER'S NAME FOR FIRST OVER AND AFTER SELECTING CLICK ON 'START'",
                              font=('Times 15 bold'))

    Button(board_root, text="OK", width=5, bg="light blue", command=error_1, fg="black",
           font=('Helvetica 10 bold')).grid(row=18, column=3)
    Button(board_root, text="OK", width=5, bg="light blue", command=error_1, fg="black",
           font=('Helvetica 10 bold')).grid(row=20, column=3)
    Button(board_root, text="WIDE / NO BALL", bg="orange", fg="black", padx=20, pady=20, font=('Helvetica 15 bold'),
           command=out_1_error).grid(row=14, column=2, columnspan=6)
    Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=end_start_2,
           font=('Helvetica 10 bold')).grid(row=10, column=3, rowspan=2)
    Button(board_root, text="WICKET", bg="RED", fg="white", padx=20, pady=20, font=('Helvetica 15 bold'),
           command=out_1_error).grid(row=14, column=7, columnspan=3)
    Button(board_root, text="START MATCH", bg="VIOLET", fg="black", padx=15, pady=20, font=('Helvetica 15 bold'),
           command=error).grid(row=22, column=7, columnspan=3, rowspan=8)

    global l1
    global l2
    l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
    l2 = Label(board_root, text="PLAYER II  ", fg="black", font=('Ebrima 14 bold'))
    l1.grid(row=18, column=0)
    l2.grid(row=20, column=0)
    global l1_get
    global l2_get
    l1_get = "*"
    l2_get = " "

    global canvas_runs
    global canvas_wickets
    global canvas_overs
    global canvas
    canvas.delete(canvas_runs)
    canvas.delete(canvas_wickets)
    canvas.delete(canvas_overs)

    canvas_runs = canvas.create_text(160, 70, text="0", fill="black", font=('Helvetica 70 bold'))
    canvas_wickets = canvas.create_text(343, 70, text="0", fill="black", font=('Helvetica 70 bold'))
    canvas_overs = canvas.create_text(250, 190, text="0.0", fill="black", font=('Helvetica 70 bold'))

    global c1_lights
    global c2_lights
    global c2_lights_1
    global c2_lights_2
    global c3_lights
    global c_runs
    global c_wicket
    global c_lights
    global c_lights_1
    global canvas_lights

    canvas_lights.delete(c1_lights)
    canvas_lights.delete(c2_lights)
    canvas_lights.delete(c2_lights_1)
    canvas_lights.delete(c2_lights_2)
    canvas_lights.delete(c3_lights)
    canvas_lights.delete(c_runs)
    canvas_lights.delete(c_wicket)
    canvas_lights.delete(c_lights)
    canvas_lights.delete(c_lights_1)

    c1_lights = canvas_lights.create_text(242, 20, text="'name' " + " WILL BE BOWLING FOR THIS OVER",
                                          font=('Consolas 15 bold'), fill="blue")
    c2_lights = canvas_lights.create_text(90, 100, text="'balls played'", font=('Ebrima 15 bold'))
    c2_lights_1 = canvas_lights.create_text(90, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
    c2_lights_2 = canvas_lights.create_text(400, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
    c3_lights = canvas_lights.create_text(400, 100, text="'balls played'", font=('Ebrima 15 bold'))
    c_runs = canvas_lights.create_text(215, 200, text=" 0 ", font=('Ebrima 20 bold'))
    c_wicket = canvas_lights.create_text(285, 200, text=" 0 ", font=('Ebrima 20 bold'))
    c_lights = canvas_lights.create_text(120, 300, text="'0.0'", font=('Courier 20 bold'), fill="blue")
    c_lights_1 = canvas_lights.create_text(360, 300, text="'0'", font=('Courier 20 bold'), fill="blue")
    global a
    global c_target_1
    global ball_total
    c_target_1 = canvas_3.create_text(320, 35, text="TEAM NEEDS : " + str(a + 1) + " RUNS IN " + str(
        ball_total) + " BALLS TO WIN",
                                      font="TIMES 20 bold")
    global c
    global count
    global ball
    global over
    global ball_stop_1
    global target
    global wide_over
    global no_over
    wide_over = 0
    no_over = 0
    ball_stop_1 = over_entry * 6
    ball_opener_count = 0
    ball_non_count = 0
    ball_total = 0
    ball = 0
    over = 0
    #li_runs_scored.append(opener_sum)
    opener_sum = 0
    #li_runs_scored.append(non_striker_sum)
    non_striker_sum = 0
    target = a
    a = 0
    #li_over_runs.append(c)
    c = 0
    count = 0

    li_over_number.append("end")
    li_bowlers_name.append("end")
    li_over_runs.append("end")
    li_over_out.append("end")
    li_over_noball.append("end")
    li_over_wide.append("end")
    li_batsman_name.append("end")
    li_runs_scored.append("end")
    li_ball_played.append("end")
    li_mode_of_dismayal.append("end")

def end_match():
    global ball_opener_count
    global ball_non_count
    global opener_sum
    global non_striker_sum
    if play1_var.get() != "'PLAYER NAME'":
        li_batsman_name.append(play1_var.get())
        li_ball_played.append(ball_opener_count)
    if play2_var.get() != "'PLAYER NAME'":
        li_batsman_name.append(play2_var.get())
        li_ball_played.append(ball_non_count)

    if play1_var.get() != "'PLAYER NAME'":
        li_runs_scored.append(opener_sum)
    if play2_var.get() != "'PLAYER NAME'":
        li_runs_scored.append(non_striker_sum)
    messagebox.showinfo("MATCH IS OVER", "YOUR MATCH IS OVER, MATCH IS SAVED SUCCESSFULLY")
    board_root.destroy()



board_root = Tk()
board_root.geometry("2000x1000")
board_root.maxsize(1530, 1000)
board_root.title("PROJECT SCOREBOARD")
# VARIABLES
run_1 = IntVar()
run_2 = IntVar()
diss_1 = IntVar()
diss_2 = IntVar()
diss_3 = IntVar()
diss_4 = IntVar()
diss_5 = IntVar()
others = StringVar()
bowler_var = StringVar()
play1_var = StringVar()
play2_var = StringVar()


canvas_2 = Canvas(board_root, width=1525, height=60, bg="pink")
t1 = canvas_2.create_text(760, 30,
                          text="WELCOME TO OUR SCOREBOARD , PLEASE CONTINUE BY SELECTING YOUR PLAYER'S NAME FOR FIRST OVER AND AFTER SELECTING CLICK ON 'START'",
                          font=('Times 15 bold'))
canvas_2.grid(row=1, column=0, columnspan=20, rowspan=2)

bat_team_l = Label(board_root, text = bat_main, padx=10, pady=10, fg="black", font=('Helvetica 15 bold'))
bowl_team_l = Label(board_root, text = bowl_main, padx=10, pady=10, fg="black", font=('Helvetica 15 bold'))
bat_team_l.place(x=350,y=420)
bowl_team_l.place(x=350,y=120)


l1_get = "*"
l2_get = " "

var_1 = IntVar()
var_2 = IntVar()

#                                     ..............PLAYERS NAME..............
li_bowl = ["Ruturaj Gaikwad",
           "Shikhar Dhawan",
           "Shreyas Iyer",
           "Suryakumar Yadav",
           "Virat Kohli",
           "Ravichandran Ashwin",
           "Venkatesh Iyer",
           "Ishan Kishan",
           "KL Rahul",
           "Rishabh Pant",
           "Bhuvneshwar Kumar"]
li_1 = ["'PLAYER NAMES'"]

li_2 = ["'PLAYER NAMES'"]
li_bat = ["Asif Ali",
          "Babar Azam",
          "Fakhar Zaman",
          "Haider Ali",
          "Khushdil Shah",
          "Iftikhar Ahmed",
          "Mohammad Nawaz",
          "Shadab Khan",
          "Mohammad Rizwan",
          "Haris Rauf",
          "Mohammad Hasnain",
          "Mohammad Wasim"]

# CANVAS NO 2

canvas_1 = Canvas(board_root, width=520, height=270, bg="black")
canvas = Canvas(board_root, width=500, height=250, bg="SpringGreen2")
canvas_runs = canvas.create_text(160, 70, text="0", fill="black", font=('Helvetica 70 bold'))
canvas.create_text(250, 70, text="-", fill="black", font=('Helvetica 70 bold'))
canvas_wickets = canvas.create_text(343, 70, text="0", fill="black", font=('Helvetica 70 bold'))
canvas_overs = canvas.create_text(250, 190, text="0.0", fill="black", font=('Helvetica 70 bold'))
canvas_1.grid(row=7, column=11, columnspan=10, rowspan=8)
canvas.grid(row=7, column=11, columnspan=10, rowspan=8)

Label(board_root, text="", padx=14, pady=10).grid(row=3, column=0)

#                                   .............BOWLING TEAM...............
Label(board_root, text="BOWLING ", padx=25, pady=15, bg="light blue", fg="black", relief=SUNKEN,
      font=('Algerian 20 bold')).grid(row=7, column=0, columnspan=3)
Label(board_root, text="BOWLER NAME", fg="black", font=('Helvetica 14 bold')).grid(row=10, column=0, rowspan=2)

# li_bowl = ["bhai change krr lio"]
drop_down_bowl = OptionMenu(board_root, bowler_var, *li_bowl)
drop_down_bowl.config(width=20, bg='pink', font=('TimesNewRoman 10 bold'))
bowler_var.set("'SELECT'")
drop_down_bowl.grid(row=10, column=1, columnspan=2, rowspan=2)
Button(board_root, text="OK", width=5, bg="light blue", fg="black", command=start_2, font=('Helvetica 10 bold')).grid(row=10,column=3, rowspan=2)


c_bore = Canvas(board_root, height=93, width=187, bg="light blue")
c_bore.create_text(94, 22, text="OVER", font='Times 20 bold')
c_bore.configure(highlightthickness=0)
c_bore.grid(row=8, column=4, columnspan=5, rowspan=4)

l1_ov = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l1_ov.grid(row=10, column=4, columnspan=4, rowspan=2)
l2_ov = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l2_ov.grid(row=10, column=4, columnspan=5, rowspan=2)
l3_ov = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l3_ov.grid(row=10, column=4, columnspan=6, rowspan=2)

c_bore_ball = Canvas(board_root, height=93, width=187, bg="light blue")
c_bore_ball.create_text(75, 22, text="BALLS", font='Times 20 bold')
c_bore_ball.configure(highlightthickness=0)
c_bore_ball.grid(row=8, column=6, columnspan=6, rowspan=4)

l1_ball = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l1_ball.grid(row=10, column=7, columnspan=2, rowspan=2)
l2_ball = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l2_ball.grid(row=10, column=7, columnspan=3, rowspan=2)
l3_ball = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l3_ball.grid(row=10, column=7, columnspan=4, rowspan=2)
l4_ball = Label(board_root, text="0", font=('Helvetica 25 bold'), relief=SUNKEN, padx=5)
l4_ball.grid(row=10, column=7, columnspan=5, rowspan=2)

# BUTTONS...............

Canvas_type = Canvas(height=50, width=280, bg="light green")
Canvas_type.create_text(140, 15, text="CLICK ON THE RESPECTIVE TYPE : ", font=('Helvetica 11 bold'))
Canvas_type.create_text(140, 40, text="(IF ANY)", font=('Helvetica 13 bold'))
Canvas_type.grid(row=14, column=0, columnspan=3)

Button(board_root, text="WIDE / NO BALL", bg="orange", fg="black", padx=20, pady=20, font=('Helvetica 15 bold'),
       command=out_1_error).grid(row=14, column=2, columnspan=6)

#                          * BATTING TEAM DETAILS **
Label(board_root, text="").grid(row=15, column=0)
Label(board_root, text="BATTING ", padx=25, pady=15, bg="light blue", fg="black", relief=SUNKEN,
      font=('Algerian 20 bold')).grid(row=16, column=0, columnspan=3)

l1 = Label(board_root, text="PLAYER I  *", fg="black", font=('Ebrima 14 bold'))
l1.grid(row=18, column=0)
l2 = Label(board_root, text="PLAYER II ", fg="black", font=('Ebrima 14 bold'))
l2.grid(row=20, column=0)

drop_play1 = OptionMenu(board_root, play1_var, *li_bat)
drop_play1.config(width=30, bg="pink", font=('TimesNewRoman 10 bold'))
play1_var.set("'SELECT'")
drop_play1.grid(row=18, column=1, columnspan=2)
drop_play2 = OptionMenu(board_root, play2_var, *li_bat)
drop_play2.config(width=30, bg="pink", font=('TimesNewRoman 10 bold'))
play2_var.set("'SELECT'")
drop_play2.grid(row=20, column=1, columnspan=2)

Button(board_root, text="OK", width=5, bg="light blue", command=error_1, fg="black", font=('Helvetica 10 bold')).grid(row=18, column=3)
Button(board_root, text="OK", width=5, bg="light blue", command=error_1, fg="black", font=('Helvetica 10 bold')).grid(row=20, column=3)

Label(board_root, text="RUNS MADE PER PLAYER", fg="black", bg="light green", font=('Helvetica 15 bold')).grid(row=16,column=5,columnspan=6,rowspan=3)

Label(board_root, text="RUN MADE BY P1", fg="black", font=('Helvetica 13 ')).grid(row=18, column=3, columnspan=7)
Label(board_root, text="RUN MADE BY P2", fg="black", font=('Helvetica 13 ')).grid(row=20, column=3, columnspan=7)

run_1_entry = Entry(board_root, textvariable=run_1, font=1, width=15).grid(row=18, column=7, columnspan=5)
run_2_entry = Entry(board_root, textvariable=run_2, font=1, width=15).grid(row=20, column=7, columnspan=5)

Label(board_root, text="").grid(row=21, column=0)

Button(board_root, text="WICKET", bg="RED", fg="white", padx=20, pady=20, font=('Helvetica 15 bold'),
       command=out_1_error).grid(row=14, column=7, columnspan=3)
Button(board_root, text="START MATCH", bg="VIOLET", fg="black", padx=15, pady=20, font=('Helvetica 15 bold'),
       command=error).grid(row=22, column=7, columnspan=3, rowspan=8)
# CANVAS
canvas_3 = Canvas(board_root, width=650, height=70, bg="#ffaec8")
canvas_3.grid(row=22, column=0, columnspan=7, rowspan=8)

# CANVAS NUMBER 3
canvas_high = Canvas(board_root, width=520, height=360, bg="purple")
canvas_lights = Canvas(board_root, width=500, height=340, bg="pink")
c1_lights = canvas_lights.create_text(242, 20, text="'name' " + " WILL BE BOWLING FOR THIS OVER",font=('Consolas 15 bold'), fill="blue")
c2_lights = canvas_lights.create_text(90, 100, text="'balls played'", font=('Ebrima 15 bold'))
c2_lights_1 = canvas_lights.create_text(90, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
c2_lights_2 = canvas_lights.create_text(400, 70, text="'name'" + " " + "'runs'", font=('Ebrima 15 bold'))
c3_lights = canvas_lights.create_text(400, 100, text="'balls played'", font=('Ebrima 15 bold'))
c4_lights = canvas_lights.create_text(245, 160, text="SCORE MADE IN LAST OVER", font=('Algerian 17 bold'), fill="red")
c_runs = canvas_lights.create_text(215, 200, text=" 0 ", font=('Ebrima 20 bold'))
c_slash = canvas_lights.create_text(250, 200, text="  /  ", font=('Ebrima 20 bold'))
c_wicket = canvas_lights.create_text(285, 200, text=" 0 ", font=('Ebrima 20 bold'))
c5_lights = canvas_lights.create_text(120, 270, text="RUN RATE", font=('ComicSansMS 15 bold'))
c6_lights = canvas_lights.create_text(360, 270, text="PROJECTED SCORE", font=('ComicSansMS 15 bold'))
c_lights = canvas_lights.create_text(120, 300, text="'0.0'", font=('Courier 20 bold'), fill="blue")
c_lights_1 = canvas_lights.create_text(360, 300, text="'0'", font=('Courier 20 bold'), fill="blue")
c_rect_1 = canvas_lights.create_rectangle(70, 140, 430, 220)
canvas_high.grid(row=16, column=11, columnspan=10, rowspan=14)
canvas_lights.grid(row=16, column=11, columnspan=10, rowspan=14)

board_root.mainloop()