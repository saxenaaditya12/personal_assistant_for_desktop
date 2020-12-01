import the_voice
import main_harshit
import main_aditya
import main_archit
import store_process
import find

# store_process.start_pro()
# find.pre_process()
the_voice.say("Hey there, What should I call you?")
print("What should I call you?")
user = the_voice.listening()
print("Hey " + user + " what can i do for you.......")
the_voice.say("Hey " + user + " what can i do for you.......")
# main_harshit.IAM(a)


while 1:
    a = the_voice.listening()
    if a.lower() == 'send mail':
        main_harshit.start(a.lower())
    elif a.lower() == 'read inbox':
        main_harshit.start(a.lower())
    elif a.lower() == 'send whatsapp':
        main_harshit.start(a.lower())
    elif a.lower() == 'object recognise':
        main_harshit.start(a.lower())
    elif a.lower() == "weather" or a.lower() == "how is the weather":
        main_harshit.start("weather")
    elif "save workspace" in a.lower() or ("save" in a.lower() and "workspace" in a.lower()):
        main_aditya.start("save workspace")
    elif "set up workspace" in a.lower() or ("set" in a.lower() and "workspace" in a.lower()):
        main_aditya.start("set up workspace")
    elif "search file" in a.lower() or ("search" in a.lower() and "file" in a.lower()):
        main_aditya.start("search file")
    elif "open application" in a.lower() or ("open" in a.lower() and "app" in a.lower()):
        main_aditya.start("open application")
    elif a.lower() == "find meaning":
        main_archit.start("meaning")
    elif a.lower() == "google search":
        main_archit.start("google")
    elif a.lower() == 'open websites':
        main_archit.start("frequent site")
    elif a.lower() == "set reminder":
        main_archit.start("set reminder")
    elif a.lower() == "movies nearby":
        main_archit.start("movies nearby")
    elif a.lower() == "latest updates":
        main_archit.start("latest updates")
    elif a.lower() == "cricket score":
        main_archit.start("cricket score")
    elif a.lower() == 'exit' or a.lower() == 'stop' or a.lower() == 'end' or a.lower() == 'quit' or a.lower() == 'terminate' or a.lower() == 'shut down':
        print("Have a good day!")
        the_voice.say("Have a good day!")
        exit()
    else:
        print("Didn't understand what you said!")
        the_voice.say("Didn't understand what you said!")
    the_voice.say("Anything Else " + user + " yes or no")
    print("Anything Else " + user + " yes or no ?")
    while 1:
        flag = the_voice.listening()
        if flag.lower() == "yes":
            print("okay!\n what it is")
            the_voice.say("okay, what it is")
            break
        elif flag.lower() == 'no':
            print("Have a good day!")
            the_voice.say("Have a good day!")
            exit()
        else:
            the_voice.say("Didn't understand what you said!")
            print("Didn't understand what you said!")
            the_voice.say("Try saying again")
            print("Try saying again")
