from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from sqlite3 import *
import datetime
import calendar
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
     NavigationToolbar2Tk
from matplotlib import patches
#colour codes         
blue = "#264653"      
green = "#0D5E53"     
yellow = "#F2C337"    
orange = "#F49303"    
red = "#FF4C3F"       
peach="#F7AC94"
grey = "#BCE0CC"
red = "#FF4C3F"
pink = "#F29696"

#Current year and month
current_year=int(datetime.date.today().strftime("%Y"))
current_month=datetime.date.today().strftime("%B")
current_month_no = int(datetime.date.today().strftime("%m"))

#Initializing the main screen
def build_screen():
    global root,frame1
    root = Tk()
    root.title("d r á k o n : Your personal budget tracker")
    root.attributes('-fullscreen',True)
    root.bind('<Escape>',small_screen)
    canvas = Canvas(root,height=710,width=1250)
    canvas.pack()
    frame1 = Frame(root, bg = blue)
    frame1.place(relwidth = 1, relheight = 1)

#def function for esc to small screen
def small_screen(x) :
    root.attributes('-fullscreen',False)

build_screen()

#Fonts to be used
r18 = Font(family = "Bahnschrift", size = 18)
c22i = Font(family = "Courier New", size = 22 , slant = "italic")
c30 = Font(family = "Courier New", size = 30)
title = Font(family = "Rockwell", size = 100)
b20 = Font(family = "Bahnschrift", size = 20)
b16 = Font(family = "Bahnschrift", size = 16)
r24 = Font(family = "Rockwell", size = 24)
r20 = Font(family = "Rockwell", size = 20, slant = "italic")
r55 = Font(family = "Rockwell", size = 55)
b22 = Font(family = "Bahnschrift", size = 22)
g28 = Font(family = "Yu Gothic UI Semilight", size = 28)
g16b = Font(family = "Yu Gothic UI Semilight", size = 16, weight = "bold")
g45 = Font(family = "Yu Gothic UI Semilight", size = 45)
c60 = Font(family = "Courier New", size = 60)
c60i = Font(family = "Courier New", size = 60, slant = "italic")
r40 = Font(family = "Rockwell", size = 55)
r30 = Font(family = "Rockwell", size = 30)
b40 = Font(family = "Bahnschrift", size = 40)
g24 = Font(family = "Yu Gothic UI Semilight", size = 24)
c35 = Font(family = "Courier New", size = 35, weight = "bold")
c12 = Font(family = "Yu Gothic UI Semilight", size = 12)

def clear_frame():
    for widget in frame1.winfo_children():
        widget.destroy()

def textbox(frame,width=18,font=b20):
    box = Entry(frame, selectborderwidth = "2px", bd = "1px", width = width, \
                relief = SUNKEN, font = font, fg = blue)
    return box
def asterisk_textbox(frame,width=18,font=b20):
    box = Entry(frame, selectborderwidth = "2px", bd = "1px", width = width, \
                           relief = SUNKEN, font = font, \
                           fg = blue, show = "*")
    return box
    
def login_screen():
    
    #Assigning function to the login button
    def login_function():
        username=username_entry.get()
        password=password_entry.get()

        error=Label(login_frame, font = g16b ,\
                        bg = green , fg = '#800000')
        error.place(relx=0.5,rely=0.591,relwidth=1,anchor=CENTER)

        cur.execute('SELECT Username,Password FROM userinfo WHERE Username==?'\
                    ,(username,))
        
        if username=='' or password=='':
            error.config(text = 'Invalid Input') 
            username_entry.delete(0,END)
            password_entry.delete(0,END)
        elif cur.fetchone()!=(username,password):
            error.config(text = 'Incorrect username or password')
            username_entry.delete(0,END)
            password_entry.delete(0,END)
        else:
            main_screen(username)
    clear_frame()    

    #logo
    canvas = Canvas(frame1, width = 120, height = 120)
    canvas.config(bg = blue, relief = FLAT, bd=0, highlightthickness=0)
    canvas.place(relx = 0.33, rely = 0.38, anchor = CENTER)
    picture = PhotoImage(file = "C:\\Users\\Rehan pc\\Desktop\\budget tracker\\LOGO BLUE.png")
    logo = canvas.create_image(60, 60, image = picture)
    
    #app name
    app_name = Label(frame1, text="d  r  á  k  o  n", \
                           font = title, \
                           bg = blue, foreground = yellow) 
    app_name.place(relx = 0.33, rely = 0.55, anchor = CENTER)
    app_ = Label(frame1, text="personal budget tracker", \
                           font = c22i, \
                           bg = blue, foreground = yellow) 
    app_.place(relx = 0.33, rely = 0.68 , anchor = CENTER)

    #login/register frame
    login_frame = Frame(frame1, \
                        width = "9cm" , height = "10.5cm", \
                        bg = green, bd = "0px")
    login_frame.place(relx = 0.79, rely = 0.5, anchor = CENTER)
    
    #username_rname entry for logging in
    username_label = Label(login_frame, text="Username", \
                           font = r18, \
                           bg = green, foreground = yellow) 
    username_label.place(relx = 0.135, rely = 0.16, anchor = W)

    username_entry = textbox(login_frame,18,r18)
    username_entry.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    
    #password entry for logging in
    password_label = Label(login_frame, text="Password", \
                           font = r18, \
                           bg = green, foreground = yellow) 
    password_label.place(relx = 0.135, rely = 0.39, anchor = W)

    password_entry = asterisk_textbox(login_frame,18,r18)
    password_entry.place(relx = 0.5, rely = 0.48, anchor = CENTER)

    #login button
    login = Button(login_frame, text = " LOGIN ", \
                      bd = "0px", relief = FLAT, font = r18,\
                      bg = green, foreground = yellow, \
                      activebackground = green, activeforeground = peach,\
                      command=login_function)
    login.place(relx = 0.5, rely = 0.69, anchor = CENTER)

    #register button
    register = Button(login_frame, text = " REGISTER ", \
                      bd = "0px", relief = FLAT, font = r18,\
                      bg = yellow, foreground = green, \
                      activebackground = yellow, activeforeground = blue,\
                      command = register_screen)
    register.place(relx = 0.5, rely = 0.84, anchor = CENTER)
    
    root.mainloop()

def create_table():
    global cur,con
    con=connect('mydatabase.db')
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS userinfo(Username TEXT
                PRIMARY KEY,Password TEXT,First_name TEXT,Last_name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS budget_info(Username TEXT,
                Year INTEGER, Month TEXT, Monthly_budget INTEGER, 
                Tution_and_living_expenses INTEGER,Food_budget INTEGER, 
                Entertainment_budget INTEGER, Clothing_budget INTEGER, 
                Basic_utilities_budget INTEGER,
                Transport_budget INTEGER, Other_budget INTEGER,
                Tution_and_living_left INTEGER, Food_left INTEGER,
                Entertainment_left INTEGER, Clothing_left INTEGER,
                Basic_utilities_left INTEGER, Transport_left INTEGER,
                Other_left INTEGER,
                Spent_on_Tution_and_living INTEGER,Spent_on_Food INTEGER,
                Spent_on_Entertainment INTEGER,Spent_on_Clothing INTEGER,
                Spent_on_Basic_utilities INTEGER,
                Spent_on_Transport INTEGER,Spent_on_Other INTEGER)''')
    con.commit()

def register_screen():
    
    #Assigning function to done button
    def done_function():       
        username=username_entry.get()
        first_name=first_name_entry.get()
        last_name=last_name_entry.get()
        password1=password1_entry.get()
        password2=password2_entry.get()
        error = Label(register_frame, text="",font = b20,bg = green, fg = '#800000')
        error.place(relx = 0.5, rely = 0.804, relwidth=0.8, anchor = CENTER)
        
        cur.execute("SELECT Username FROM userinfo WHERE Username=?",(username,))
        
        if first_name == '' or last_name == '' or username == '' or\
            password1 == '' or password2 == '' :
            error.config(text="ERROR : Some required areas are empty")
        elif cur.fetchone()!=None:
            error.config(text="ERROR : Username not available")
        elif password1!=password2 :
            error.config(text="ERROR : Passwords do not match")
        elif len(password1)<8:
            error.config(text="ERROR : Password less than 8 characters")
        else:
            save_userinfo(username,first_name,last_name,password1)
            budget_plan_screen(username,first_name)

    #Function to save userinfo
    def save_userinfo(username,first_name,last_name,password):
        cur.execute(" INSERT INTO userinfo VALUES (?,?,?,?)",( username ,\
                    password , first_name , last_name ))
        month_no=current_month_no
        for year in range(current_year,current_year+10):
            for month in range(month_no,13):
                cur.execute("INSERT INTO budget_info VALUES(?,?,?,?,?,?,?,?,\
                            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(username,year,\
                            calendar.month_name[month],0,0,0,0,0,0,0,0,0,0,0,0,\
                            0,0,0,0,0,0,0,0,0,0))
                if month == 12:
                    month_no = 1
        con.commit()

    def label_func(text,rely):
        label = Label(register_frame, text=text, \
                           font = b20, bg = green, foreground = grey)
        label.place(relx = 0.25, rely = rely, anchor = CENTER)

    #frame
    clear_frame()
    register_frame = Frame(frame1, \
                  width = "19cm" , height = "17cm", bg = green, bd = "0px")
    register_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#labels
    heading_label = Label(register_frame, text="Create your account", \
                          font = r24, bg = green, foreground = peach)
    heading_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    #First name
    label_func("First Name",0.22)
    #Last name
    label_func("Last Name",0.345)
    #Username
    label_func("Username",0.47)
    #Password
    label_func("Password",0.595)
    #Re enter password
    label_func("Re-Enter Password",0.72)

    first_name_entry =textbox(register_frame)
    first_name_entry.place(relx = 0.45, rely = 0.22, anchor = W)

    last_name_entry = textbox(register_frame)
    last_name_entry.place(relx = 0.45, rely = 0.345, anchor = W)

    username_entry = textbox(register_frame)
    username_entry.place(relx = 0.45, rely = 0.47, anchor = W)

    password1_entry = asterisk_textbox(register_frame)
    password1_entry.place(relx = 0.45, rely = 0.595, anchor = W)

    password2_entry = asterisk_textbox(register_frame)
    password2_entry.place(relx = 0.45, rely = 0.72, anchor = W)

    #Back button
    back = Button(frame1, text = " BACK ", \
                      bd = "0px", relief = FLAT, font = b20,\
                      bg = peach, foreground = blue, \
                      activebackground = peach, activeforeground = green, \
                      command = login_screen)
    back.place(x = 30, y = 30, anchor = NW)

    #done button
    done = Button(register_frame, text = " DONE ", \
                      bd = "0px", relief = FLAT, font = b20,\
                      bg = peach, foreground = green, \
                      activebackground = peach, activeforeground = blue,\
                      command = done_function)
    done.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    root.mainloop()

def budget_plan_screen(username,first):

    def error(text):
        Label(frame2, text = text, font = r20, \
                  bg = green, fg = '#800000').place(relx = 0.5, rely = 0.85,\
                  anchor = CENTER)
    #Assigning function to done button
    def done(budget,charges,food,entertainment,clothing,basic_utilities,\
             transport,other):
        
        if budget=='' or charges=='' or \
           food=='' or entertainment=='' or clothing=='' or \
           basic_utilities=='' or transport=='' or other=='':
            error("Error : Required field(s) empty")
        elif not((budget+charges+food+entertainment+clothing+basic_utilities+\
           transport+other).isdigit()):
            error("Error : Invalid input")        
        elif int(charges) + int(food) + int(entertainment) + int(clothing) \
           + int(basic_utilities) + int(transport) + int(other) > int(budget) :
            error("Error : Goals exceed budget")
        else:
            if int(charges) + int(food) + int(entertainment) + int(clothing)\
               + int(basic_utilities) + int(transport) + int(other) < int(budget) :
                option=warning()

                if option=="yes":
                    save_budget(budget,charges,food,entertainment,clothing,\
                                basic_utilities,transport,other)
                    main_screen(username)
            else:
                save_budget(budget,charges,food,entertainment,clothing,\
                            basic_utilities,transport,other)
                main_screen(username)              
            
    def save_budget(budget,charges,food,entertainment,clothing,basic_utilities,\
                    transport,other):
        
        cur.execute("""UPDATE budget_info SET (Monthly_budget,
                    Tution_and_living_expenses, Food_budget, 
                    Entertainment_budget, Clothing_budget,
                    Basic_utilities_budget, Transport_budget, 
                    Other_budget)=(?,?,?,?,?,?,?,?) WHERE Username=?""", \
                   (budget,charges,food,entertainment,clothing,basic_utilities,\
                    transport,other,username))
        
        cur.execute("""UPDATE budget_info SET 
                (Tution_and_living_left, Food_left, Entertainment_left, 
                Clothing_left, Basic_utilities_left, Transport_left, 
                Other_left) = (?,?,?,?,?,?,?) WHERE Username=?""", \
                (charges, food, entertainment, clothing, \
                basic_utilities, transport, other, username))
        
        con.commit()
        
    def warning():
        warning = messagebox.askquestion("Unused amount", "You have an \
amount left unused.\nDo you want to add it to savings?")
        return warning
    
    def label_func(text, rely, relx = 0.33, fg = grey):
        label = Label(frame2, text = text, font = b20, bg = green, fg = fg)
        label.place(relx = relx, rely = rely, anchor = CENTER)
            
#Initializing the screen
    clear_frame()
    frame2 = Frame(frame1, bg = green, width = "22cm", height = "15.5cm")
    frame2.place(relx = 0.5, rely = 0.56, anchor = CENTER)

#labels and textboxes

    #WElcome label
    welcome_label = Label(frame1,text='Welcome {},'.format(first), \
                        bg = blue, fg = peach, font = r55)
    welcome_label.place(relx = 0.07, rely = 0.04)
    #Budget
    label_func("Set your monthly budget : ", 0.075, 0.35)    
    budget_entry = textbox(frame2,15)
    budget_entry.place(relx = 0.7, rely = 0.075, anchor = CENTER)
    #Tution and living
    label_func("Tution and Living Expense : ", 0.165, 0.35)
    charges_entry = textbox(frame2,15)
    charges_entry.place(relx = 0.7, rely = 0.165, anchor = CENTER)
    #Main label
    label_func("How much would you like to spend on", 0.245, 0.5, peach)
    #Food
    label_func("Food",0.33)
    food_entry = textbox(frame2,15)
    food_entry.place(relx = 0.63,rely = 0.33, anchor = CENTER)
    #Entertainment
    label_func("Entertainment",0.42)
    entertainment_entry = textbox(frame2,15)
    entertainment_entry.place(relx = 0.63, rely = 0.42, anchor = CENTER)
    #Clothing
    label_func("Clothing",0.51)
    clothing_entry = textbox(frame2,15)
    clothing_entry.place(relx = 0.63, rely = 0.51, anchor = CENTER)
    #Basic utilities
    label_func("Basic Utilities",0.6)
    basic_utilities_entry= textbox(frame2,15)
    basic_utilities_entry.place(relx=0.63, rely = 0.6, anchor = CENTER)
    #Transport
    label_func("Transport",0.69)
    transport_entry = textbox(frame2,15)
    transport_entry.place(relx = 0.63, rely = 0.69, anchor = CENTER)
    #Other
    label_func("Other",0.78)
    other_entry = textbox(frame2,15)
    other_entry.place(relx = 0.63, rely = 0.78, anchor = CENTER)

    done_button = Button(frame2, text = "DONE", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = green, activebackground = peach,\
                         activeforeground = blue,
                    command=lambda:done(budget_entry.get(),charges_entry.get(),\
                                   food_entry.get(), entertainment_entry.get(),\
                                   clothing_entry.get(),\
                                   basic_utilities_entry.get(),\
                                   transport_entry.get(), other_entry.get()))
    done_button.place(relx = 0.5, rely=0.925, anchor = CENTER)
    root.mainloop()

def daily_entry_screen(username):

    def save_daily_entry(state,food,entertainment,clothing,basic_utilities, \
                         transport,other):
            
        cur.execute("""SELECT Tution_and_living_expenses, Spent_on_Food, 
                Spent_on_Entertainment, Spent_on_Clothing, 
                Spent_on_Basic_utilities, Spent_on_Transport,
                Spent_on_Other FROM budget_info WHERE USERNAME = ? AND 
                Year = ? AND Month = ?""",(username,current_year,current_month))
        spent = cur.fetchone()
        fee,food1,entertainment1,clothing1,basic_utilities1,transport1,\
        other1=spent[0],spent[1], spent[2],spent[3],spent[4],spent[5],spent[6]

        state = state.get()

        if state == 0:
            current_fee , spent_on_fee = fee , 0
        elif state == 1:
            current_fee , spent_on_fee = 0 , fee
            
        cur.execute("""UPDATE budget_info SET ( Spent_on_Tution_and_living, 
                    Spent_on_Food, Spent_on_Entertainment, Spent_on_Clothing,
                    Spent_on_Basic_utilities, Spent_on_Transport,
                    Spent_on_Other ) = (?,?,?,?,?,?,?) WHERE Username=? AND
                    Year=? AND Month=?""",(spent_on_fee,food1+int(food), \
                     entertainment1+int(entertainment),clothing1+int(clothing),\
                     basic_utilities1+int(basic_utilities), \
                     transport1+int(transport),other1+int(other),username, \
                     current_year, current_month))

        cur.execute("""SELECT Spent_on_Food, Spent_on_Entertainment, 
                Spent_on_Clothing, Spent_on_Basic_utilities,Spent_on_Transport,
                Spent_on_Other FROM budget_info WHERE USERNAME = ? AND 
                Year = ? AND Month = ?""",(username,current_year,current_month))
        spent = cur.fetchone()
        food1,entertainment1,clothing1,basic_utilities1,transport1,\
        other1=spent[0],spent[1], spent[2], spent[3], spent[4], spent[5]

        cur.execute("""SELECT Food_budget, Entertainment_budget, Clothing_budget,
                    Basic_utilities_budget, Transport_budget, Other_budget FROM
                    budget_info WHERE USERNAME=? AND Year=? AND Month = ?""", \
                    (username, current_year, current_month))
        total=cur.fetchone()
        food2,entertainment2,clothing2,basic_utilities2,transport2,\
        other2=total[0],total[1], total[2], total[3], total[4], total[5]

        cur.execute("""UPDATE budget_info SET (Tution_and_living_left,Food_left, 
                    Entertainment_left,Clothing_left, Basic_utilities_left, 
                    Transport_left, Other_left ) = (?,?,?,?,?,?,?) WHERE 
                    Username = ? AND Year = ? AND Month = ?""", \
                    (current_fee, food2-food1, entertainment2-entertainment1, \
                     clothing2-clothing1, basic_utilities2-basic_utilities1, \
                     transport2-transport1, other2-other1, username, \
                     current_year, current_month))                                                   

        con.commit()

    def done(state,food,entertainment,clothing,basic_utilities,transport,other):

        error = Label(frame2, text = "", font = r20, \
                bg = green,fg = '#800000').place(relx = 0.5, rely = 0.82, \
                anchor = CENTER)
        
        if food == '' or entertainment == '' or clothing == '' or \
           basic_utilities == '' or transport == '' or other == '':

            error.config(text = "Error : Required field(s) empty")

        elif not((food + entertainment + clothing + basic_utilities + transport +\
                other).isdigit()):

            error.config(text = "Error : Invalid Input")

        else:
            save_daily_entry(state, food, entertainment, clothing, \
                             basic_utilities, transport, other)
            main_screen(username)
            
    def label_func(text, rely, relx = 0.33, fg = grey):
        label = Label(frame2,text = text, font = b20, bg = green, fg = fg)
        label.place(relx = relx, rely = rely, anchor = CENTER)
#Initializing the screen
    clear_frame()
    frame2 = Frame(frame1, bg = green, width = "22cm", height = "15.5cm")
    frame2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#labels and textboxes

    #Main label
    label_func("How much have you spent on", 0.105, 0.5, peach)
    #Food
    label_func("Food", 0.21)
    food_entry = textbox(frame2,15)
    food_entry.place(relx = 0.63,rely = 0.21, anchor = CENTER)
    #Entertainment
    label_func("Entertainment",0.315)
    entertainment_entry = textbox(frame2,15)
    entertainment_entry.place(relx = 0.63, rely = 0.315, anchor = CENTER)
    #Clothing
    label_func("Clothing", 0.42)
    clothing_entry = textbox(frame2,15)
    clothing_entry.place(relx = 0.63, rely = 0.42, anchor = CENTER)
    #Basic utilities
    label_func("Basic Utilities", 0.525)
    basic_utilities_entry = textbox(frame2,15)
    basic_utilities_entry.place(relx = 0.63, rely = 0.525, anchor = CENTER)
    #Transport
    label_func("Transport", 0.63)
    transport_entry = textbox(frame2,15)
    transport_entry.place(relx = 0.63, rely = 0.63, anchor = CENTER)
    #Other
    label_func("Other", 0.735)
    other_entry = textbox(frame2,15)
    other_entry.place(relx = 0.63, rely = 0.735, anchor = CENTER)
    #Back button
    back_button = Button(frame1, text = "BACK", border = "0px", \
                         relief = FLAT, font = b20, bg = peach, fg = green, \
                         activebackground = peach, activeforeground = blue, \
                         command = lambda: main_screen(username))                   
    back_button.place(x = 30, y = 30, anchor = NW )
    state=IntVar()

    charges_checkbox=Checkbutton(frame2,text="Tution fee and hostel charges\
 paid" , font = ("times new roman",16) , bg = green , variable = state, \
onvalue = 1, offvalue = 0 )
    charges_checkbox.place( relx = 0.75, rely = 0.9 , anchor = CENTER)
    charges_checkbox.select()                                                      
    #Done button
    done_button = Button(frame2, text = "DONE", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = green, activebackground = peach,\
                         activeforeground = blue, \
                         command = lambda: done( state,food_entry.get(), \
                         entertainment_entry.get(), clothing_entry.get(), \
                         basic_utilities_entry.get(), transport_entry.get(), \
                         other_entry.get()))    
    done_button.place(relx = 0.5, rely=0.91, anchor = CENTER, relheight = 0.078)
    
    root.mainloop()

def main_screen(username):
    global current_year, current_month, current_month_no
    current_year=int(datetime.date.today().strftime("%Y"))
    current_month=datetime.date.today().strftime("%B")
    current_month_no = int(datetime.date.today().strftime("%m"))
    click_counter=0
    #settings frame
    def settings_frame():                                                           
        nonlocal click_counter,settings_frame
        click_counter+=1
        if click_counter%2 != 0:
            settings_frame = Frame(frame1,bg=yellow,width="7cm",height="5cm")
            settings_frame.place(relx = 0.975, rely = 0.1, anchor = NE)
            change_budget = Button(settings_frame, text = "Change Budget", \
                               relief = FLAT, bd = "0px", font = b22, \
                               bg = yellow, activebackground = yellow, \
                               fg = blue, activeforeground = green, \
                               command = lambda: change_budget_screen(username))    
            change_budget.place(relx = 0.5, rely = 0.2, anchor = CENTER)
            change_password = Button(settings_frame, text = "Change Password", \
                             relief = FLAT, bd = "0px", font = b22, \
                             bg = yellow, activebackground = yellow, \
                             fg = blue, activeforeground = green,
                             command = lambda: change_password_screen(username))
            change_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            logout = Button(settings_frame, text = "Logout", \
                        relief = FLAT, bd = "0px", font = b22, \
                        bg = yellow, activebackground = yellow, \
                        fg = blue, activeforeground = green, \
                            command = login_screen)
            logout.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        
        elif click_counter%2==0:
            settings_frame.destroy()
    def load_data():
        cur.execute("""SELECT Spent_on_Tution_and_living, Spent_on_food,
                Spent_on_Entertainment, Spent_on_Clothing ,
                Spent_on_Basic_utilities, Spent_on_Transport, Spent_on_Other,
                Tution_and_living_left, Food_left, 
                Entertainment_left, Clothing_left, Basic_utilities_left,
                Transport_left, Other_left FROM budget_info WHERE Username = ? \
                AND Year = ? AND Month = ?""",(username, current_year, \
                current_month))
        info = cur.fetchone()
        return info
    def error(text,rely):
        error=Label(frame1, text=text,font = b20,bg = blue, fg = red)
        error.place(relx = 0.5, rely = rely,relwidth=0.8,anchor = CENTER)
    def tab(text, relx, command):
        tab = Button(frame2, text = text, \
                         border = "0px",height = "1", width = "15", \
                         relief = FLAT, font = b22, bg = green, \
                         activebackground = green, fg = peach, \
                         activeforeground = grey, \
                         command = command)
        tab.place(anchor = CENTER, relx = relx, rely = 0.5)
    def label(text):
        label = Label(frame1,text = text, font = g28, bg = blue, \
                        fg = grey)
        return label
#initializing the screen
    clear_frame()
    frame2 = Frame(frame1, bg = green)
    frame2.place(relwidth = 1,relheight = 0.1,relx = 0.5,rely = 0,anchor = N)
    
#screens buttons
    #Budget Goals
    tab("Daily Entry", 0.1, lambda: daily_entry_screen(username))
    #month pie charts
    tab("Monthly Review", 0.26, lambda: year_selection(username))                            
    #year review
    tab("Yearly Analysis", 0.44, lambda: select_year(username))                             
#ONSCREEN labels
    date = Label(frame1, text=datetime.date.today().strftime("%d-%b-%Y"), \
                 font = b22, bg = blue, fg = grey)
    date.place(relx = 0.015, rely = 0.11, anchor = NW)
    
    spent_label = label("Amount Spent")
    spent_label.place(relx = 0.49, rely = 0.175, anchor = CENTER)
    left_label = label("Amount Left")
    left_label.place(relx = 0.665, rely = 0.175, anchor = CENTER)
#load data
    charges_spent,food_spent,entertainment_spent,clothing_spent, \
    utilities_spent, transport_spent,other_spent,chargesleft,foodleft, \
    entertainmentleft, \
    clothingleft,utilitiesleft,transportleft,otherleft =load_data()

#Tution and living
    charges = label("Tution and living")
    charges.place(relx = 0.29, rely = 0.265, anchor = CENTER)
    charges_spent = label(charges_spent)
    charges_spent.place(relx = 0.49, rely = 0.265, anchor = CENTER)
    charges_left = label(chargesleft)
    charges_left.place(relx = 0.665, rely = 0.265, anchor = CENTER)
#food
    food = label("Food")
    food.place(relx = 0.29, rely = 0.3675, anchor = CENTER)
    food_spent = label(food_spent)
    food_spent.place(relx = 0.49, rely = 0.3675, anchor = CENTER)
    food_left = label(foodleft)
    food_left.place(relx = 0.665, rely = 0.3675, anchor = CENTER)
#entertainment
    entertainment = label("Entertainment")
    entertainment.place(relx = 0.29, rely = 0.47, anchor = CENTER)
    entertainment_spent = label(entertainment_spent)
    entertainment_spent.place(relx = 0.49, rely = 0.47, anchor = CENTER)
    entertainment_left = label(entertainmentleft)
    entertainment_left.place(relx = 0.665, rely = 0.47, anchor = CENTER)
#clothing
    clothing = label("Clothing")
    clothing.place(relx = 0.29, rely = 0.5725, anchor = CENTER)
    clothing_spent = label(clothing_spent)
    clothing_spent.place(relx = 0.49, rely = 0.5725, anchor = CENTER)
    clothing_left = label(clothingleft)
    clothing_left.place(relx = 0.665, rely = 0.5725, anchor = CENTER)
#utilities
    utilities = label("Basic Utilities")
    utilities.place(relx = 0.29, rely = 0.675, anchor = CENTER)
    utilities_spent = label(utilities_spent)
    utilities_spent.place(relx = 0.49, rely = 0.675, anchor = CENTER)
    utilities_left = label(utilitiesleft)
    utilities_left.place(relx = 0.665, rely = 0.675, anchor = CENTER)
#transport
    transport = label("Transport")
    transport.place(relx = 0.29, rely = 0.7775, anchor = CENTER)
    transport_spent = label(transport_spent)
    transport_spent.place(relx = 0.49, rely = 0.7775, anchor = CENTER)
    transport_left = label(transportleft)
    transport_left.place(relx = 0.665, rely = 0.7775, anchor = CENTER)
#other
    other = label("Other")
    other.place(relx = 0.29, rely = 0.88, anchor = CENTER)
    other_spent = label(other_spent)
    other_spent.place(relx = 0.49, rely = 0.88, anchor = CENTER)
    other_left = label(otherleft)
    other_left.place(relx = 0.665, rely = 0.88, anchor = CENTER)
#Errors
    if foodleft<0:
        error("Food budget has been exceeded by "+ str(abs(foodleft)),0.41875)
        food_left.config(text=0)
    if entertainmentleft<0:
        error("Entertainment budget has been exceeded by "+ \
              str(abs(entertainmentleft)),0.52125)
        entertainment_left.config(text=0)
    if clothingleft<0:
        error("Clothing budget has been exceeded by " + \
              str(abs(clothingleft)),0.62375)
        clothing_left.config(text=0)
    if utilitiesleft<0:
        error("Basic utilities budget has been exceeded by " + \
              str(abs(utilitiesleft)),0.72625)
        utilities_left.config(text=0)
    if transportleft<0:
        error("Transport budget has been exceeded by " + \
              str(abs(transportleft)),0.82875)
        transport_left.config(text=0)
    if otherleft<0:
        error("Other budget has been exceeded by " + \
              str(abs(otherleft)),0.93125)
        other_left.config(text=0)
    if foodleft + entertainmentleft + clothingleft + utilitiesleft + \
       transportleft + otherleft + chargesleft < 0:
        messagebox.showwarning("WARNING","You have exceeded your total budget.\n\
 Any extra amount spent will be considered as debt.")
#settings button
    photo = PhotoImage(file = "C:\\Users\\Rehan pc\\Desktop\\budget tracker\\button.png")
    setting_button = Button(frame2, image = photo, highlightthickness = 0, \
                            bd = "0px", relief = FLAT, command = settings_frame)
    setting_button.place(anchor = CENTER, relx = 0.95, rely = 0.5)
    
    root.mainloop()

def change_password_screen(username):

    def done():
        cur.execute("SELECT Password FROM userinfo WHERE Username=?", \
                    (username,))
        password = cur.fetchone()
        password = password[0]
        old_password, new_password, re_enter_password = password_textbox.get(),\
                            new_password_textbox.get(), re_enter_textbox.get()

        error = Label(change_password, text = "", font = r20, \
                  bg = green, fg = '#800000')
        error.place(relx = 0.5, rely = 0.72, anchor = CENTER)

        if old_password == '' or new_password == '' or re_enter_password =='' :
            error.config(text = "Error : Required field(s) empty")           
        elif old_password != password :
            error.config(text = "Error : Incorrect password")
        elif new_password != re_enter_password:
            error.config(text = "Error : Passwords do not match")
        elif len(new_password) < 8:
            error.config(text = "Error : Password less than 8 characters")
        else:
            cur.execute("UPDATE userinfo SET Password = ? WHERE Username = ?", \
                        (new_password, username))
            main_screen(username)

    def inner_label(text,rely):
        label = Label(change_password,text = text,\
                        font = b22, bg = green, fg = peach)
        label.place(relx = 0.25, rely = rely, anchor = CENTER)
        
    clear_frame()
    change_password = Frame(frame1, bg = green)
    change_password.place(relwidth = 0.55, relheight = 0.5,\
                          relx = 0.5, rely = 0.6, anchor = CENTER)

#labels
    username_label = Label(frame1,text = "Username",\
                        font = c60, bg = blue, fg = yellow)
    username_label.place(relx = 0.5, rely = 0.15, anchor = CENTER)
#personal label would be the actual username of the person
    personal_label = Label(frame1,text = username,\
                        font = c60i, bg = blue, fg = yellow)
    personal_label.place(relx = 0.5, rely = 0.25, anchor = CENTER) 

#inside change password frame
    inner_label("Enter Old Password", 0.15)
    inner_label("Enter New Password", 0.35)
    inner_label("Re-enter New Password", 0.55)
    password_textbox = asterisk_textbox(change_password,18,b22)
    password_textbox.place(relx = 0.75, rely = 0.15, anchor = CENTER)
    new_password_textbox = asterisk_textbox(change_password,18,b22)
    new_password_textbox.place(relx = 0.75, rely = 0.35, anchor = CENTER)
    re_enter_textbox = asterisk_textbox(change_password,18,b22)
    re_enter_textbox.place(relx = 0.75, rely = 0.55, anchor = CENTER)

#back button
    back = Button(frame1, text = " BACK ", \
                      bd = "0px", relief = FLAT, font = b22,\
                      bg = peach, foreground = green, \
                      activebackground = peach, activeforeground = blue, \
                      command = lambda: main_screen(username))
    back.place(x = 30, y = 30, anchor = NW)

#done button
    done = Button(change_password, text = " DONE ", \
                      bd = "0px", relief = FLAT, font = b22,\
                      bg = peach, foreground = green, \
                      activebackground = peach, activeforeground = blue, \
                      command = done)
    done.place(relx = 0.5, rely = 0.85, anchor = CENTER)

    root.mainloop()

def change_budget_screen(username):
    def error(text):
        Label(frame2, text = text, font = r20, \
                  bg = green, fg = '#800000').place(relx = 0.5, rely = 0.85,\
                  anchor = CENTER)
    #Assigning function to done button
    def done(budget,charges,food,entertainment,clothing,basic_utilities,\
             transport,other):
        
        if budget=='' or charges=='' or \
           food=='' or entertainment=='' or clothing=='' or \
           basic_utilities=='' or transport=='' or other=='':
            error("Error : Required field(s) empty")
        elif not((budget+charges+food+entertainment+clothing+basic_utilities+\
           transport+other).isdigit()):
            error("Error : Invalid input")
        elif int(charges) + int(food) + int(entertainment) + int(clothing) \
           + int(basic_utilities) + int(transport) + int(other) > int(budget) :
            error("Error : Goals exceed budget")
        else:
            if int(charges) + int(food) + int(entertainment) + int(clothing)\
               + int(basic_utilities) + int(transport) + int(other) < int(budget) :
                option=warning()

                if option=="yes":
                    save_budget(budget,charges,food,entertainment,clothing,\
                                basic_utilities,transport,other)
                    main_screen(username)
            else:
                save_budget(budget,charges,food,entertainment,clothing,\
                            basic_utilities,transport,other)
                main_screen(username)
                
    def save_budget(budget,charges,food,entertainment,clothing,basic_utilities,\
                    transport,other):

        cur.execute("SELECT Year FROM budget_info WHERE Username=?",(username,))
        year_list = cur.fetchall()
        year_limit = year_list[-1][0]
        month_no=current_month_no

        for year in range(current_year,year_limit+1):
            for month in range(month_no,13):

                cur.execute("""UPDATE budget_info SET (Monthly_budget,
                            Tution_and_living_expenses, Food_budget, 
                            Entertainment_budget, Clothing_budget,
                            Basic_utilities_budget, Transport_budget,
                            Other_budget)=(?,?,?,?,?,?,?,?) WHERE Username=?
                            AND Year=? AND Month=?""",(budget,charges,food, \
                                entertainment,clothing,\
                                basic_utilities,transport,other,username,\
                                year,calendar.month_name[month]))
                cur.execute("""SELECT Spent_on_Tution_and_living, Spent_on_Food,
                        Spent_on_Entertainment, Spent_on_Clothing,
                        Spent_on_Basic_utilities,Spent_on_Transport,
                        Spent_on_Other FROM budget_info WHERE USERNAME = ?
                        AND Year = ? AND Month = ?""",(username, year, \
                        calendar.month_name[month]))
                spent = cur.fetchone()
                fee_spent, food_spent, entertainment_spent, clothing_spent, \
                basic_utilities_spent, transport_spent, other_spent = spent[0], \
                spent[1], spent[2], spent[3], spent[4], spent[5], spent[6]
                cur.execute("""UPDATE budget_info SET (Tution_and_living_left, 
                        Food_left, Entertainment_left, Clothing_left,
                        Basic_utilities_left, Transport_left, Other_left ) = 
                        (?,?,?,?,?,?,?) WHERE Username = ? AND Year = ? AND \
                        Month = ?""", (int(charges)-fee_spent, \
                         int(food)-food_spent, \
                         int(entertainment)-entertainment_spent, \
                         int(clothing)-clothing_spent, int(basic_utilities)-\
                         basic_utilities_spent, int(transport)-transport_spent,\
                         int(other)-other_spent, username, year, \
                         calendar.month_name[month]))
                if month == 12:
                    month_no = 1

        con.commit()
    def warning():
        warning = messagebox.askquestion("Unused Amount", "You have an \
amount left unused.\nDo you want to add it to savings?")
        return warning

    def label_func(text, rely, relx = 0.33, fg = grey):
        label = Label(frame2, text = text, font = b20, bg = green, fg = fg)
        label.place(relx = relx, rely = rely, anchor = CENTER)    

#Initializing the screen
    clear_frame()
    frame2 = Frame(frame1, bg = green, width = "22cm", height = "15.5cm")
    frame2.place(relx = 0.5, rely = 0.56, anchor = CENTER)

#labels and textboxes

    #Budget
    label_func("Set your monthly budget : ", 0.075, 0.35)    
    budget_entry = textbox(frame2,15)
    budget_entry.place(relx = 0.7, rely = 0.075, anchor = CENTER)
    #Tution and living
    label_func("Tution and Living Expense : ", 0.165, 0.35)
    charges_entry = textbox(frame2,15)
    charges_entry.place(relx = 0.7, rely = 0.165, anchor = CENTER)
    #Main label
    label_func("How much would you like to spend on", 0.245, 0.5, peach)
    #Food
    label_func("Food",0.33)
    food_entry = textbox(frame2,15)
    food_entry.place(relx = 0.63,rely = 0.33, anchor = CENTER)
    #Entertainment
    label_func("Entertainment",0.42)
    entertainment_entry = textbox(frame2,15)
    entertainment_entry.place(relx = 0.63, rely = 0.42, anchor = CENTER)
    #Clothing
    label_func("Clothing",0.51)
    clothing_entry = textbox(frame2,15)
    clothing_entry.place(relx = 0.63, rely = 0.51, anchor = CENTER)
    #Basic utilities
    label_func("Basic Utilities",0.6)
    basic_utilities_entry= textbox(frame2,15)
    basic_utilities_entry.place(relx=0.63, rely = 0.6, anchor = CENTER)
    #Transport
    label_func("Transport",0.69)
    transport_entry = textbox(frame2,15)
    transport_entry.place(relx = 0.63, rely = 0.69, anchor = CENTER)
    #Other
    label_func("Other",0.78)
    other_entry = textbox(frame2,15)
    other_entry.place(relx = 0.63, rely = 0.78, anchor = CENTER)

    done_button = Button(frame2, text = "DONE", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = green, activebackground = peach,\
                         activeforeground = blue,
                    command=lambda:done(budget_entry.get(),charges_entry.get(),\
                                   food_entry.get(), entertainment_entry.get(),\
                                   clothing_entry.get(),\
                                   basic_utilities_entry.get(),\
                                   transport_entry.get(), other_entry.get()))
    done_button.place(relx = 0.5, rely=0.925, anchor = CENTER)
    
    back = Button(frame1, text = " BACK ", \
                      bd = "0px", relief = FLAT, font = b20,\
                      bg = peach, foreground = green, \
                      activebackground = peach, activeforeground = blue, \
                      command = lambda: main_screen(username))
    back.place(x = 30, y = 30, anchor = NW)
    
    root.mainloop()

def select_category(username, year):

    def category(text,rely,command):
        button = Button(frame1, text = text, bd = "0px", \
                            font = r30, relief = FLAT, bg = blue, fg = peach, \
                            activebackground = blue, activeforeground = pink, \
                            command = command)
        button.place(relx = 0.5, rely = rely, anchor = CENTER)

    #label
    clear_frame()
    select = Label(frame1, text = "Select a category", font = c30, \
                   bg = blue, fg = grey)
    select.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    #Category buttons
    category("Tution and Living", 0.2, \
             lambda: graph(username,"Tution and Living", year))
    category("Food", 0.3, lambda: graph(username,"Food", year))
    category("Entertainment",0.4, lambda: graph(username,"Entertainment", \
                                                      year))
    category("Clothing", 0.5, lambda: graph(username,"Clothing", year))
    category("Basic Utilities", 0.6, \
             lambda: graph(username,"Basic Utilities", \
                                 year))
    category("Transport", 0.7, lambda: graph(username, "Transport", year))
    category("Other", 0.8, lambda: graph(username,"Other", year))

    #Back button
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = lambda: select_year(username))
    back_button.place( x = 30, y = 30, anchor = NW)

    root.mainloop()

def select_year(username):

    def select_func():
        if years_listbox.curselection() != ():
            year_choice = years_listbox.get(years_listbox.curselection())
            select_category(username, year_choice)
        else:
            Label(frame1, text = "Please click on the year to select it.", \
                  font = r20, bg = blue, fg = "#800000").place(relx = 0.5, \
                            rely = 0.635, anchor = CENTER)
    #Initializing the screen
    clear_frame()
    label = Label(frame1, text = "Select the year", font = c60, \
                  bg = blue, fg = grey)
    label.place(rely = 0.4, relx = 0.5, anchor = CENTER)
    #list of years
    years_listbox = Listbox(frame1, font = c60, bd = "0px", relief = FLAT, \
                            bg = blue, fg = yellow, justify = "center", \
                            selectmode = SINGLE, selectbackground = green)          
    years_listbox.place(relx = 0.5, rely = 0.55, anchor = CENTER, \
                        relwidth = 0.17, relheight = 0.1)#Adding scroll bar
    scrollbar = Scrollbar(years_listbox, orient = "vertical", \
                          command = years_listbox.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    years_listbox.config(yscrollcommand = scrollbar.set)
    
    #Adding options to list box
    cur.execute("SELECT Year FROM budget_info WHERE Username=?",(username,))
    year_list = cur.fetchall()
    first_year = year_list[0][0]
    for year in range(first_year, current_year+1):
        years_listbox.insert(END, year)

    #Buttons
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = lambda: main_screen(username))
    back_button.place( x = 30, y = 30, anchor = NW)

    select_button = Button(frame1, text = "SELECT", bd = "0px", \
                         relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = select_func)
    select_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    root.mainloop()

def graph(username, choice, year):

    def back_func():
        bar.destroy()
        canvas2.get_tk_widget().destroy()
        select_category(username, year)
    #Initializing the screen
    clear_frame()
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = back_func)
    back_button.place(x = 30, y = 30, anchor = NW)

    #Category
    if choice == 'Tution and Living':
        cur.execute("""SELECT Tution_and_living_expenses, 
                        Spent_on_Tution_and_living FROM budget_info WHERE
                        Username = ? AND Year = ?""",(username,year))

    elif choice == 'Food':
        cur.execute("""SELECT Food_budget,Spent_on_Food FROM budget_info WHERE
                       Username = ? AND Year = ?""",(username,year))

    elif choice == 'Entertainment':
        cur.execute("""SELECT Entertainment_budget,Spent_on_Entertainment
                       FROM budget_info WHERE
                       Username = ? AND Year = ?""",(username,year))

    elif choice == 'Clothing':
        cur.execute("""SELECT Clothing_budget,Spent_on_Clothing FROM budget_info
                       WHERE Username = ? AND Year = ?""",(username,year))

    elif choice == 'Basic Utilities':
        cur.execute("""SELECT Basic_utilities_budget,Spent_on_Basic_utilities
                       FROM budget_info WHERE
                       Username = ? AND Year = ?""",(username,year))

    elif choice == 'Transport':
        cur.execute("""SELECT Transport_budget,
                       Spent_on_Transport FROM budget_info
                       WHERE Username = ? AND Year = ?""",(username,year))

    elif choice == 'Other':
        cur.execute("""SELECT Other_budget,Spent_on_Other FROM budget_info WHERE
                       Username = ? AND Year = ?""",(username,year))
    #Plotting the graph
    y=cur.fetchall()
    ln=len(y)
    x=[calendar.month_name[month] for month in range(13-ln,13)]
    y1=[value[0] for value in y]
    y2=[value[1] for value in y]

    fig = Figure(figsize = (5,4),dpi = 100)
    subplot=fig.add_subplot(111)
    subplot.plot(x,y1,marker='o',label = choice + " goal",color=pink)
    subplot.plot(x,y2,marker='o',label = choice + " spent",color=yellow)
    canvas2 = FigureCanvasTkAgg(fig, master =root)
    canvas2.draw()
    canvas2.get_tk_widget().place(relx=0.5,rely=0.5,relheight=0.8,relwidth=0.8,\
                                  anchor =CENTER)

    bar = NavigationToolbar2Tk(canvas2,root)
    bar.update()
    
    subplot.set_title(year,fontsize=26,color=grey)
    subplot.grid(True)
    fig.legend()
    fig.tight_layout()
    subplot.set_facecolor(green)
    fig.set_facecolor(green)
    root.mainloop()

def year_selection(username):
    def select_func():
        if years_listbox.curselection() != ():
            year_choice = years_listbox.get(years_listbox.curselection())
            month_selection(username, year_choice)
        else:
            Label(frame1, text = "Please click on the year to select it.", \
                  font = r20, bg = blue, fg = "#800000").place(relx = 0.5, \
                            rely = 0.635, anchor = CENTER)
    #Initializing the screen
    clear_frame()
    label = Label(frame1, text = "Select the year", font = c60, \
                  bg = blue, fg = grey)
    label.place(rely = 0.4, relx = 0.5, anchor = CENTER)
    #list of years
    years_listbox = Listbox(frame1, font = c60, bd = "0px", relief = FLAT, \
                            bg = blue, fg = yellow, justify = "center", \
                            selectmode = SINGLE, selectbackground = green)          
    years_listbox.place(relx = 0.5, rely = 0.55, anchor = CENTER, \
                        relwidth = 0.17, relheight = 0.1)
    #Adding scroll bar
    scrollbar = Scrollbar(years_listbox, orient = "vertical", \
                          command = years_listbox.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    years_listbox.config(yscrollcommand = scrollbar.set)
    
    #Adding options to list box
    cur.execute("SELECT Year FROM budget_info WHERE Username=?",(username,))
    year_list = cur.fetchall()
    first_year = year_list[0][0]
    for year in range(first_year, current_year+1):
        years_listbox.insert(END, year)

    #Buttons
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = lambda: main_screen(username))
    back_button.place( x = 30, y = 30, anchor = NW)

    select_button = Button(frame1, text = "SELECT", bd = "0px", \
                         relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = select_func)
    select_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    root.mainloop()

def month_selection(username, year):

    def btn_func(month):
        cur.execute("""SELECT * FROM budget_info WHERE Username == ? AND
                        Year == ? AND Month ==?""",(username, year, month))
        if cur.fetchone() == None:
            messagebox.showerror("Error","No data to display")                          
        else:
            pie_chart(username, year, month)

    def button(month):
        button = Button(frame1, text = month, bd = "0px", \
                            font = r30, relief = FLAT, bg = blue, fg = peach,\
                            activebackground = blue, activeforeground = pink, \
                            command = lambda: btn_func(month))
        return button
#Initializing the screen
    clear_frame()
    #back button
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = lambda: year_selection(username))
    back_button.place( x = 30, y = 30, anchor = NW)

#label
    select = Label(frame1, text = "Select a month", font = c30, bg = blue, \
                   fg = grey)
    select.place(relx = 0.5, rely = 0.15, anchor = CENTER)

#month buttons
    jan = button("January")
    jan.place(relx = 0.35, rely = 0.25, anchor = CENTER)

    feb = button("February")
    feb.place(relx = 0.35, rely = 0.36, anchor = CENTER)

    mar  = button("March")
    mar.place(relx = 0.35, rely = 0.47, anchor = CENTER)

    apr = button("April")
    apr.place(relx = 0.35, rely = 0.58, anchor = CENTER)

    may = button("May")
    may.place(relx = 0.35, rely = 0.69, anchor = CENTER)

    jun = button("June")
    jun.place(relx = 0.35, rely = 0.8, anchor = CENTER)

    jul = button("July")
    jul.place(relx = 0.65, rely = 0.25, anchor = CENTER)
    
    aug = button("August")
    aug.place(relx = 0.65, rely = 0.36, anchor = CENTER)
    
    sep = button("September")
    sep.place(relx = 0.65, rely = 0.47, anchor = CENTER)
    
    octo = button("October")
    octo.place(relx = 0.65, rely = 0.58, anchor = CENTER)

    nov = button("November")
    nov.place(relx = 0.65, rely = 0.69, anchor = CENTER)
    
    dec = button("December")
    dec.place(relx = 0.65, rely = 0.8, anchor = CENTER)
    
#running the proram
    root.mainloop()

def pie_chart(username, year, month):

    def back_func():
        try:
            debt_label.destroy()
        except:
            None
        legend_frame.destroy()
        canvas3.get_tk_widget().destroy()
        month_selection(username, year)

    def legend(text,rely):
        label = Label(legend_frame, text = text, font = c12, \
                    bg = blue, fg = grey)
        label.place(rely = rely, relx = 0.3, anchor = W)

    def color(color,rely):
        color = Frame(legend_frame, bg = color, width = "1cm", height = "0.5cm")
        color.place(relx = 0.16, rely = rely, anchor = CENTER)    
#Initializing the screen
    clear_frame()
    
    back_button = Button(frame1, text = "BACK", bd = "0px", \
                         border = "0px", relief = FLAT, font = b20, \
                         bg = peach, fg = blue, \
                         activebackground = pink, activeforeground = blue, \
                         command = back_func )
    back_button.place( x = 30, y = 30, anchor = NW)

    cur.execute("""SELECT Monthly_budget,Tution_and_living_expenses,Food_budget, 
                Entertainment_budget, Clothing_budget, Basic_utilities_budget, 
                Transport_budget, Other_budget, Spent_on_Tution_and_living,
                Spent_on_Food, Spent_on_Entertainment, Spent_on_Clothing,
                Spent_on_Basic_utilities, Spent_on_Transport, Spent_on_Other 
                FROM budget_info WHERE Username = ? AND Year = ? AND
                Month = ?""",(username, year, month))
    
    record = cur.fetchone()
    total_budget = record[0]
    goals = [record[x] for x in range(1,8)]
    colors1 = ["#0F52BA",  "#5ac981", "#ce361e", "#f97a25", \
               "#3597CC", "#037272", grey]

    if sum(goals) < total_budget:
        savings = total_budget - sum(goals)
        goals.append(savings)
        colors1.append("#efca08")
        
    fig = Figure(figsize = (4,4),dpi = 100)
    subplot=fig.add_subplot(121)
    subplot.pie(goals, startangle = 45, colors = colors1, \
                textprops = {'color': 'w'})
    circle1 = patches.Circle((0,0),0.6,color = blue)
    subplot.add_artist(circle1)
    canvas3 = FigureCanvasTkAgg(fig, master =root)
    canvas3.draw()
    canvas3.get_tk_widget().place(relx=0.44, rely=0.55, relheight=0.8, \
                                  relwidth=1,anchor =CENTER)
    subplot.set_title("Budget goals",fontsize=26,color=grey)
    fig.tight_layout()
    subplot.set_facecolor(blue)
    fig.set_facecolor(blue)

    spent = [record[x] for x in range(8,15)]
    colors2 = ["#0F52BA",  "#5ac981", "#ce361e", "#f97a25", \
               "#3597CC", "#037272", grey]
    if sum(spent) < total_budget:
        savings = total_budget - sum(spent)
        spent.append(savings)
        colors2.append("#efca08")

    subplot1=fig.add_subplot(1,2,2)
    subplot1.pie(spent, startangle = 45, colors = colors2, \
                 textprops = {'color': 'w'})
    circle2 = patches.Circle((0,0),0.6,color = blue)
    subplot1.add_artist(circle2)
    subplot1.set_title("Expenditure",fontsize=26,color=grey)
    subplot1.set_facecolor(blue)

    #Onscreen headings
    heading = Label(frame1, text = str(month) +' '+ str(year), fg = grey, \
                    bg =blue, font = b40)
    heading.place(relx = 0.5, rely = 0.059, anchor = CENTER)

    if sum(spent) > total_budget:
        debt = sum(spent) - total_budget
        debt_label = Label(root, text = "Debt = "+str(debt), fg = grey, \
                           bg = blue, font = b20)
        debt_label.place(relx = 0.75, rely = 0.85, anchor = CENTER)
    #Legend
    legend_frame = Frame(root, bg = blue, width = "5cm", height = "8cm")
    legend_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    #Tution and living
    legend("Tuition & Living", 0.1)
    color("#0F52BA", 0.1)
    #Food
    legend("Food", 0.2)
    color("#5AC981", 0.2)
    #Entertainment
    legend("Entertainment", 0.3)
    color("#CE361E", 0.3)
    #Clothing
    legend("Clothing", 0.4)
    color("#F97A25", 0.4)
    #Basic Utilities
    legend("Basic Utilities", 0.5)
    color("#3597CC", 0.5)
    #Transport
    legend("Transport", 0.6)
    color("#037272", 0.6)
    #Other
    legend("Other", 0.7)
    color("#93C4A9", 0.7)
    #Savings
    legend("Savings", 0.8)
    color("#EFCA08", 0.8)
        
    root.mainloop()

create_table();
login_screen()
