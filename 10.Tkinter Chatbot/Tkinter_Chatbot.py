from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root,bd = 4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat = Image.open('cc.png')
        img_chat = img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame,bd =3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image = self.photoimg,text='Chat Me',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)


        self.scroll_y = ttk.Scrollbar(main_frame,orient = VERTICAL)
        self.text = Text(main_frame,width =65,height = 20,bd=3,relief =RAISED,font=('arial',14),yscrollcommand = self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill =Y)
        self.text.pack()

        btn_frame = Frame(self.root ,bd =4,bg='white',width = 730)
        btn_frame.pack()

        label_1 = Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send = Button(btn_frame,text="Send>>",command = self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear = Button(btn_frame,text="Clear",command = self.clear,font=('arial',15,'bold'),width=8,bg='red')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg = ''
        self.label_1 = Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.label_1.grid(row=1,column=1,padx=5,sticky=W)

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set()




    def send(self):
        send = '\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg = 'Please Enter some Input'
            self.label_1.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_1.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif(self.entry.get()=='how are yoi'):
            self.text.insert(END,'\n\n'+'Bot: Fine Thank you')

        elif(self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Ehtisham Raza created me')

        elif(self.entry.get()=='I love food'):
            self.text.insert(END,'\n\n'+'Bot: Have you tried Sushi')

        elif(self.entry.get()=='Yes I like it'):
            self.text.insert(END,'\n\n'+'Bot: Yeah its a good food')

        elif(self.entry.get()=='What is your Name'):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr.Hacker')
        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry I didnt get it')






















if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()