import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def talk(text):
    engine.say(text)
    # engine.say('What can I do for you')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command





def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Mr. Manav Arora he current time is ' + time)
    elif 'define' in command:
        person = command.replace('define', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk('Mr. Manav Arora this person is ' + info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk('Mr. Manav Arora I hope you find this funny. ' + joke)
    else:
        talk('Please forgive me Mr.Manav Arora. Please say the command again.')


while True:
    run_alexa()
