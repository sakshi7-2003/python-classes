import tkinter as tk
app=tk.Tk()

app.geometry("600x500")
app.title("FaceBook")
app.configure(bg="black")

frame=tk.Frame(app,width=600,height=500)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)

lb1=tk.Label(app,text="Name",font=("cursive",20,"italic"),bg="white",fg="grey")
lb2=tk.Label(app,text="LastName",font=("cursive",20,"italic"),bg="white",fg="grey")
lb3=tk.Label(app,text="Password",font=("cursive",20,"italic"),bg="white",fg="grey")

lb1.grid(row=1,column=3,pady=20,padx=40)
lb2.grid(row=2,column=3,pady=20,padx=40)
lb3.grid(row=3,column=3,pady=20,padx=40)

en1=tk.Entry(app,font=("cursive",20,"italic"),bg="white",fg="grey")
en2=tk.Entry(app,font=("cursive",20,"italic"),bg="white",fg="grey")
en3=tk.Entry(app,font=("cursive",20,"italic"),bg="white",fg="grey")

en1.grid(row=1,column=5)
en2.grid(row=2,column=5)
en3.grid(row=3,column=5)

bt1=tk.Button(app,text="Retry",font=("cursive",20,"italic"),bg="white",fg="grey")
bt2=tk.Button(app,text="Submit",font=("cursive",20,"italic"),bg="white",fg="grey")

bt1.grid(row=4,column=3,pady=20)
bt2.grid(row=4,column=5,pady=20)

app.mainloop()