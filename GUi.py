import tkinter as tk
from tkinter import scrolledtext
import Database_of_student
import register_student
#import button3_code

# Function to update current text display
def update_current_text(event):
    current_text.set(text_input.get())

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create three buttons
button1 = tk.Button(button_frame, text="Data base", command=lambda: Database_of_student.run(output_box))
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(button_frame, text="Register", command=lambda: register_student.run(output_box))
button2.pack(side=tk.LEFT, padx=5)

'''button3 = tk.Button(button_frame, text="Button 3", command=lambda: button3_code.run(output_box))
button3.pack(side=tk.LEFT, padx=5)'''

# Create a text input box
text_input = tk.Entry(root, width=50)
text_input.pack(pady=10)
text_input.bind("<KeyRelease>", update_current_text)

# Create a box to display the current text being typed
current_text = tk.StringVar()
current_text_label = tk.Label(root, textvariable=current_text, bg="lightgray", width=50, height=2)
current_text_label.pack(pady=5)

# Create an output box
output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(pady=10)

# Start the GUI event loop
root.mainloop()
