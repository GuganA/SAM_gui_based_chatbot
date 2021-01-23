import tkinter # python inbuilt package 
from tkinter import * #importing all the package
import datetime # for date and time
import wikipedia # for searchin in wiki
import webbrowser
import os
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer


sam_bot = ChatBot("SAM", storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            database_uri="sqlite:///db.sqlite3")
#trainer = ChatterBotCorpusTrainer(sam_bot)
#trainer.train("chatterbot.corpus.english")

chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #for windows

def chat_response(msg):
    feed = msg
    if 'open youtube' in feed:
            webbrowser.get(chromedir).open("youtube.com") # for windows
            #webbrowser.open("youtube.com") # for every os
            return str('Opening Youtube')
    elif 'your name' in feed:
            return str("My name is Sam")
    
    elif 'play music' in feed:
        music_dir = "E:\Gugan\Music"
        #music_dir = "/media/gugan/Gugan/Gugan/Music"
        songs = os.listdir(music_dir)
        #os.system(os.path.join(music_dir, songs[1])) # for linux
        os.startfile(os.path.join(music_dir, songs[0])) # for windows
        return str('Opening music')

    elif 'time' in feed:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        return str(f"Sir, the time is {strTime}")

    elif 'who created' in feed:
        return str("I am created by Gugan and Vikash")
        
    else:
        return str(sam_bot.get_response(feed))

def send():
    """
    This method is for to get from user and displays to chatbox with bot response 
    """
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "YOU: " + msg + '\n\n')
        ChatBox.config(foreground="#ffffff", font=("Helvetica", 12 ))
        res = chat_response(msg)
        ChatBox.insert(END, "SAM: " + res + '\n\n')
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)
sam = Tk()
sam.title("Sam Chatbot")
sam.geometry("400x440")
sam.iconbitmap('E:/bot/S.ico')
sam.resizable(width=False, height=False)
ChatBox = Text(sam, bg="#00264d", bd=2, height="30", width="42",
               font="Arial",cursor="heart")
ChatBox.config(state=NORMAL)
scrollbar = Scrollbar(sam, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set
SendButton = Button(sam, font=("Verdana",8,'bold'), text="Send", width="9",
                    height="4", bd=3, bg="#005C97",
                    activebackground="#2093A7",fg='#ffffff',
                    command= lambda:send())
EntryBox = Text(sam, bd=2, bg="#B9B4B1",width="25", height="2", font=("Arial",15))
scrollbar.place(x=385,y=6, height=386, width=10)
ChatBox.place(x=6,y=6, height=386, width=375)
EntryBox.place(x=6, y=401, height=30, width=280)
SendButton.place(x=300, y=400, height=30)


sam.mainloop()
