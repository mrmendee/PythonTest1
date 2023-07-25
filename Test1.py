from tkinter import *

root = Tk()
root.title('Full Window Scrolling X Y Scrollbar Example')
root.geometry("1000x500")

main_frame = Frame(root)
canv = Canvas(main_frame,background="white")
ybar = Scrollbar(main_frame,orient="vertical", command=canv.yview)
scr_frame = Frame(canv,background="green")

scr_frame.bind("<Configure>",lambda e: canv.configure(scrollregion=canv.bbox("all")))

canv.create_window((0, 0), window=scr_frame, anchor=NW)
canv.configure(yscrollcommand=ybar.set, highlightthickness=0)

for i in range(50):
    label = Label(scr_frame, text=f"Label-{i}",background="blue",width=9)
    label.grid(row=i, column=0,padx=1,pady=1)
    label.bind("<MouseWheel>", lambda e: canv.yview_scroll(int(-1 * (e.delta)), "units"))

main_frame.pack()
canv.pack(fill=BOTH, side=LEFT, expand=TRUE)
ybar.pack(fill=Y, side=RIGHT)

canv.bind("<MouseWheel>", lambda e: canv.yview_scroll(int(-1 * (e.delta)), "units"))
scr_frame.bind("<MouseWheel>", lambda e: canv.yview_scroll(int(-1 * (e.delta)), "units"))

canv.update()

root.mainloop()
