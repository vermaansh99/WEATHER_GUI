from tkinter import messagebox
import sys
def handlInternetError():
    messagebox.showerror('Internet', 'No Internet Connection!Turn ON internet and Restart Application')
    sys.exit(0)