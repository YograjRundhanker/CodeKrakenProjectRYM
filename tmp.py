import tkinter as tk
from PIL import Image, ImageTk

def fade_to_black():
    global alpha
    alpha -= fade_step
    if alpha <= 0:
        alpha = 0
    set_background_color()
    if alpha > 0:
        root.after(fade_speed, fade_to_black)

def set_background_color():
    hex_color = "#{:02X}{:02X}{:02X}".format(0, 0, 0)
    root.configure(bg=hex_color)
    root.attributes("-alpha", alpha)

# Create the main window
root = tk.Tk()
root.title("Background Fade Animation")

# Set initial alpha (transparency) value
alpha = 255

# Set fade step and speed
fade_step = 5
fade_speed = 50  # milliseconds

# Create a label to fill the window
label = tk.Label(root, text="Window with Fading Background", font=("Helvetica", 16))
label.pack(fill=tk.BOTH, expand=True)

# Call the fade_to_black function to start the fade animation
fade_to_black()

# Start the Tkinter main loop
root.mainloop()
