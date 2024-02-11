import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import subprocess
from PIL import Image, ImageTk



class CongratulationsPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Congratulations")

        # Create a Style object to use with ttkbootstrap
        self.style = Style(theme="superhero")  # Set the theme to 'superhero'

        # Set background color to white
        self.configure(bg="#ffffff")  # White background color

        # Message Label with customized text color and background color
        self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#000000", background="#ffffff")
        self.message_label.pack(pady=50)

        # # Green Tick Image
        # self.blue_tick_image = tk.PhotoImage(file="greentick.png")  # Replace with the path to your blue tick image
        # self.resized_image = self.blue_tick_image.subsample(4,4)
        # self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#ffffff")
        # self.blue_tick_label.pack()

        # Green Tick Image
        self.blue_tick_image = tk.PhotoImage(file=".\greentick.png")  # Replace with the path to your blue tick image
        self.resized_image = self.blue_tick_image.subsample(4,4)
        self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#ffffff")
        self.blue_tick_label.image = self.resized_image  # Keep a reference to the image
        self.blue_tick_label.pack()






        # Frame to contain the buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=30)

        # Deny Button with customized background and text color
        self.take_test_button = ttk.Button(self.button_frame, text="No! Thanks", command=self.additional_action, style="success.Outline")
        self.take_test_button.pack(side=tk.LEFT, padx=10)

        def on_take_test_button_clicked():
            self.additional_action()
            subprocess.Popen(["python", "quiz.py"])
            #quiz.QuizApp()

        # Take Test Button
        self.additional_button = ttk.Button(self.button_frame, text="Take Test", command=self.take_test, style="success.Outline")
        self.additional_button.pack(side=tk.LEFT, padx=30)

        # def on_take_test_button_clicked():
        #     self.additional_action()        
            
            

        # self.additional_button = ttk.Button(self.button_frame, text="Take Test", style="success.Outline")
        # self.additional_button.pack(side=tk.LEFT, padx=30)

    def take_test(self):
        print("Redirecting to the test page...")
          # Placeholder for redirection functionality
        subprocess.call(["python", "quiz.py"])
    def additional_action(self):
        print("Additional button clicked.")  # Placeholder for additional button functionality
        subprocess.call(["python", "recommendation.py"])

# app = CongratulationsPage()
# app.mainloop()