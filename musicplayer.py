import pygame
import tkinter as tkr
from mutagen.mp3 import MP3
import soundfile as sf
from tinytag import TinyTag

# create GUI
player=tkr.Tk()

player.title('Python Player')
player.geometry('500x600')

# File can be changed
File = 'ImpactModerato.wav'

# metadata
tag=TinyTag.get(File)

# play when run program
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(File)
pygame.mixer.music.play()

# define functions for buttons
def PlayAgain():
	pygame.mixer.music.load(File)
	pygame.mixer.music.play()

def Stop():
	pygame.mixer.music.stop()

def Pause():
	pygame.mixer.music.pause()

def Resume():
	pygame.mixer.music.unpause()

# create buttons
pause=tkr.Button(player,width=5,height=3,text='PAUSE',command=Pause)
pause.pack(fill='x')

resume=tkr.Button(player,width=5,height=3,text='RESUME',command=Resume)
resume.pack(fill='x')

stop=tkr.Button(player,width=5,height=3,text='STOP',command=Stop)
stop.pack(fill='x')

play=tkr.Button(player,width=5,height=3,text='PLAY AGAIN',command=PlayAgain)
play.pack(fill='x')

name=tkr.LabelFrame(player,text='File Name')
name.pack(fill='both' , expand='yes')
contents1=tkr.Label(name,text=File)
contents1.pack()

title=tkr.LabelFrame(player,text='Title')
title.pack(fill='both' , expand='yes')
contents2=tkr.Label(title,text=tag.title)
contents2.pack()

artist=tkr.LabelFrame(player,text='Artist')
artist.pack(fill='both' , expand='yes')
contents3=tkr.Label(artist,text=tag.artist)
contents3.pack()

album=tkr.LabelFrame(player,text='Album')
album.pack(fill='both' , expand='yes')
contents4=tkr.Label(album,text=tag.album)
contents4.pack()

genre=tkr.LabelFrame(player,text='Genre')
genre.pack(fill='both' , expand='yes')
contents5=tkr.Label(genre,text=tag.genre)
contents5.pack()

#song length mm:ss
if File.endswith('.mp3'):
	song=MP3(File)
	songlength=int(song.info.length)
elif File.endswith('.wav'):
	song=sf.SoundFile(File)
	songlength=int(len(song)/song.samplerate)

Minute=int(songlength/60)
Sec=str(int(songlength-60*Minute))

if len(str(Minute))==1: Minute='0'+str(Minute)
else: Minute=str(Minute)

if len(Sec)==1: Sec='0'+Sec

Total=Minute+':'+Sec

TotalTime=tkr.LabelFrame(player,text='Time')
TotalTime.pack(fill='both' , expand='yes')
contents6=tkr.Label(TotalTime,text=Total)
contents6.pack()

#time to end
def timer():
	if pygame.mixer.music.get_busy():

		smin=songlength-int(pygame.mixer.music.get_pos()/1000)
		minute=int(smin/60)
		sec=str(int(smin-60*minute))

		if len(str(minute))==1: minute='0'+str(minute)
		else: minute=str(minute) 

		if len(sec)==1: sec='0'+sec

		time=minute+':'+sec
	else:
		time='00:00'

	Timer.config(text=time,font='times 15')
	player.after(1000,timer)

Timer=tkr.Label(player,justify='center')
Timer.pack()


timer()

player.mainloop()
