import time                                                 #pip install python-time
import datetime                                             #pip install DateTime
from Speak import Say, Just_Say
import wikipedia                                            #pip install wikipedia
import webbrowser                                           #pip install pycopy-webbrowser
import pywhatkit                                            #pip install pywhatkit
import wikipedia as googleScrap                             #pip install scrap-engine
import qrcode                                               #pip install qrcode
import pyautogui                                            #pip install PyAutoGUI
import speedtest                                            #pip install speedtest-cli
import os                                                   #pip install os-sys
from pdf2docx import parse                                  #pip install pdf2docx   #pip install parse
import PyPDF2                                               #pip install PyPDF2
from pdf2image import convert_from_path                     #pip3 install pdf2image #choco install poppler
from docx2pdf import convert                                #pip install docx2pdf
import urllib.request                                       #pip install urllib3
import requests                                             #pip install requests
from pytube import YouTube                                  #pip install pytube
from moviepy.video.io.VideoFileClip import VideoFileClip    #pip install moviepy
import docx                                                 #pip install docx
import pdfreader                                            #pip install pdfreader
import zipfile                                              #pip install zip-files
import cv2                                                  #pip install opencv-python imutils
import imutils                                              #pip install imutils
import threading
import winsound

def Time():
    hours = datetime.datetime.now().strftime("%H")
    minutes = datetime.datetime.now().strftime(":%M %p")
    hours = int(hours)
    if hours > 12:
        hours = hours-12
        time = str(hours) + minutes
        Say(time)
        
    else:
        time = str(hours) + minutes
        Say(time)
    
def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    date = (str(int(month))+"/"+str(int(date))+"/"+str(int(year)))
    Say(date)
    
def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)
    
def task():
        Say("I am an Artificial Intelligent. I have no imotions like humans! But I can perform a several works, see the below:")
        print("\n I can tell the present Date, Time and Day,\n  I can take screenshot,\n I can determine the internet speed,\n I can clear the all history from chrome browser,\n I can close applications,\n I can search data from wikipedia and internet,\n I can generate QR code,\n I can convert the file like, pdf to docx, docx to pdf, pdf to jpeg, docx to jpeg, pdf to txt and so on,\n I can download video from youtube,\n I can extract audio from a video,\n I can read any type of file,\n I can unlock a zip file and create a zip file also, \n I can detect any kind of motion")
    
#All non input functions are here___________________________________________________________________________________________________________________   
    
def NonInputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()

    elif "task" in query:
        Say("I am an Artificial Intelligent. I have no imotions like humans! But I can perform a several works, see below:") 
        print(" I can tell the present Date, Time and Day,\n I can take screenshot,\n I can determine the internet speed,\n I can clear the all history from chrome browser,\n I can close applications,\n I can search data from wikipedia and internet,\n I can generate QR code,\n I can convert the file like, pdf to docx, docx to pdf, pdf to jpeg, docx to jpeg, pdf to txt and so on,\n I can download video from youtube,\n I can extract audio from a video,\n I can read any type of file,\n I can unlock a zip file and create a zip file also")
        
    elif "screenshot" in query:
        im = pyautogui.screenshot()
        Say('Done')
        Just_Say("give a name")
        ss = input("give a name: ")
        im.save(ss + ".png")
        Say("successfully save") 

    elif "internet_speed" in query:
        print("Please wait, it may take some time....")
        Just_Say("Please wait, it may take some time")
        wifi = speedtest.Speedtest()
        upload_net = wifi.upload()/1048576
        format_upload_net = "{:.2f}".format(upload_net)
        download_net = wifi.download()/1048576
        format_download_net= "{:.2f}".format(download_net)
        Say("upload speed is: " + str(format_upload_net) + " Mbps")
        Say("download speed is: " + str(format_download_net) + " Mbps")
        
    elif 'clear_browser_history' in query:
            Say("take a second")
            pyautogui.press('super')
            pyautogui.write("chrome")
            pyautogui.press('enter')
            pyautogui.sleep(5)
            pyautogui.hotkey('tab', 'enter')
            pyautogui.sleep(1)
            pyautogui.hotkey('ctrl', 'h')
            pyautogui.sleep(1)
            pyautogui.hotkey('tab', 'ctrl', 'a')
            pyautogui.sleep(1)
            pyautogui.press('delete')
            pyautogui.sleep(1)
            pyautogui.hotkey('enter', 'alt', 'f4')
            Say("Removed all history")
            
    # elif 'close' in query:
        # pyautogui.hotkey('alt','f4')
        # Say("close")