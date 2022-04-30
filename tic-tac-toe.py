from tkinter import *

from tkinter import messagebox







root=Tk()

root.title("Tic Tac Toe.....")





user1=StringVar()

user2=StringVar()



usr1=0

usr2=0



#game should starts by X

clickd=True

cnt=0







#check to see winner for X

def win():

    global winner,usr1,user1,usr2,user2

    winner= False



    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":

        b1.config(bg="black")

        b2.config(bg="black")

        b3.config(bg="black")

        winner= True

        messagebox.showinfo("Tic Tac Toe","Congrats X wins...")

        # button_disable()

        usr1+=1

        user1.set(usr1)

        reset()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":

        b4.config(bg="black")

        b5.config(bg="black")

        b6.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":

        b7.config(bg="black")

        b8.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":

        b1.config(bg="black")

        b4.config(bg="black")

        b7.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()





    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":

        b4.config(bg="black")

        b5.config(bg="black")

        b6.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":

        b2.config(bg="black")

        b5.config(bg="black")

        b8.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":

        b3.config(bg="black")

        b6.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":

        b3.config(bg="black")

        b5.config(bg="black")

        b7.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":

        b1.config(bg="black")

        b5.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats X wins...")

        # button_disable()

        usr1 += 1

        user1.set(usr1)

        reset()

    # check to see winner for O



    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":

        b1.config(bg="black")

        b2.config(bg="black")

        b3.config(bg="black")

        winner= True

        messagebox.showinfo("Tic Tac Toe","Congrats O wins...")

        # button_disable()

        usr2+=1

        user2.set(usr2)

        reset()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":

        b4.config(bg="black")

        b5.config(bg="black")

        b6.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":

        b7.config(bg="black")

        b8.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":

        b1.config(bg="black")

        b4.config(bg="black")

        b7.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()





    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":

        b4.config(bg="black")

        b5.config(bg="black")

        b6.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":

        b2.config(bg="black")

        b5.config(bg="black")

        b8.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":

        b3.config(bg="black")

        b6.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":

        b3.config(bg="black")

        b5.config(bg="black")

        b7.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":

        b1.config(bg="black")

        b5.config(bg="black")

        b9.config(bg="black")

        winner = True

        messagebox.showinfo("Tic Tac Toe", "Congrats O wins...")

        # button_disable()

        usr2 += 1

        user2.set(usr2)

        reset()



    elif cnt == 9 and winner == False:

            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")

            # button_disable()

            reset()



#buttns clicked function

def click(b):

    global clickd,cnt

    if b["text"] == " " and clickd== True:

        b["text"] ="X"

        clickd=False

        cnt=cnt+1

        win()

    elif b["text"] == " " and clickd== False:

        b["text"]="O"

        clickd=True

        cnt=cnt+1

        win()

    else:

        messagebox.showerror("Tic Tac Toe","The button is already clicked \n click another button")

def reset():

   global cnt

   b1["text"]=" "

   b2["text"]=" "

   b3["text"]=" "

   b4["text"]=" "

   b5["text"]=" "

   b6["text"]=" "

   b7["text"]=" "

   b8["text"]=" "

   b9["text"]=" "



   b1.config(bg="white")

   b2.config(bg="white")

   b3.config(bg="white")

   b4.config(bg="white")

   b5.config(bg="white")

   b6.config(bg="white")

   b7.config(bg="white")

   b8.config(bg="white")

   b9.config(bg="white")

   cnt=0

#buttons



b1=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b1))

b2=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b2))

b3=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b3))



b4=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b4))

b5=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b5))

b6=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b6))



b7=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b7))

b8=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b8))

b9=Button(root,text=" ",font=("helvetica",20),height=3,width=6,bg="white",command=lambda : click(b9))





b1.grid(row=0,column=0)

b2.grid(row=0,column=1)

b3.grid(row=0,column=2)



b4.grid(row=1,column=0)

b5.grid(row=1,column=1)

b6.grid(row=1,column=2)



b7.grid(row=2,column=0)

b8.grid(row=2,column=1)

b9.grid(row=2,column=2)



l1=Label(root,text="User_1",font=("Comic Sans MS", 10,"bold"),bg="black",fg="white")

l1.grid(row=3,column=0)

e1=Entry(root,textvariable=user1)

e1.grid(row=3,column=1)



l2=Label(root,text="User_2",font=("Comic Sans MS", 10,"bold"),bg="black",fg="white")

l2.grid(row=4,column=0)

e2=Entry(root,textvariable=user2)

e2.grid(row=4,column=1)





root.mainloop()
