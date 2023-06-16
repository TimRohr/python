# Import required modules
import tkinter as tk
from time import strftime

# Function display time, day of week, and date.
def time():
    dt = strftime('%H:%M:%S %p \n %A \n %x')
    label.config(text=dt)
    label.after(1000, time)
    
# Create and configure clock window
def create_clock_window():
    clock = tk.Tk()
    clock.title('Clock')
    return clock

# Configure clock fonts and colors
def configure_clock_text():
    label = tk.Label(clock, font=('calibri', 35, 'bold'), background='black', foreground='green2')
    label.pack(anchor='center')
    return label

# Set Variables for clock settings
clock = create_clock_window()
label = configure_clock_text()

# Invoke time to get time and run continuous loop for the clock.
time() 
tk.mainloop()