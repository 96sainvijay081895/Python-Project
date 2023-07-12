def main_window():
    global entry1, entry2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="Green")
    win.title("Vijay Project")

    label1= Label(win, text="Incorrect spelling", font=("Time New Roman", 25,"bold"), bg="Green", fg="White")
    label1.place(x=100, y=20,height=50,width=300)

    entry1= Entry(win,font=("Time New Roman", 20,))
    entry1.place(x= 50, y= 80, height=50,width=400)

    label2 = Label(win, text="Correct spelling", font=("Time New Roman", 25, "bold"), bg="Green", fg="White")
    label2.place(x=100, y=140, height=50, width=300)

    entry2 = Entry(win, font=("Time New Roman", 20,))
    entry2.place(x=50, y=200, height=50, width=400)

    button= Button(win, text="Done",font=("Time New Roman", 25, "bold"), bg="Yellow", command= correct_spelling )
    button.place(x= 150, y=290, height=50, width=200 )
    win.mainloop()

main_window()