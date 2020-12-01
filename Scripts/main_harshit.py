import the_voice
import send_mail
import read_mail
import send_whatsapp
import obj_recog
import weather_report


def start(cmd):

    if 'send mail' in cmd or ("send" in cmd and "mail" in cmd):
        the_voice.say_and_print("Preparing to send email...")
        send_mail.start()
        return 1

    elif 'read inbox' in cmd or ("read" in cmd and "inbox" in cmd):
        the_voice.say_and_print("Reading Email...")
        read_mail.start()
        return 1

    elif 'send whatsapp' in cmd or ("send" in cmd and "whatsapp" in cmd):
        the_voice.say_and_print("Preparing to send whatsapp...")
        send_whatsapp.start()
        return 1
    elif 'recognise object' in cmd or (("recognise" in cmd or "recognize" in cmd) and "object" in cmd):
        the_voice.say_and_print("This feature is currently in beta mode!")
        # the_voice.say_and_print("Object recognition activating...")
        # obj_recog.start()
        return 1
    elif ("tell" in cmd and "weather" in cmd) or ("what" in cmd and "weather" in cmd) or ("how" in cmd and "weather" in cmd):
        the_voice.say_and_print("Weather report:")
        weather_report.weather()
        return 1

    return 0
