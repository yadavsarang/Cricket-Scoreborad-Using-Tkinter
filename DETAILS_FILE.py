import xlsxwriter
from tkinter import *
from PIL import Image,ImageTk
from DETAILS import list_matchdetails,list_locationdetails_C,list_teamdetails, li_toss, li_1, li_2, bat, bowl, li, li_1_sub, li_2_sub
import os
outwork = xlsxwriter.Workbook("DETAILS.xlsx")
score_sheet = outwork.add_worksheet()

name = ["TYPE OF MATCH : ","DATE OF MATCH : ","TIME OF MATCH : ","NAME OF TEAMS :"]


score_sheet.write(0,14,"TEAM I")
score_sheet.write(0,16,"TEAM II")

score_sheet.write(1,0, name[0])
score_sheet.write(1,4, name[1])
score_sheet.write(1,8, name[2])
score_sheet.write(1,12, name[3])

score_sheet.write(1,2, list_matchdetails[0])
score_sheet.write(1,6, list_matchdetails[1])
score_sheet.write(1,10, list_matchdetails[2])
score_sheet.write(1,14, list_matchdetails[3])
score_sheet.write(1,16, list_matchdetails[4])

score_sheet.write(3,0,"         COUNTRY : ")
score_sheet.write(3,4,"STATE : ")
score_sheet.write(3,8,"CITY : ")
score_sheet.write(3,12,"CODE : ")
score_sheet.write(3,15,"VENUE : ")

score_sheet.write(3,2, list_locationdetails_C[2])
score_sheet.write(3,5, list_locationdetails_C[3])
score_sheet.write(3,9, list_locationdetails_C[4])
score_sheet.write(3,13, list_locationdetails_C[5])
score_sheet.write(3,16, list_locationdetails_C[1].upper())
score_sheet.write(4,0,"------------------------------------------------------------------------------------------------------------------"
                     "---------------------------------------------------------------------------------------------------------------------")
name_1 = ["TEAM I : ", "TEAM II : ", "CAPTAIN NAME => " , "COACH NAME => "]
score_sheet.write(5,4,name_1[0])
score_sheet.write(7,4,name_1[1])
score_sheet.write(5,5,name_1[3])
score_sheet.write(7,5,name_1[3])
score_sheet.write(5,10,name_1[2])
score_sheet.write(7,10,name_1[2])

score_sheet.write(5,7,list_teamdetails[0])
score_sheet.write(7,7,list_teamdetails[1])
score_sheet.write(5,12,list_teamdetails[2])
score_sheet.write(7,12,list_teamdetails[3])

name_2 = ["TOSS IS WON BY ","AND THE TEAM CHOOSE TO"]
score_sheet.write(9,6,name_2[0] +"  " + "'" +li_toss[0] + "'" +"  "+ name_2[1] +"  "+ "'" + li_toss[1] + "'"  )

toss_won = li_toss[0]
toss_chose = li_toss[1]

li_1_main = li_1
li_2_main = li_2

over_entry = list_matchdetails[5]

bat_main = bat
bowl_main = bowl
if bat == li[0]:
    li_sub_bat = li_1_sub
    li_sub_bowl = li_2_sub
    li_bat = li_1_main
    li_bowl = li_2_main
if bat == li[1] :
    li_sub_bat = li_2_sub
    li_sub_bowl = li_1_sub
    li_bat = li_2_main
    li_bowl = li_1_main

outwork.close()

root_1 = Tk()
root_1.geometry("750x500")
root_1.maxsize(750,500)

def open():
    b = os.path.abspath("DETAILS.xlsx")
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
can_1.create_text(150,20,text="IF YOU WANT TO PROCEED TO " ,font = 'Times 12 bold')
can_1.create_text(150,40,text="'SCOREBOARD' , CLICK HERE" ,font = 'Times 12 bold')
can_arrow_1 = can_1.create_line(150, 50, 150, 98, arrow=LAST)
can_1.configure(highlightthickness=0)
can_1.grid(row=2,column=2,rowspan=2)

Button(root_1,text="OPEN YOUR FILE",width=15,padx=5,bg="GREEN",fg='white',font = 'Times 20 bold',command=open).grid(row=3,column=0,rowspan=2)
Button(root_1,text="CONTINUE",width=15,padx=5,bg="GREEN",fg='white',font = 'Times 20 bold',command=destroy).grid(row=3,column=2,rowspan=2)


root_1.mainloop()