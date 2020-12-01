import the_voice
import random

greet_text = ["What are my orders?",
              "Fully functional!",
              "At your service!",
              "Hey, what can I do for you?"]
failure_text = ["Sorry didn't get you!",
                "Sorry, can't do that yet!",
                "I don't know what to do!",
                "Naah! not one of my skills",
                "Sorry, but my powers are limited..."]
goodbye_text = ["See you later mater!",
                "Hasta la Vista!",
                "Good day!",
                "Adios amigo!",
                "See you soon!"]


class Assistant:
    creators = ["Aditya Saxena",
                "Archit Dogra",
                "Harshit Singh"]
    developers = ["Aditya Saxena",
                  "Archit Dogra",
                  "Harshit Singh"]
    commands = {"save workspace": "for saving workspace",
                "set up workspace": "to open workspace apps",
                "search file": "for searching a file",
                "open application": "for opening an application",
                "calculate": "for opening calculator",
                "send mail": "for sending email",
                "read inbox": "for opening inbox",
                "send whatsapp": "for whatsapp messaging",
                "tell weather": "for weather report",
                "find meaning": "for finding meaning of a word",
                "search google": "for browsing",
                "open site": "for opening website",
                "set reminder": "for setting a reminder",
                "movies nearby": "for finding movies nearby",
                "plan travel": "to plan travel, or booking hotels, flights and trains",
                "latest updates": "for showing latest news",
                "cricket score": "for live cricket score"}

    version = "1.0"

    def __init__(self):
        self.name = "doughnut"
        self.voice = 0  # 1 for female, 0 for male
        self.voice_type = "female"
        self.vrate = 180  # range 150-200
        self.greet = greet_text
        self.failure = failure_text
        self.goodbye = goodbye_text
        the_voice.set_voice(self.voice)
        the_voice.set_voice_rate(self.vrate)

    def set_vals(self, voice, vrate, name, greet=tuple(greet_text), failure=tuple(failure_text),
                 goodbye=tuple(goodbye_text)):
        self.set_nm(name)
        self.set_voice(voice)
        self.voice_type = None
        if self.voice == 1:
            self.voice_type = "female"
        elif self.voice == 0:
            self.voice_type = "male"
        self.set_voice_rate(vrate)
        self.greet = list(greet)
        self.failure = list(failure)
        self.goodbye = list(goodbye)

    def set_voice(self, typ):
        if typ == self.voice or typ == self.voice_type:
            pass
        elif typ == "female" or typ == 1 or typ == 2:
            if typ == "female":
                self.voice = random.choice([1, 2])
            else:
                self.voice = typ
            self.voice_type = "female"
            the_voice.set_voice(self.voice)
        elif typ == "male" or typ == 0:
            self.voice = 0
            self.voice_type = "male"
            the_voice.set_voice(self.voice)
        elif 3 <= typ <= 5:
            self.voice = typ
            self.voice_type = "unknown"
            the_voice.set_voice(self.voice)
        else:
            print("Invalid parameters for voice type!")
        write_vals()

    def set_voice_rate(self, rate):
        if rate == self.vrate:
            pass
        elif 50 <= rate <= 400:
            self.vrate = rate
            the_voice.set_voice(self.vrate)
        else:
            print("Invalid parameters for voice rate!")
        write_vals()

    def set_nm(self, nm):
        if self.name == nm:
            pass
        elif type(nm) == type("abc"):
            self.name = nm.lower()
        else:
            print("Name should be a string!")
        write_vals()

    def set_greet(self):
        txt = []
        print("Enter greet text (or \"CANCEL\" to cancel:")
        while True:
            temp = input(">>>")
            if temp is None:
                continue
            elif temp == "cancel":
                return
            else:
                txt.append(temp)
            print("Enter more and type \"CANCEL\" to cancel:")
        if len(txt) != 0:
            self.greet = txt
            write_vals()

    def set_failure(self):
        txt = []
        print("Enter failure text (or \"CANCEL\" to cancel:")
        while True:
            temp = input(">>>")
            if temp is None:
                continue
            elif temp == "cancel":
                return
            else:
                txt.append(temp)
            print("Enter more and type \"CANCEL\" to cancel:")
        if len(txt) != 0:
            self.failure = txt
            write_vals()

    def set_goodbye(self):
        txt = []
        print("Enter goodbye text (or \"CANCEL\" to cancel:")
        while True:
            temp = input(">>>")
            if temp is None:
                continue
            elif temp == "cancel":
                return
            else:
                txt.append(temp)
            print("Enter more and type \"CANCEL\" to cancel:")
        if len(txt) != 0:
            self.goodbye = txt
            write_vals()


def read_vals():
    try:
        fr = open("data_files/assistant_settings.txt", "r")
    except:
        write_vals()
        return
    try:
        temp = fr.read()
        data = eval(temp)
        voice = data["voice"]
        rate = data["rate"]
        name = data["name"]
        greet = data["greet"]
        failure = data["failure"]
        goodbye = data["goodbye"]
        assistant.set_vals(voice, rate, name, greet, failure, goodbye)
    except:
        print("Data in data_files/assistant_settings.txt is corrupted!")
        print("Setting default values!")
        write_vals()
    fr.close()


def write_vals():
    fw = open("data_files/assistant_settings.txt", "w")
    fw2 = open("data_files/" + assistant.name + "_assistant_settings.txt", "w")
    data = {"voice": assistant.voice,
            "rate": assistant.vrate,
            "name": assistant.name,
            "greet": assistant.greet,
            "failure": assistant.failure,
            "goodbye": assistant.goodbye}
    fw.write(str(data))
    fw2.write(str(data))
    fw2.close()
    fw.close()


def load_assistant(nm):
    if nm is None or type(nm) != type("abc"):
        print("No such profile!")
        return -1
    nm = nm.lower()
    try:
        fr = open("data_files/" + nm + "_assistant_settings.txt", "r")
    except:
        print("No such profile found!")
        the_voice.say_and_print("Do you want to make a new assistant profile? (yes or no)")
        while True:
            ch = the_voice.listening()
            try:
                ch = ch.lower()
                if ch == "yes":
                    new_profile(nm)
                    return
                elif ch == "no":
                    return -1
                else:
                    print("Please say YES or NO!")
            except:
                print("Please say YES or NO!")
    try:
        temp = fr.read()
        data = eval(temp)
        voice = data["voice"]
        rate = data["rate"]
        name = data["name"]
        greet = data["greet"]
        failure = data["failure"]
        goodbye = data["goodbye"]
        assistant.set_vals(voice, rate, name, greet, failure, goodbye)
    except:
        print("Data in data_files/" + nm + "_assistant_settings.txt is corrupted!")
        the_voice.say_and_print("Do you want to make a new assistant profile? (yes or no)")
        while True:
            ch = the_voice.listening()
            try:
                ch = ch.lower()
                if ch == "yes":
                    new_profile(nm)
                    fr.close()
                    return
                elif ch == "no":
                    fr.close()
                    return -1
                else:
                    print("Please say YES or NO!")
            except:
                print("Please say YES or NO!")
    fr.close()


def new_profile(name=None):
    if name is not None:
        nm = name
    else:
        print("Enter name of the assistant: (used to wake up assistant)")
        while True:
            nm = input(">>>")
            if len(nm) != 0:
                break
            else:
                print("Name can not be empty!")
                print("Enter correct choice!")
    nm = nm.lower()
    ex_voice = assistant.voice
    ex_rate = assistant.vrate
    try:
        fr = open("data_files/" + nm + "_assistant_settings.txt", "r")
        temp = fr.read()
        data = eval(temp)
        ex_voice = data["voice"]
        ex_rate = data["rate"]
        fr.close()
    except:
        pass

    print("Enter voice type: (male/female or \"default\" to use existing value)")
    while True:
        voice = input(">>>")
        voice = voice.lower()
        if voice == "male":
            voice = 0
            break
        elif voice == "female":
            voice = 1
            break
        elif voice == "default":
            voice = ex_voice
            break
        elif voice.isdigit():
            voice = int(voice)
            break
        else:
            print("Voice type is only male/female or \"default\"!")
            print("Enter correct choice!")
    print("Enter voice rate: (integer between 50-400 or \"default\" to use existing value)")
    while True:
        rate = input(">>>")
        try:
            rate = rate.lower()
            if rate == "default":
                rate = ex_rate
                break
            rate = int(rate)
            if 50 <= rate <= 400:
                break
            else:
                print("Rate should be in range 50-400!")
        except:
            print("Rate should be an integer!")
        print("Enter correct choice!")
    print("Do you want to edit advanced settings? enter YES or NO:")
    while True:
        flag = input(">>>")
        try:
            flag = flag.lower()
            break
        except:
            print("Please enter YES or NO!")
    if flag == "yes":
        assistant.set_vals(voice, rate, nm)
        assistant.set_greet()
        assistant.set_failure()
        assistant.set_goodbye()
    else:
        assistant.set_vals(voice, rate, nm)


def intro():
    txt = "Hello,\nI am a personal assistant for your desktop."
    the_voice.say_and_print(txt)
    txt = "I was developed by:"
    the_voice.say_and_print(txt)
    for i in Assistant.creators:
        the_voice.say_and_print(i)
    txt = "I am your assistant, so you can call me whatever you want to."
    the_voice.say_and_print(txt)
    features()


def features():
    txt = "\nI can perform various tasks such as:"
    the_voice.say_and_print(txt)
    for i in Assistant.commands:
        txt = "say " + i + " " + Assistant.commands[i]
        the_voice.say_and_print(txt)


assistant = Assistant()
read_vals()

