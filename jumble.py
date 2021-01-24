# -*- coding: utf-8 -*-

# Import
import tkinter as tk  # import tkinter
from random import choice, shuffle
from tkinter import messagebox, END
from tkinter import ttk
import csv


# Class
class JumbleGUI:

    # class variables
    round = 1
    points = 0
    word = ""
    count_list = []

    def __init__(self):
        # Root
        self.root = tk.Tk()
        self.root.title("Wörter raten")
        self.root.iconbitmap('jumble_icon.ico')
        self.root.geometry("400x400")
        self.root.resizable(0, 0)

        # Style
        s = ttk.Style()
        s.theme_use("vista")
        s.configure("TButton", font="Arial 12")

        # Word Label
        self.label = tk.Label(self.root, text="", font=("Arial", 24), bg=None, height=1, width=19)
        self.label.pack(pady=20)

        # Entry box
        self.entry_answer = ttk.Entry(self.root, font=("Arial", 22))
        self.entry_answer.pack(pady=20)

        # Answer Button
        self.ans_button = ttk.Button(self.root, text="Bewerten", command=self.answer)
        self.ans_button.pack(pady=20)

        # Score Label
        self.score_label = tk.Label(self.root, text="Punkte: ", font=("Arial", 12))
        self.score_label.pack(pady=20)

        # Status bar
        self.statusbar = tk.Label(self.root, text="Runde 1 von 10", width=15)
        self.statusbar.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")

        self.shuffle_func()

        # Mainloop
        self.root.mainloop()


    # Function
    def shuffle_func(self):

        # clear answer entry box
        self.entry_answer.delete(0, END)

        # csv reader
        with open('countries.csv', newline='', encoding="UTF-8") as f:
            reader = csv.reader(f)
            next(reader)
            csv_list = list(reader)

        # create jumble list
        jumble_list = []
        for entry in csv_list:
            jumble_list.append(entry[1])

        # pick random element from list
        JumbleGUI.word = choice(jumble_list)

        # avoid doubles
        while JumbleGUI.word in JumbleGUI.count_list and len(JumbleGUI.count_list) < len(jumble_list):
            word = choice(jumble_list)
        JumbleGUI.count_list.append(JumbleGUI.word)

        # break word into letters
        break_word = list(JumbleGUI.word)
        print(break_word)
        shuffle(break_word)
        print(break_word)

        # turn into word again
        shuffled_word = ""
        for letter in break_word:
            shuffled_word += letter
        print(shuffled_word)

        # print shuffled_word to gui
        self.label.config(text=shuffled_word)


    # Function
    def answer(self):

        # check if word is correct
        if JumbleGUI.word == self.entry_answer.get():
            JumbleGUI.points += 1
            self.ans_label = tk.Label(text="Richtig", fg="green", font=("Arial", 10))
            self.ans_label.pack(pady=20)
            self.root.after(1000, self.ans_label.destroy)
        else:
            self.ans_label = tk.Label(text="Falsch", fg="red", font=("Arial", 10))
            self.ans_label.pack(pady=20)
            self.root.after(1000, self.ans_label.destroy)

        # call shuffle function
        self.shuffle_func()

        # update score label
        self.score_label.configure(text="Punkte: " + str(JumbleGUI.points))

        # check if game ends
        if JumbleGUI.round == 10:
            # clear teh labels
            self.entry_answer.delete(0, END)
            self.label.config(text="")
            # check the points and call msgbox
            if JumbleGUI.points <= 3:
                msg = messagebox.askyesno('Spiel beendet', 'Das war keine gute Leistung!\nDeine Punktzahl beträgt: ' +
                                          str(JumbleGUI.points) + '\nWillst du nocheinmal spielen?')
            elif JumbleGUI.points <= 7:
                msg = messagebox.askyesno('Spiel beendet', 'Das war passabel!\nDeine Punktzahl beträgt: ' +
                                          str(JumbleGUI.points) + '\nWillst du nocheinmal spielen?')
            else:
                msg = messagebox.askyesno('Spiel beendet', 'Tolle Leistung!\nDeine Punktzahl beträgt: ' +
                                          str(JumbleGUI.points) + '\nWillst du nocheinmal spielen?')
            print(msg)
            # handle the click
            if msg == 1:
                self.entry_answer.delete(0, END)
                JumbleGUI.points = 0
                JumbleGUI.round = 0
                self.shuffle_func()
                self.score_label.configure(text="Punkte: " + str(JumbleGUI.points))
            else:
                self.root.destroy()

        # count up round
        if JumbleGUI.round < 10:
            JumbleGUI.round += 1
            self.statusbar.config(text="Runde {} von {}".format(JumbleGUI.round, 10))


# Run
if __name__ == "__main__":
    Jumble = JumbleGUI()
