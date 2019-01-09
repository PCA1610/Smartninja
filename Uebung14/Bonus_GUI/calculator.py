import Tkinter
import tkMessageBox

window = Tkinter.Tk()

# greeting text
title = Tkinter.Label(window, text="CALCULATOR")
title.pack()

# guess entry field
number1 = Tkinter.Entry(window)
number1.pack()
number2 = Tkinter.Entry(window)
number2.pack()


# ADDITION
def addition():
    result = int(number1.get()) + int(number2.get())

    tkMessageBox.showinfo("Result", result)


def subtraction():
    result = int(number1.get()) - int(number2.get())

    tkMessageBox.showinfo("Result", result)


def multiplication():
    result = int(number1.get()) * int(number2.get())

    tkMessageBox.showinfo("Result", result)


def division():
    result = int(number1.get()) / int(number2.get())

    tkMessageBox.showinfo("Result", result)


# add button
add_button = Tkinter.Button(window, text="+", command=addition)  # check_guess, not check_guess()
add_button.pack()
# add button
subtraction_button = Tkinter.Button(window, text="-", command=subtraction)  # check_guess, not check_guess()
subtraction_button.pack()
# add button
multiplication_button = Tkinter.Button(window, text="*", command=multiplication)  # check_guess, not check_guess()
multiplication_button.pack()
# add button
division_button = Tkinter.Button(window, text="/", command=division)  # check_guess, not check_guess()
division_button.pack()

window.mainloop()
