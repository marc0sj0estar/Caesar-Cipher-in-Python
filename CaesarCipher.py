import tkinter as tk
from tkinter import scrolledtext as st
from math import *
from ctypes import windll

# Caesar ciphers the input
def Shift(sliderValue):
    output.config(state = tk.NORMAL)
    result = ""
    shiftAmount = int(sliderValue)

    for char in inputText.get("1.0", tk.END):
        newChar = ""
        if char.isalpha():
            if char.isupper():
                newChar = chr(65 + (ord(char) - 65 + shiftAmount) % 26) #uppercase
            else:
                newChar = chr(97 + (ord(char) - 97 + shiftAmount) % 26) #lowercase
            result += newChar
        else:
            result += char
            
    output.delete("1.0", tk.END)
    output.insert("1.0", result)
    output.config(state = tk.DISABLED)

# Updates the output when the input is changed
def UpdateOutput(event):
    Shift(slider.get())

# Main window
windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x500")

# Input Window
inputText = st.ScrolledText(root, width = 50, height = 10)
inputText.pack(pady = 20)
inputText.bind("<KeyRelease>", UpdateOutput)

# Shift Slider
sliderLabel = tk.Label(root, text = "Shift Amount")
sliderLabel.pack()

slider = tk.Scale(root, length=400, from_= -25, to = 25, orient = "horizontal", command = Shift)
slider.pack()

# Ouput text
output = st.ScrolledText(root, width = 50, height = 10, state = tk.DISABLED)
output.pack(pady = 20)
root.mainloop()