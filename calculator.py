import tkinter as tk
import math

window = tk.Tk()
window.title("Calculator")
window.geometry("360x360")
window.config(bg="#000000")
window.resizable(False, False) #When the window get resized, my alignment is ruined. So I disabled it.

display = tk.Label(window, width=25, height=2, relief=tk.SUNKEN, anchor=tk.E, bg="#191919", fg="white", bd=0)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky=tk.W+tk.E)

#Calculating the result
def calculate_result(expression):
    try:
        #For some operators I've set different icons. So i am replacing it here. 
        expression = expression.replace("mod", "%")
        expression = expression.replace("root", "math.sqrt")
        result = eval(expression) #I am using eval to evaluate expression because python made it sooo easy;)
        return result
    except:
        return "Error"



#Displaying all the elements
def button_click(number):
    current_text = display.cget("text")  # Get the current text of the display label
    display.config(text=current_text + str(number))  # Update the text by appending the clicked number

def button_backspace_command():
    current_text = display.cget("text")
    try:
        int(current_text)
        display.config(text="")
    except ValueError:
        if current_text == "Error":
            display.config(text="")
        else:
            display.config(text=current_text[:-1])


def button_open_bracket_command():
    current_text = display.cget("text")
    display.config(text=current_text + "(")

def button_close_bracket_command():
    current_text = display.cget("text")
    display.config(text=current_text + ")")

def button_mod_command():
    current_text = display.cget("text")
    display.config(text=current_text + "mod")

def button_pi_command():
    current_text = display.cget("text")
    display.config(text=current_text + "3.14")

def button_division_command():
    current_text = display.cget("text")
    display.config(text=current_text + "/")

def button_root_command():
    current_text = display.cget("text")
    display.config(text=current_text + "root(")

def button_multiplication_command():
    current_text = display.cget("text")
    display.config(text=current_text + "*")

def button_square_command():
    current_text = display.cget("text")
    display.config(text=current_text + "**2")

def button_minus_command():
    current_text = display.cget("text")
    display.config(text=current_text + "-")

def button_cube_command():
    current_text = display.cget("text")
    display.config(text=current_text + "**3")

def button_dot_command():
    current_text = display.cget("text")
    display.config(text=current_text + ".")

def button_percentage_command():
    current_text = display.cget("text")
    display.config(text=current_text + "%")

def button_plus_command():
    current_text = display.cget("text")
    display.config(text=current_text + "+")

def button_equal_command():
    current_text = display.cget("text")
    result = calculate_result(current_text)
    if result == "Error":
        display.config(text=result)
    else:
        display.config(text=str(result))



# Row one of buttons
button_backspace = tk.Button(window, text="C", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_backspace_command)
button_backspace.grid(row=1, column=0, padx=5, pady=5)

button_open_bracket = tk.Button(window, text="(", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_open_bracket_command)
button_open_bracket.grid(row=1, column=1, padx=5, pady=5)

button_close_bracket = tk.Button(window, text=")", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_close_bracket_command)
button_close_bracket.grid(row=1, column=2, padx=5, pady=5)

button_mod = tk.Button(window, text="mod", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_mod_command)
button_mod.grid(row=1, column=3, padx=5, pady=5)

button_pi = tk.Button(window, text="pi", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_pi_command)
button_pi.grid(row=1, column=4, padx=5, pady=5)


# Row two of buttons
button_seven = tk.Button(window, text="7", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(7))
button_seven.grid(row=2, column=0, padx=5, pady=5)

button_eight = tk.Button(window, text="8", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(8))
button_eight.grid(row=2, column=1, padx=5, pady=5)

button_nine = tk.Button(window, text="9", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(9))
button_nine.grid(row=2, column=2, padx=5, pady=5)

button_division = tk.Button(window, text="/", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_division_command)
button_division.grid(row=2, column=3, padx=5, pady=5)

button_root = tk.Button(window, text="root", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_root_command)
button_root.grid(row=2, column=4, padx=5, pady=5)

# Row three of buttons
button_four = tk.Button(window, text="4", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(4))
button_four.grid(row=3, column=0, padx=5, pady=5)

button_five = tk.Button(window, text="5", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(5))
button_five.grid(row=3, column=1, padx=5, pady=5)

button_six = tk.Button(window, text="6", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(6))
button_six.grid(row=3, column=2, padx=5, pady=5)

button_multiplication = tk.Button(window, text="x", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=button_multiplication_command)
button_multiplication.grid(row=3, column=3, padx=5, pady=5)

button_square = tk.Button(window, text="sqr", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_square_command)
button_square.grid(row=3, column=4, padx=5, pady=5)

# Row four of buttons
button_one = tk.Button(window, text="1", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(1))
button_one.grid(row=4, column=0, padx=5, pady=5)

button_two = tk.Button(window, text="2", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(2))
button_two.grid(row=4, column=1, padx=5, pady=5)

button_three = tk.Button(window, text="3", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(3))
button_three.grid(row=4, column=2, padx=5, pady=5)

button_minus = tk.Button(window, text="-", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_minus_command)
button_minus.grid(row=4, column=3, padx=5, pady=5)

button_cube = tk.Button(window, text="cube", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_cube_command)
button_cube.grid(row=4, column=4, padx=5, pady=5)

# Row five of buttons
button_zero = tk.Button(window, text="0", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command=lambda: button_click(0))
button_zero.grid(row=5, column=0, padx=5, pady=5)

button_dot = tk.Button(window, text=".", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_dot_command)
button_dot.grid(row=5, column=1, padx=5, pady=5)

#I have no idea why I am including this, and also I am lazy to create some function for percentage
button_percentage = tk.Button(window, text="%", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_percentage_command)
button_percentage.grid(row=5, column=2, padx=5, pady=5)

button_plus = tk.Button(window, text="+", width=5, height=2, bd=0, bg='#191919', fg="white", highlightthickness=0, command= button_plus_command)
button_plus.grid(row=5, column=3, padx=5, pady=5)

button_equal = tk.Button(window, text="=", width=5, height=2, bd=0, bg='red', fg="white", highlightthickness=0, command= button_equal_command)
button_equal.grid(row=5, column=4, padx=5, pady=5)


window.columnconfigure(0, weight=1)

window.mainloop()
