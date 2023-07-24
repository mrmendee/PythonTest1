from tkinter import *

root = Tk()
root.title('Full Window Scrolling X Y Scrollbar Example')
root.geometry("1000x800")

main_frame = Frame(root)
main_frame.pack()

canv = Canvas(main_frame, width=500, height=300)
frame = Frame(canv)
ybar = Scrollbar(main_frame)

def createScrollableContainer():
    canv.config(yscrollcommand=ybar.set, highlightthickness=0)
    ybar.config(orient=VERTICAL, command=canv.yview)

    ybar.pack(fill=Y, side=RIGHT, expand=FALSE)
    canv.pack(fill=BOTH, side=LEFT, expand=TRUE)
    canv.create_window(0, 0, window=frame, anchor=NW)

createScrollableContainer()

for i in range(50):
    label = Label(frame, text=f"Label-{i}")
    label.grid(row=i, column=0)

canv.update()
canv.config(scrollregion=frame.bbox())

# マウスホイールイベントをCanvasにバインドする
canv.bind("<MouseWheel>", lambda e: canv.yview_scroll(int(-1 * (e.delta / 120)), "units"))

root.mainloop()
