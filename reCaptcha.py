from tkinter import *
import random as r

class tmp:
    c=''
    t=''


def cap():
    c.delete("all")
    h=''
    for i in range(0,5):
        h+=(chr(r.randint(65,90)))
    colour=["black","purple","red","blue","green","orange"]
    fnt=["Verdana","Arial","Papyrus","Calibri","Algerian"]
    t1=c.create_text(20+r.randint(0,10),20+r.randint(0,10),text=h[0],font=fnt[r.randint(0,4)]+" 12 bold",fill=colour[r.randint(0,5)])
    t2=c.create_text(40+r.randint(0,10),20+r.randint(0,10),text=h[1],font=fnt[r.randint(0,4)]+" 12 bold",fill=colour[r.randint(0,5)])
    t3=c.create_text(60+r.randint(0,10),20+r.randint(0,10),text=h[2],font=fnt[r.randint(0,4)]+" 12 bold",fill=colour[r.randint(0,5)])
    t4=c.create_text(80+r.randint(0,10),20+r.randint(0,10),text=h[3],font=fnt[r.randint(0,4)]+" 12 bold",fill=colour[r.randint(0,5)])
    t5=c.create_text(100+r.randint(0,10),20+r.randint(0,10),text=h[4],font=fnt[r.randint(0,4)]+" 12 bold",fill=colour[r.randint(0,5)])
    T.c=str(h)
    for i in range(0,10):
        l = c.create_line(r.randint(5,295),r.randint(5,195),r.randint(5,295),r.randint(5,195),fill=colour[r.randint(0,5)],width=r.randint(1,3))

def val():
    T.t=text.get()
    if T.c==T.t:
        print("Ok")
    else:
        print("Inval reCaptcha")

T=tmp()
root = Tk()
root.geometry("250x200")
root.title("reCaptcha")
c= Canvas(root,width=120,height=40,bg='white')
text = Entry(root)
cap()
pic=PhotoImage(file="refresh.png")
b= Button(root,image=pic,command=cap)
sub=Button(root,text="Submit",command=val)
c.pack()
b.pack()
text.pack()
sub.pack()
mainloop()
