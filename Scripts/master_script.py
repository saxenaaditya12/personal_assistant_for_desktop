import assistant_settings
import the_voice
import user_data
import main_archit
import main_harshit
import main_aditya
import random

asst_nm = None
greet_text = []
failure_text = []
goodbye_text = []


def on_startup():
    main_aditya.preprocess()


def assistant_setup():
    global asst_nm, greet_text, failure_text, goodbye_text
    asst_nm = assistant_settings.assistant.name
    greet_text = assistant_settings.assistant.greet
    failure_text = assistant_settings.assistant.failure
    goodbye_text = assistant_settings.assistant.goodbye


assistant_setup()
try:
    the_voice.say_and_print("Hello " + user_data.user.nicknm)
except:
    the_voice.say_and_print("Hello!")
the_voice.say_and_print("Starting, Please wait...")
on_startup()  # this function takes some time, it reads current processes and looks for any new directory
the_voice.say_and_print(random.choice(greet_text))
cmd = the_voice.wake_listen(asst_nm)
try:
    cmd = cmd.lower()
except:
    cmd = None
while True:
    if cmd is None:
        pass
    elif asst_nm in cmd:
        the_voice.say("yes")
        cmd = the_voice.listening()
        try:
            cmd = cmd.lower()
        except:
            cmd = None

        if cmd is None:
            pass
        elif ("add" in cmd and "user" in cmd) or ("new" in cmd and "user" in cmd) or ("new" in cmd and "user" in cmd and "info" in cmd):
            the_voice.say_and_print("Enter your details")
            user_data.collect_user_data()
        elif ("edit" in cmd and "personal" in cmd and "info" in cmd) or ("edit" in cmd and "user" in cmd and "details" in cmd) or ("edit" in cmd and "personal" in cmd and "details" in cmd) or ("edit" in cmd and "user" in cmd and "info" in cmd):
            the_voice.say_and_print("Reading user data...")
            user_data.edit_user_data()
        elif ("change" in cmd and "profile" in cmd) or ("change" in cmd and "user" in cmd):
            the_voice.say_and_print("What is the first name of user?")
            while True:
                fnm = the_voice.listening()
                try:
                    fnm.lower()
                    if fnm == "cancel":
                        break
                    user_data.change_user(fnm)
                    break
                except:
                    print("Please say the name again!")
                    print("or Say \"CANCEL\" to cancel")
        elif ("setup" in cmd and "assistant" in cmd) or ("settings" in cmd and "assistant" in cmd) or (
                "settings" in cmd and "change" in cmd):
            the_voice.say_and_print("Enter the settings of your wish:")
            assistant_settings.new_profile()
            assistant_setup()
            the_voice.say_and_print("Assistant settings successfully updated!")
            try:
                the_voice.say_and_print("Hello " + user_data.user.nicknm)
            except:
                the_voice.say_and_print("Hello!")
        elif ("change" in cmd and "assistant" in cmd) or ("load" in cmd and "assistant" in cmd) or (
                "assistant" in cmd and "profile" in cmd):
            the_voice.say_and_print("Tell the name of assistant you want to use?")
            name = the_voice.listening()
            while True:
                try:
                    name = name.lower()
                    if name == "cancel":
                        break
                    else:
                        t = assistant_settings.load_assistant(name)
                        if t != -1:
                            assistant_setup()
                            the_voice.say_and_print("Assistant profile successfully loaded!")
                            try:
                                the_voice.say_and_print("Hello " + user_data.user.nicknm)
                            except:
                                the_voice.say_and_print("Hello!")
                        break
                except:
                    print("Please Enter a name or \"CANCEL\" to cancel")
                    name = input(">>>")
        elif main_aditya.start(cmd):
            pass
        elif main_harshit.start(cmd):
            pass
        elif main_archit.start(cmd):
            pass
        elif "exit" in cmd or "terminate" in cmd or ("shut" in cmd and "down" in cmd) or "stop" in cmd or (
                "good" in cmd and "bye" in cmd) or "see you later" in cmd or ("turn" in cmd and "off" in cmd):
            the_voice.say_and_print(random.choice(goodbye_text))
            break
        else:
            the_voice.say_and_print(random.choice(failure_text))
            the_voice.say_and_print("Please try any other command...")

    else:
        pass
    cmd = the_voice.wake_listen(asst_nm)
    try:
        cmd = cmd.lower()
    except:
        cmd = None
