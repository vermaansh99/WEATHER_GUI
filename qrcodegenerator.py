from tkinter import *
from PIL import Image, ImageTk
import qrcode
from tkinter import messagebox


class calc:

    def about(self):
        newwin = Toplevel(root)
        newwin.title('')
        newwin.geometry('350x200')
        app_name = 'QRCode Generator';
        newwin.resizable(0,0)
        name = Label(newwin,text=app_name,font=("Courier", 22))
        name.place(x=70,y=50)

        version = Label(newwin, text='v1.0')
        version.place(x=150, y=100)

        description = '''
        This is a Qr code generator written 
        in Python made with Tkinter
        '''

        desc = Label(newwin, text=description,font=("Courier", 12))
        desc.place(x=0, y=120)




    def gen(self):
        data = self.TextArea.get();
        if data == '':
            messagebox.showwarning("Warning", "Empty fields")
        else:
            qr = qrcode.make(data);
            qr.save('qr.png')
            self.img = Image.open('qr.png')
            self.img = self.img.resize((310,310),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0,0,anchor=NW,image=self.img)

    def __init__(self,master):
        master.title('QRCode Generator')
        master.geometry('700x450')
        master.resizable(0,0)
        self.TextArea = Entry()
        self.TextArea.place(x=450,y=200)

        # menu
        menu = Menu(master)
        master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="About QRCode Generator",command=lambda:self.about())
        # added "file" to our menu
        menu.add_cascade(label="About", menu=file)
        self.genBtn = Button(master,text="Generate QR",height = 2, width = 10,command=lambda:self.gen())
        self.genBtn.place(x=450,y=250)
        self.canvas = Canvas(root, width=300, height=300,background='white')
        self.canvas.place(x=100,y=50)
        self.img = Image.open("icon.png")  # PIL solution
        self.img = self.img.resize((310, 310), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)



root = Tk()

obj = calc(root)  # object instantiated

root.mainloop()
