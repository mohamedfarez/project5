"""
BY: mohamed fares
Imports the `string` and `random` modules, which provide utility functions for working with strings and generating random values.

Also imports the `tkinter` module, which is a standard GUI toolkit for Python. This allows the creation of graphical user interfaces (GUIs) in Python applications.
"""
import string,random
from tkinter import *

"""
Creates a Tkinter window with the title "password Generator by mohamed fares" and sets its size to 500x300 pixels.
"""
Screen= Tk()
Screen.geometry("500x300")
Screen.title("password Generator by mohamed fares")

"""
Sets the title of the application window to "Random Password generator in Python".
"""
Title = StringVar()
TitleLabel = Label(Screen, textvariable=Title).pack()
Title.set("Random Password generator in Python")


"""
Displays a set of radio buttons that allow the user to select an option, and updates a label with the selected option.

The `SelectionOptions()` function is called whenever the user selects a radio button, and it updates the `LabelChoice` label with the selected option.

The radio buttons are created with the following options:
- POOR (value 1)
- AVERAGE (value 2)
- STRONG (value 3)

The `LengthLabel` variable is used to set the text of a label that displays the "Password Length" text.
"""
def SelectionOptions():
    SelectionOptions = Choice.get()
 
Choice= IntVar()
RadioButton1 = Radiobutton(Screen,text="POOR",variable=Choice,value=1,command=SelectionOptions).pack(anchor=CENTER)
RadioButton2 = Radiobutton(Screen,text="AVERAGE",variable=Choice,value=2,command=SelectionOptions).pack(anchor=CENTER)
RadioButton3 = Radiobutton(Screen,text="STRONG",variable=Choice,value=3,command=SelectionOptions).pack(anchor=CENTER)
 
LabelChoice = Label(Screen)
LabelChoice.pack()
 
LengthLabel = StringVar()
LengthLabel.set("Password Length")
LengthTitle = Label(Screen,textvariable=LengthLabel).pack()



"""
Creates a Spinbox widget with a variable to store the selected value.

The Spinbox widget allows the user to select a value from a range of 9 to 25. The selected value is stored in the `Value` variable, which is an instance of `IntVar()`.
"""
Value = IntVar()
SpinLength = Spinbox(Screen, from_=9, to_=25 , textvariable = Value , width = 14).pack()

"""
Generates a random password based on the user's selected password complexity.

The `PassGen()` function generates a random password string of the length specified by the user. The password can be generated with the following complexity levels:

1. Poor: Only uses uppercase and lowercase letters.
2. Average: Uses uppercase and lowercase letters, and digits.
3. Advance: Uses uppercase and lowercase letters, digits, and symbols.

The function returns the generated password string.
"""
Poor = string.ascii_uppercase+string.ascii_lowercase
Average = string.ascii_uppercase+string.ascii_lowercase+string.digits
Symbols="""~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/ """
Advance= Poor+Average+Symbols
 
def PassGen():
    if Choice.get()==1:
        return "".join(random.sample(Poor,Value.get()))
    if Choice.get()==2:
        return "".join(random.sample(Average,Value.get()))
    if Choice.get()==3:
        return "".join(random.sample(Advance,Value.get()))
    


"""
Generates a password and displays it on the screen.

The `CallBack()` function is called when the "generate Password" button is clicked. It generates a password using the `PassGen()` function and updates the text of the `Lsum` label to display the generated password.

The `PassGenButton` is a button that, when clicked, calls the `CallBack()` function to generate and display a new password.

The `Screen.mainloop()` function starts the main event loop, which keeps the application running and responsive to user interactions.
"""
Lsum=Label(Screen,text="")
Lsum.pack(side=BOTTOM)
def CallBack():
    Lsum.config(text=PassGen())
Password=str(CallBack())
PassGenButton = Button(Screen,text="generate Password",bd=5, height=2 ,command=CallBack,pady=3)
PassGenButton.pack()
 
Screen.mainloop()