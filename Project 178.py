from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("Project 178")
root.configure(bg = "teal")
name = Label(root, font = ("Times", 24), bg = "teal")
name.place(relx = 0.5, rely = 0.5, anchor = CENTER)

class Game :
    def __init__(self) :
        self.__score = 0
        
    def updateGame(self) :
        self.text = ["blue", "yellow", "red", "green", "orange", "purple", "brown", "black", "white"]
        self.random_number_for_text = random.randint(0,9)
        self.color = ["BLUE", "YELLOW", "RED", "GREEN", "ORANGE", "PURPLE", "BROWN", "BLACK", "WHITE"]
        self.random_number_for_color = random.randint(0,9)
        name['text'] = self.text[self.random_number_for_text]
        name['fg'] = self.color[self.random_number_for_color]

obj1 = Game()
btn1 = Button(root, text = "Start", command = obj1.updateGame, bg = "light skyblue", fg = "black", relief = FLAT, padx = 15, pady = 15, font = ("Times", 15))
btn1.place(relx = 0.5, rely = 0.8, anchor = CENTER)
root.mainloop()