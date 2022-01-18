import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("hey, i am siri. How can i help you")
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('siri', '')
            print(command)
    except:
        pass
    return command

def run_siri():
    command = take_command()
    if 'play song' in command:
        song = command.replace('play song', '')
        talk('playing song')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('time')
        talk('Currenet time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        exit()
    else:
        talk("sorry, i did not get that")

while True:
    run_siri()
