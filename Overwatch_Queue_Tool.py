import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
import win32gui
import pytesseract
import smtplib
import tkinter as tk 
import re
import threading as tr

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

################## GLOBAL VARIABLES ###########################
global running_thread
global running
running = False
################## PREREQUISUTES ###########################
# Mention the installed location of Tesseract-OCR in your system 
os.environ["TESSDATA_PREFIX"] = "tesseract/"
pytesseract.pytesseract.tesseract_cmd = 'tesseract/tesseract.exe'
################## Check if email is set ###################
default_email_set = False
if os.path.exists('default.dat'):
    with open('default.dat', 'r') as fp:
        line = fp.readline()
        receiver_address = line
        default_email_set = True
else:
    receiver_address = "Enter Email Address here"
   
#################### COLOUR PALLETE ##################
primary = "#101820"

##################### GUI ######################
window = tk.Tk()
window.title("Overwatch Queue Tool")
window.iconbitmap('assets/icon.ico')
################ FRAMES ##########################
frame1 = tk.Frame(master=window, width=200, bg=primary, padx=5, pady=5)
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, width=100,  bg=primary, padx=5, pady=5)
frame2.pack(fill=tk.BOTH, expand=True)

frame3 = tk.Frame(master=window, width=100,  bg=primary, padx=5, pady=5)
frame3.pack(fill=tk.BOTH, expand=True)

frame4 = tk.Frame(master=window, width=50, bg=primary, padx=5, pady=5)
frame4.pack(fill=tk.BOTH, expand=True)

#################### WIDGETS ####################
lbl_title = tk.Label(
    master=frame1,
    text="Overwatch Queue Tool",  
    fg="orange",
    bg=primary,
    width=20,
    height=5
    )
lbl_title.pack() 

ent_email = tk.Entry(
    master=frame2,
    fg="yellow", 
    bg="blue", 
    width=30,
    )
ent_email.pack(side=tk.LEFT)
ent_email.insert(index=0, string=receiver_address)

btn_email_set = tk.Button(
    master=frame2,
    text="Set",
    width=5,
    fg="blue",
    bg="white",
    padx=5
    )
btn_email_set.pack(side=tk.RIGHT)

lbl_email_alert = tk.Label(
    master=frame3,
    bg=primary,
    width=20
    )
lbl_email_alert.pack(side=tk.BOTTOM)

btn_start = tk.Button(
    master=frame4,
    text="Start",
    width=25,
    height=5,
    )
btn_start.pack()

lbl_primary_alert = tk.Label(
    master=frame4,
    fg="red",
    bg=primary,
    width=25
    )
lbl_primary_alert.pack(side=tk.BOTTOM)

lbl_secondary_alert = tk.Label(
    master=frame4,
    fg="green",
    bg=primary,
    width=25
    )
lbl_secondary_alert.pack(side=tk.BOTTOM)



################# Middleware ###############
def validate_email(email):
    if re.search(
        """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
        email):
        lbl_email_alert['text'] = "Email is Valid"
        lbl_email_alert['fg'] = "green"
        btn_start['text'] = "Start"
        btn_start['fg'] = "blue"
        btn_start['bg'] = "white"
        # save the email address for future use
        with open('default.dat', 'w+') as fp:
            fp.write(email)
    else:  
        lbl_email_alert['text'] = "Set a valid email address"
        lbl_email_alert['fg'] = "red"
        btn_start['text'] = "Start"
        btn_start['fg'] = "white"
        btn_start['bg'] = "red"


def send_notification():
    #The mail addresses and password
    sender_address = 'XXXXXXXXXXXXXX@XXXXXXXX.XXX'
    sender_pass = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    #The subject line
    message['Subject'] = 'Overwatch Queue Tool'   
    #The body and the attachments for the mail
    mail_content = "Your Overwatch Queue Has Ended"
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    lbl_secondary_alert['text'] = "Email has been sent to you"


def start_search():
    lbl_secondary_alert['text'] = ""
    # Detect the window with Overwatch
    game_hwnd = win32gui.FindWindow(None, 'Overwatch')
    if not game_hwnd:
        lbl_primary_alert['text'] = "Overwatch application not found"
    else:
        lbl_primary_alert['text'] = ""
        btn_start['text'] = "Waiting for search..."
        btn_start['fg'] = "blue"
        btn_start['bg'] = "white"
        
        win32gui.SetForegroundWindow(game_hwnd)
        time.sleep(2)
        position = win32gui.GetWindowRect(game_hwnd)
        min_x, min_y, max_x, max_y = position
        width = max_x - min_x
        height = max_y - min_y
        center_x = (min_x + max_x) // 2 
        offset = round(0.1 * width)  
        min_x = center_x - offset
        max_x = center_x + offset
        max_y = min_y + round(height*0.2)
        
        search_started = False
        active = True
        while active:
            if(win32gui.GetForegroundWindow() == game_hwnd):
                # Take screenshot
                screenshot = ImageGrab.grab((min_x, min_y, max_x, max_y))
                screenshot = np.array(screenshot)
                
                # Convert the image to gray scale 
                gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) 
                  
                # Performing OTSU threshold 
                ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
                  
                # Specify structure shape and kernel size.  
                # Kernel size increases or decreases the area  
                # of the rectangle to be detected. 
                # A smaller value like (10, 10) will detect  
                # each word instead of a sentence. 
                rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10)) 
                  
                # Appplying dilation on the threshold image 
                dilation = cv2.dilate(thresh, rect_kernel, iterations = 1) 
                
                # Finding contours 
                contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_NONE) 
                text_found = False
                for cnt in contours: 
                    x, y, w, h = cv2.boundingRect(cnt) 
                      
                    # Cropping the text block for giving input to OCR 
                    cropped = screenshot[y:y + h, x:x + w] 
                      
                    # Apply OCR on the cropped image 
                    text = pytesseract.image_to_string(cropped) 
                    text_found = len(text) > 1
                    if not search_started and "search" in text.lower():
                        btn_start['text'] = "Searching for a game"
                        btn_start['fg'] = "white"
                        btn_start['bg'] = "green"
                        search_started = True
                    if "search" in text.lower():
                        break
                        
                if search_started and not text_found:
                    btn_start['text'] = "Queue has ended!"
                    btn_start['fg'] = "red"
                    btn_start['bg'] = "white"
                    send_notification()
                    active = False
                
################# Callbacks ################
def set_email(event):
    email = ent_email.get()
    validate_email(email)

def start(event):
        global running, running_thread
        if not running:
            running_thread = tr.Thread(target=start_search, daemon = True)
            running_thread.start()
            running = True
        if running and not running_thread.is_alive():
            btn_start['text'] = "Start"
            btn_start['fg'] = "blue"
            btn_start['bg'] = "white"
            running = False
################# Event Handlers ############
btn_email_set.bind("<Button-1>", set_email)
btn_start.bind("<Button-1>", start)


################ MAIN #############

if __name__ == '__main__':
    validate_email(receiver_address)
    window.mainloop()
        
