from tkinter import *
from time import strftime
root=Tk()
root.geometry("500x500")
root.resizable(1,0)
root.title('First Python Clock in WWW')
Label(root,text = 'IG: marzouk_sofien', font ='palatino 30 bold').pack(side=BOTTOM)
mark =Label(root,
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')

mark.pack(anchor = 'center')
def time():
    global after_id
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    after_id=mark.after(1000, time)

def pause(): 
    global T1
    T1=strftime('%H:%M:%S %p')
    mark.config(text = T1)
    mark.after_cancel(after_id)
    #T1= strftime('%H:%M:%S %p')
    #mark.config(text= T1)

def continueBe():
    time()
    #mark2.config(str(T2-T1))


#mark2 = tk.Label(root,
# font = ('calibri', 40, 'bold'),
#pady=150,
#foreground = 'black')
time()
pauseB = Button(root, text="Pause", command=pause)
continueB = Button(root, text="Continue", command=time)#hiya bch tarja3 temchi w fard wakt tdhhar l duree li kaedt mposiya,
continueB.place(x=300,y=300)
pauseB.place(x=150,y=300)
root.mainloop()