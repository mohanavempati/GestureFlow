import tkinter as tk

class WelcomeScreen:
    
    def __init__(self):
        self.root = tk.Tk()
        
    def show(self):
        self.root.title("Gesture Flow")
        self.root.geometry("500x500")
        self.root.mainloop()

welcome = WelcomeScreen()
welcome.show()
