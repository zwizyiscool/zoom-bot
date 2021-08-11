import tkinter
from tkinter import *
import pyautogui
import subprocess 
import time
import schedule
from tkinter import ttk


def meeting_id_get():
    meeting_id_get_text = meeting_id_text_123.get()
    print("Meeting id: " ,meeting_id_get_text)
    return None

def password_get():
    password_text = password_123.get()
    print("Password:  " ,password_text)
    return None

def time_get():
    time_123_text = time_123.get()
    print("Time Set To: " ,time_123_text)
    return None

def days_get():
    days_text = days_123.get()
    print("Day:  ", days_text)
    return None


def mic():
    micmute= pyautogui.locateOnScreen('./assets/unmute.png')
    micunmute = pyautogui.locateOnScreen('./assets/muted.png')

    if micunmute != None:
        pyautogui.click(micunmute)
        print("Mic unmuted Succesful!")

    elif micmute != None:
        pyautogui.click(micmute)
        print('Mic muted successfully!')

    else:
        print("Mic Failed!")


    
    

def cam():
    camoff = pyautogui.locateOnScreen('./assets/camon.png')
    camon = pyautogui.locateOnScreen('./assets/camoff.png')

    if camon != None:
        pyautogui.click(camon)
        print("Cam off Succesful!")
    elif camoff != None:
        
        pyautogui.click(camoff)
        print("Cam on Succesful!")
    else:
        print("Cam  Failed!")

    
    



def join():


    print("Loop 1 started")
    subprocess.call("C:\\Users\\ASD\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    print("Zoom run succesful!")
    while True:
        join1 = pyautogui.locateOnScreen('./assets/join1.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Join 1 Succesful!")
            break
        else:
            print("Join 1 Failed!")
            time.sleep(2)

    while True:
        print("Loop 2 started")
        meeting_id = pyautogui.locateOnScreen('./assets/meeting_id.png')
        if meeting_id != None:
            print("meeting id box active!")
            textgui_meetingid = meeting_id_text_123.get()
            pyautogui.typewrite(textgui_meetingid)
            break
        else:
            print("Meeting id process Failed!")
            time.sleep(2)

    while True:
        print("Join loop started!")
        join2 =  pyautogui.locateOnScreen('./assets/join2.png')
        if join2 != None:
            pyautogui.click(join2)
            print("Join 2 Succesful!")
            break
        else:
            print("Join 2 Failed!")
            time.sleep(2)


    while True:
        print("Loop 3 started")
        passcode =  pyautogui.locateOnScreen('./assets/password.png')
        if passcode != None:
            pyautogui.click(passcode)
            print("password box active!")
            textgui_password = password_123.get()
            pyautogui.typewrite(textgui_password)
            join3 = pyautogui.locateOnScreen('./assets/join3.png')
            pyautogui.click(join3)
            break
        else:
            print("Password process Failed!")
            time.sleep(2)

    while True:
        join_audio =  pyautogui.locateOnScreen('./assets/join_audio.png')
        if join_audio != None:
            pyautogui.click(join_audio)
            print("Joined Audio!")
            break
        else:
            print("Joining Audio Failed!")
            time.sleep(2)

    while True:
        days_text = days_123.get()
        time_text = time_123.get()

        if days_text == "Everyday":
            print("Scheduled to Everyday!")
            schedule.every().day.at(time_text).do(join)

        elif days_text == "Monday":
            schedule.every().monday.at(time_text).do(join)

        elif days_text == "Tuesday":
            schedule.every().tuesday.at(time_text).do(join)

        elif days_text == "Wednesday":
            schedule.every().wednesday.at(time_text).do(join)

        elif days_text == "Thursday":
            schedule.every().thursday.at(time_text).do(join)

        elif days_text == "Friday":
            schedule.every().friday.at(time_text).do(join)

        elif days_text == "Saturday":
            schedule.every().saturday.at(time_text).do(join)

        elif days_text == "Sunday":
            schedule.every().sunday.at(time_text).do(join)

        else:
            print("Invalid Input")




print("GUI Started!")



window = tkinter.Tk()
window.title("Zoomer V1.0 BETA")
window.geometry("500x500")
window.minsize(400, 400)
window.maxsize(600, 600)
window.config(bg="#FFC98B")

intro_label = tkinter.Label(window, text="Hi this is Zoomer V1.0 BETA!", font="Arial")
intro_label.pack(anchor=tkinter.CENTER)

meeting_id_label = tkinter.Label(window, text="Meeting Id:", font="Arial", )
meeting_id_label.pack()

meeting_id_text_123 = tkinter.Entry(window, width=50, font="Arial", bg="black", fg="white")
meeting_id_text_123.pack(anchor=tkinter.CENTER,)

bt_meetingid = Button(window, text="Meeting Id ", width=40, bg="black", fg="white", command=meeting_id_get)
bt_meetingid.pack(anchor=tkinter.CENTER, expand=True )

meeting_id_label = tkinter.Label(window, text="Password:", font="Arial", )
meeting_id_label.pack()

password_123 = tkinter.Entry(window, width=50, font="Arial", bg="black", fg="white" )
password_123.pack(anchor=tkinter.CENTER, )

bt_password = Button(window, text="Password ", width=40, bg="black", fg="white", command=password_get)
bt_password.pack(anchor=tkinter.CENTER, expand=True)


bt_mic = Button(window, text="Mic On/Off", width=40, bg="black", fg="white", command=mic)
bt_mic.pack(anchor=tkinter.CENTER, expand=True)

bt_cam = Button(window, text="Cam On/Off", width=40, bg="black", fg="white", command=cam)
bt_cam.pack(anchor=tkinter.CENTER, expand=True)

bt_coming = Button(window, text="Coming Soon", width=40, bg="black", fg="white")
bt_coming.pack(anchor=tkinter.CENTER, expand=True)

time_label = tkinter.Label(window, text="Time:", font="Arial", )
time_label.pack()

time_123 = tkinter.Entry(window, width=50, font="Arial", bg="black", fg="white" )
time_123.pack(anchor=tkinter.CENTER, )

bt_time = Button(window, text="Time", width=40, bg="black", fg="white", command=time_get)
bt_time.pack(anchor=tkinter.CENTER, expand=True)



days_label = tkinter.Label(window, text="Day:", font="Arial", )
days_label.pack()

days_123 = tkinter.Entry(window, width=50, font="Arial", bg="black", fg="white" )
days_123.pack(anchor=tkinter.CENTER)

bt_days = Button(window, text="Days", width=40, bg="black", fg="white", command=days_get)
bt_days.pack(anchor=tkinter.CENTER, expand=True)

bt_join = Button(window, text="Join Meeting", width=40, bg="black", fg="white", command=join)
bt_join.pack(anchor=tkinter.CENTER, expand=True)

window.mainloop()



