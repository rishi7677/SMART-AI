#All imported files can be install using the pip command 
import pyttsx3  
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui as pgui
import psutil
import pyjokes as pj


engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #I -> In 12 hrs clock  #H -> for 24 hrs clock
    speak("The current time is")
    speak(Time)

def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if(hour >= 5 and hour <= 12):
        speak("Good Morning sir")
    elif(hour >12 and hour<=17):
        speak("Good AfterNoon sir")
    elif(hour >17 and hour<=24):
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("Rishi, at your service ..Tell me how can I help you .. Thank You!!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listining...") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Please speak it again .... Audio was not clear")
        return "None"

    return query

def takeScreenshot():
	ss=pgui.screenshot()
	ss.save("C:\\Users\\acer\\Desktop\\Project\\AI_Jarvis\\ss.png")

def jokes():
    speak(pj.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('rishi7677238823@gmail.com','***********')
    server.sendmail('rishi7677238823@gmail.com',to,content)
    server.close()

#speak("This is JARVIS \n Hello  Rishi!")
#wishme()
#takeCommand()
if __name__ == "__main__":
    wishme()
    while True:

        query=takeCommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif "offline" in query:
            speak("Rishi sighning off!!")
            quit()

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'play song' in query:
            musicdir = 'C:\\Users\\Hp\\Music'
            song=os.listdir(musicdir)
            os.startfile(os.path.join(musicdir,song[0]))

        elif 'remember that' in query:
            speak("What should I remember")
            data = takeCommand()
            speak("You said me to remember"+ data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("You said to remember that" + remember.raed())

        elif 'search in chrome' in query:
            speak("What should I search")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'screenshot' in query:
            takeScreenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'send email' in query:
            try:
                speak("What are the contents?")
                content = takeCommand()
                print(content)
                to = 'rishiranjan7677@gmail.com'
                sendEmail(to,content)
                speak("Email sent successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
    

