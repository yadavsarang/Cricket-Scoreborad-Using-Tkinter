from tkinter import *
import xlsxwriter
from latest import li_over_number, li_bowlers_name, li_over_runs, li_over_out, li_over_noball, li_over_wide, li_batsman_name, li_ball_played, li_runs_scored, li_mode_of_dismayal
import os
from PIL import Image, ImageTk

# SETTING INDEX FOR end IN BOWLING

end_index_over_num = li_over_number.index("end")
end_index_bowler_name = li_bowlers_name.index("end")
end_index_over_runs = li_over_runs.index("end")
end_index_over_out = li_over_out.index("end")
end_index_over_wide = li_over_wide.index("end")
end_index_over_no_ball = li_over_noball.index("end")

# LISTS FOR FIRST INNINGS OF BOWLING
li_over_number_1 = li_over_number[0:end_index_over_num]
li_bowlers_name_1 = li_bowlers_name[0:end_index_bowler_name]
li_over_runs_1 = li_over_runs[0:end_index_over_runs]
li_over_out_1 = li_over_out[0:end_index_over_out]
li_over_wide_1 = li_over_wide[0:end_index_over_wide]
li_over_noball_1 = li_over_noball[0:end_index_over_no_ball]

# LISTS FOR SECOND INNINGS OF BOWLING
li_over_number_2 = li_over_number[end_index_over_num+1:end_index_over_num + len(li_over_number)]
li_bowlers_name_2 = li_bowlers_name[end_index_bowler_name+1:end_index_bowler_name + len(li_bowlers_name)]
li_over_runs_2 = li_over_runs[end_index_over_runs+1:end_index_over_runs + len(li_over_runs)]
li_over_out_2 = li_over_out[end_index_over_out+1:end_index_over_out + len(li_over_out)]
li_over_wide_2 = li_over_wide[end_index_over_wide+1:end_index_over_wide + len(li_over_wide)]
li_over_noball_2 = li_over_noball[end_index_over_no_ball+1:end_index_over_no_ball + len(li_over_noball)]

# CREATING WORKBOOK
outwork = xlsxwriter.Workbook("Cricket Scoreboard.xlsx")


# BOWLING


# BOWLING SHEETS
outsheet_bowl_1 = outwork.add_worksheet("Bowling Sheet 1")
outsheet_bowl_2 = outwork.add_worksheet("Bowling Sheet 2")

# FORMATTING
cell_format = outwork.add_format()
cell_format.set_bold()
cell_format.set_font_color('red')
cell_format.set_underline()
cell_format.set_italic()
cell_format = outwork.add_format({'bold':True, 'font_color':'red', 'underline':True, 'italic':True})

# FIRST INNINGS BOWLING
li_bowl_1 = ["Over Number", "Bowler's Name for this over", "Runs made in his over", "Wicket taken in this over", "No. of Wide balls", "No. of No Balls "]

outsheet_bowl_1.write(0, 0, li_bowl_1[0], cell_format)
outsheet_bowl_1.write(0, 2, li_bowl_1[1], cell_format)
outsheet_bowl_1.write(0, 6, li_bowl_1[2], cell_format)
outsheet_bowl_1.write(0, 9, li_bowl_1[3], cell_format)
outsheet_bowl_1.write(0, 12, li_bowl_1[4], cell_format)
outsheet_bowl_1.write(0, 15, li_bowl_1[5], cell_format)

a = 2

for i_1 in range(len(li_over_number_1)):
    outsheet_bowl_1.write(a, 0, li_over_number_1[i_1])
    a += 2

b = 2
for i_2 in range(len(li_bowlers_name_1)):
    outsheet_bowl_1.write(b, 2, li_bowlers_name_1[i_2])
    b += 2

c = 2
for i_3 in range(len(li_over_runs_1)):
    outsheet_bowl_1.write(c, 6, li_over_runs_1[i_3])
    c += 2

d = 2
for i_4 in range(len(li_over_out_1)):
    outsheet_bowl_1.write(d, 9, li_over_out_1[i_4])
    d += 2

e = 2
for i_5 in range(len(li_over_wide_1)):
    outsheet_bowl_1.write(e, 12, li_over_wide_1[i_5])
    e += 2

f = 2
for i_6 in range(len(li_over_noball_1)):
    outsheet_bowl_1.write(f, 15, li_over_noball_1[i_6])
    f += 2

# SECOND INNINGS BOWLING

li_bowl_2 = ["Over Number", "Bowler's Name for this over", "Runs made in his over", "Wicket taken in this over", "No. of Wide balls", "No. of No Balls "]

outsheet_bowl_2.write(0, 0, li_bowl_2[0], cell_format)
outsheet_bowl_2.write(0, 2, li_bowl_2[1], cell_format)
outsheet_bowl_2.write(0, 6, li_bowl_2[2], cell_format)
outsheet_bowl_2.write(0, 9, li_bowl_2[3], cell_format)
outsheet_bowl_2.write(0, 12, li_bowl_2[4], cell_format)
outsheet_bowl_2.write(0, 15, li_bowl_2[5], cell_format)

a_1 = 2

for i1 in range(len(li_over_number_2)):
    outsheet_bowl_2.write(a_1, 0, li_over_number_2[i1])
    a_1 += 2

b_1 = 2
for i2 in range(len(li_bowlers_name_2)):
    outsheet_bowl_2.write(b_1, 2, li_bowlers_name_2[i2])
    b_1 += 2

c_1 = 2
for i3 in range(len(li_over_runs_2)):
    outsheet_bowl_2.write(c_1, 6, li_over_runs_2[i3])
    c_1 += 2

d_1 = 2
for i4 in range(len(li_over_out_2)):
    outsheet_bowl_2.write(d_1, 9, li_over_out_2[i4])
    d_1 += 2

e_1 = 2
for i5 in range(len(li_over_wide_2)):
    outsheet_bowl_2.write(e_1, 12, li_over_wide_2[i5])
    e_1 += 2

f_1 = 2
for i6 in range(len(li_over_noball_2)):
    outsheet_bowl_2.write(f_1, 15, li_over_noball_2[i6])
    f_1 += 2



# SETTING INDEX FOR end IN BATTING
end_index_batsman_name = li_batsman_name.index("end")
end_index_ball_played = li_ball_played.index("end")
end_index_runs_scored = li_runs_scored.index("end")
# end_index_fours = li_fours.index("end")
# end_index_sixes = li_sixes.index("end")
end_index_mode_of_dismayal = li_mode_of_dismayal.index("end")

# LISTS FOR FIRST INNING FOR BATTING
li_batsman_name_1 = li_batsman_name[0:end_index_batsman_name]
li_runs_scored_1 = li_runs_scored[0:end_index_runs_scored]
li_ball_played_1 = li_ball_played[0:end_index_ball_played]
# li_fours_1 = li_fours[0:end_index_fours]
# li_sixes_1 = li_sixes[0:end_index_sixes]
li_mode_of_dismayal_1 = li_mode_of_dismayal[0:end_index_mode_of_dismayal]

# LISTS FOR SECOND INNING FOR BATTING
li_batsman_name_2 = li_batsman_name[end_index_batsman_name+1:end_index_batsman_name + len(li_batsman_name)]
li_runs_scored_2 = li_runs_scored[end_index_runs_scored+1:end_index_runs_scored + len(li_runs_scored)]
li_ball_played_2 = li_ball_played[end_index_ball_played+1:end_index_ball_played + len(li_ball_played)]
# li_fours_2 = li_fours[end_index_fours+1:end_index_fours + len(li_fours)]
# li_sixes_2 = li_sixes[end_index_sixes+1:end_index_sixes + len(li_sixes)]
li_mode_of_dismayal_2 = li_mode_of_dismayal[end_index_mode_of_dismayal+1:end_index_mode_of_dismayal + len(li_mode_of_dismayal)]


# BATTING


# BATTING SHEETS
outsheet_bat_1 = outwork.add_worksheet("Batting Sheet 1")
outsheet_bat_2 = outwork.add_worksheet("Batting Sheet 2")

# FORMATTING
cell_format_1 = outwork.add_format()
cell_format_1.set_bold()
cell_format_1.set_font_color('blue')
cell_format_1.set_underline()
cell_format_1.set_italic()
cell_format_1 = outwork.add_format({'bold':True, 'font_color':'blue', 'underline':True, 'italic':True})

# BATTING FOR FIRST INNINGS

li_bat_1 = ["Batsman Name", "Runs Scored", "Balls Played", "Mode of Dismayal"]
outsheet_bat_1.write(0, 0, li_bat_1[0], cell_format_1)
outsheet_bat_1.write(0, 2, li_bat_1[1], cell_format_1)
outsheet_bat_1.write(0, 5, li_bat_1[2], cell_format_1)
outsheet_bat_1.write(0, 8, li_bat_1[3], cell_format_1)
# outsheet_bat_1.write(0, 11, li_bat_1[4], cell_format_1)
# outsheet_bat_1.write(0, 14, li_bat_1[5], cell_format_1)

a_2 = 2
for j_1 in range(len(li_batsman_name_1)):
    outsheet_bat_1.write(a_2, 0, li_batsman_name_1[j_1])
    a_2 += 2

b_2 = 2
for j_2 in range(len(li_runs_scored_1)):
    outsheet_bat_1.write(b_2, 2, li_runs_scored_1[j_2])
    b_2 += 2

c_2 = 2
for j_3 in range(len(li_ball_played_1)):
    outsheet_bat_1.write(c_2, 5, li_ball_played_1[j_3])
    c_2 += 2

d_2 = 2
for j_4 in range(len(li_mode_of_dismayal_1)):
    outsheet_bat_1.write(d_2, 8, li_mode_of_dismayal_1[j_4])
    d_2 += 2

# e_2 = 2
# for j_5 in range(len(li_sixes_1)):
#     outsheet_bat_1.write(e_2, 11, li_sixes_1[j_5])
#     e_2 += 2
#
# f_2 = 2
# for j_6 in range(len(li_mode_of_dismayal_1)):
#     outsheet_bat_1.write(f_2, 14, li_mode_of_dismayal_1[j_6])
#     f_2 += 2

# BATTING FOR SECOND INNINGS

li_bat_2 = ["Batsman Name", "Runs Scored", "Balls Played", "Mode of Dismayal"]
outsheet_bat_2.write(0, 0, li_bat_2[0], cell_format_1)
outsheet_bat_2.write(0, 2, li_bat_2[1], cell_format_1)
outsheet_bat_2.write(0, 5, li_bat_2[2], cell_format_1)
outsheet_bat_2.write(0, 8, li_bat_2[3], cell_format_1)
# outsheet_bat_2.write(0, 11, li_bat_2[4], cell_format_1)
# outsheet_bat_2.write(0, 14, li_bat_2[5], cell_format_1)

a2 = 2
for j1 in range(len(li_batsman_name_2)):
    outsheet_bat_2.write(a2, 0, li_batsman_name_2[j1])
    a2 += 2

b2 = 2
for j2 in range(len(li_runs_scored_2)):
    outsheet_bat_2.write(b2, 2, li_runs_scored_2[j2])
    b2 += 2

c2 = 2
for j3 in range(len(li_ball_played_2)):
    outsheet_bat_2.write(c2, 5, li_ball_played_2[j3])
    c2 += 2

d2 = 2
for j4 in range(len(li_mode_of_dismayal_2)):
    outsheet_bat_2.write(d2, 8, li_mode_of_dismayal_2[j4])
    d2 += 2

# e2 = 2
# for j5 in range(len(li_sixes_2)):
#     outsheet_bat_1.write(e2, 11, li_sixes_2[j5])
#     e2 += 2
#
# f2 = 2
# for j6 in range(len(li_mode_of_dismayal_2)):
#     outsheet_bat_1.write(f2, 14, li_mode_of_dismayal_2[j6])
#     f2 += 2
print(li_ball_played_1)
print(li_ball_played_2)
outwork.close()

root_1 = Tk()
root_1.geometry("750x500")
root_1.maxsize(750,500)

def open():
    b = os.path.abspath("MATCH.xlsx")
    os.system(b)
def destroy():
    root_1.destroy()
image = Image.open("root_1_image.jpg")
img = ImageTk.PhotoImage(image)
label = Label(image=img)
label.grid(row=0,column=0,columnspan=3,rowspan=5)

Label(root_1,text="YOUR DETAILS ARE SUCCESSFULLY STORED",bg="light blue",relief=SUNKEN, font = 'Times 20 bold').grid(row=0,column=0,columnspan=3)

can = Canvas(root_1,width=300,height=100,bg="springgreen2")
can.create_text(150,20,text="IF YOU WANT TO OPEN YOUR FILE ," ,font = 'Times 12 bold')
can.create_text(150,40,text="CLICK HERE" ,font = 'Times 12 bold')
can_arrow = can.create_line(150, 50, 150, 98, arrow=LAST)
can.configure(highlightthickness=0)
can.grid(row=2,column=0,rowspan=2)

can_1 = Canvas(root_1,width=300,height=100,bg="springgreen2")
can_1.create_text(150,20,text="IF YOU WANT TO CLOSE " ,font = 'Times 12 bold')
can_1.create_text(150,40,text="'SCOREBOARD' , CLICK HERE" ,font = 'Times 12 bold')
can_arrow_1 = can_1.create_line(150, 50, 150, 98, arrow=LAST)
can_1.configure(highlightthickness=0)
can_1.grid(row=2,column=2,rowspan=2)

Button(root_1,text="OPEN YOUR FILE",width=15,padx=5,bg="GREEN",fg='white',font = 'Times 20 bold',command=open).grid(row=3,column=0,rowspan=2)
Button(root_1,text="CLOSE",width=15,padx=5,bg="GREEN",fg='white',font = 'Times 20 bold',command=destroy).grid(row=3,column=2,rowspan=2)


root_1.mainloop()