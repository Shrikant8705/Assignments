from tkinter import *
from webbrowser import *

root = Tk(className= " Ads Survey")

root.geometry("450x270")
Label(root).pack()
nameLabel = Label(root, text="Name:").pack()
userName = Entry(root).pack()
contactLabel = Label(root, text="Contact:").pack()
userContact = Entry(root).pack()
Label(root).pack()
questionLabel = Label(master = root, text= "Where did you see this AD?", font=("Poppins medium",15)).pack()
userChoice = StringVar(root)
userChoice.set("Select One Option")
checkBox = OptionMenu(root, userChoice, "FaceBook Ads", "Twitter Ads").pack()
Label(root).pack()
def submitOnClick():
    if userChoice.get() == "Twitter Ads":
        open("https://business.twitter.com/en/advertising.html")
    elif userChoice.get() == "FaceBook Ads":
        open("https://en-gb.facebook.com/business/ads")
    root.destroy()
submitButton = Button(root,text = "Submit",command = submitOnClick).pack()
Label(root).pack()

root.mainloop()
