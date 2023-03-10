import streamlink
import subprocess

def kanal(urlf):
    # url belirle 
    url = urlf

    # streams objesi oluştur 
    streams = streamlink.streams(url)
    best = streams["best"]
    
    # vlc ile aç
    return subprocess.call(["vlc", best.url])



channel_list = [
    ["1- ShowTV",           "https://www.showtv.com.tr/canli-yayin"],
    ["2- KanalD",           "https://www.kanald.com.tr/canli-yayin"],
    ["3- Atv",              "https://www.atv.com.tr/canli-yayin"],
    ["4- TRT Haber",        "https://youtu.be/-Lrxv1_i3qc"],
    ["5- Habertürk",        "https://www.youtube.com/watch?v=SqHIO2zhxbA"],
    ["6- HalkTV",           "https://www.youtube.com/watch?v=r2ZgRoX2orE"],
    ["7- CNNTÜRK",          "https://www.youtube.com/watch?v=X_EWYemclKA"],
    ["8- HaberGlobal",      "https://www.youtube.com/watch?v=UVPejgEw21c"],
    ["9- NTV",              "https://www.youtube.com/watch?v=XEJM4Hcgd3M"],
    ["10- AHaber",          "https://www.youtube.com/watch?v=g4QA9Sh_g_8"],
]




for i in range(len(channel_list)):
    print(channel_list[i][0])
channel_select = int(input("Lütfen bir kanal seçiniz: "))
index = channel_select - 1
channel_link = channel_list[index][1]
kanal(channel_link)






