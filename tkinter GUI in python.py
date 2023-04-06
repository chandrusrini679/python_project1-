import tkinter as tk

# create the window
window = tk.Tk()

# create a StringVar to hold the selected option
selected_option = tk.StringVar()

# create the option buttons
option1 = tk.Radiobutton(root, text="OPTION 1", variable=var, value="OPTION 1")
option2 = tk.Radiobutton(root, text="OPTION 2", variable=var, value="OPTION 2")
option3 = tk.Radiobutton(root, text="OPTION 3", variable=var, value="OPTION 3")

# pack the option buttons into the window
option1.pack()
option2.pack()
option3.pack()

window.mainloop()

# This code creates a window using the Tk() function and assigns it to the variable window. It also creates a StringVar
# object named selected_option to hold the currently selected option.

# Then we create three Radiobutton objects, each with a different label and value. The variable parameter is set to
# selected_option to tie them all together, and the value parameter is set to a unique string for each button.

# Finally, we use the pack() method to add the buttons to the window, and start the main event loop using the
# mainloop() method of the root window.

# When the user selects one of the option buttons, the selected_option variable will be updated with the
# corresponding value. You can access the selected value by reading the selected_option.get() method.



