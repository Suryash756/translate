from tkinter import*
from googletrans import Translator
from tkinter import ttk

root = Tk()
root.configure(background="cyan",bd=2)
root.geometry("1000x1000")
"""
input
"""
head =Label(root,text="Language Translator",font=("arial",20,"bold"),fg="black",bg="cyan")
head.place(relx=0.5,rely=0.1,anchor=CENTER)
val1=["english","hindi","chinese"]

drop1 = ttk.Combobox(root,state="readonly",values=val1,width=10,height=10,font=("arial",10))
drop1.set("english")
drop1.place(relx=0.6,rely=0.3,anchor=CENTER)
enter_text = Label(root,text="Enter Text Below :-",font=("arial",15),fg="black",bg="cyan")
enter_text.place(relx=0.3,rely=0.3,anchor=CENTER)
input_area = Text(root,height=10,width=50,bd=2)
input_area.place(relx=0.5,rely=0.5,anchor=CENTER)
"""
output
"""
output_text = Label(root,text="OUTPUT",font=("arial",15),fg="black",bg="cyan")
output_text.place(relx=0.3,rely=0.65,anchor=CENTER)
drop2 = ttk.Combobox(root,state="readonly",values=val1,width=30,height=10,font=("arial",10))
drop2.set("choose a output language")
drop2.place(relx=0.6,rely=0.65,anchor=CENTER)
output = Text(root,height=10,width=50,bd=2)
output.place(relx=0.5,rely=0.8,anchor=CENTER)

btn = Button(root,text="translate",height=2,width=7,font=("arial",15),fg="black",bg="cyan",background="orange")
btn.place(relx=0.9,rely=0.65,anchor=CENTER)
root.mainloop()