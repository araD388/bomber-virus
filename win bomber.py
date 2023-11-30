import threading
import  pyautogui as pg 
import random 
import os 


count=1
def vsr():
    for f in range (1):
        try:
            a=random.randint(0,1080)
            b=random.randint(0,1920)

            os.system('@echo off')
            os.system('start calc')
            os.system('start explorer')
            os.system('start notepad')
            os.system('start control')
            os.system('start cmd')
            os.system('start write')
            os.system('start mspaint')

            pg.click(a,b,duration=0.3)

            pg.hotkey('win','i')
            pg.hotkey('win','a')
            pg.hotkey('win','s')
            pg.hotkey('win','c')
            pg.hotkey('win','f')
            pg.hotkey('win','a')
            pg.hotkey('win','d')

            pg.alert(text='ok?',title='hey',button='ok')
        except:
            os.system('@echo off')
            os.system('start calc')
            os.system('start explorer')
            os.system('start notepad')
            os.system('start control')
            os.system('start cmd')
            os.system('start write')
            os.system('start mspaint')

for i in range (count):
    st=threading.Thread(target=vsr)
    st.start()

