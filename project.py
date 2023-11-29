import tkinter as tk
expression=""
def press (num):
    global expression
    expression=expression+str(num)
# update the equation by using set method
    equation.set(expression)

def equalpress():
    try:
        global expression
        total=set(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")

if __name__=="__main__":
    gui=tk.Tk()
    gui.configure(bg="sky blue")
    gui.title("Simple Calculator!!")
    gui.geometry("300x300")
    