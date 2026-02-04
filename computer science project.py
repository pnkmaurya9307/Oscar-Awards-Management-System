import imageio
from tkinter import*
from PIL import ImageTk, Image
import pygame

import mysql.connector as mysql
import tkinter.messagebox as MessageBox;

from moviepy.editor import *
import tkinter as tk
PR=Tk()

def mynew(x):
        pygame.mixer.init()
        file =x
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

def RP():
    RP=Toplevel()
    RP.minsize(height=1100,width=1900)
    im="background1.jpg"
    
    img = Image.open(im)
    img = img.resize((2000, 1500))
    img = ImageTk.PhotoImage(img)
    panel = Label(RP, image=img,bd=2)
    panel.image = img
    panel.place(x=0,y=0)
    
    pygame.mixer.init()
    file = 'laila.mp3'
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    def audio9():
        pygame.mixer.init()
        file = 'audio9.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        RP.destroy()
    lbl=Label(RP,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=90)
    btn=Button(RP,text="𝐁𝐀𝐂𝐊",font=("", 35),fg="white",bg="black", bd=10,command=audio9,width=10).place(x=70,y=880)
    btn=Button(RP,text="𝐏𝐑𝐎𝐂𝐄𝐄𝐃 ➸",font=("", 35),fg="white",bg="black", bd=10,command=func,width=10).place(x=1560,y=880)
    #PR.bind('Enter',lambda event:audio9())
    PR.bind('<Return>',lambda event:func())
    
    #PR.bind('<control-x>',lambda event:jj())
    
    
    def img1():
        im="image1.jpg"
        img = Image.open(im)
        img = img.resize((800, 550))
        img = ImageTk.PhotoImage(img)
        panel = Label(RP, image=img,bd=2)
        panel.image = img
        panel.place(x=565,y=270)
        btn2=Button(RP,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=1430,y=488)
        
        PR.bind('<Right>',lambda event:img2())   
    def img2():
        im="image2.jpg"
        img = Image.open(im)
        img = img.resize((800, 550))
        img = ImageTk.PhotoImage(img)
        panel = Label(RP, image=img,bd=2)
        panel.image = img
        panel.place(x=565,y=270)
        btn2=Button(RP,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img3,width=3).place(x=1430,y=488)
        btn1=Button(RP,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img1,width=3).place(x=400,y=488)
        PR.bind('<Right>',lambda event:img3())
        PR.bind('<Left>',lambda event:img1())   
    def img5():
            im="image5.jpg"
            img = Image.open(im)
            img = img.resize((800, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(RP, image=img,bd=2)
            panel.image = img
            panel.place(x=565,y=270)
            btn1=Button(RP,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img4,width=3).place(x=400,y=488)
            
            PR.bind('<Left>',lambda event:img4())   
    def img4():
            im="image4.jpg"
            img = Image.open(im)
            img = img.resize((800, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(RP, image=img,bd=2)
            panel.image = img
            panel.place(x=565,y=270)
            btn1=Button(RP,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img3,width=3).place(x=400,y=488)
            btn2=Button(RP,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img5,width=3).place(x=1430,y=488)
            
            PR.bind('<Right>',lambda event:img5())
            PR.bind('<Left>',lambda event:img3())
    def img3():
            im="image3.jpg"
            img = Image.open(im)
            img = img.resize((800, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(RP, image=img,bd=2)
            panel.image = img
            panel.place(x=565,y=270)
            btn1=Button(RP,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=400,y=488)
            btn2=Button(RP,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img4,width=3).place(x=1430,y=488)
            
            PR.bind('<Right>',lambda event:img4())
            PR.bind('<Left>',lambda event:img2())
    img1()        
    btn1=Button(RP,text="《",font=("", 35),fg="white",bg="black",bd=10,width=3).place(x=400,y=488)
    btn2=Button(RP,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=1430,y=488)
     
#....................................................................window1.............................................................

def new():
    PR.title("░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░")
    PR.minsize(height=1100,width=1900)
    #PR.iconbitmap('C:/Users/Acer/Downloads/new.ico')
   
    
    im="background1.jpg"
    
    img = Image.open(im)
    img = img.resize((2000, 1500))
    img = ImageTk.PhotoImage(img)
    panel = Label(PR, image=img,bd=2)
    panel.image = img
    panel.place(x=0,y=0)
#............................................................................image..........................................
    im="img1.jpg"
    img = Image.open(im)
    img = img.resize((690, 480))
    img = ImageTk.PhotoImage(img)
    panel = Label(PR, image=img,bd=2)
    panel.image = img
    panel.place(x=620,y=280)
   

    btn=Button(PR,text="𝐄𝐗𝐈𝐓",font=("", 35),fg="white",bg="black", bd=10,command=PR.destroy,width=10).place(x=60,y=880)
    btn=Button(PR,text="𝐏𝐑𝐎𝐂𝐄𝐄𝐃 ➸",font=("", 35),fg="white",bg="black", bd=10,command=RP,width=10).place(x=1550,y=880)
#............................................................................levels of window 1...................................................
    lbl=Label(PR,text=" ",bg="blue",height=4,width=9,font=("####", 70)).place(x=25,y=280)
    lbl=Label(PR,text=" ",bg="blue",height=4,width=9,font=("####", 70)).place(x=1370,y=280)
    lbl=Label(PR,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
    def voice1():
         x="Pankaj.mp3"
         mynew(x)
    def voice2():
         x="Ritik.mp3"
         mynew(x)
    def voice4():
         x="Sameersir.mp3"
         mynew(x)
    def voice5():
         x="JK.mp3"
         mynew(x)    
         
    
    lbl2=Button(PR,text="✧𝟐𝟎𝟏𝟓 -𝟐𝟎𝟐𝟐✧",font=("r", 30),fg="white",bd=5,width=18,bg="black").place(x=750,y=790)
    lbl3=Button(PR,text="✧𝐆𝐔𝐈𝐃𝐄𝐃 𝐁𝐘✧",font=("", 30),fg="WHITE",bg="black",bd=5,width=18).place(x=40,y=340)
    lbl4=Button(PR,text="✧𝐒𝐔𝐁𝐌𝐈𝐓𝐓𝐄𝐃 𝐁𝐘✧",font=("", 30),fg="white",bg="black",bd=5,width=18).place(x=1410,y=340)
    lbl5=Button(PR,text="➸ 𝐏𝐀𝐍𝐊𝐀𝐉",font=("", 30),fg="WHITE",bg="BLACK",bd=5,command=voice1,width=18).place(x=1410,y=435)
    lbl5=Button(PR,text="➸ 𝐑𝐈𝐓𝐈𝐊",font=("", 30),fg="WHITE",bg="BLACK",bd=5,command=voice2,width=18).place(x=1410,y=530)
    lbl3=Button(PR,text="✧𝐆𝐔𝐈𝐃𝐄𝐃 𝐁𝐘✧",font=("", 30),fg="WHITE",bg="black",bd=5,width=18).place(x=40,y=340)
    lbl6=Button(PR,text="➸𝐌𝐑 𝐒𝐀𝐌𝐄𝐄𝐑 𝐊𝐔𝐌𝐀𝐑",font=("", 30),fg="WHITE",bg="BLACK",command=voice4,bd=5,width=18).place(x=40,y=450)
    lbl7=Button(PR,text="➸ 𝐏𝐆𝐓 𝐂𝐎𝐌𝐏. 𝐒𝐂𝐈𝐄𝐍𝐂𝐄",font=("", 30),fg="WHITE",command=voice4,bg="BLACK",bd=5,width=18).place(x=40,y=550)
    pygame.mixer.init()
    file = 'starting.mp3'
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    clip = VideoFileClip('starting.mp4').resize((1920,1080))
    clip.preview()
    pygame.quit()
    pygame.mixer.init()
    file = 'Startinhintro.mp3'
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    def mynew(x):
        pygame.mixer.init()
        file =x
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    
    
    PR.bind('<Return>',lambda event:RP())
   
#____________________________________________________________2015______________________________________________________________
def allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1):
        win8=Toplevel(PR)
        win8.minsize(height=1100,width=1900)
        im=a1
        img = Image.open(im)
        img = img.resize((2000, 1500))
        img = ImageTk.PhotoImage(img)
        panel = Label(win8, image=img,bd=2)
        panel.image = img
        panel.place(x=0,y=0)
        pygame.mixer.init()
        file =b1
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        lbl=Label(win8,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
        btn2=Button(win8,text="☆ 𝐁𝐄𝐒𝐓 𝐌𝐎𝐕𝐈𝐄 ☆",font=("", 35),fg="black",bg="white",bd=0,width=15,height=0).place(x=740,y=240)
        btn4=Button(win8,text=c1,font=("", 35),fg="black",bg="white",bd=0,width=22,height=0).place(x=620,y=905)
        def audio8():
            pygame.mixer.init()
            file = d1
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            win8.destroy()
        def win81():
            win81=Toplevel()
            win81.minsize(height=1100,width=1900)
            im=a1
            img = Image.open(im)
            img = img.resize((2000, 1500))
            img = ImageTk.PhotoImage(img)
            panel = Label(win81, image=img,bd=2)
            panel.image = img
            panel.place(x=0,y=0)
            pygame.mixer.init()
            file =b1
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            lbl=Label(win81,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
            btn1=Button(win81,text="《",font=("", 35),fg="white",bg="black",bd=10,command=win81.destroy,width=3).place(x=60,y=488)
            def win82():
                    win82=Toplevel()
                    win82.minsize(height=1100,width=1900)
                    im=a1
                    img = Image.open(im)
                    img = img.resize((2000, 1500))
                    img = ImageTk.PhotoImage(img)
                    panel = Label(win82, image=img,bd=2)
                    panel.image = img
                    panel.place(x=0,y=0)
                    lbl=Label(win82,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
                    btn2=Button(win82,text="☆ 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑 ☆",font=("", 35),fg="black",bg="white",bd=0,width=15,height=0).place(x=740,y=240)
                    btn4=Button(win82,text=n1,font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
                    btn1=Button(win82,text="《",font=("", 35),fg="white",bg="black",bd=10,command=win82.destroy,width=3).place(x=60,y=488)
                    def win83():
                        win83=Toplevel()
                        win83.minsize(height=1100,width=1900)
                        im=a1
                        img = Image.open(im)
                        img = img.resize((2000, 1500))
                        img = ImageTk.PhotoImage(img)
                        panel = Label(win83, image=img,bd=2)
                        panel.image = img
                        panel.place(x=0,y=0)
                        
                        lbl=Label(win83,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
                        btn1=Button(win83,text="《",font=("", 35),fg="white",bg="black",bd=10,command=win83.destroy,width=3).place(x=60,y=488)
                        btn2=Button(win83,text=" 》",font=("", 35),fg="white",bg="black",bd=10,width=3).place(x=1735,y=488)
                        btn2=Button(win83,text="☆ 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒 ☆",font=("", 35),fg="black",bg="white", bd=0,width=16,height=0).place(x=740,y=240)
                        btn4=Button(win83,text=q1,font=("", 35),fg="black",bg="white",bd=0,width=20,height=0).place(x=710,y=905)  
                    #_____________________________image______________________     
                        im=r1
                        img = Image.open(im)
                        img = img.resize((850, 550))
                        img = ImageTk.PhotoImage(img)
                        panel = Label(win83, image=img,bd=2)
                        panel.image = img
                        panel.place(x=535,y=340)
                        def win841():
                            win841=Toplevel()
                            win841.minsize(height=1100,width=1900)
                            cn=Canvas(win841, bg="black",height=1100, width=1900).pack()
                            lbl1=Label(win841,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
                            btn1=Button(win841,text="《 ",font=("", 35),fg="white",bg="black",bd=10,command=win841.destroy,width=3).place(x=60,y=488)
                            btn2=Button(win841,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=win841.destroy,width=3).place(x=1735,y=488)
                            
                            lbl1=Label(win841,text=s1,fg="black",bd=60,bg="cyan",justify=LEFT,font=("####", 55)).place(x=550,y=300)
                        tmr=Button(win83,text="",image=n,command=win841 ,bd=5,bg="black").place(x=1395,y=820)
                    btn2=Button(win82,text=" 》 ",font=("", 35),fg="white",bg="black",bd=10,command=win83,width=3).place(x=1735,y=488)
                #_____________________________image______________________     
                    im=o1
                    img = Image.open(im)
                    img = img.resize((850, 550))
                    img = ImageTk.PhotoImage(img)
                    panel = Label(win82, image=img,bd=2)
                    panel.image = img
                    panel.place(x=535,y=340)
                    #ACTOR
                    def win831():
                        win831=Toplevel(PR)
                        win831.minsize(height=1100,width=1900)
                        cn=Canvas(win831, bg="black",height=1100, width=1900).pack()
                        lbl1=Label(win831,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
                        btn1=Button(win831,text="《 ",font=("", 35),fg="white",bg="black",bd=10,command=win831.destroy,width=3).place(x=60,y=488)
                        btn2=Button(win831,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=win831.destroy,width=3).place(x=1735,y=488)
                        lbl1=Label(win831,text=p1,fg="black",bd=60,bg="cyan",justify=LEFT,font=("####", 55)).place(x=550,y=300)
                    tmr=Button(win82,text="",image=n,command=win831 ,bd=5,bg="black").place(x=1395,y=820)
            btn2=Button(win81,text=" 》",font=("", 35),fg="white",bg="black",command=win82,bd=10,width=3).place(x=1735,y=488)
            btn2=Button(win81,text="☆ 𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 ☆",font=("", 35),fg="black",bg="white", bd=0,width=18,height=0).place(x=740,y=240)
            btn4=Button(win81,text=k1,font=("", 35),fg="black",bg="white",bd=0,width=20,height=0).place(x=710,y=905)
        #_____________________________image______________________     
            im=l1
            img = Image.open(im)
            img = img.resize((850, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(win81, image=img,bd=2)
            panel.image = img
            panel.place(x=535,y=340)
            #DIRECTOR
            def win821():
                win821=Toplevel(PR)
                cn=Canvas(win821, bg="black",height=1100, width=1900).pack()
                lbl1=Label(win821,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
                btn1=Button(win821,text="《 ",font=("", 35),fg="white",bg="black",bd=10,command=win821.destroy,width=3).place(x=60,y=488)
                btn2=Button(win821,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=win821.destroy,width=3).place(x=1735,y=488)
                lbl1=Label(win821,text=m1,fg="black",bg="cyan",bd=50,justify=LEFT,font=("####", 55)).place(x=500,y=300)
            tmr=Button(win81,text="",image=n,command=win821 ,bd=5,bg="black").place(x=1395,y=820)
        btn1=Button(win8,text="《 ",font=("", 35),fg="white",bg="black",bd=10,command=audio8,width=3).place(x=60,y=488)
        btn2=Button(win8,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=win81,width=3).place(x=1735,y=488)
    #_____________________________image______________________     
        im=e1
        img = Image.open(im)
        img = img.resize((850, 550))
        img = ImageTk.PhotoImage(img)
        panel = Label(win8, image=img,bd=2)
        panel.image = img
        panel.place(x=535,y=340)
        def win8111():
            pygame.mixer.init()
            file =f1
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            clip = VideoFileClip(g1).resize((1902,1020))
            clip.preview()            
            pygame.quit()
        def win811():
            win811=Toplevel(PR)
            cn=Canvas(win811, bg="black",height=1100, width=1900).pack()
            lbl1=Label(win811,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=100)
            btn1=Button(win811,text="《 ",font=("", 35),fg="white",bg="black",bd=10,command=win811.destroy,width=3).place(x=60,y=488)
            btn2=Button(win811,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=win811.destroy,width=3).place(x=1735,y=488)
            lbl1=Label(win811,text=h1,fg="black",bg="cyan",bd=60,font=("####", 55),justify=LEFT).place(x=410,y=280)
        tmr=Button(win8,text="",image=n,command=win811 ,bd=5,bg="black").place(x=1395,y=740)
        tmr1=Button(win8,text="",image=h,command=win8111 ,bd=3,bg="black").place(x=1395,y=820)
def year2015():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐁𝐈𝐑𝐃𝐌𝐀𝐍 ☆",'music3.mp3',"m2015.jpg"
    k1,l1= " ☆ 𝐀𝐋𝐄𝐉𝐀𝐍𝐃𝐑𝐎 𝐆𝐎𝐍𝐙𝐀𝐋𝐈𝐙 ☆","d2015.jpg"
    q1,r1,f1,g1,n1,o1= "☆ 𝐉𝐔𝐋𝐈𝐀𝐍𝐍𝐄 𝐌𝐎𝐎𝐑𝐄 ☆","b2015.jpg",'audio2015.mp3','movie2015.mp4',"☆ 𝐄𝐃𝐃𝐈𝐄 𝐑𝐄𝐃𝐌𝐀𝐘𝐍𝐄 ☆","a2015.jpg"
    h1="𝐀𝐖𝐀𝐑𝐃  :  𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟐𝟐\n𝐌𝐎𝐕𝐈𝐄  : 𝐁𝐈𝐑𝐃𝐌𝐀𝐍 \n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑  : 𝐀𝐋𝐄𝐉𝐀𝐍𝐃𝐑𝐎 𝐆𝐎𝐍𝐙𝐀𝐋𝐄𝐙\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟏𝟕 𝐎𝐂𝐓,𝟐𝟎𝟏𝟒\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟕.𝟕\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍    : 𝟏𝟏𝟗 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟏𝟎𝟑.𝟐𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐀𝐋𝐄𝐉𝐀𝐍𝐃𝐑𝐎 𝐆𝐎𝐍𝐙𝐀𝐋𝐈𝐙\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐌𝐄𝐗𝐈𝐂𝐎\n𝐃𝐎𝐁 :𝟏𝟓 𝐀𝐔𝐆,𝟏𝟗𝟔𝟑\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟒𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟏𝟎" '''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐄𝐃𝐃𝐈𝐄 𝐑𝐄𝐃𝐌𝐀𝐘𝐍𝐄\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐊𝐈𝐍𝐆𝐃𝐎𝐌\n𝐃𝐎𝐁 : 𝟔 𝐉𝐀𝐍,𝟏𝟗𝟖𝟐\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟏𝟓𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 :𝟓'𝟏𝟏'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐉𝐔𝐋𝐈𝐀𝐍𝐍𝐄 𝐌𝐎𝐎𝐑𝐄\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 : 𝟑 𝐃𝐄𝐂,𝟏𝟗𝟔𝟎\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟓𝟓𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟑"'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)

def year2016():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐒𝐏𝐎𝐓𝐋𝐈𝐆𝐇𝐓 ☆", 'music3.mp3',"m2016.jpg"
    k1,l1= "☆ 𝐀𝐋𝐄𝐉𝐀𝐍𝐃𝐑𝐎 𝐆𝐎𝐍𝐙𝐀𝐋𝐈𝐙 ☆","d2016.jpg"
    q1,r1,f1,g1,n1,o1="☆ 𝐁𝐑𝐈𝐄 𝐋𝐀𝐑𝐒𝐎𝐍 ☆","b2016.jpg" ,'audio2016.mp3','movie2016.mp4',"☆ 𝐋𝐄𝐎𝐍𝐀𝐑𝐃𝐎 𝐃𝐈𝐂𝐀𝐏𝐑𝐈𝐎 ☆","a2016.jpg"
    h1="𝐀𝐖𝐀𝐑𝐃  : 𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟏𝟔\n𝐌𝐎𝐕𝐈𝐄   : 𝐒𝐏𝐎𝐓𝐋𝐈𝐆𝐇𝐓\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑  : 𝐓𝐎𝐌 𝐌𝐂𝐂𝐀𝐑𝐓𝐇𝐘\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟑 𝐒𝐄𝐏𝐓,𝟐𝟎𝟏𝟓\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟖.𝟏\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍 : 𝟏𝟐𝟗 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟗𝟖.𝟕"
    m1='''𝐀𝐖𝐀𝐑𝐃  : 𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐀𝐋𝐄𝐉𝐀𝐍𝐃𝐑𝐎 𝐆𝐎𝐍𝐙𝐀𝐋𝐈𝐙 \n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐌𝐄𝐗𝐈𝐂𝐎\n𝐃𝐎𝐁  :𝟏𝟓 𝐀𝐔𝐆,𝟏𝟗𝟔𝟑\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟒𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟏𝟎" '''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 :𝐋𝐄𝐎𝐍𝐀𝐑𝐃𝐎 𝐃𝐈𝐂𝐀𝐏𝐑𝐈𝐎\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  :𝟏𝟏 𝐍𝐎𝐕,𝟏𝟗𝟕𝟒\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟑𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟗"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 :𝐁𝐑𝐈𝐄 𝐋𝐀𝐑𝐒𝐎𝐍\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 : 𝟏𝟎 𝐎𝐂𝐓,𝟏𝟗𝟖𝟗\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟐𝟓𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 :𝟓'𝟕"''' 
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)
def year2017():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐌𝐎𝐎𝐍𝐋𝐈𝐆𝐇𝐓 ☆", 'music3.mp3',"m2017.jpg"
    k1,l1="☆ 𝐃𝐎𝐌𝐈𝐄𝐍 𝐂𝐇𝐀𝐙𝐄𝐋𝐋𝐄 ☆","d2017.jpg"
    q1,r1,n1,o1,f1,g1= "☆ 𝐄𝐌𝐌𝐀 𝐒𝐓𝐎𝐍𝐄 ☆","b2017.jpg","☆ 𝐂𝐀𝐒𝐄𝐘 𝐀𝐅𝐅𝐋𝐄𝐂𝐊 ☆","a2017.jpg",'audio2017.mp3','movie2017.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃   :  𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟏𝟕\n𝐌𝐎𝐕𝐈𝐄  :𝐌𝐎𝐎𝐍𝐋𝐈𝐆𝐇𝐓\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑     : 𝐁𝐀𝐑𝐑𝐘 𝐉𝐄𝐍𝐊𝐈𝐍𝐒\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟐 𝐒𝐄𝐏𝐓,𝟐𝟎𝟏𝟔\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟕.𝟒\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍    : 𝟏𝟏𝟏 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟔𝟓.𝟑𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃  :  𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐃𝐎𝐌𝐈𝐄𝐍 𝐂𝐇𝐀𝐙𝐄𝐋𝐋𝐄\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  : 𝟏𝟗 𝐉𝐀𝐍,𝟏𝟗𝟖𝟓\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟔𝟓𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟓'𝟗"'''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐂𝐀𝐒𝐄𝐘 𝐀𝐅𝐅𝐋𝐄𝐂𝐊\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  :𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  : 𝟏𝟐 𝐀𝐔𝐆,𝟏𝟗𝟕𝟓\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟑𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟖"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐄𝐌𝐌𝐀 𝐒𝐓𝐎𝐍𝐄\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘   : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 : 𝟔 𝐍𝐎𝐕,𝟏𝟗𝟖𝟖\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟒𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟔"'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)
def year2022():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐂𝐎𝐃𝐀 ☆", 'music3.mp3',"m2022.jpg"
    k1,l1="☆ 𝐒𝐈𝐀𝐍 𝐇𝐄𝐃𝐄𝐑 ☆","d2022.jpg"
    q1,r1,n1,o1,f1,g1="☆ 𝐉𝐄𝐒𝐒𝐈𝐂𝐀 𝐂𝐇𝐀𝐒𝐓𝐀𝐈𝐍 ☆","b2022.jpg","☆ 𝐖𝐈𝐋𝐋 𝐒𝐌𝐈𝐓𝐇 ☆","a2022.jpg", 'audio2022.mp3','movie2022.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟐𝟐\n𝐌𝐎𝐕𝐈𝐄  : 𝐂𝐎𝐃𝐀\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 : 𝐒𝐈𝐀𝐍 𝐇𝐄𝐃𝐄𝐑\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍  : 𝟏𝟑 𝐀𝐔𝐆,𝟐𝟎𝟐𝟏\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟖.𝟎\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍  : 𝟏𝟏𝟏 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟏.𝟔𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐒𝐈𝐀𝐍 𝐇𝐄𝐃𝐄𝐑\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐍𝐄𝐖 𝐙𝐄𝐀𝐋𝐀𝐍𝐃\n𝐃𝐎𝐁 : 𝟑𝟎 𝐀𝐏𝐑,𝟏𝟗𝟓𝟒\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟏𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟖" '''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐖𝐈𝐋𝐋 𝐒𝐌𝐈𝐓𝐇\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐀𝐌𝐄𝐑𝐈𝐂𝐀\n𝐃𝐎𝐁 : 𝟐𝟓 𝐒𝐄𝐏𝐓,𝟏𝟗𝟔𝟖\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇  : $𝟑𝟓𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟔'𝟏"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐉𝐄𝐒𝐒𝐈𝐂𝐀 𝐂𝐇𝐀𝐒𝐓𝐀𝐈𝐍\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐀𝐌𝐄𝐑𝐈𝐂𝐀\n𝐃𝐎𝐁 : 𝟐𝟓 𝐒𝐄𝐏𝐓,𝟏𝟗𝟔𝟖\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟑𝟓𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟔'𝟏"'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)
def year2019():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆𝐆𝐑𝐄𝐄𝐍 𝐁𝐎𝐎𝐊☆", 'music3.mp3',"m2019.jpg"
    k1,l1="☆ 𝐀𝐋𝐅𝐎𝐍𝐒𝐎 𝐂𝐔𝐀𝐑𝐎𝐍 ☆","d2019.jpg"
    q1,r1,n1,o1,f1,g1="☆𝐎𝐋𝐈𝐕𝐈𝐀 𝐂𝐎𝐋𝐌𝐀𝐍☆","b2019.jpg","☆𝐑𝐀𝐌𝐈 𝐌𝐀𝐋𝐄𝐊☆","a2019.jpg", 'audio2019.mp3','movie2019.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟏𝟗\n𝐌𝐎𝐕𝐈𝐄  :𝐆𝐑𝐄𝐄𝐍 𝐁𝐎𝐎𝐊\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 : 𝐏𝐄𝐓𝐄𝐑 𝐅𝐀𝐑𝐑𝐄𝐋𝐘\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟏𝟏 𝐃𝐄𝐂, 𝟐𝟎𝟏𝟖\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 :𝟖.𝟐\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍  : 𝟏𝟑𝟎 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟑𝟐𝟏.𝟖𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 :𝐀𝐋𝐅𝐎𝐍𝐒𝐎 𝐂𝐔𝐀𝐑𝐎𝐍\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐌𝐄𝐗𝐈𝐂𝐎\n𝐃𝐎𝐁 : 𝟐𝟖 𝐍𝐨𝐯,𝟏𝟗𝟔𝟏\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟓𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟏𝟏"'''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐑𝐀𝐌𝐈 𝐌𝐀𝐋𝐄𝐊\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  :𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 : 𝟏𝟐 𝐌𝐚𝐲,𝟏𝟗𝟖𝟏\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟐𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟕"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐎𝐋𝐈𝐕𝐈𝐀 𝐂𝐎𝐋𝐌𝐀𝐍\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐔𝐊\n𝐃𝐎𝐁 : 𝟑𝟎 𝐉𝐀𝐍,𝟏𝟗𝟕𝟒\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟖𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟕""'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)
def year2020():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐏𝐀𝐑𝐀𝐒𝐈𝐓𝐄 ☆", 'music3.mp3',"m2020.jpg"
    k1,l1="☆ 𝐁𝐎𝐍𝐆 𝐉𝐎𝐎𝐍-𝐇𝐎 ☆","d2020.jpg"
    q1,r1,n1,o1,f1,g1="☆ 𝐑𝐄𝐍𝐄𝐄 𝐙𝐄𝐋𝐋𝐖𝐄𝐆𝐄𝐑 ☆","b2020.jpg","☆ 𝐉𝐎𝐀𝐐𝐔𝐈𝐍 𝐏𝐇𝐎𝐄𝐍𝐈𝐗 ☆","a2020.jpg", 'audio2020.mp3','movie2020.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟐𝟎\n𝐌𝐎𝐕𝐈𝐄  :𝐏𝐀𝐑𝐀𝐒𝐈𝐓𝐄\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 : 𝐁𝐎𝐍𝐆 𝐉𝐎𝐍-𝐇𝐎\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟐𝟏 𝐌𝐀𝐘,𝟐𝟎𝟏𝟗\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟖.𝟓\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍 : 𝟏𝟑𝟐 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟐𝟔𝟑.𝟏𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐁𝐎𝐍𝐆 𝐉𝐎𝐍-𝐇𝐎\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐒𝐎𝐔𝐓𝐇 𝐊𝐎𝐑𝐄𝐀\n𝐃𝐎𝐁 : 𝟏𝟒 𝐒𝐄𝐏,𝟏𝟗𝟔𝟗\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟑𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟗"'''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐉𝐎𝐀𝐐𝐔𝐈𝐍 𝐏𝐇𝐎𝐄𝐍𝐈𝐗\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 :𝟐𝟖 𝐎𝐂𝐓,𝟏𝟗𝟕𝟒\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟔𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟖"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐑𝐄𝐍𝐄𝐄 𝐙𝐄𝐋𝐋𝐖𝐄𝐆𝐄𝐑\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁 : 𝟐𝟓 𝐀𝐏𝐑,𝟏𝟗𝟔𝟗\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟗𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟒"'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)
def year2021():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝗡𝗢𝗠𝗔𝗗𝗟𝗔𝗡𝗗 ☆",'music3.mp3',"m2021.jpg"
    k1,l1="☆ 𝗖𝗛𝗟𝗢𝗘 𝗭𝗛𝗔𝗢 ☆","d2021.jpg"
    q1,r1,n1,o1,f1,g1="☆ 𝗙𝗥𝗔𝗡𝗖𝗘𝗦 𝗠𝗖𝗗𝗢𝗥𝗠𝗔𝗡𝗗 ☆","b2021.jpg","☆ 𝗔𝗡𝗧𝗛𝗢𝗡𝗬 𝗛𝗢𝗣𝗞𝗜𝗡𝗦 ☆","a2021.jpg", 'audio2021.mp3','movie2021.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟐𝟏\n𝐌𝐎𝐕𝐈𝐄  :𝗡𝗢𝗠𝗔𝗗𝗟𝗔𝗡𝗗\n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑  :𝗖𝗛𝗟𝗢𝗘 𝗭𝗛𝗔𝗢\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟐𝟗 𝐉𝐀𝐍 𝟐𝟎𝟐𝟏\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟕.𝟑\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍 : 𝟏𝟎𝟖 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟑𝟗.𝟓𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 :𝐂𝐇𝐋𝐎𝐄 𝐙𝐇𝐀𝐎 \n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐂𝐇𝐈𝐍𝐀\n𝐃𝐎𝐁 : 𝟑𝟏 𝐌𝐀𝐑,𝟏𝟗𝟖𝟐\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟔.𝟏𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓 : 𝟓'𝟗"'''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐀𝐍𝐓𝐇𝐎𝐍𝐘 𝐇𝐎𝐏𝐊𝐈𝐍𝐒\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐊\n𝐃𝐎𝐁 : 𝟑𝟏 𝐃𝐄𝐂,𝟏𝟗𝟑𝟕\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟏𝟔𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟗"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐅𝐑𝐀𝐍𝐂𝐄𝐒 𝐌𝐂𝐃𝐎𝐑𝐌𝐀𝐍𝐃\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  : 𝟐𝟑 𝐉𝐔𝐍𝐄,𝟏𝟗𝟓𝟕\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟏𝟎𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟓"'''
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)   
def year2018():
    a1,b1,c1,d1,e1="background1.jpg", 'audio.mp3',"☆ 𝐓𝐇𝐄 𝐒𝐇𝐀𝐏𝐄 𝐎𝐅 𝐖𝐀𝐓𝐄𝐑 ☆",'music3.mp3',"m2018.jpg"
    k1,l1="☆ 𝐆𝐔𝐈𝐋𝐋𝐄𝐑𝐌𝐎 𝐃𝐄𝐋 𝐓𝐎𝐑𝐎 ☆","d2018.jpg"
    q1,r1,n1,o1,f1,g1="☆ 𝗙𝗥𝗔𝗡𝗖𝗘𝗦 𝗠𝗖𝗗𝗢𝗥𝗠𝗔𝗡𝗗 ☆","b2018.jpg","☆ 𝐆𝐀𝐑𝐘 𝐎𝐋𝐃𝐌𝐀𝐍 ☆","a2018.jpg", 'audio2018.mp3','movie2018.mp4'
    h1="𝐀𝐖𝐀𝐑𝐃  :  𝐁𝐄𝐒𝐓 𝐎𝐒𝐂𝐀𝐑 𝐌𝐎𝐕𝐈𝐄 𝟐𝟎𝟏𝟖\n𝐌𝐎𝐕𝐈𝐄 :𝐓𝐇𝐄 𝐒𝐇𝐀𝐏𝐄 𝐎𝐅 𝐖𝐀𝐓𝐄𝐑 \n𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 : 𝐆𝐈𝐈𝐋𝐋𝐄𝐑𝐌𝐎 𝐃𝐄𝐋 𝐓𝐎𝐑𝐎\n𝐑𝐄𝐋𝐄𝐀𝐒𝐄𝐃 𝐎𝐍 : 𝟏 𝐃𝐄𝐂,𝟐𝟎𝟏𝟕\n𝐈𝐌𝐃𝐛 𝐑𝐀𝐓𝐈𝐍𝐆 : 𝟕.𝟑\n𝐃𝐔𝐑𝐀𝐓𝐈𝐎𝐍    : 𝟏𝟐𝟑 𝐌𝐈𝐍𝐔𝐓𝐄𝐒\n𝐁𝐎𝐗 𝐎𝐅𝐅𝐈𝐂𝐄  : $𝟏𝟗𝟓.𝟑𝐌"
    m1='''𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐆𝐈𝐈𝐋𝐋𝐄𝐑𝐌𝐎 𝐃𝐄𝐋 𝐓𝐎𝐑𝐎\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐌𝐄𝐗𝐈𝐂𝐎\n𝐃𝐎𝐁 : 𝟗 𝐎𝐂𝐓,𝟏𝟗𝟔𝟒\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟒𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟓'𝟏𝟎" '''
    p1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐎𝐑\n𝐍𝐀𝐌𝐄 : 𝐆𝐀𝐑𝐘 𝐎𝐋𝐃𝐌𝐀𝐍\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘  : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  :𝟐𝟏 𝐌𝐀𝐑,𝟏𝟗𝟓𝟖\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟒𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟖"'''
    s1='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐀𝐂𝐓𝐑𝐄𝐒𝐒\n𝐍𝐀𝐌𝐄 : 𝐅𝐑𝐀𝐍𝐂𝐄𝐒 𝐌𝐂𝐃𝐎𝐑𝐌𝐀𝐍𝐃\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : 𝐔𝐍𝐈𝐓𝐄𝐃 𝐒𝐓𝐀𝐓𝐄𝐒\n𝐃𝐎𝐁  : 𝟐𝟑 𝐉𝐔𝐍𝐄,𝟏𝟗𝟓𝟕\n𝐍𝐄𝐓 𝐖𝐎𝐑𝐓𝐇 : $𝟏𝟎𝟎𝐌\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃 : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  : 𝟓'𝟓"''' 
    allyears(a1,b1,c1,d1,e1,f1,g1,h1,k1,l1,m1,n1,o1,p1,q1,r1,s1)  
#....................................................................modify window.....................
def modifywin():
    modifywin=Toplevel(PR)   
    modifywin.minsize(height=1100,width=1900)
    pygame.mixer.init()
    file = 'm6.mp3'
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    im="background1.jpg"
    img = Image.open(im)
    img = img.resize((2000, 1500))
    img = ImageTk.PhotoImage(img)
    panel = Label(modifywin, image=img,bd=2)
    panel.image = img
    panel.place(x=0,y=0)      
    def insert():
        Year=e_Year.get();
        Movie_Name=e_Movie_Name.get();
        Director_Name=e_Director_Name.get();
        Actor_Name=e_Actor_Name.get();
        Actress_Name=e_Actress_Name.get();
        if(Year<='2023' or Movie_Name=="" or Director_Name=="" or Actress_Name=="" ):
            pygame.mixer.init()
            file = 'somethingwentwrong.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            MessageBox.showwarning("Insert Status","Something Went Wrong Please Try Again!",parent=modifywin)
        else:
            con=mysql.connect(host="localhost",user="root",password="root",database="pr")
            cursor=con.cursor()
            cursor.execute("INSERT INTO rp VALUES ('"+ Year +"','"+ Movie_Name +"','"+ Director_Name +"','"+Actor_Name+"','"+ Actress_Name +"')")
            cursor.execute("commit");
            e_Year.delete(0,'end')
            pygame.mixer.init()
            file = 'click1.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            e_Movie_Name.delete(0,'end')
            e_Director_Name.delete(0,'end')
            e_Actor_Name.delete(0,'end')
            e_Actress_Name.delete(0,'end')
            MessageBox.showinfo("Data sucessesfully inserted","Thank You Your Data is Inserted",parent=modifywin)
            con.close();
    def delete():
        if(e_Year.get()==""):   
            pygame.mixer.init()
            file = 'somethingwentwrong.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            
            MessageBox.showwarning("Delete Status","Something Went Wrong Please Try Again!",parent=modifywin)
        else:
            con=mysql.connect(host="localhost",user="root",password="root",database="pr")
            cursor=con.cursor()
            cursor.execute("delete from rp where Year='"+ e_Year.get() +"'")
            cursor.execute("commit")
            e_Year.delete(0,'end')
            pygame.mixer.init()
            file = 'click3.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            e_Movie_Name.delete(0,'end')
            e_Director_Name.delete(0,'end')
            e_Actor_Name.delete(0,'end')
            e_Actress_Name.delete(0,'end')
            MessageBox.showinfo("Data succsesfully removed","Data Deleted",parent=modifywin);
            con.close();
    def update():
        Movie_Name=e_Movie_Name.get();
        Director_Name=e_Director_Name.get();
        Actor_Name=e_Actor_Name.get();
        Actress_Name=e_Actress_Name.get();
        Year=e_Year.get();
        
        if( Year=="" or Movie_Name=="" or Director_Name=="" or Actor_Name=="" or Actress_Name==""  ):
            pygame.mixer.init()
            file = 'somethingwentwrong.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            MessageBox.showwarning("Update Status", "Something Went Wrong Please Try Again!",parent=modifywin)
        else:
            con=mysql.connect(host="localhost",user="root",password="root",database="pr")
            cursor=con.cursor()
            query=("UPDATE rp SET Movie_Name=%s,Director_Name=%s,Actor_Name=%s,Actress_Name=%s where Year=%s")
            record=(Movie_Name,Director_Name,Actor_Name,Actress_Name,Year)
            cursor.execute(query,record)
            pygame.mixer.init()
            file = 'click2.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            cursor.execute("commit");
            e_Year.delete(0,'end')
            e_Movie_Name.delete(0,'end')
            e_Director_Name.delete(0,'end')
            e_Actor_Name.delete(0,'end')
            e_Actress_Name.delete(0,'end')
            MessageBox.showinfo("Data succesesfully updated","Data updated",parent=modifywin);
            con.close();        
    def get():
      
        Year=e_Year.get();
        if (e_Year.get()==""):
            pygame.mixer.init()
            file = 'somethingwentwrong.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            MessageBox.showwarning("Fetch Status","Something Went Wrong Please Try Again!",parent=modifywin)
        else:
            con=mysql.connect(host="localhost",user="root",password="root",database="pr")
            cursor=con.cursor()
            cursor.execute("select * from rp where Year='"+ Year +"'")
            rows=cursor.fetchall()
            for row in rows:
                e_Movie_Name.insert(0,row[1])
                e_Director_Name.insert(0,row[2])
                e_Actor_Name.insert(0,row[3])
                e_Actress_Name.insert(0,row[4])
            con.close();
            
    def data():
        
        data=Toplevel()
        data.minsize(height=1100,width=1900)
        im="background1.jpg"
        img = Image.open(im)
        img = img.resize((1900, 1100))
        img = ImageTk.PhotoImage(img)
        panel = Label(data, image=img,bd=2)
        panel.image = img
        panel.place(x=0,y=0)
        btn=Button(data,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="white",bg="black", bd=10,command=data.destroy,width=10).place(x=70,y=880)
        def display(x,y):
            
            con=mysql.connect(host="localhost",user="root",password="root",database="pr")
            cursor=con.cursor()
            cursor.execute("select * from rp")
            rows=cursor.fetchall()
            
            list.delete(0,list.size())
            heading=y
            list.insert(list.size(),heading)
            for row in rows:
                insertData=    str(row[x])
                list.insert(list.size()+1,insertData)
            con.close()
       
        lbl1=Label(data,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=60)         
        list=Listbox(font=("italic",20),height=20,width=7,bg="cyan",fg= "black",master=data)
        list.place(x=190-30,y=185)
        x,y=0,"𝐘𝐄𝐀𝐑"
        display(x,y)   
        list=Listbox(font=("italic",20),height=20,width=25,bg="cyan",fg= "black",master=data)
        list.place(x=290-30,y=185)
        x,y=1,"𝐌𝐎𝐕𝐈𝐄 𝐍𝐀𝐌𝐄"
        display(x,y)
        list=Listbox(font=("italic",20),height=20,width=35,bg="cyan",fg= "black",master=data)
        list.place(x=615-30,y=185)
        x,y=2,"𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 𝐍𝐀𝐌𝐄"
        display(x,y)
        list=Listbox(font=("italic",20),height=20,width=22,bg="cyan",fg= "black",master=data)
        list.place(x=1090-30,y=185)
        x,y=3,"𝐀𝐂𝐓𝐎𝐑 𝐍𝐀𝐌𝐄"
        display(x,y)
        list=Listbox(font=("italic",20),height=20,width=25,bg="cyan",fg= "black",master=data)
        list.place(x=1410-30,y=185)
        x,y=4,"𝐀𝐂𝐓𝐑𝐄𝐒𝐒 𝐍𝐀𝐌𝐄 "
        display(x,y)
        
    def clear():
            
        
        pygame.mixer.init()
        file = 'click4.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()   
        e_Year.delete(0,'end')
        e_Movie_Name.delete(0,'end')
        e_Director_Name.delete(0,'end')
        e_Actor_Name.delete(0,'end')
        e_Actress_Name.delete(0,'end')
    
    e_Year = Entry(modifywin,width= 30,fg="blue",bg="red",font=("", 29))
    e_Year.place(x=510,y=340)
    e_Movie_Name = Entry(modifywin,width= 30,bg="cyan",fg="black",font=("", 29))
    e_Movie_Name.place(x=510,y=435)
    e_Director_Name = Entry(modifywin,width= 30,bg="cyan",fg="black",font=("", 29))
    e_Director_Name.place(x=510,y=525)
    e_Actor_Name = Entry(modifywin,width= 30,bg="cyan",fg="black",font=("", 29))
    e_Actor_Name.place(x=510,y=610)
    e_Actress_Name = Entry(modifywin,width= 30,bg="cyan",fg="black",font=("", 29))
    e_Actress_Name.place(x=510,y=710)
    lbl=Label(modifywin,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=50)
    lbl=Label(modifywin,text=" ░▒▓█ 𝟐𝟎𝟏𝟓-𝟐𝟎𝟐𝟐 █▓▒░",fg="white",bg="black",font=("####", 40)).place(x=665,y=150)
    def yearaudio():
        x= 'enteryear.mp3'
        mynew(x)
    def movieaudio():
        x= 'enter movie nmae.mp3'
        mynew(x)
    def directoraudio():
        x= 'enter director name.mp3'
        mynew(x)
    def actoraudio():
        x= 'enter actor name.mp3'
        mynew(x)
    def actressaudio():
        x= 'ener actress name.mp3'
        mynew(x)
    def dataaudio():
        x= 'main window.mp3'
        mynew(x)
    def music():
        x= 'dta.mp3'
        mynew(x)
        modifywin.destroy()
    def enterdata():
        v= 'enteryourdata.mp3'
        audd2(v)
    btn1=Button(modifywin,text="𝐘𝐄𝐀𝐑 :-                   ",fg="white",command=yearaudio,bg="blACK",font=("",25),bd=5,width=15).place(x=150,y=330)    
    btn2=Button(modifywin,text="𝐌𝐎𝐕𝐈𝐄 𝐍𝐀𝐌𝐄 :-        ",fg="white",command=movieaudio,bg="BLACK",font=("",25) ,bd=5,width=15).place(x=150,y=420)
    btn3=Button(modifywin,text="𝐃𝐈𝐑𝐄𝐂𝐓𝐎𝐑 𝐍𝐀𝐌𝐄 :-   ",fg="white",command=directoraudio,bg="BLACK",font=("",25) ,bd=5,width=15).place(x=150,y=510)
    btn4=Button(modifywin,text="𝐀𝐂𝐓𝐎𝐑 𝐍𝐀𝐌𝐄 :-        ",fg="white",command=actoraudio,bg="BLACK",font=("",25),bd=5,width=15).place(x=150,y=600)
    btn5=Button(modifywin,text="𝐀𝐂𝐓𝐑𝐄𝐒𝐒 𝐍𝐀𝐌𝐄 :-     ",fg="white",command=actressaudio,bg="BLACK",font=("",25) ,bd=5,width=15).place(x=150,y=700)    
    btn6=Button(modifywin,text="𝐘𝐎𝐔𝐑 𝐃𝐀𝐓𝐀 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐀𝐃𝐃𝐄𝐃 𝐒𝐎𝐎𝐍 𝐈𝐍 𝐓𝐇𝐄 𝐌𝐀𝐈𝐍 𝐖𝐈𝐍𝐃𝐎𝐖.......................                              ",command=dataaudio,fg="white",bg="blACK",font=("",26),bd=5,width=70).place(x=410,y=900)
    
    btn=Button(modifywin,text="𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐃𝐀𝐓𝐀             ",fg="white",command=enterdata,bg="blACK",font=("",25),bd=5,width=53).place(x=150,y=240)    
    btn=Button(modifywin,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="WHITE",bg="black", bd=10,command=music,width=10).place(x=70,y=880)
    modifywin.bind('<Return>',lambda event:insert())
    btn=Button(modifywin,text="𝐈𝐍𝐒𝐄𝐑𝐓",fg="white",bg="BLACK",font=("",25),command=insert ,bd=7,width=15).place(x=1450,y=240)
    btn=Button(modifywin,text="𝐔𝐏𝐃𝐀𝐓𝐄",fg="white",bg="BLACK",font=("",25),command=update ,bd=5,width=15).place(x=1450,y=325)
    btn=Button(modifywin,text="𝐃𝐄𝐋𝐄𝐓𝐄",fg="white",bg="BLACK",font=("",25),command=delete ,bd=7,width=15).place(x=1450,y=405)
    btn=Button(modifywin,text="𝐂𝐋𝐄𝐀𝐑",fg="white",bg="bLACK",font=("",25),command=clear ,bd=7,width=15).place(x=1450,y=488)
    btn=Button(modifywin,text="𝐒𝐇𝐎𝐖 𝐑𝐄𝐂𝐎𝐑𝐃𝐒",fg="white",bg="bLACK",font=("",25),command=get ,bd=7,width=15).place(x=1450,y=570)
    btn=Button(modifywin,text="𝐒𝐇𝐎𝐖 𝐓𝐀𝐁𝐋𝐄",fg="black",bg="red",font=("",25),command=data,bd=7,width=15).place(x=1450,y=655)

def d():
        Review=Toplevel()
        Review.minsize(width=1900,height=1100)
        im="background1.jpg"
        img = Image.open(im)
        img = img.resize((2000, 1500))
        img = ImageTk.PhotoImage(img)
        panel = Label(Review, image=img,bd=0)
        panel.image = img
        panel.place(x=0,y=0)
        pygame.mixer.init()
        file = 'audio.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
        def m():
            def view(x,y):
                    con=mysql.connect(host="localhost",user="root",password="root",database="pr")
                    cursor=con.cursor()
                    cursor.execute("select * from Review")
                    rows=cursor.fetchall()            
                    list.delete(0,list.size())
                    heading=   y
                    list.insert(list.size(),heading)
                    for row in rows:
                        insertData=    str(row[x])
                        list.insert(list.size()+1,insertData)
                    con.close()
            
            list=Listbox(font=("italic",20),height=12,width=30,bg="cyan",fg= "black",master=Review)
            list.place(x=45,y=600)
            x,y=0,"𝐍𝐀𝐌𝐄"
            view(x,y)
            list=Listbox(font=("italic",20),height=12,width=70,bg="cyan",fg= "black",master=Review)
            list.place(x=450,y=600)
            x,y=1,"𝐂𝐎𝐌𝐌𝐄𝐍𝐓"
            view(x,y)
            list=Listbox(font=("italic",20),height=12,width=25,bg="cyan",fg= "black",master=Review)
            list.place(x=1220,y=600)
            x,y=2,"𝐘𝐄𝐀𝐑 𝐋𝐈𝐊𝐄𝐃"
            view(x,y)
            list=Listbox(font=("italic",20),height=12,width=21,bg="cyan",fg= "black",master=Review)
            list.place(x=1545,y=600)
            x,y=3,"𝐑𝐀𝐓𝐈𝐍𝐆"
            view(x,y)
            
        def submit():
            Name=e_Name.get();
            Comment=e_Comment.get();
            Year_Liked=e_Year_Liked.get();
            Rating=e_Rating.get();
            if(Name=="" or Comment=="" or Year_Liked=="" or Year_Liked>"2022" or Year_Liked<"2015" or Rating=="" or Rating>"5.0"):   
                pygame.mixer.init()
                file ="somethingwentwrong.mp3"
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                MessageBox.showwarning("Insert Status","Something Went Wrong Please Try Again!",parent=Review)
            else:
                pygame.mixer.init()
                file ="Responsws are precious.mp3"
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                con=mysql.connect(host="localhost",user="root",password="root",database="pr")
                cursor=con.cursor()
                cursor.execute("INSERT INTO Review ( Name,Comment,Year_Liked,Rating) VALUES ('"+ Name +"','"+ Comment +"','"+  Year_Liked +"','"+Rating+"')")
                cursor.execute("commit");
                m()
                btn1=Button(Review,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="WHITE",bg="black", bd=10,command=Review1,width=8).place(x=10,y=890)
                e_Name.delete(0,'end')
                e_Comment.delete(0,'end')
                e_Year_Liked.delete(0,'end')
                e_Rating.delete(0,'end')
                MessageBox.showinfo("Data sucessesfully inserted","Thank You for your Response",parent=Review)
                con.close();
        lbl1=Label(Review,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=60)
        def au1():
            x=  'name.mp3'
            mynew(x)   
        def au2():
            x= 'comment.mp3'
            mynew(x)
        def au3():
            x='year.mp3'
            mynew(x)  
        def au4():
            x='rating.mp3'
            mynew(x)
        def heart():
                file3 = open("likes.txt","r+")
                y=file3.read()
                x=int(y)
                a=str(x)
                file3.close()
                file3 = open("likes.txt","w")
                file3.write(a)
                bl=Label(Review,text=a,font=("Courier", 20),width=4,bg="cyan",fg="black",bd=10).place(x=1750,y=350)
        def like2():
                file3 = open("likes2.txt","r+")
                y=file3.read()
                x=int(y)
                a=str(x)
                file3.close()
                file3 = open("likes2.txt","w")
                file3.write(a)
                bl=Label(Review,text=a,font=("Courier", 20),width=4,bg="cyan",fg="black",bd=10).place(x=1750,y=510)
        def heart2():
                file3 = open("likes.txt","r+")
                y=file3.read()
                x=int(y)
                x+=1
                a=str(x)
                file3.close()
                file3 = open("likes.txt","w")
                file3.write(a)
                bl=Label(Review,text=a,font=("Courier", 20),width=4,bg="cyan",fg="black",bd=10).place(x=1750,y=350)
                
        def likes2():
                file3 = open("likes2.txt","r+")
                y=file3.read()
                x=int(y)
                x+=1
                a=str(x)
                file3.close()
                file3 = open("likes2.txt","w")
                file3.write(a)
                bl=Label(Review,text=a,font=("Courier", 20),width=4,bg="cyan",fg="black",bd=10).place(x=1750,y=510)                
      
        
       
        
        tmr=Button(Review,text="",image=li,command=heart2,bd=5,bg="black").place(x=1750,y=250)       
            
        
         
        tmr=Button(Review,text="",image=L,command=likes2,bd=5,bg="black").place(x=1750,y=415)    
        btn1=Button(Review,text="𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐍𝐀𝐌𝐄 :-                                                         ",font=("", 25),command=au1,fg="white",bg="black",bd=5,width=42).place(x=60,y=200)
        btn1=Button(Review,text="𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐂𝐎𝐌𝐌𝐄𝐍𝐓 :-                                                  ",font=("", 25),command=au2,fg="white",bg="black",bd=5,width=42).place(x=60,y=280)
        btn1=Button(Review,text="𝐖𝐇𝐈𝐂𝐇 𝐘𝐄𝐀𝐑 𝐃𝐎 𝐘𝐎𝐔 𝐋𝐈𝐊𝐄𝐃 𝐌𝐎𝐒𝐓 ?                                   ",font=("", 25),fg="white",command=au3,bg="black",bd=5,width=42).place(x=60,y=360)
        btn1=Button(Review,text="𝐖𝐇𝐀𝐓 𝐑𝐀𝐓𝐈𝐍𝐆 𝐖𝐎𝐔𝐋𝐃 𝐘𝐎𝐔 𝐋𝐈𝐊𝐄 𝐓𝐎 𝐆𝐈𝐕𝐄 𝐔𝐒 (𝐎𝐔𝐓 𝐎𝐅 𝟓) :-  ",font=("", 25),fg="white",bg="black",bd=5,command=au4,width=42).place(x=60,y=440)

        
       
        e_Name = Entry(Review,width= 35,fg="blue",bg="red",font=("", 29))
        e_Name.place(x=900,y=215)
        e_Comment = Entry(Review,width= 35,fg="blue",bg="red",font=("", 29))
        e_Comment.place(x=900,y=290)
        e_Year_Liked = Entry(Review,width= 35,fg="blue",bg="red",font=("", 29))
        e_Year_Liked.place(x=900,y=375)
        e_Rating= Entry(Review,width= 35,fg="blue",bg="red",font=("", 29))
        e_Rating.place(x=900,y=450)

        Review.bind('<Return>',lambda event:submit())
        btn1=Button(Review,text="𝐒𝐔𝐁𝐌𝐈𝐓",font=("", 25),command=submit,fg="black",bg="red",bd=5,width=15).place(x=1150,y=510)
        def Review1():
            pygame.mixer.init()
            file = 'mm1.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            Review.destroy()
        
        m()
        heart()
        like2()
        btn1=Button(Review,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="WHITE",bg="black", bd=10,command=Review1,width=8).place(x=10,y=890)
    
    
        
#_____________________________________________________WINDOW 2_________________________________________________________

    
def func():
    win=Toplevel(PR)    
    win.minsize(height=1100,width=1900)    
    pygame.mixer.init()
    file = 'audio.mp3'
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    im="peakpx.jpg"
    img = Image.open(im)
    img = img.resize((2000,1100))
    img = ImageTk.PhotoImage(img)
    panel = Label(win, image=img,bd=0)
    panel.image = img
    panel.place(x=0,y=0)
    im="peakpx (23).jpg"
    img = Image.open(im)
    img = img.resize((900,870))
    img = ImageTk.PhotoImage(img)
    panel = Label(win, image=img,bd=0)
    panel.image = img
    panel.place(x=1010,y=210)
    lbl=Label(win,text=" ",fg="red",bg="red",bd=270,width=1,font=("####", 70)).place(x=100,y=220)
    def file():
        pygame.mixer.init()
        file = 'music2.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        win.destroy()
    lbl=Label(win,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=75)
    btn=Button(win,text="𝐂𝐇𝐎𝐎𝐒𝐄 𝐓𝐇𝐄 𝐘𝐄𝐀𝐑 :-           ",font=("", 30),fg="white",bg="black",bd=10,width=21,height=1).place(x=150,y=270)
    btn=Button(win,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="white",bg="black", bd=10,command=file,width=10).place(x=150,y=880)
#............................................................buttons of 2nd window.........................................
    btn1=Button(win,text="2022",fg="white",bg="black",font=("",25),bd=10,command=year2022,width=8).place(x=150,y=390)
    btn2=Button(win,text="2021",fg="white",bg="black",font=("",25) ,bd=10,command=year2021,width=8).place(x=150,y=480)
    btn3=Button(win,text="2020",fg="white",bg="black",font=("",25) ,bd=10,command=year2020,width=8).place(x=150,y=570)
    btn4=Button(win,text="2019",fg="white",bg="black",font=("",25),bd=10,command=year2019,width=8).place(x=150,y=660)
    btn5=Button(win,text="2018",fg="white",bg="black",font=("",25) ,bd=10,command=year2018,width=8).place(x=370,y=390)
    btn6=Button(win,text="2017",fg="white",bg="black",font=("",25) ,bd=10,command=year2017,width=8).place(x=370,y=480)
    btn7=Button(win,text="2016",fg="white",bg="black",font=("",25) ,bd=10,command=year2016,width=8).place(x=370,y=570)
    btn8=Button(win,text="2015",fg="white",bg="black",font=("",25),bd=10,command=year2015,width=8).place(x=370,y=660)
    def about():

                    about=Toplevel()
                    about.minsize(height=1100,width=1900)
                    pygame.mixer.init()
                    file = 'Oscar intro.mp3'
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    im="background1.jpg"
                    img = Image.open(im)
                    img = img.resize((2000, 1500))
                    img = ImageTk.PhotoImage(img)
                    panel = Label(about, image=img,bd=0)
                    panel.image = img
                    panel.place(x=0,y=0)
                                       
                    lbl=Label(about,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                    def music1():
                        pygame.mixer.init()
                        file = 'dta.mp3'
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        about.destroy()
                    btn2=Button(about,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=music1,width=3).place(x=1735-60,y=488)
                    btn1=Button(about,text="《",font=("", 35),fg="white",bg="black",bd=10,command=music1,width=3).place(x=60+80,y=488)    
                   
                    lbl1=Label(about,text='''𝐓𝐡𝐞 𝐀𝐜𝐚𝐝𝐞𝐦𝐲 𝐀𝐰𝐚𝐫𝐝𝐬 𝐂𝐨𝐦𝐦𝐨𝐧𝐥𝐲 𝐤𝐧𝐨𝐰𝐧 𝐚𝐬 𝐎𝐬𝐜𝐚𝐫
𝐀𝐰𝐚𝐫𝐝𝐬,𝐢𝐭 𝐢𝐬 𝐚 𝐩𝐫𝐞𝐬𝐭𝐢𝐠𝐢𝐨𝐮𝐬 𝐚𝐰𝐚𝐫𝐝 𝐭𝐡𝐚𝐭 𝐫𝐞𝐜𝐨𝐠𝐧𝐢𝐬𝐞𝐬
𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐭𝐢𝐞𝐬 𝐰𝐢𝐭𝐡 𝐚𝐫𝐭𝐢𝐬𝐭𝐢𝐜 𝐚𝐧𝐝 𝐭𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐦𝐞𝐫𝐢𝐭 𝐢𝐧 𝐭𝐡𝐞
𝐦𝐨𝐯𝐢𝐞 𝐢𝐧𝐝𝐮𝐬𝐭𝐫𝐲.𝐈𝐭 𝐢𝐬 𝐩𝐫𝐞𝐬𝐞𝐧𝐭𝐞𝐝 𝐚𝐧𝐧𝐮𝐚𝐥𝐥𝐲 𝐛𝐲 𝐭𝐡𝐞
𝐀𝐜𝐚𝐝𝐞𝐦𝐲 𝐨𝐟 𝐌𝐨𝐭𝐢𝐨𝐧 𝐏𝐢𝐜𝐭𝐮𝐫𝐞 𝐀𝐫𝐭𝐬 𝐚𝐧𝐝 𝐒𝐜𝐢𝐞𝐧𝐜𝐞𝐬. 𝐈𝐭
𝐰𝐚𝐬 𝐟𝐨𝐮𝐧𝐝𝐞𝐝 𝐢𝐧 𝟏𝟗𝟐𝟕,𝐛𝐮𝐭 𝐭𝐡𝐞 𝐩𝐫𝐞𝐬𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧 𝐰𝐚𝐬
𝐟𝐢𝐫𝐬𝐭 𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐢𝐧 𝟏𝟗𝟐𝟗, 𝐚𝐧𝐝 𝐰𝐢𝐧𝐧𝐞𝐫𝐬 𝐬𝐢𝐧𝐜𝐞 𝐭𝐡𝐞𝐧
𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐚 𝐠𝐨𝐥𝐝-𝐩𝐥𝐚𝐭𝐞𝐝 𝐬𝐭𝐚𝐭𝐮𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐨𝐧𝐥𝐲 𝐜𝐚𝐥𝐥𝐞𝐝
𝐎𝐬𝐜𝐚𝐫.''',fg="black",justify=LEFT,bd=50,bg="cyan",font=("####", 42)).place(x=318,y=250)
                    btn=Button(about,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="WHITE",bg="black", bd=10,command=music1,width=10).place(x=70,y=880)
                
        
    def othrec():
        othrec=Toplevel()
        cn=Canvas(othrec, bg="black",height=1100, width=1900).pack()
        othrec.minsize(height=1100,width=1900)
        im="joker1.jpg"
        img = Image.open(im)
        img = img.resize((1000, 900))
        img = ImageTk.PhotoImage(img)
        panel = Label(othrec, image=img,bd=0)
        panel.image = img
        panel.place(x=900,y=150)
        lbl=Label(othrec,text=" ",bg="blue",bd=270,width=1,font=("####", 70)).place(x=100,y=220)
        btn=Button(othrec,text="𝐄𝐗𝐈𝐓",font=("", 35),fg="white",bg="black", bd=10,command=othrec.destroy,width=10).place(x=60,y=880)
        btn=Button(othrec,text="𝐂𝐇𝐎𝐎𝐒𝐄 𝐓𝐇𝐄 𝐘𝐄𝐀𝐑 :-           ",font=("", 30),fg="white",bg="black",bd=10,width=21,height=1).place(x=150,y=270)
        lbl=Label( othrec,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=75)
        def data(z):
           
            data=Toplevel()
            data.minsize(height=1100,width=1900)
            im="background1.jpg"
            img = Image.open(im)
            img = img.resize((1900, 1100))
            img = ImageTk.PhotoImage(img)
            panel = Label(data, image=img,bd=2)
            panel.image = img
            panel.place(x=0,y=0)
            btn=Button(data,text="𝐁𝐀𝐂𝐊",font=("", 30),fg="white",bg="black", bd=10,command=data.destroy,width=10).place(x=70,y=880)
            def display(x,y):
                con=mysql.connect(host="localhost",user="root",password="root",database="pr")
                cursor=con.cursor()
                cursor.execute(z)
                rows=cursor.fetchall()
                
                list.delete(0,list.size())
                heading=y
                list.insert(list.size(),heading)
                for row in rows:
                    insertData=    str(row[x])
                    list.insert(list.size()+1,insertData)
                con.close()
           
            lbl1=Label(data,text=" ░▒▓█ 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=340,y=60)         
            list=Listbox(font=("italic",20),height=20,width=40,bg="cyan",fg= "black",master=data)
            list.place(x=190-30,y=185)
            x,y=0,"𝐀𝐖𝐀𝐑𝐃 𝐍𝐀𝐌𝐄 "
            display(x,y)   
            list=Listbox(font=("italic",20),height=20,width=50,bg="cyan",fg= "black",master=data)
            list.place(x=640,y=185)
            x,y=1,"𝐖𝐈𝐍𝐍𝐄𝐑"
            display(x,y)
            list=Listbox(font=("italic",20),height=20,width=30,bg="cyan",fg= "black",master=data)
            list.place(x=1300,y=185)
            x,y=2,"𝐂𝐎𝐔𝐍𝐓𝐑𝐘"
            display(x,y)
           
            
            
        def selected():
            z="select * from  REC2022"
            data(z)
    
        def selected1():
            z="select * from REC2021"
            data(z)    
        def selected2():
            z="select * from REC2020"
            data(z)
        def selected3():
            z="select * from REC2019"
            data(z)
        def selected4():
            z="select * from REC2018"
            data(z)
        def selected5():
            z="select * from REC2017"
            data(z)
        def selected6():
            z="select * from REC2016"
            data(z)
        def selected7():
            z="select * from REC2015"
            data(z) 
        btn1=Button( othrec,text="2022",fg="white",bg="black",font=("",25),bd=10,command=selected,width=8).place(x=150,y=390)
        btn2=Button( othrec,text="2021",fg="white",bg="black",font=("",25) ,bd=10,command=selected1,width=8).place(x=370,y=390)
        btn3=Button( othrec,text="2020",fg="white",bg="black",font=("",25) ,bd=10,command=selected2,width=8).place(x=150,y=480)
        btn4=Button( othrec,text="2019",fg="white",bg="black",font=("",25) ,bd=10,command=selected3,width=8).place(x=370,y=480)
        btn5=Button( othrec,text="2018",fg="white",bg="black",font=("",25) ,bd=10,command=selected4,width=8).place(x=150,y=570)
        btn6=Button( othrec,text="2017",fg="white",bg="black",font=("",25) ,bd=10,command=selected5,width=8).place(x=370,y=570)
        btn7=Button( othrec,text="2016",fg="white",bg="black",font=("",25),bd=10,command=selected6,width=8).place(x=150,y=660)
        btn8=Button( othrec,text="2015",fg="white",bg="black",font=("",25),bd=10,command=selected7,width=8).place(x=370,y=660)
        

    btn9=Button(win,text=" 𝐃𝐀𝐓𝐀 𝐌𝐀𝐍𝐈𝐏𝐔𝐋𝐀𝐓𝐈𝐎𝐍 ",fg="white",bg="black",font=("",30),bd=10,command=modifywin,width=17).place(x=820,y=870)   
    btn=Button(win,text="𝐆𝐈𝐕𝐄 𝐑𝐄𝐕𝐈𝐄𝐖",fg="white",bg="BlAcK",command=d,font=("",30),bd=10,width=15).place(x=840,y=625)
    btn=Button(win,text="𝐎𝐓𝐇𝐄𝐑 𝐑𝐄𝐂𝐎𝐑𝐃𝐒",fg="white",bg="BlAcK",command=othrec,font=("",30),bd=10,width=15).place(x=840,y=750)
    btn=Button(win,text="𝐀𝐁𝐎𝐔𝐓",fg="white",bg="BlAcK",command=about,font=("",30),bd=10,width=15).place(x=840,y=500)
    def vid():
        pygame.mixer.init()
        file = 'video2audeo.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        video = VideoFileClip("video2.mp4").resize((1920,1020))
        video.preview()
        pygame.quit()
    btn10=Button(win,text="",image=k,command=vid,bd=5,bg="black").place(x=419,y=760)
    def india():
        india=Toplevel()
        india.minsize(height=1100,width=1900)
        pygame.mixer.init()
        
        file = 'm2.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
        im="background1.jpg"
        img = Image.open(im)
        img = img.resize((2000, 1500))
        img = ImageTk.PhotoImage(img)
        panel = Label(india, image=img,bd=0)
        panel.image = img
        panel.place(x=0,y=0)
        lbl=Label(india,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
        
        def img1():    
            im="india1.jpg"
            img = Image.open(im)
            img = img.resize((850, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(india, image=img,bd=2)
            panel.image = img
            panel.place(x=535,y=340)
            btn2=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=1430,y=488)
            btn2=Button(india,text="☆ 𝐁𝐄𝐒𝐓 𝐎𝐑𝐈𝐆𝐈𝐍𝐀𝐋 𝐒𝐎𝐍𝐆 ☆",font=("", 35),fg="black",bg="white",bd=0,width=22,height=0).place(x=660,y=240)
            btn4=Button(india,text="☆ 𝐀𝐑 𝐑𝐀𝐇𝐌𝐀𝐍 ☆",font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
            def info():
                info=Toplevel()
                info.minsize(height=1100,width=1900)
                pygame.mixer.init()
                file = 'sandeshe.mp3'
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                
                im="background1.jpg"
                img = Image.open(im)
                img = img.resize((2000, 1500))
                img = ImageTk.PhotoImage(img)
                panel = Label(info, image=img,bd=0)
                panel.image = img
                panel.place(x=0,y=0)
                lbl=Label(info,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                lbl1=Label(info,justify=LEFT,text='''𝐀𝐖𝐀𝐑𝐃 : 𝐁𝐄𝐒𝐓 𝐎𝐑𝐈𝐆𝐈𝐍𝐀𝐋 𝐒𝐎𝐍𝐆\n𝐍𝐀𝐌𝐄 : 𝐀𝐑 𝐑𝐀𝐇𝐌𝐀𝐍\n𝐀𝐖𝐀𝐑𝐃 𝐘𝐄𝐀𝐑  : 𝟐𝟎𝟎𝟗\n𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄 :-𝐉𝐀𝐈 𝐇𝐎\n𝐃𝐎𝐁   : 𝟔 𝐉𝐀𝐍,𝟏𝟗𝟔𝟕\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟓'𝟓"''',fg="black",bg="cyan",bd=50,font=("####", 55)).place(x=490,y=250)
                btn2=Button(info,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=info.destroy,width=3).place(x=1735-60,y=488)
                btn1=Button(info,text="《",font=("", 35),fg="white",bg="black",bd=10,command=info.destroy,width=3).place(x=60+80,y=488)
            def vid():
                pygame.mixer.init()
                file = 'jaiho.mp3'
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                clip = VideoFileClip("jaiho_muted.mp4").resize((1920,1020))
                clip.preview()
                pygame.quit()

            tmr=Button(india,text="",image=n,command=info,bd=5,bg="black").place(x=1395,y=740)
            tmr1=Button(india,text="",image=h ,command=vid,bd=3,bg="black").place(x=1395,y=820)
        def img2():
            im="india2.jpg"
            img = Image.open(im)
            img = img.resize((850, 550))
            img = ImageTk.PhotoImage(img)
            panel = Label(india, image=img,bd=2)
            panel.image = img
            panel.place(x=535,y=340)
            btn1=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img3,width=3).place(x=1430,y=488)
            btn2=Button(india,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img1,width=3).place(x=400,y=488)
            btn3=Button(india,text="☆ 𝐁𝐄𝐒𝐓 𝐒𝐎𝐔𝐍𝐃 𝐌𝐈𝐗𝐈𝐍𝐆 ☆",font=("", 35),fg="black",bg="white",bd=0,width=22,height=0).place(x=660,y=240)
            btn4=Button(india,text="☆ 𝐑𝐄𝐒𝐔𝐋 𝐏𝐎𝐎𝐊𝐔𝐓𝐓𝐘 ☆",font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
            def info1():
                info1=Toplevel()
                info1.minsize(height=1100,width=1900)
                pygame.mixer.init()
                file = 'sandeshe.mp3'
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                
                im="background1.jpg"
                img = Image.open(im)
                img = img.resize((2000, 1500))
                img = ImageTk.PhotoImage(img)
                panel = Label(info1, image=img,bd=0)
                panel.image = img
                panel.place(x=0,y=0)
                btn2=Button(info1,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=info1.destroy,width=3).place(x=1735-60,y=488)
                btn1=Button(info1,text="《",font=("", 35),fg="white",bg="black",bd=10,command=info1.destroy,width=3).place(x=60+80,y=488)
                lbl=Label(info1,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                lbl1=Label(info1,justify=LEFT,text=''' 𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐒𝐎𝐔𝐍𝐃 𝐌𝐈𝐗𝐈𝐍𝐆 \n𝐍𝐀𝐌𝐄 : 𝐑𝐄𝐒𝐔𝐋 𝐏𝐎𝐎𝐊𝐔𝐓𝐓𝐘\n𝐒𝐏𝐎𝐔𝐒𝐄 :- 𝐒𝐇𝐀𝐃𝐈𝐀 𝐏𝐎𝐎𝐊𝐔𝐓𝐓𝐘\n𝐀𝐖𝐀𝐑𝐃 𝐘𝐄𝐀𝐑 :- : 𝟐𝟎𝟎𝟗\n𝐃𝐎𝐁   : 𝟑𝟎 𝐌𝐀𝐘,𝟏𝟗𝟕𝟏\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟔'𝟏"''',fg="black",bd=50,bg="cyan",font=("####", 55)).place(x=490,y=250)
            def vid1():
                pygame.mixer.init()
                file = 'resul.mp3'
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                clip = VideoFileClip("resul_muted.mp4").resize((1920,1020))
                clip.preview()
                pygame.quit()

            tmr=Button(india,text="",image=n,command=info1,bd=5,bg="black").place(x=1395,y=740)
            tmr1=Button(india,text="",image=h ,command=vid1,bd=3,bg="black").place(x=1395,y=820)
        def img5():
                im="india5.jpg"
                img = Image.open(im)
                img = img.resize((850, 550))
                img = ImageTk.PhotoImage(img)
                panel = Label(india, image=img,bd=2)
                panel.image = img
                panel.place(x=535,y=340)
                btn1=Button(india,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img4,width=3).place(x=400,y=488)
                btn2=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,width=3).place(x=1430,y=488)
                btn3=Button(india,text="☆ 𝐇𝐎𝐍𝐎𝐑𝐀𝐑𝐘 𝐀𝐖𝐀𝐑𝐃 ☆",font=("", 35),fg="black",bg="white",bd=0,width=22,height=0).place(x=660,y=240)
                btn4=Button(india,text="☆ 𝐒𝐀𝐓𝐘𝐀𝐉𝐈𝐓 𝐑𝐀𝐘  ☆",font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
                def info2():
                        info2=Toplevel()
                        info2.minsize(height=1100,width=1900)
                        pygame.mixer.init()
                        file = 'sandeshe.mp3'
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        
                        im="background1.jpg"
                        img = Image.open(im)
                        img = img.resize((2000, 1500))
                        img = ImageTk.PhotoImage(img)
                        panel = Label(info2, image=img,bd=0)
                        panel.image = img
                        panel.place(x=0,y=0)
                        btn2=Button(info2,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=info2.destroy,width=3).place(x=1735-60,y=488)
                        btn1=Button(info2,text="《",font=("", 35),fg="white",bg="black",bd=10,command=info2.destroy,width=3).place(x=60+80,y=488)
                        lbl=Label(info2,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                        lbl1=Label(info2,justify=LEFT,text='''𝐀𝐖𝐀𝐑𝐃 : 𝐇𝐎𝐍𝐎𝐑𝐀𝐑𝐘 𝐀𝐖𝐀𝐑𝐃 \n𝐍𝐀𝐌𝐄 : 𝐒𝐀𝐓𝐘𝐀𝐉𝐈𝐓 𝐑𝐀𝐘\n𝐒𝐏𝐎𝐔𝐒𝐄 : 𝐁𝐈𝐉𝐎𝐘𝐀 𝐑𝐀𝐘\n𝐀𝐖𝐀𝐑𝐃 𝐘𝐄𝐀𝐑  : 𝟏𝟗𝟗𝟐\n𝐃𝐎𝐁   : 𝟐 𝐌𝐀𝐘,𝟏𝟗𝟐𝟏\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟔'𝟒"''',fg="black",bd=50,bg="cyan",font=("####", 55)).place(x=490,y=250)
                def vid2():
                    pygame.mixer.init()
                    file = 'satyajit.mp3'
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    clip = VideoFileClip("satyajit.mp4").resize((1920,1020))
                    clip.preview()
                    pygame.quit()
                tmr=Button(india,text="",image=n,command=info2,bd=5,bg="black").place(x=1395,y=740)
                tmr1=Button(india,text="",image=h ,command=vid2,bd=3,bg="black").place(x=1395,y=820)
        def img4():
                im="india4.jpeg"
                img = Image.open(im)
                img = img.resize((850, 550))
                img = ImageTk.PhotoImage(img)
                panel = Label(india, image=img,bd=2)
                panel.image = img
                panel.place(x=535,y=340)
                btn1=Button(india,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img3,width=3).place(x=400,y=488)
                btn2=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img5,width=3).place(x=1430,y=488)
                btn3=Button(india,text="☆ 𝐁𝐄𝐒𝐓 𝐎𝐑𝐈𝐆𝐈𝐍𝐀𝐋 𝐒𝐎𝐍𝐆 ☆",font=("", 35),fg="black",bg="white",bd=0,width=22,height=0).place(x=660,y=240)
                btn4=Button(india,text="☆ 𝐆𝐔𝐋𝐙𝐀𝐑  ☆",font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
                def info3():
                    info3=Toplevel()
                    info3.minsize(height=1100,width=1900)
                    pygame.mixer.init()
                    file = 'sandeshe.mp3'
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    im="background1.jpg"
                    img = Image.open(im)
                    img = img.resize((2000, 1500))
                    img = ImageTk.PhotoImage(img)
                    panel = Label(info3, image=img,bd=0)
                    panel.image = img
                    panel.place(x=0,y=0)
                    btn2=Button(info3,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=info3.destroy,width=3).place(x=1735-60,y=488)
                    btn1=Button(info3,text="《",font=("", 35),fg="white",bg="black",bd=10,command=info3.destroy,width=3).place(x=60+80,y=488)
                    
                    lbl=Label(info3,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                    lbl1=Label(info3,justify=LEFT,text='''𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐎𝐑𝐈𝐆𝐈𝐍𝐀𝐋 𝐒𝐎𝐍𝐆 \n𝐍𝐀𝐌𝐄 : 𝐆𝐔𝐋𝐙𝐀𝐑\n𝐒𝐏𝐎𝐔𝐒𝐄 : 𝐑𝐀𝐊𝐇𝐄𝐄 𝐆𝐔𝐋𝐙𝐀𝐑\n𝐀𝐖𝐀𝐑𝐃 𝐘𝐄𝐀𝐑 : 𝟐𝟎𝟎𝟗\n𝐃𝐎𝐁   : 𝟏𝟖 𝐀𝐔𝐆,𝟏𝟗𝟑𝟒\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟓'𝟕"''',fg="black",bd=50,bg="cyan",font=("####", 55)).place(x=490,y=250)
                def vid3():

                    pygame.mixer.init()
                    file = "Gulzar.mp3"
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    clip = VideoFileClip("Gulzar.mp4").resize((1920,1020))

                    clip.preview()
                    pygame.quit()
                tmr=Button(india,text="",image=n,command=info3,bd=5,bg="black").place(x=1395,y=740)
                tmr1=Button(india,text="",image=h ,command=vid3,bd=3,bg="black").place(x=1395,y=820)
        def img3():
                im="india3.jpg"
                img = Image.open(im)
                img = img.resize((850, 550))
                img = ImageTk.PhotoImage(img)
                panel = Label(india, image=img,bd=2)
                panel.image = img
                panel.place(x=535,y=340)
                btn1=Button(india,text="《",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=400,y=488)
                btn2=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img4,width=3).place(x=1430,y=488)
                btn3=Button(india,text="☆ 𝐁𝐄𝐒𝐓 𝐂𝐎𝐒𝐓𝐔𝐌𝐄 𝐃𝐄𝐒𝐈𝐆𝐍 ☆",font=("", 35),fg="black",bg="white", bd=0,width=22,height=0).place(x=660,y=240)
                btn4=Button(india,text="☆ 𝐁𝐇𝐀𝐍𝐔 𝐀𝐓𝐇𝐀𝐈𝐘𝐀 ☆",font=("", 35),fg="black",bg="white", bd=0,width=20,height=0).place(x=700,y=905)
                def info4():
                    info4=Toplevel()
                    info4.minsize(height=1100,width=1900)
                    pygame.mixer.init()
                    file = 'sandeshe.mp3'
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    
                    im="background1.jpg"
                    img = Image.open(im)
                    img = img.resize((2000, 1500))
                    img = ImageTk.PhotoImage(img)
                    panel = Label(info4, image=img,bd=0)
                    panel.image = img
                    panel.place(x=0,y=0)
                    btn2=Button(info4,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=info4.destroy,width=3).place(x=1735-60,y=488)
                    btn1=Button(infotext="《",font=("", 35),fg="white",bg="black",bd=10,command=info4.destroy,width=3).place(x=60+80,y=488)
                    lbl=Label(info4,text=" ░▒▓█ 𝐈𝐍𝐃𝐈𝐀𝐍 𝐎𝐒𝐂𝐀𝐑 𝐀𝐖𝐀𝐑𝐃𝐒 █▓▒░",fg="white",bg="black",font=("####", 70)).place(x=210,y=75)
                    lbl1=Label(info4,justify=LEFT,text='''𝐀𝐖𝐀𝐑𝐃 :  𝐁𝐄𝐒𝐓 𝐂𝐎𝐒𝐓𝐔𝐌𝐄 𝐃𝐄𝐒𝐈𝐆𝐍 \n𝐍𝐀𝐌𝐄 :  𝐁𝐇𝐀𝐍𝐔 𝐀𝐓𝐇𝐀𝐈𝐘𝐀 \n𝐒𝐏𝐎𝐔𝐒𝐄 : 𝐒𝐀𝐓𝐘𝐄𝐍𝐃𝐑𝐀  𝐀𝐓𝐇𝐀𝐈𝐘𝐀\n𝐀𝐖𝐀𝐑𝐃 𝐘𝐄𝐀𝐑 : 𝟏𝟗𝟖𝟐\n𝐃𝐎𝐁   : 𝟏𝟖 𝐀𝐔𝐆,𝟏𝟗𝟑𝟒\n𝐌𝐀𝐑𝐑𝐈𝐄𝐃  : 𝐘𝐄𝐒\n𝐇𝐄𝐈𝐆𝐇𝐓  :𝟓'𝟕"''',fg="black",bd=50,bg="cyan",font=("####", 55)).place(x=490,y=250)
                    tmr1=Button(india,text="",image=n ,command=info4,bd=3,bg="black").place(x=1395,y=740)
                def vid4():
                    pygame.mixer.init()
                    file = 'bhanu1.mp3'
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    clip = VideoFileClip("bhanu1.mp4").resize((1920,1020))
                    clip.preview()
                    pygame.quit()

                tmr1=Button(india,text="",image=h,command=vid4 ,bd=3,bg="black").place(x=1395,y=820)
        btn1=Button(india,text="《",font=("", 35),fg="white",bg="black",bd=10,width=3).place(x=400,y=488)
        btn2=Button(india,text=" 》",font=("", 35),fg="white",bg="black",bd=10,command=img2,width=3).place(x=1430,y=488)
        
        def music():
            pygame.mixer.init()
            file = 'music3.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            india.destroy()
        btn3=Button(india,text="𝐁𝐀𝐂𝐊",font=("", 35),fg="white",bg="black", bd=10,command=music,width=10).place(x=70,y=880)
        img1()
    tmr=Button(win,text="",image=kimage,command=india,bd=5,bg="black").place(x=190,y=760)
#_________________________________________________image paths__________________________________
li=ImageTk.PhotoImage(Image.open("LIKE1.png"))
o1=ImageTk.PhotoImage(Image.open("LIKE2.png"))  
o=ImageTk.PhotoImage(Image.open("LIKE4.png"))    
L=ImageTk.PhotoImage(Image.open("LIKE3.png"))
n=ImageTk.PhotoImage(Image.open("icon1.ico"))
h=ImageTk.PhotoImage(Image.open("icon2.png"))
k=ImageTk.PhotoImage(Image.open("icon3.png"))
kimage=ImageTk.PhotoImage(Image.open("india.png"))
new()
PR.mainloop()
#https://videocandy.com/result/6918d0b3169c8080.html
