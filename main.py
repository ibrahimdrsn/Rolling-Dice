import tkinter as tk
from PIL import Image, ImageTk
import random

class Dice:

    def __init__(self, root):
        self.root = root
        self.root.title("Rolling the Dice")
        self.root.geometry("400x400")

        self.image_path = 'cartoon_style_dice.jpg'
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((50, 50))
        self.image = ImageTk.PhotoImage(self.image)

        self.Label_image = tk.Label(self.root, image=self.image)
        self.Label_image.pack()

        self.Button = tk.Button(self.root, text="Generate", command=self.roll_dice)
        self.Button.pack()

        self.Label_text1 = tk.Label(self.root, text="Please click on the button above to roll the dices")
        self.Label_text1.pack()
        self.Label_text2 = tk.Label(self.root, text="")
        self.Label_text2.pack()



    def roll_dice(self):
            dice_value1 = random.randint(1, 6)
            self.Label_text1.config(text=f"First dice value: {dice_value1}")
            dice_value2 = random.randint(1, 6)
            self.Label_text2.config(text=f"Second dice value: {dice_value2}")




if __name__ == "__main__":
    root = tk.Tk()
    app = Dice(root)
    root.mainloop()
