import json
import os
import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from Handler import handlInternetError
import webbrowser
from sys import platform


class Weather():
    def openInBrowser(self,city):
        uri = 'https://openweathermap.org/find?q='+city
        webbrowser.open(uri)

    def Morining(self):
        root.config(background='#ffffff')
        self.min_temp.config(fg='#262626', background='#ffffff')
        self.temp.config(fg='#262626', background='#ffffff')
        self.max_temp.config(fg='#262626', background='#ffffff')
        self.description.config(fg='#262626', background='#ffffff')
        self.canvas.config(background='#ffffff')
        self.speed.config(fg='#262626', background='#ffffff')
        self.city.config(fg='#262626', background='#ffffff')
        self.greeting.config(fg='#262626', background='#ffffff')
        self.humidity.config(fg='#262626', background='#ffffff')
        self.entry.config(bd=1)
        self.profileCanvas.config(background='#ffffff')
        self.pin.config(background='#ffffff')

    def aftenoon(self):
        root.config(background='#eeff41')
        self.min_temp.config(fg='#262626', background='#eeff41')
        self.temp.config(fg='#262626', background='#eeff41')
        self.max_temp.config(fg='#262626', background='#eeff41')
        self.description.config(fg='#262626', background='#eeff41')
        self.canvas.config(background='#eeff41')
        self.speed.config(fg='#262626', background='#eeff41')
        self.city.config(fg='#262626', background='#eeff41')
        self.greeting.config(fg='#262626', background='#eeff41')
        self.humidity.config(fg='#262626', background='#eeff41')
        self.profileCanvas.config(background='#eeff41')
        self.pin.config(background='#eeff41')

    def evening(self):
        root.config(background='#ff9800')
        self.min_temp.config(fg='#262626', background='#ff9800')
        self.temp.config(fg='#ffffff', background='#ff9800')
        self.max_temp.config(fg='#262626', background='#ff9800')
        self.description.config(fg='#262626', background='#ff9800')
        self.canvas.config(background='#ff9800')
        self.speed.config(fg='#262626', background='#ff9800')
        self.city.config(fg='#262626', background='#ff9800')
        self.greeting.config(fg='#262626', background='#ff9800')
        self.humidity.config(fg='#262626', background='#ff9800')
        self.profileCanvas.config(background='#ff9800')
        self.pin.config(background='#ff9800')

    def night(self):
        root.config(background='#262626')
        self.min_temp.config(fg='#ffffff', background='#262626')
        self.temp.config(fg='#ffffff', background='#262626')
        self.max_temp.config(fg='#ffffff', background='#262626')
        self.description.config(fg='#ffffff', background='#262626')
        self.canvas.config(background='#262626')
        self.speed.config(fg='#ffffff', background='#262626')
        self.city.config(fg='#ffffff', background='#262626')
        self.greeting.config(fg='#ffffff', background='#262626')
        self.humidity.config(fg='#ffffff', background='#262626')
        self.profileCanvas.config(background='#262626')
        self.pin.config(background='#262626')

    def checkTimeSatatus(self):
        mytime = time.localtime()
        if mytime.tm_hour <= 11:
            return 'Morning'
        elif 12 <= mytime.tm_hour <= 15:
            return 'Afternoon'
        elif 16 <= mytime.tm_hour <= 18:
            return 'Evening'
        else:
            return 'Night'

    def checkMAN(self):
        mytime = time.localtime()
        if mytime.tm_hour < 12:
            self.Morining()
        elif 12 <= mytime.tm_hour <= 15:
            self.aftenoon()
        elif 16 <= mytime.tm_hour <= 18:
            self.evening()
        else:
            self.night()

    def genCurrent(self, city):
        try:
            with open('data.json', 'r') as myfile:
                data = myfile.read()

            userData = json.loads(data)
            self.userfname = str(userData['fname'])
            self.userlname = str(userData['lname'])
            username = self.userfname + ' ' + self.userlname
            res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=16020d8d307b65395a579b8cdb9b33dd&units=metric')
            print('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=16020d8d307b65395a579b8cdb9b33dd&units=metric')
            data = res.json()
            temprature = int(data['main']['temp'])
            min_temp = int(data['main']['temp_min'])
            max_temp = int(data['main']['temp_max'])
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            print(desc)
            speed = data['wind']['speed']
            country = data['sys']['country']
            self.entry.delete(0,END)
            if desc == 'scattered clouds':
                image_name = 'assets/clouds.png'
            elif desc == 'haze':
                image_name = 'assets/fog.png'
            elif desc == 'overcast clouds':
                image_name = 'assets/overcast.png'
            elif desc == 'mist':
                image_name = 'assets/mist.png'
            elif desc == 'clear sky':
                image_name = 'assets/clear.png'
            elif desc == 'light rain':
                image_name = 'assets/rain.png'
            elif desc == 'drizzle':
                image_name = 'assets/drizzle.png'
            elif desc == 'thunderstorm with light rain':
                image_name = 'assets/thunder.png'
            elif desc == 'thunderstorm with rain':
                image_name = 'assets/thunder.png'
            else:
                image_name = 'assets/sun.png'
            root.title(city)
            self.temp.config(text=str(temprature) + chr(176) + 'C', font=('Arial', 80))
            self.min_temp.config(text='Min: ' + str(min_temp) + chr(176) + 'C')
            self.max_temp.config(text='Max: ' + str(max_temp) + chr(176) + 'C')
            self.img = Image.open(image_name)  # PIL solution
            self.img = self.img.resize((60, 60), Image.ANTIALIAS)  # The (250, 250) is (height, width)
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.place(x=50, y=50)
            self.canvas.create_image(12, 10, anchor=NW, image=self.img)
            self.description.config(text=desc, font=('Arial', 25))
            self.humidity.config(text='Humidity: ' + str(humidity) + ' %', font=('Arial', 22))
            self.speed.config(text='Wind Speed: ' + str(speed) + 'm/s', font=('Arial', 22))
            self.city.config(text='Location: ' + city + '(' + country + ')')
            self.dayStatus = self.checkTimeSatatus()
            self.greeting.config(text='Good ' + self.dayStatus + '\n' + username)
            image_name = 'userPic/cropped.jpg'
            self.img2 = Image.open(image_name)  # PIL solution
            self.img2 = self.img2.resize((100, 100), Image.ANTIALIAS)  # The (250, 250) is (height, width)
            self.img2 = ImageTk.PhotoImage(self.img2)
            self.profileCanvas.create_image(0, 0, anchor=NW, image=self.img2)
            self.checkMAN()
        except requests.exceptions.ConnectionError as e:
            messagebox.showerror('Connection', 'No Internet Connection')
        except:
            image_name = 'userPic/user.jpg'
            self.img2 = Image.open(image_name)  # PIL solution
            self.img2 = self.img2.resize((100, 100), Image.ANTIALIAS)  # The (250, 250) is (height, width)
            self.img2 = ImageTk.PhotoImage(self.img2)
            self.profileCanvas.create_image(0, 0, anchor=NW, image=self.img2)

    def gen(self, city):
        if city != '':
            try:
                res = requests.get(
                    'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=16020d8d307b65395a579b8cdb9b33dd&units=metric')
                print(
                    'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=16020d8d307b65395a579b8cdb9b33dd&units=metric')
                data = res.json()

                temprature = round(data['main']['temp'])
                min_temp = round(data['main']['temp_min'])
                max_temp = int(data['main']['temp_max'])
                desc = data['weather'][0]['description']
                humidity = data['main']['humidity']
                print(desc)
                speed = data['wind']['speed']
                country = data['sys']['country']
                root.title('Search Results for :' + city + '(' + country + ')')
                self.checkMAN()
                if desc == 'scattered clouds':
                    image_name = 'assets/clouds.png'
                elif desc == 'haze':
                    image_name = 'assets/fog.png'
                elif desc == 'overcast clouds':
                    image_name = 'assets/overcast.png'
                elif desc == 'mist':
                    image_name = 'assets/mist.png'
                elif desc == 'clear sky':
                    image_name = 'assets/clear.png'
                elif desc == 'light rain':
                    image_name = 'assets/rain.png'
                elif desc == 'drizzle':
                    image_name = 'assets/drizzle.png'
                elif desc == 'thunderstorm with light rain':
                    image_name = 'assets/thunder.png'
                elif desc == 'thunderstorm with rain':
                    image_name = 'assets/thunder.png'
                else:
                    image_name = 'assets/sun.png'
                self.temp.config(text=str(temprature) + chr(176) + 'C', font=('Arial', 80))
                self.min_temp.config(text='Min: ' + str(min_temp) + chr(176) + 'C')
                self.max_temp.config(text='Max: ' + str(max_temp) + chr(176))
                self.img = Image.open(image_name)  # PIL solution
                self.img = self.img.resize((60, 60), Image.ANTIALIAS)  # The (250, 250) is (height, width)
                self.img = ImageTk.PhotoImage(self.img)
                self.canvas.place(x=50, y=50)
                self.canvas.create_image(12, 10, anchor=NW, image=self.img)
                self.description.config(text=desc, font=('Arial', 25))
                self.speed.config(text='Wind Speed: ' + str(speed) + 'm/s', font=('Arial', 22))
                self.city.config(text='Location: ' + city + '(' + country + ')')
                self.humidity.config(text='Humidity: '+str(humidity)+' %',font=('Arial', 22))
            except requests.exceptions.ConnectionError as e:
                messagebox.showerror('Connection', 'No Internet Connection')
            except:
                root.title('Error')
                messagebox.showwarning('Not found', 'City Not Found!')
                self.temp.config(text='')
                self.min_temp.config(text='')
                self.max_temp.config(text='')
                self.description.config(text='')
                self.speed.config(text='')
                self.canvas.place_forget()
                self.city.config(text='')
                self.humidity.config(text='')
                self.Morining()
                self.entry.config(bd=1)
                self.greeting.config(fg='#262626', background='#ffffff')
        else:
            messagebox.showerror('Error!','Empty Fields!')




    def saveProfile(self, fname, lname):
        data = {'fname': fname, 'lname': lname, 'profilepath': 'userPic/cropped.jpg'}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        self.genCurrent(city)
        self.newwin.destroy()

    def userPicture(self):
        filename = fd.askopenfilename()
        print(filename)
        imageObject = Image.open(filename)
        cropped = imageObject
        cropped.save('userPic/cropped.jpg')
        self.image_name = 'userPic/cropped.jpg'
        self.img2 = Image.open(self.image_name)  # PIL solution
        self.img2 = self.img2.resize((100, 100), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.profileCanvas.create_image(0, 0, anchor=NW, image=self.img2)

    def clearPref(self):
        data = {'fname': '', 'lname': '', 'profilepath': 'userPic/user.jpg'}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        messagebox.showinfo('Success', 'user data cleared!')
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        os.remove('userPic/cropped.jpg')
        self.genCurrent(city)

    def openPref(self):
        self.newwin = Toplevel(root)
        self.newwin.geometry('300x400')
        self.newwin.resizable(0, 0)
        self.newwin.title('Preferences')
        self.Fname = Label(self.newwin, text='Enter Your First Name:')
        self.Fname.place(x=60, y=120)
        self.fname = Entry(self.newwin, width=20, text='Hello')
        self.fname.place(x=60, y=150)
        self.Lname = Label(self.newwin, text='Enter Your Last Name:')
        self.Lname.place(x=60, y=180)
        self.lname = Entry(self.newwin, width=20)
        self.lname.place(x=60, y=200)
        self.saveBtn = Button(self.newwin, text='Save Profile', width=10, height=2,
                              command=lambda: self.saveProfile(self.fname.get(), self.lname.get()))
        self.saveBtn.place(x=60, y=230)

    def __init__(self, master):
        master.title('Weather Api')
        master.geometry('1050x450')
        master.resizable(0, 0)
        self.entry = Entry(master, width=20, bd=0)
        self.entry.place(x=450, y=200)
        self.btn = Button(master, text='Find Weather By City', width=15, height=2,
                          command=lambda: self.gen(self.entry.get()))
        self.btn.place(x=450, y=260)
        self.temp = Label(master, text='', font=('Arial', 40))
        self.temp.place(x=50, y=120)
        self.min_temp = Label(master, text='', font=('Arial', 20))
        self.min_temp.place(x=50, y=220)
        self.max_temp = Label(master, text='', font=('Arial', 20))
        self.max_temp.place(x=150, y=220)
        self.canvas = Canvas(master, width=70, height=70, bd=0, highlightthickness=0, relief='ridge')
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        self.description = Label(master, text='')
        self.description.place(x=50, y=250)
        self.speed = Label(master, text='')
        self.speed.place(x=50, y=285)

        self.city = Label(master, text='', font=('Arial', 22))
        self.city.place(x=50, y=325)
        self.humidity = Label(master, text='Demo')
        self.humidity.place(x=50, y=365)
        self.greeting = Label(master, text='Good Morning!', fg='#ffffff', background='#262626', font=('Arial', 35))
        self.greeting.place(x=750, y=220)
        self.profileCanvas = Canvas(master, width=100, height=100, bd=0, highlightthickness=0, relief='ridge',
                                    background='#262626')
        self.pin = Canvas(master, width=100, height=100, bd=0, highlightthickness=0, relief='ridge',
                          background='#262626')
        self.pin.place(x=490, y=80)

        pin_image = 'assets/pin.png'
        self.pinImage = Image.open(pin_image)  # PIL solution
        self.pinImage = self.pinImage.resize((80, 80), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        self.pinImage = ImageTk.PhotoImage(self.pinImage)
        self.pin.create_image(45, 50, anchor='c', image=self.pinImage)

        image_name = 'assets/user.png'
        self.img2 = Image.open(image_name)  # PIL solution
        self.img2 = self.img2.resize((100, 100), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.profileCanvas.place(x=820, y=60)
        self.profileCanvas.create_image(0, 0, anchor='c', image=self.img2)
        menubar = Menu(master)
        edit = Menu(menubar, tearoff=0)
        edit.add_command(label="Change Profile Picture", command=lambda: self.userPicture())
        edit.add_command(label="Open In Browser", command=lambda: self.openInBrowser(city))
        edit.add_command(label="Edit Preferences", command=lambda: self.openPref())
        edit.add_command(label="Clear Preferences", command=lambda: self.clearPref())
        edit.add_command(label="Reset", command=lambda: self.genCurrent(city))
        menubar.add_cascade(label="Options", menu=edit)
        master.config(menu=menubar)


root = Tk()


def main():
    try:
        obj = Weather(root)
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        obj.genCurrent(city)
        obj.checkMAN()
    except requests.exceptions.ConnectionError as e:  # This is the correct syntax
        handlInternetError()


if __name__ == "__main__":
    main()

root.mainloop()
