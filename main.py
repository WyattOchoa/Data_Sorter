import tkinter as tk
import pandas as pd

def browse():
    global user_file
    #Global variable for use in functions 1-6
    from tkinter.filedialog import askopenfilename
    user_file = askopenfilename()
    #asks tkinter to open a file that is defined as user_file
    browselabel.config(text=user_file)
    #updates the topframe browse label with the file path selected by the user

def browsesave():
    global save_file
    from tkinter import filedialog
    save_file = filedialog.asksaveasfilename()
    savelabel.config(text=save_file)

def op1():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file = (user_file.sort_values('Name'))
    #function 1-6 all use the pandas function of sort_values for data sorting
    user_file.to_csv(save_file, index=False)
    #functions 1-6 also use pandas to_csv without indexing to save the file in the selected .csv file

def op2():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file = (user_file.sort_values('Name', ascending=False))
    #ascending=False to sort in descending order
    user_file.to_csv(save_file, index=False)

def op3():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file = (user_file.sort_values('IP'))
    user_file.to_csv(save_file, index=False)

def op4():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file = (user_file.sort_values('IP', ascending=False))
    user_file.to_csv(save_file, index=False)

def op5():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file =  (user_file.sort_values('Date Captured'))
    user_file.to_csv(save_file, index=False)

def op6():
    global user_file
    user_file = pd.read_csv(user_file)
    user_file = (user_file.sort_values('Missing Patches'))
    user_file.to_csv(save_file, index=False)

root = tk.Tk()
#root window for tkinter
canvas = tk.Canvas(root, height=300, width=500)
canvas.pack()

topframe = tk.Frame(root, bg='#21c2c4')
topframe.place(relx=.01, rely=.01, relwidth=.98, relheight=.15)
#Establishes a frame in root to house other widgets

label = tk.Label(topframe, text="Step 1: Select CSV File for Analysis:", bg="#ceded2" )
label.place(relx=.01, rely=.02, relwidth=.40, relheight=.4)

button = tk.Button(topframe, text="Browse", bg="yellow", command=browse)
#command=browse is used to activate the browse function when clicking the button
button.place(relx=.42, rely=.02, relwidth=.1, relheight=.4)

browselabel = tk.Label(topframe, text='', bg="white")
browselabel.place(relx=.01, rely=.5, relwidth=.98, relheight=.4)

midframe = tk.Frame(root, bg='#21c2c4')
midframe.place(relx=.01, rely=.17, relwidth=.98, relheight=.15)

label = tk.Label(midframe, text="Step 2: Select output location for sorted File:", bg="#ceded2" )
label.place(relx=.01, rely=.02, relwidth=.5, relheight=.4)

button = tk.Button(midframe, text="Browse", bg="yellow", command=browsesave)
button.place(relx=.52, rely=.02, relwidth=.1, relheight=.4)

savelabel = tk.Label(midframe, text="", bg="white" )
savelabel.place(relx=.01, rely=.5, relwidth=.98, relheight=.4)
botframe = tk.Frame(root, bg='#21c2c4')

botframe.place(relx=.01, rely=.33, relwidth=.98, relheight=.66)

label = tk.Label(botframe, text="Step 3: How would you like the data sorted?", bg="#ceded2" )
label.place(relx=.01, rely=.02, relwidth=.50, relheight=.1)

button = tk.Button(botframe, text="Alphabetized", bg="pink", command=op1)
button.place(relx=.01, rely=.2, relwidth=.3, relheight=.25)

button = tk.Button(botframe, text="IPs", bg="pink", command=op3)
button.place(relx=.35, rely=.2, relwidth=.3, relheight=.25)

button = tk.Button(botframe, text="Date Captured", bg="pink", command=op5)
button.place(relx=.69, rely=.2, relwidth=.3, relheight=.25)

button = tk.Button(botframe, text="Alphabetized Desc.", bg="pink", command=op2)
button.place(relx=.01, rely=.6, relwidth=.3, relheight=.25)

button = tk.Button(botframe, text="IPs Desc.", bg="pink", command=op4)
button.place(relx=.35, rely=.6, relwidth=.3, relheight=.25)

button = tk.Button(botframe, text="Missing Patches", bg="pink", command=op6)
button.place(relx=.69, rely=.6, relwidth=.3, relheight=.25)

root.mainloop()
#end of the root tkinter window