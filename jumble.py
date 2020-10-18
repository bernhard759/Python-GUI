# -*- coding: utf-8 -*-

# Import
from tkinter import *  # import tkinter
from random import choice, shuffle
from tkinter import messagebox
import csv

# Root
root = Tk()
root.title("Wörter raten")
root.iconbitmap('jumble_icon.ico')
root.geometry("400x400")
root.resizable(0, 0)

# Background
background_image = PhotoImage(file='img1.png') #set background image
background_label = Label(root, image=background_image) #create background label
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Global variable points
global points
points = 0

# Global variable round
global round
round = 1

# Global variable count list
global count_list
count_list = []

# Function
def shuffle_func():

    global count_list

    # clear answer entry box
    entry_answer.delete(0, END)

    # csv reader
    with open('countries.csv', newline='', encoding="UTF-8") as f:
        reader = csv.reader(f)
        csv_list = list(reader)

    # create jumble list
    jumble_list = []
    for entry in csv_list:
            jumble_list.append(entry[1])

    # pick random element from list
    global word
    word = choice(jumble_list)

    # avoid doubles
    while word in count_list and len(count_list) < len(jumble_list):
            word = choice(jumble_list)

    # configure label
    label.config(text=word)
    count_list.append(word)

    # break word into letters
    break_word = list(word)
    print(break_word)
    shuffle(break_word)
    print(break_word)

    # turn into word again
    global shuffled_word
    shuffled_word = ''
    for letter in break_word:
        shuffled_word += letter
    print(shuffled_word)

    # print shuffled_word to screen
    label.config(text=shuffled_word)


# Function
def answer():

    # global variables
    global points
    global round
    global word

    # check if word is correct
    if word == entry_answer.get():
        points += 1
        ans_label = Label(text="Richtig", fg="green", font=("Arial", 10))
        ans_label.pack(pady=20)
        root.after(1000, ans_label.destroy)
    else:
        ans_label= Label(text="Falsch", fg="red", font=("Arial", 10))
        ans_label.pack(pady=20)
        root.after(1000, ans_label.destroy)

    # call shuffle function
    shuffle_func()

    # update score label
    score_label.configure(text="Punkte: " + str(points))

    # check if game ends
    if round == 10:
        # clear teh labels
        entry_answer.delete(0, END)
        label.config(text="")
        # check the points and call msgbox
        if points <=3:
            msg = messagebox.askyesno('Spiel beendet', 'Das war keine gute Leistung!\nDeine Punktzahl beträgt: ' + str(points) + '\nWillst du nocheinmal spielen?')
        elif points <=7:
            msg = messagebox.askyesno('Spiel beendet', 'Das war passabel!\nDeine Punktzahl beträgt: ' + str(points) + '\nWillst du nocheinmal spielen?')
        else:
            msg = messagebox.askyesno('Spiel beendet', 'Tolle Leistung!\nDeine Punktzahl beträgt: ' + str(points) + '\nWillst du nocheinmal spielen?')
        print(msg)
        # handle the click
        if msg == 1:
            entry_answer.delete(0, END)
            shuffle_func()
            points = 0
            round = 0
            shuffle_func()
            score_label.configure(text="Punkte: " + str(points))
        else:
            root.destroy()

    # count up round
    if round < 10:
        round += 1
        statusbar.config(text="Runde {} von {}".format(round, 10))


# Word Label
label = Label(root, text="", font=("Arial", 24), bg=None, height=1, width=19)
label.pack(pady=20)

# Entry box
entry_answer = Entry(root, font=("Arial", 22))
entry_answer.pack(pady=20)

# Answer Button
ans_button = Button(root, text="Bewerten", font=("Arial", 12), command=answer)
ans_button.pack(pady=20)

# Score Label
score_label = Label(root, text="Punkte: " + str(points), font=("Arial", 12))
score_label.pack(pady=20)

# Status bar
statusbar = Label(root, text="Runde 1 von 10", width=15)
statusbar.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


# Run shuffle function
shuffle_func()

# Mainloop
root.mainloop()