import tkinter as tk

class App:
    def __init__(self, root : tk.Tk = None):
        self.root :tk.Tk = root
        self.root.title("Hi")
        self.root.geometry("400x200")
        
        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid()

        # top frame
        self.top_frame = tk.Frame(self.main_frame,bg="red",width=200,height=100)
        self.top_frame.grid(row=0,column=0)
        
        # left frame
        self.left_frame = tk.Frame(self.main_frame,bg="green",width=200,height=100)
        self.left_frame.grid(row=1,column=1)
        self.button = tk.Button(self.left_frame, text="Click me!", command=self.button_clicked)
        self.button.place(x=0,y=0)
    
    def button_clicked(self):
        self.label.config(text="Button clicked!")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    
    app = App(root)
    app.run()
