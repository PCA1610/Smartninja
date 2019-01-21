import Tkinter
import tkMessageBox

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Enter a Number between 1 and 100")
greeting.pack()

# guess entry field
number1 = Tkinter.Entry(window)
number1.pack()


# check guess
def fizz_funk():

    for x in range(1, int(number1.get()) + 1):

        if x % 3 == 0 and x % 5 == 0:
            print "fizzbuzz"
        elif x % 3 == 0:
            print "fizz"
        elif x % 5 == 0:
            print "buzz"
        else:
            print x

    tkMessageBox.showinfo("Result", fizz_funk)


# submit button
submit = Tkinter.Button(window, text="Submit", command=fizz_funk)  # check_guess, not check_guess()
submit.pack()

window.mainloop()
