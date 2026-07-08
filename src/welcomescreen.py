import tkinter as tk


class WelcomeScreen:

    def __init__(self, application):
        self.application = application

        self.root = tk.Tk()
        self.root.title("GestureFlow")
        self.root.geometry("1200x1000")

        label = tk.Label(
            self.root,
            text="WELCOME TO GESTURE FLOW",
            font=("Arial", 50)
        )
        label.pack(pady=50)

        enable_button = tk.Button(
            self.root,
            text="ENABLE",
            command=self.on_enable_clicked
        )
        enable_button.pack(pady=100)

        exit_button = tk.Button(
            self.root,
            text="EXIT",
            command=self.root.destroy
        )
        exit_button.pack()

    def on_enable_clicked(self):
        self.root.destroy()
        self.application.start_camera()

    def show(self):
        self.root.mainloop()
