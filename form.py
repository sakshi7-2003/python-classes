import tkinter as tk
import mysql.connector

connection=mysql.connector.connect(host="localhist",username="root",password="sakshi#2003**",database="data")
couser=connection.cursor()

def savedata():
    n1=en1.get()
    n2=en2.get()
    n3=en3.get()
    print(n1,n2,n3)

couser.execute(f"insert into savedata")
app=tk.Tk()
app.geometry("800x400")
app.title("My Form")
app.configure(bg="yellow")

lbl1=tk.Label(app,text="Name",font=("cursive",20,"italic"))
lbl2=tk.Label(app,text="Phone Number",font=("cursive",20,"italic"))
lbl3=tk.Label(app,text="Email",font=("cursive",20,"italic"))


lbl1.grid(row=1,column=0,pady=10)
lbl2.grid(row=2,column=0,pady=10)
lbl3.grid(row=3,column=0,pady=10)

en1=tk.Entry(app,font=("cursive",20,"italic"))
en2=tk.Entry(app,font=("cursive",20,"italic"))
en3=tk.Entry(app,font=("cursive",20,"italic"))

en1.grid(row=1,column=3)
en2.grid(row=2,column=3)
en3.grid(row=3,column=3)

bt=tk.Button(app,text="submit",command=savedata,font=("cursive",20,"italic"))
bt.grid(row=6,column=3,pady=30,padx=60)

app.mainloop()