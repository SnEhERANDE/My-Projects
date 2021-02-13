import tkinter as tk
import os 
from datetime import datetime 
from cryptocode import encrypt, decrypt
from random import randint
from tkinter import ttk

win = tk.Tk()

usernameis = ""
uname2 =  ""
dt = datetime.today()
t = dt.time()
d = dt.date()
date = d.strftime("%d/%m/%Y")
time = t.strftime("%I:%M:%S %p")
dtime = date+" "+time
# title for app
win.title("Login Manager")
win.configure(bg='#2E2E2E')

# base size 
win.geometry("500x500")


# Frames
start = tk.Frame(win, bg = "#2E2E2E")
signed = tk.Frame(win, bg = "#2E2E2E")
signeduser = tk.Frame(win, bg = "#2E2E2E")
create = tk.Frame(win, bg = "#2E2E2E")
createnewuser = tk.Frame(win, bg = "#2E2E2E")
successCreate = tk.Frame(win, bg = "#2E2E2E")
failedCreate = tk.Frame(win, bg = "#2E2E2E")
logs = tk.Frame(win,bg = "#2E2E2E", borderwidth = 0)
canvas = tk.Canvas(logs,bg = "#2E2E2E",width=480, height=520, bd=0,highlightthickness=0)
scrollbar = ttk.Scrollbar(logs, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas,bg = "#2E2E2E")
addleaveframe = tk.Frame(win, bg = "#2E2E2E")


if os.path.isfile("Log Public"):
    with open("Log Public","a") as f:
        f.close()
else:
    with open("Log Public","w") as f:
        f.write("WELCOME TO LOG MANAGEMENT\n")
        f.write("FILE CREATED AT ")
        f.write(dtime)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()

if os.path.isfile("usersprivate"):
    with open("usersprivate","a") as f:
        f.close()
else:
    with open("usersprivate","w") as f:
        f.write("USERNAMES\n")
        f.close()

if os.path.isfile("userpassdata"):
    with open("userpassdata","a") as f:
        
        f.close()
else:
    with open("userpassdata","w") as f:
        f.write("!!confidential!!\n")
        f.write("\n")
        f.close()

if os.path.isfile("userlogdata"):
    with open("userlogdata","a") as f:
        f.close()
else:
    with open("userlogdata","w") as f:
        f.close()

if os.path.isfile("Leaves"):
    with open("Leaves","a") as f:
        f.close()
else:
    with open("Leaves","w") as f:
        f.write("WELCOME TO LEAVES MANAGEMENT\n")
        f.write("FILE CREATED AT ")
        f.write(dtime)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()





# Functions
def nextscene():
    signed.place_forget()
    create.place(relwidth = 500, relheight = 500)
    return

def user(u,n,p):
    u = str(u)
    n = str(n)
    un = u+", "+n
    with open("usersprivate","r") as f:
        for line  in f:
            if un in line or u in line or n in line:
                create.place_forget()
                failedCreate.place(relwidth = 500, relheight = 500)
                win.after(10000,sucfai)
                return
        with open("usersprivate","a") as f:
            f.write("\n")
            f.write(un)
            f.close()
    usern = n
    userp = p
    randomnumber = str(randint(1,100)) 
    userdata = []
    usern = encrypt(usern,randomnumber)
    userp = encrypt(userp,randomnumber)
    userdata = [usern, userp, randomnumber]
    with open("userpassdata","a") as f:
        f.write(str(userdata))
        f.write("\n")
        f.close()
    create.place_forget()
    successCreate.place(relwidth = 500, relheight = 500)
    win.after(5000,sucfai)
    return

def user2(u,n,p):
    u = str(u)
    n = str(n)
    un = u+", "+n
    with open("usersprivate","r") as f:
        for line  in f:
            if un in line or u in line or n in line:
                create.place_forget()
                failedCreate.place(relwidth = 500, relheight = 500)
                win.after(10000,sucfai)
                return
        with open("usersprivate","a") as f:
            f.write("\n")
            f.write(un)
            f.close()
    usern = n
    userp = p
    randomnumber = str(randint(101,200)) 
    userdata = []
    usern = encrypt(usern,randomnumber)
    userp = encrypt(userp,randomnumber)
    userdata = [usern, userp, randomnumber]
    with open("userpassdata","a") as f:
        f.write(str(userdata))
        f.write("\n")
        f.close()
    create.place_forget()
    successCreate.place(relwidth = 500, relheight = 500)
    win.after(5000,sucfai)
    return

def nextscene2():
    createnewuser.place(relwidth = 500, relheight = 500)
    return

def createuser():
    newuse = newuser.get()
    newpas = newpass.get()
    unam = uname.get()
    if newuse != "" and newuse != " " and newpas != "" and newpas != " ": 
        user(unam,newuse,newpas)
        return

def createuser2():
    newuse2 = userentryname.get()
    newpas2 = userpassword.get()
    unam2 = nameofuser.get()
    if newuse2 != "" and newuse2 != " " and newpas2 != "" and newpas2 != " ": 
        user2(unam2,newuse2,newpas2)
        return
                        
def checkuser():
    user = entry1.get()
    password = entry2.get()
    with open("userpassdata","r") as f:
        for line in f:
            lst = line
            lst = lst.replace("'","")
            lst = lst.replace(" ","")
            lst=  lst.strip("[] \n")
            ls = lst.split(",")
            userdata = []
            print(ls)
            if ls != ['!!confidential!!']:
                usern = decrypt(ls[0],ls[2])
                userp = decrypt(ls[1],ls[2])
                userdata = [usern, userp, ls[2]]
                if userdata[0] == user and userdata[1] == password and int(ls[2]) <= 100:
                    start.place_forget()
                    with open("usersprivate","r") as f:
                        for line2 in f:
                            if user in line2:
                                uun = line2.split(",") 
                                uun.pop(-1)
                                un = ""
                                un = un.join(uun)
                                break
                    signed.place(relwidth = 500, relheight = 500)
                    sighendscreen(un,user)
                    return
                elif userdata[0] == user and userdata[1] == password and int(ls[2]) > 100:
                    start.place_forget()
                    with open("usersprivate","r") as f:
                        for line2 in f:
                            if user in line2:
                                uun = line2.split(",") 
                                uun.pop(-1)
                                un = ""
                                un = un.join(uun)
                                break
                    signeduser.place(relwidth = 500, relheight = 500)
                    sighendscreen2(un,user)
                    return
            else:
                    print("fail2")
    l5_1.place(anchor = "center",x = 250, y = 100)

def sighendscreen(name,uname):
    global usernameis
    global uname2
    usernameis = name
    uname2 = uname 
    namef["text"] = usernameis
    usern["text"] = uname2
    with open("userlogdata","r") as f:
        line = ""
        for l in f:
            if uname2 in l:
                line = l 
        if uname2 in line and "True" in line:
            loginbutton.place_forget()
            logoutbutton.place(anchor = "center",x = 300,y = 400)
            f.close()
        elif uname2 in line and "False" in line:
            logoutbutton.place_forget() 
            loginbutton.place(anchor = "center",x = 200,y = 400)
            f.close()                    
        else:
            loginbutton.place(anchor = "center",x = 200,y = 400)

    return

def sighendscreen2(name,uname):
    global usernameis
    global uname2
    usernameis = name
    uname2 = uname 
    nameff["text"] = usernameis
    usernn["text"] = uname2
    with open("userlogdata","r") as f:
        line = ""
        for l in f:
            if uname2 in l:
                line = l 
        if uname2 in line and "True" in line:
            loginbutton2.place_forget()
            logoutbutton2.place(anchor = "center",x = 300,y = 400)
            f.close()
        elif uname2 in line and "False" in line:
            logoutbutton2.place_forget() 
            loginbutton2.place(anchor = "center",x = 200,y = 400)
            f.close()                    
        else:
            loginbutton2.place(anchor = "center",x = 200,y = 400)
    return

def loggedin():
    with open("Log Public","a") as f:
        f.write("\n") 
        f.write("\n")
        f.write(dtime)
        f.write("\n")
        wr = "Logged In" + " " + usernameis
        f.write(str(wr))
        f.close()

    with open("userlogdata","r") as f:
        lines = f.readlines()
        f.close()
    with open("userlogdata","w") as ff:
        for l in lines:                        
            if "True" in l and uname2 in l:
                continue
            else:
                ff.write(l)
        ff.close()    
    with open("userlogdata","a") as f:
        wr = uname2 +","+ "True"
        f.write(str(wr))
        f.write("\n")
        f.close()
    loginbutton.place_forget()
    logoutbutton.place(anchor = "center",x = 300,y = 400)
    return   
        
def loggedout():
    print(uname2)
    with open("Log Public","a") as f:
        f.write("\n") 
        f.write("\n")        
        f.write(dtime)
        f.write("\n")        
        wr = "Logged Out" + " " + usernameis
        f.write(str(wr))
        f.close()               
    
    with open("userlogdata","r") as f:
        lines = f.readlines()
        f.close()    
    with open("userlogdata","w") as ff:
        for l in lines:                        
            if "False" in l and uname2 in l:
                continue
            else:
                ff.write(l)
        ff.close()

    with open("userlogdata","a") as f:
        wr = uname2 +","+ "False"
        f.write(str(wr))
        f.write("\n")
        f.close() 

    logoutbutton.place_forget()

    loginbutton.place(anchor = "center",x = 200,y = 400)
    return
 
def sucfai():
    successCreate.place_forget()
    win.destroy()
    return

def showcontent():
    signed.place_forget()
    logs = tk.Frame(win,bg = "#2E2E2E", borderwidth = 0)
    canvas = tk.Canvas(logs,bg = "#2E2E2E",width=480, height=520, bd=0,highlightthickness=0)
    scrollbar = ttk.Scrollbar(logs, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas,bg = "#2E2E2E")


    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    
    stuff = []
    c = 0
    with open("Log Public", "r") as f:
        for i in range(3):
            stuff.append(f.readline()) 
        stuff = []
        for i in f.readlines():
            if i[0].isdigit():
                tm = i
                c = 1
            elif c == 1:
                i = i.replace("\n", "")
                m = i+" At "+tm
                stuff.append(m)
                c = 0
            else:
                c = 0 
    a = 0
    label = tk.Label(scrollable_frame, text="Logs",fg = "#D1D1D1", bg = "#2E2E2E", font = "italic")
    label.pack()
    backbut = tk.Button(scrollable_frame, text = "Exit", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = backscene)
    backbut.pack()
    for i in stuff:
        i = i.title()
        i = i.replace("\n","")
        a += 1
        if "In" in i:
            label = tk.Label(scrollable_frame, text=i,fg = "#2E2E2E", bg = "#5CFF5C", font = "italic", pady = 0)
            label.pack()
        elif "Out" in i:
            label = tk.Label(scrollable_frame, text=i,fg = "#2E2E2E", bg = "#FF5C5C", font = "italic", pady = 0)
            label.pack()
        elif "Leave" in i:
            label = tk.Label(scrollable_frame, text=i,fg = "#2E2E2E", bg = "#FF5C5C", font = "italic", pady = 0)
            label.pack() 
    logs.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="both",expand=True)

def showcontent2():
    signed.place_forget()
    logs = tk.Frame(win,bg = "#2E2E2E", borderwidth = 0)
    canvas = tk.Canvas(logs,bg = "#2E2E2E",width=783, height=800, bd=0,highlightthickness=0)
    scrollbar = ttk.Scrollbar(logs, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas,bg = "#2E2E2E")


    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    
    stuff = []
    c = 0
    with open("Leaves", "r") as f:
        for i in range(3):
            stuff.append(f.readline()) 
        stuff = []
        for i in f.readlines():
            if i[0].isdigit():
                tm = i
                c = 1
            elif c == 1:
                i = i.replace("\n", "")
                m = i+" At "+tm
                stuff.append(m)
                c = 0
            else:
                c = 0 
    a = 0
    label = tk.Label(scrollable_frame, text="Logs",fg = "#D1D1D1", bg = "#2E2E2E", font = "italic")
    label.pack()
    backbut = tk.Button(scrollable_frame, text = "Exit", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = backscene)
    backbut.pack()
    for i in stuff:
        i = i.title()
        i = i.replace("\n","")
        a += 1
        if "Leave" in i:
            label = tk.Label(scrollable_frame, text=i,fg = "#2E2E2E", bg = "#FF5C5C", font = "italic", pady = 0)
            label.pack() 

    logs.pack()
    canvas.pack(side="left", fill=tk.BOTH, expand=tk.YES)
    scrollbar.pack(side="right", fill="both",expand=True)
    win.resizable(True,True)
    win.maxsize(800,600)
def backscene():
    win.destroy()

def addleavefunc():
    addleaveframe.place(relwidth = 500, relheight = 500)
    return

def addleavetomfunc():
    user = leaveusername.get()
    mainuser = entry1.get()
    with open("userpassdata","r") as f:
        for line in f:
            lst = line
            lst = lst.replace("'","")
            lst = lst.replace(" ","")
            lst=  lst.strip("[] \n")
            ls = lst.split(",")
            userdata = []
            if ls != ['!!confidential!!']:
                usern = decrypt(ls[0],ls[2])
                userp = decrypt(ls[1],ls[2])
                userdata = [usern, userp, ls[2]]
                if userdata[0] == user:
                    with open("usersprivate","r") as f:
                        for line2 in f:
                            if user in line2:
                                uun = line2.split(",") 
                                uun.pop(-1)
                                un = ""
                                un = un.join(uun)
                                f.close()
                                break
                    with open("usersprivate","r") as f:
                        for line2 in f:
                            if mainuser in line2:
                                uun = line2.split(",") 
                                uun.pop(-1)
                                un2 = ""
                                un2 = un2.join(uun)
                                f.close()
                                break
                    with open("Leaves","a") as f:
                        f.write("\n") 
                        f.write("\n")
                        dtime2 = dtime.split(" ")
                        dtime2 = dtime2[0]
                        f.write(dtime2)
                        f.write("\n")
                        wr = un +" "+"On Leave Tomorrow"+" "+"Added By" +" "+ un2
                        f.write(str(wr))
                        f.close()
                    win.destroy()
                    return
#### UI #####


    
# button properties
okbutton = tk.Button(start, text = "Sign In", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = checkuser)
okbutton.place(x = 120,y = 400) 

# signed screen
gocreatebutton = tk.Button(signed, text = "Go To Create Manager", bg = "#5C5CFF", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = nextscene)
gocreatebutton.place(x = 305,y = 5) 

gocreateuserbutton = tk.Button(signed, text = "Go To Create User", bg = "#5C5CFF", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = nextscene2)
gocreateuserbutton.place(x = 335,y = 50) 

addleave = tk.Button(signed, text = "Add Leave", bg = "#5C5CFF", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = addleavefunc)
addleave.place(x = 160,y = 5)


loginbutton = tk.Button(signed, text = "Log In", bg = "#5CFF5C", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0,command = loggedin)


logoutbutton = tk.Button(signed, text = "Log Out", bg = "#FF5C5C", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = loggedout)


logsbutton = tk.Button(signed, text = "Show Logs", bg = "#5C5CFF", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = showcontent)
logsbutton.place(x = 5,y = 5)

leavesbutton = tk.Button(signed, text = "Show Leaves", bg = "#5C5CFF", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = showcontent2)
leavesbutton.place(x = 5,y = 50)


# CREATE MANAGER SCREEN
createbutton = tk.Button(create, text = "Create User", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = createuser)
createbutton.place(x = 105, y = 400) 

l = tk.Label(start, text = "Please Enter Your Username Bellow", fg = "white", bg = "#2E2E2E", font = "italic")
l.place(x = 105, y = 150)

l2 = tk.Label(start, text = "Please Enter Your Password Bellow", fg = "white", bg = "#2E2E2E", font = "italic")
l2.place(x = 105, y = 250)

l3 = tk.Label(create, text = "Please Enter Your Full Name Bellow", fg = "white", bg = "#2E2E2E", font = "italic")
l3.place(anchor = "center", x = 250, y = 60)

l4 = tk.Label(create, text = "Enter a Username You Will Remember (Do Not Tell Others)", fg = "white", bg = "#2E2E2E", font = "italic")
l4.place(anchor = "center",x = 260, y = 170)

l5 = tk.Label(create, text = "Enter a Password You Will Remember (Do Not Tell Others)", fg = "white", bg = "#2E2E2E", font = "italic")
l5.place(anchor = "center",x = 260, y = 270)
l5_1 = tk.Label(start, text = "Password Or Username Wrong Or Doesn't Exist...", fg = "#FF0000", bg = "#2E2E2E", font = ("italic", 10))


l6 = tk.Label(successCreate, text = "Your Account Has Been Created!!", fg = "#5CFF5C", bg = "#2E2E2E", font = ("italic", 20))
l6.place(anchor = "center",x = 260, y = 250)
l6_1 = tk.Label(successCreate, text = "window will close in 5 seconds", fg = "white", bg = "#2E2E2E", font = ("italic", 10))
l6_1.place(anchor = "center",x = 260, y = 300)
l7 = tk.Label(failedCreate, text = "Failed To Create Account (Account Name Already Exists)", fg = "#FF0000", bg = "#2E2E2E", font = ("italic", 13))
l7.place(anchor = "center",x = 260, y = 250)
l7_1 = tk.Label(failedCreate, text = "window will close in 5 seconds", fg = "white", bg = "#2E2E2E", font = ("italic", 10))
l7_1.place(anchor = "center",x = 260, y = 300)



# CREATE USER SCREEEN
large_font = ('Verdana',20)
createbutton = tk.Button(createnewuser, text = "Create User", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = createuser2)
createbutton.place(x = 105, y = 400) 

lcu1 = tk.Label(createnewuser, text = "Please Enter Your Full Name Bellow", fg = "white", bg = "#2E2E2E", font = "italic")
lcu1.place(anchor = "center", x = 250, y = 60)

lcu2 = tk.Label(createnewuser, text = "Enter a Username You Will Remember (Do Not Tell Others)", fg = "white", bg = "#2E2E2E", font = "italic")
lcu2.place(anchor = "center",x = 260, y = 170)

lcu3 = tk.Label(createnewuser, text = "Enter a Password You Will Remember (Do Not Tell Others)", fg = "white", bg = "#2E2E2E", font = "italic")
lcu3.place(anchor = "center",x = 260, y = 270)

nameofuser = tk.Entry(createnewuser, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
nameofuser.place(x = 85, y = 100)
userentryname = tk.Entry(createnewuser, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
userentryname.place(x = 85, y = 200)
userpassword = tk.Entry(createnewuser, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
userpassword.place(x = 85, y = 300)

# SIGHNED USER SCREEN
loginbutton2 = tk.Button(signeduser, text = "Log In", bg = "#5CFF5C", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0,command = loggedin)

logoutbutton2 = tk.Button(signeduser, text = "Log Out", bg = "#FF5C5C", fg = "black", activebackground = "#8A8A8A", padx = 10, font = "bold", borderwidth=0, command = loggedout)

nameff = tk.Label(signeduser,text = "Loading", bg = "#2E2E2E", fg = "#189AB4", borderwidth=0, font = large_font, anchor = "center")
nameff.place(anchor = "center",x = 250, y = 200)
usernn = tk.Label(signeduser,text = "Loading", bg = "#2E2E2E", fg = "#D4F1F4", borderwidth=0, font = large_font, )
usernn.place(anchor = "center", x = 250, y = 300)

# Start Screen
large_font = ('Verdana',20)
entry1 = tk.Entry(start, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
entry1.place(x = 85, y = 200)

entry2 = tk.Entry(start, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
entry2.place(x = 85, y = 300)

# Signed screen 
namef = tk.Label(signed,text = "Loading", bg = "#2E2E2E", fg = "#189AB4", borderwidth=0, font = large_font, anchor = "center")
namef.place(anchor = "center",x = 250, y = 200)
usern = tk.Label(signed,text = "Loading", bg = "#2E2E2E", fg = "#D4F1F4", borderwidth=0, font = large_font, )
usern.place(anchor = "center", x = 250, y = 300)

# create screen
uname = tk.Entry(create, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
uname.place(x = 85, y = 100)
newuser = tk.Entry(create, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
newuser.place(x = 85, y = 200)
newpass = tk.Entry(create, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
newpass.place(x = 85, y = 300)

# leave screen
leaveusername = tk.Entry(addleaveframe, fg = "black", bg = "#D1D1D1", borderwidth=0,font = large_font)
leaveusername.place(x = 85, y = 200)

okleavebutton = tk.Button(addleaveframe, text = "Add Leave For Tomorrow", bg = "#D1D1D1", fg = "black", activebackground = "#8A8A8A", padx = 100, font = "bold", borderwidth=0, command = addleavetomfunc)
okleavebutton.place(x = 70,y = 300) 



win.iconbitmap(r"Main_Logo.ico")
win.resizable(False, False)
start.place(relwidth = 500, relheight = 500)
win.mainloop()
