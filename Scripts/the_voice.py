import pyttsx3
import speech_recognition as sr

# for listening
r = sr.Recognizer()

# for speaking
engine = pyttsx3.init()
rate = engine.getProperty('rate')  # getting details of current speaking rate
# print(rate)  # printing current voice rate
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices)
vid = 0
vrate = 180

engine.setProperty('rate', vrate)
engine.setProperty('voice', voices[vid].id)  # changing index, changes voices. 0 for male and 1 for female.


def set_voice_rate(x):
    if 50 <= x <= 400:
        engine.setProperty('rate', x)


def set_voice(x):
    if 0 <= x <= 5:
        engine.setProperty('voice', voices[x].id)


def say(a):
    if a is None:
        return
    engine.say(a)
    engine.runAndWait()


def say_and_print(a):
    if a is None:
        return
    print(a)
    engine.say(a)
    engine.runAndWait()


def listening():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(">>>", text)
            return text
        except Exception as e:
            print("Sorry, I didn't get you!")
            print(e)
            return


def wake_listen(nm="Assistant"):
    with sr.Microphone() as source:
        print("Say", nm, "to activate assistant...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except Exception as e:
            return
