import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    else:
        #openAI
        pass




if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # recognize speech using Sphinx
        print("Recognizing.....")
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if ("jervis" in word.lower() or "jarvis" in word.lower() or "jervic" in word.lower() or "jarvic" in word.lower()):
                speak("Yaa")
               # listen for command
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
            print("Error; {0}".format(e))



