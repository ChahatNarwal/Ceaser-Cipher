import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *


# Creating a window
root = tk.Tk()
# For changing the title of the title bar
root.title("Ceaser Cipher ")
root.geometry("500x500")
root.resizable(width=FALSE, height=FALSE)


canvas = tk.Canvas(root,height = 500, width=500, bg= "Lavender" )
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")

# Creating a label with a text and attaching it to the root
label1 = tk.Label(root,text= "Enter the Text",width=20,bg="Lavender")
label1.config(font=bold_font)
canvas.create_window(250,80,window=label1)
user_text = tk.Entry(root,width = 40)
canvas.create_window(250,130,window=user_text)


#Another Label for Key
label2 = tk.Label(root,text= "Enter the Key",width=20,bg="Lavender")
label2.config(font=bold_font)
canvas.create_window(250,180,window=label2)
user_key = tk.Entry(root)
canvas.create_window(250,230,window=user_key)

# Label for choice
label3=tk.Label(root,text="Choose an Operation",width=25,bg="Lavender")
label3.config(font=bold_font)
canvas.create_window(250,290,window=label3)
v = tk.IntVar()
def choice():
  # Retrieve the value of the radio button
    x = v.get()
  # Performs Encryption if the value is 1 else performs Decryption.
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

# Defined a function Encryption
def encryption():
    plain_text = user_text.get()
  # To store the result
    cipher_text = ""
  # Number of shift to be performed.
    key = int(user_key.get())
    #traversing the text
    for char in plain_text.upper():
        if char.isalpha():
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher_text += char
    '''for i in range(len(plain_text)):
        letter = plain_text[i]
  # UpperCase Condition
        if(letter.isupper()):
            cipher_text += chr((ord(letter)+key-65)%26+65)
        else:
  # LowerCase Condition
            cipher_text += chr((ord(letter)+key-97)%26+97)'''
  # Creating a label with a text and attaching it to the root
    #label4 =tk.Label(root,text=cipher_text,width = 20,pady = 5,bg="LightSalmon")
    label4 = Entry(root, text = cipher_text,width = 40)
    label4.insert(0,cipher_text)
  # adding the font features to the label
    label4.config(font=bold_font)
  # placing the label in the canvas
    canvas.create_window(250,420,window=label4)

def decryption():
    cipher_text = user_text.get()
    plain_text = ""
  # Number of shifts to be performed.
    key = int(user_key.get())
  # Traversing the text
    for char in cipher_text.upper():
      if char.isalpha():
        plain_text += chr((ord(char) - key - 65) % 26 + 65)
      else:
        plain_text += char
    '''for i in range(len(cipher_text)):
        letter = cipher_text[i]
  # Uppercase condition
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
  # Lowercase condition
            plain_text+=chr((ord(letter)-key-97)%26+97)'''
  # Creating a label with a text and attaching it to the root
    #label5 =tk.Label(root,text=plain_text,bg="LightSalmon")
    label5 = Entry(root, text=plain_text, width=40)
    label5.insert(0, plain_text)
  # Adding the font features to the label
    label5.config(font=bold_font)
  # Placing the label in the canvas
    canvas.create_window(250,420,window=label5)

# Radio Button for Encryption
label6=tk.Radiobutton(root, text="Encrypt",padx = 20, variable=v, value=1,command=choice, relief = RAISED,borderwidth = 5 ,bg="Thistle")
label6.config(font=bold_font)
canvas.create_window(150,330,window=label6)
# Radio Button for Decryption
label7=tk.Radiobutton(root, text="Decrypt",padx = 20, variable=v, value=2,command=choice,relief = RAISED,borderwidth = 5,bg="Thistle")
label7.config(font=bold_font)
canvas.create_window(350,330,window=label7)

# Creating a label with a text and attaching it to the root
label8 =tk.Label(root,text="Converted Text :",width=15,bg = "Lavender")
# adding the font features to the label
label8.config(font= bold_font)
# placing the label in the canvas
canvas.create_window(250,380,window=label8)

# creating a function to reset the entries
def clearFunc() :
    user_text.delete(0,'end')
    user_key.delete(0,'end')

# Reset Button
Reset=tk.Button(root,text="Reset",command=clearFunc,padx = 15, pady = 1, bg = "PapayaWhip")
Reset.config(font = bold_font)
canvas.create_window(250,470, window = Reset)

root.mainloop()