import sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your voice assistant. Please tell me how may I help you")     

def sendMesssage(value):
    base_url = 'https://api.telegram.org/bot5869096972:AAEM3kZSz5wYKt7g5E0xop4spVIRhMb3hAE/sendMessage?chat_id=-885477547&text="{}"'.format(value)
    webbrowser.open(base_url)


def randomGenerator():
    randomNum = random.randint(0,4)
    return str(randomNum)



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


        
def performCommand(query):
        if 'search on wikipedia' in query:
            speak("What should I search on Wikipedia?")
            searchWord = takeCommand()
            results = wikipedia.summary(searchWord, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'send message' in query:
            try:
                speak("What should I send?")
                message = takeCommand()   
                sendMesssage(message)
                speak("message has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this message")
            

        elif 'play music' in query:             
            randomNum = randomGenerator()          
            music_dir = "C:\\Users\\abdu\\Desktop\\Dsp-Project\\Musics\\mus" + randomNum + ".mp3"     
            os.startfile(music_dir)    
        elif 'play video' in query:
            randomNum = randomGenerator()          
            video_dir = "C:\\Users\\abdu\\Desktop\\Dsp-Project\\videos\\vid" + randomNum + ".mkv"   
            os.startfile(video_dir)
        
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\abdu\\Desktop\\Visual Studio Code.lnk" 
            os.startfile(codePath)
        elif 'open vlc' in query:
            codePath = "C:\\Users\\Public\\Desktop\\VLC media player.lnk"
            os.startfile(codePath)      
        elif 'open camera' in query:
            codePath = "C:\\Users\\abdu\\Desktop\\Camera.lnk"   
            os.startfile(codePath)
        elif 'open telegram' in query:
            codePath = "C:\\Users\\Public\\Desktop\\Telegram.lnk"
            os.startfile(codePath) 
        elif 'open matlab' in query:    
            codePath = "C:\\Users\\Public\\Desktop\\MATLAB R2022b.lnk"
            os.startfile(codePath) 

        elif 'exit' in query:
            speak('Thank you sir')
            sys.exit()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        performCommand(query)
