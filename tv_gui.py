import customtkinter as ctk
from tkinter import *
import streamlink
import subprocess
import tkinter.font as font

# base settings for the application window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

def kanal(urlf):
    # url belirle 
    url = urlf

    # streams objesi oluştur 
    streams = streamlink.streams(url)
    best = streams["best"]
    
    # vlc ile aç
    return subprocess.call(["vlc", best.url])


root = ctk.CTk()
root.title('StreamGrabber')

frame1 = ctk.CTkFrame(master = root)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

custom_font =("segoe", 35)

button1 = ctk.CTkButton(master=frame1, text='Show', font = custom_font, command = lambda:kanal("https://www.showtv.com.tr/canli-yayin"))
button1.pack(pady=10, padx=0)

button2 = ctk.CTkButton(master=frame1, text='KanalD', font = custom_font, command = lambda:kanal("https://www.kanald.com.tr/canli-yayin"))
button2.pack(pady=10, padx=0)

button3 = ctk.CTkButton(master=frame1, text='ATV', font = custom_font, command = lambda:kanal("https://www.atv.com.tr/canli-yayin"))
button3.pack(pady=10, padx=0)

button4 = ctk.CTkButton(master=frame1, text='TRT Haber', font = custom_font, command = lambda:kanal("https://youtu.be/-Lrxv1_i3qc"))
button4.pack(pady=10, padx=0)

button5 = ctk.CTkButton(master=frame1, text='Habertürk', font = custom_font, command = lambda:kanal("https://www.youtube.com/watch?v=SqHIO2zhxbA"))
button5.pack(pady=10, padx=0)

button6 = ctk.CTkButton(master=frame1, text='Halk TV', font = custom_font, command = lambda:kanal("https://www.youtube.com/watch?v=r2ZgRoX2orE"))
button6.pack(pady=10, padx=0)

button7 = ctk.CTkButton(master=frame1, text='CNN Türk', font = custom_font, command = lambda:kanal("https://www.youtube.com/watch?v=X_EWYemclKA"))
button7.pack(pady=10, padx=0)

button8 = ctk.CTkButton(master=frame1, text='Haber Global', font = custom_font, command = lambda:kanal("https://www.youtube.com/watch?v=UVPejgEw21c"))
button8.pack(pady=10, padx=0)

button9 = ctk.CTkButton(master=frame1, text='NTV', font = custom_font, command = lambda:kanal("https://www.youtube.com/watch?v=XEJM4Hcgd3M"))
button9.pack(pady=10, padx=0)

button10 = ctk.CTkButton(master=frame1, text='A Haber', font = custom_font,  command = lambda:kanal("https://www.youtube.com/watch?v=g4QA9Sh_g_8"))
button10.pack(pady=10, padx=0)













root.mainloop()