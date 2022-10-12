file=open("car_details.txt", "a")
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


def up():

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="car_rental_owner")
    mycursor = mydb.cursor()
    uname = f1.get()
    password = f2.get()

    SQL="select * from login where uname= %s and password= %s"
    mycursor.execute(SQL, [(uname), (password)])
    result = mycursor.fetchall()

    if(uname == "" and password == ""):
        messagebox.showinfo("", "blank not allowed!!")

    elif result:
        messagebox.showinfo("", "login successfully")
        foot.destroy()
        
        x=1
        while x>0:
            def ok():
                v_no = e1.get()
                model = e2.get()
                colour = e3.get()
                no_of_seat = e4.get()
                d_name = e5.get()
                d_tp = e6.get()

                file.write("v_no : " + v_no + "\n")
                file.write("model : " + model + "\n")
                file.write("colour : " + colour + "\n")
                file.write("no_of_seat : " + no_of_seat + "\n")
                file.write("d_name : " + d_name + "\n")
                file.write("d_tp : " + d_tp + "\n")
                file.write("################" + "\n")
                file.close()

                if(v_no == "" and model == "" and colour == "" and no_of_seat == "" and d_name == "" and d_tp == "" ):
                    messagebox.showinfo("", "blank not allowed")
                    root.destroy()
                    return()

                else:
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="car_rental_system")
                    mycursor = mydb.cursor()


                    SQL="insert into car(v_no,model,colour,no_of_seat,d_name,d_tp) values(%s,%s,%s,%s,%s,%s)"
                    VAL=(v_no,model,colour,no_of_seat,d_name,d_tp)
                    mycursor.execute(SQL,VAL)
                    mydb.commit()
                    messagebox.showinfo("information","record inserted successfully...")
                    e1.delete(0, 'end')
                    e2.delete(0, 'end')
                    e3.delete(0, 'end')
                    e4.delete(0, 'end')
                    e5.delete(0, 'end')
                    e6.delete(0, 'end')

            root = Tk()
            root.title("car rental")
            root.geometry("470x500")
            root.configure(bg='blue')
            global e1
            global e2
            global e3
            global e4
            global e5
            global e6

            Label(root, text="CAR RENTAL", width=27,height = 2, fg="black", font=("Times New Roman", 25)).place(x=0, y=5)
            Label(root, text="vehicle no :", width=12, font=("Arial", 10), fg="black" ).place(x=10, y=100)
            Label(root, text="model :", width=12, font=("Arial", 10), fg="black" ).place(x=10, y=150)
            Label(root, text="colour :", width=12, font=("Arial", 10) , fg="black").place(x=10, y=200)
            Label(root, text="no of seat :", width=12, font=("Arial", 10) , fg="black").place(x=10, y=250)
            Label(root, text="driver name :", width=12, font=("Arial", 10), fg="black" ).place(x=10, y=300)
            Label(root, text="driver phone no :", width=12, font=("Arial", 10) , fg="black").place(x=10, y=350)
            Label(root, width=100, bg="red", fg="red").place(x=0, y=480)
            Label(root, text="",width=70,bg="red", fg="black", font=("Arial", 10)).place(x=0, y=480)
            answer=Label(root,text="", font=("Arial", 10), fg="black" ).place(x=180, y=60)

            e1 = Entry(root, width=30)
            e1.place(x=140, y=100)

            e2 = Entry(root, width=30)
            e2.place(x=140, y=150)

            e3 = Entry(root, width=30)
            e3.place(x=140, y=200)

            e4 = Entry(root, width=30)
            e4.place(x=140, y=250)

            e5 = Entry(root, width=30)
            e5.place(x=140, y=300)

            e6 = Entry(root, width=30)
            e6.place(x=140, y=350)

            Button(root, text="SUBMIT", command=ok, bg="yellow", font="Helvetica", fg="black",height = 3, width = 13).place(x=160, y=400)

            root.mainloop()
        
    else:
        messagebox.showinfo("", "incorrect username and password")
        f1.delete(0, 'end')
        f2.delete(0, 'end')

def dp():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="car_rental_owner")
    mycursor = mydb.cursor()
    uname = f1.get()
    password = f2.get()

    SQL="insert into login(uname,password) values(%s,%s)"
    VAL=(uname,password)
    mycursor.execute(SQL,VAL)
    mydb.commit()
    messagebox.showinfo("information","record inserted successfully...")
    f1.delete(0, 'end')
    f2.delete(0, 'end')


foot = Tk()
foot.title("login page")
foot.geometry("300x300")
foot.configure(bg='pink')
global f1
global f2

Label(foot, text="CAR RENTAL LOGIN", width=35,height = 1, fg="black", font=("Times New Roman", 12)).place(x=0, y=5)
Label(foot, text="username : ",).place(x=10, y=50)
Label(foot, text="password : ",).place(x=10, y=100)

f1 = Entry(foot)
f1.place(x=140, y=50)

f2 = Entry(foot)
f2.place(x=140, y=100)
f2.config(show="*")

Button(foot, text="LOGIN", command=up, height=2, width=10).place(x=40, y=160)
Button(foot, text="registry", command=dp, height=2, width=10).place(x=150,y=160)

foot.mainloop()

