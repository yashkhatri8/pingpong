from tkinter import *
import pygame
import os
class AudioPlayer:
    def __init__(self,root):
        self.hold=root
        self.hold.geometry("500x220+500+200")
        self.hold.title("Audio Player")
        self.hold.configure(bg="#b19cd9")
        pygame.init()
        pygame.mixer.init()
        self.track=StringVar()
        self.status=StringVar()
        trackArea = LabelFrame(self.hold,text="Song Track",font=("times new roman",15,"bold"),bg="#301934",fg="white",bd=5)
        Label(trackArea,textvariable=self.track, font=("times new roman", 24, "bold"), bg="#301934",
                            fg="#fe2c54").grid(row=0, column=0, padx=10, pady=5)
        Label(trackArea, textvariable=self.status, font=("times new roman", 24, "bold"), bg="#301934",
                            fg="#fe2c54").grid(row=0, column=1, padx=10, pady=5)
        trackArea.place(bordermode="outside",x=10,y=10,height=100,width=480)
        buttonArea = LabelFrame(self.hold, text="buttonTray", font=("times new roman", 15, "bold"), bg="#301934",
                                fg="white", bd=5)
        Button(buttonArea,text="Play",command=self.play,width=5 ,height=1,bg="#b19cd9",fg="white", font=("times new roman", 15 , "bold")).grid(row=0,column=2,padx=14,pady=8)

        Button(buttonArea,command=self.pause, text="Pause",width=5 ,height=1,bg="#b19cd9",fg="white", font=("times new roman", 15, "bold")).grid(row=0,column=1,padx=14,pady=8)

        buttonArea.place(bordermode="outside",x=10,y=112,height=100,width=200)
        songsframe = LabelFrame(self.hold, text="Song Playlist", font=("times new roman", 15, "bold"), bg="#301934",
                                fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=215, y=112, width=272, height=100)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="#fe2c54", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="#301934", fg="white", bd=5)

        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:/Users/brahmdev ji ka compu/Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    def play(self):
        self.track.set(self.playlist.get(ACTIVE))

        self.status.set("Playing")

        pygame.mixer.music.load(self.playlist.get(ACTIVE))

        pygame.mixer.music.play()
    def pause(self):
        self.status.set("Playing")
        pygame.mixer.music.pause()
root=Tk()
AudioPlayer(root)

root.mainloop()
