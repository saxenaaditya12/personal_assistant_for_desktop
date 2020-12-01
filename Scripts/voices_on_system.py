import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    print(voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World")
    engine.runAndWait()

