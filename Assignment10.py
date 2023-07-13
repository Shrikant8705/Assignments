from tkinter import *
from webbrowser import *

# root = tk.Tk()
root = Tk()
root.title("Search on Google")
# e = tk.Entry(root,font=("Times New Roman",25))
e = Entry(root,font=("Times New Roman",25))
e.grid()
def navigation():
    print(f"Searching = {e.get()} on Google")
    query = "https://www.google.com/search?q="+e.get()
    open(query)
# b = tk.Button(root,text = "Search",
b = Button(root,text = "Search!",
           font = ("Times New Roman",25),
           command = navigation
        )
b.grid()    

root.mainloop()