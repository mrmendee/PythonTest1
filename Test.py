import tkinter as tk

root = tk.Tk()

main_frame = tk.Frame(root)
main_frame.grid()

subframe1 = tk.Frame(main_frame, width=200, height=200, bg="red")
subframe1.grid(row=0, column=0)

canvas = tk.Canvas(subframe1, width=200, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(subframe1, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Add your widgets or content to the canvas
for i in range(30):
    label = tk.Label(canvas, text=f"Label {i+1}")
    canvas.create_window(10, i*20, anchor=tk.NW, window=label)

canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()
