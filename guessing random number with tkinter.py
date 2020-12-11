import random
from tkinter import *
root = Tk()
root.title('guessing the number game')
root.geometry('700x500+250+100')



chances = 5
random_guess = random.randint(1, 100)
def guess(user2):
    my_guess = int(float(user2))
    if my_guess > random_guess:
        alert(my_guess, 'h', random_guess)
    elif my_guess < random_guess:
        alert(my_guess, 'l', random_guess)
    elif my_guess == random_guess:
        alert(my_guess, 'c', random_guess)

label = Label(root, text=f'Number of chances left: ({chances})', 
        font=('Arial', 30, 'bold', 'italic'), fg='orange')
label.pack()
Label(root, text='the computer has chosen a random number between 1 & 100, try to guess the number.\nyou only have 5 chances!', 
        font=('Consolas', 15, 'bold')).pack(pady= 20)
user = Entry(root,width=15)
user.pack()
button = Button(root, text="Click me!", command=lambda:guess(user.get()))
button.pack(pady= 5)


def alert(x, res,y):
    global chances
    global user
    global button
    global label
    if res == 'h':
        Label(root, text=f'{x} is too high!').pack(pady=10)
        user.delete(0,END)
        chances -= 1
        label.config(text=f'Number of chances left: ({chances})')
        if chances == 0:
            Label(root, text=f'HARD LUCK! YOU\'VE LOST :(\n the number was {y}',
         font=('Tohoma', 25, 'bold'), fg='red').pack(pady=10)
            user.configure(state=DISABLED)
            button.config(state=DISABLED)
    elif res == 'l':
        Label(root, text=f'{x} is too low!').pack(pady=10)
        user.delete(0,END)
        chances -= 1
        label.config(text=f'Number of chances left: ({chances})')
        if chances == 0:
            Label(root, text=f'HARD LUCK! YOU\'VE LOST :(\n the number was {y}',
         font=('Tohoma', 25, 'bold'), fg='red').pack(pady=10)
            user.configure(state=DISABLED)
            button.config(state=DISABLED)
    else:
        Label(root, text=f'your guess is correct! {x} is the number',
         font=('Tohoma', 25, 'bold'), fg='green').pack(pady=10)
        user.configure(state=DISABLED)
        button.config(state=DISABLED)
    
root.mainloop()

