import tkinter as tk
from tkinter import Canvas, Toplevel

def Progress_Anim(root, progress_value=0):
    global canvas

    def update_progress(new_value):
        global canvas
        if 0 <= new_value <= 100:
            canvas.delete("progress_bar")
            bar_width = int((new_value / 100) * canvas_width)
            canvas.create_rectangle(0, 0, bar_width, canvas_height, fill="blue", outline="blue", tags="progress_bar")

    canvas_width = 400
    canvas_height = 20

    # Create a transparent toplevel window
    transparent_window = Toplevel(root)
    transparent_window.overrideredirect(True)
    transparent_window.attributes('-alpha', 0.8)
    transparent_window.geometry('400x20+545+600')
    transparent_window.config(bg='black')

    # Create a canvas on the transparent window
    canvas = Canvas(transparent_window, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    update_progress(progress_value)

# Create a Tkinter window
root = tk.Tk()
root.title("Progress Bar")

# Example usage: Progress_Anim with parameter value (e.g., progress_value = 50)
Progress_Anim(root, progress_value=50)

root.mainloop()
