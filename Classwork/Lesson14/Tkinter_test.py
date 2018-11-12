import Tkinter
import random
import tkMessageBox

secret_num = random.randint(1,100)


def check_guess():
    user_number = int(guess.get())
    if user_number == secret_num:
        tkMessageBox.showinfo("Result", "Uganil si")
    else:
        tkMessageBox.showinfo("Result", "Nisi uganil")


main_window = Tkinter.Tk()
main_window.title("Guess the number")

greeting_label = Tkinter.Label(main_window, text="Guess the secet number between 1 and 100")
greeting_label.pack()

guess = Tkinter.Entry(main_window)
guess.pack()

button = Tkinter.Button(main_window, text="Check", command=check_guess)
button.pack()


main_window.mainloop()


