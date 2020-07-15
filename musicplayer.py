import shutil, os
import pygame
import tkinter as tkr
from mutagen.mp3 import MP3
import soundfile as sf
from tinytag import TinyTag

listQueue=[]

def Player(File):

    # create GUI
    player=tkr.Tk()

    player.title('Player')
    player.geometry('500x600')

    # metadata
    tag=TinyTag.get(File)
    
    pygame.init()
    pygame.mixer.init()
    
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

    Timer=tkr.Label(player,justify='center')
    Timer.pack()


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
        player.after(100,timer)

    timer()

    PlayAgain()

    player.mainloop()	
    
def mainQueue():

	Queuewindow=tkr.Tk()

	Queuewindow.title('Queue')
	Queuewindow.geometry('500x600')
    
	listNodes2 = tkr.Listbox(Queuewindow,width=40,height=20)
	listNodes2.pack(side='left' , fill='both')

	scrollbar2 = tkr.Scrollbar(Queuewindow,orient='vertical')
	scrollbar2.config(command=listNodes2.yview)
	scrollbar2.pack(fill='y')

	listNodes2.config(yscrollcommand=scrollbar2.set)

	for i in range(len(listQueue)):
		listNodes2.insert(i+1, listQueue[i])
	
	for i in range(len(listQueue)):
		Player(listQueue[i])
		
	Queuewindow.mainloop()
	
def library():
	
	libwindow=tkr.Tk()

	libwindow.title('Library')
	libwindow.geometry('500x600')

	def addMusic():
    		addingwindow = tkr.Tk()
    		addingwindow.title('Add Music')
   		
    		tkr.Label(addingwindow, text="Music File:").grid(row=0)
    		
    		ent = tkr.Entry(addingwindow)
    		ent.grid(row=0, column=1)

    		def show_entry_fields():
        		source_file = ent.get()
        		shutil.copy2(source_file, 'Library')
        		addingwindow.destroy()
        		libwindow.destroy()
    
    		tkr.Button(addingwindow, text='Add', command=show_entry_fields).grid(row=3, column=1, sticky=tkr.W, pady=4)

    		addingwindow.mainloop()

	def libOption(File):
		libOptionwindow=tkr.Tk()
	
		libOptionwindow.title('File options')
		libOptionwindow.geometry('300x400')
	
		def Queue():
			shutil.copy2('Library\\'+File, 'Queue')
			listQueue.append('Queue\\'+File)
			libOptionwindow.destroy()
		
		def Remove():
			os.remove('Library\\'+File)
			if File in os.listdir('Queue'):
				os.remove('Queue\\'+File)
				listQueue.remove('Queue\\'+File)
				
			libOptionwindow.destroy()
			libwindow.destroy()
       	
		option1=tkr.Button(libOptionwindow,width=5,height=3,text='To Queue',command=Queue)
		option1.pack(fill='x')
	
		option2=tkr.Button(libOptionwindow,width=5,height=3,text='Remove From Library',command=Remove)
		option2.pack(fill='x')
	
		libOptionwindow.mainloop()

	libButton=tkr.Button(libwindow,width=5,height=3,text='Add Music',command=addMusic)
	libButton.pack(fill='x')
	
	def musicListSelect(event):
	    list_box=event.widget
	    libOption(list_box.get(list_box.curselection()[0]))

	listNodes1 = tkr.Listbox(libwindow,width=40,height=20)
	listNodes1.bind("<<ListboxSelect>>", musicListSelect)
	listNodes1.pack(side='left',fill='both')

	scrollbar1 = tkr.Scrollbar(libwindow,orient='vertical')
	scrollbar1.config(command=listNodes1.yview)
	scrollbar1.pack(fill='y')

	listNodes1.config(yscrollcommand=scrollbar1.set)

	musicLibrary = os.listdir('Library')
	for i in range(len(musicLibrary)):
	    listNodes1.insert(i+1, musicLibrary[i])

	libwindow.mainloop()
	
mainwindow=tkr.Tk()

mainwindow.title('Python Player')
mainwindow.geometry('300x400')

mainButton1=tkr.Button(mainwindow,width=5,height=3,text='Open Library',command=library)
mainButton1.pack(fill='x')

mainButton2=tkr.Button(mainwindow,width=5,height=3,text='Open Queue' ,command=mainQueue)
mainButton2.pack(fill='x')

for Music in os.listdir('Queue'):
	os.remove('Queue\\'+Music)
	
mainwindow.mainloop()