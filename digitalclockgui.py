from tkinter import Label, Tk 
import time

# Create the main application window
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1, 1)  # Allows resizing

# Define clock styles
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"  # Light yellow
foreground = "#363529"  # Dark brown
border_width = 25

# Create the clock label
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=0)  # Changed column index from 1 to 0 for better alignment

# Function to update the clock
def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")  # Get current time
    label.config(text=time_live)  # Update label text
    label.after(1000, digital_clock)  # Refresh every second (1000ms)

# Start the clock
digital_clock()

# Run the Tkinter event loop
app_window.mainloop()
