import google_search
import tell_meaning
import frequent_site
import set_reminder
import movies_nearby
import plan_travel
import news_update
import cricket_score
import the_voice


def start(cmd):
    if "find meaning" in cmd or ("tell" in cmd and "meaning" in cmd) or ("find" in cmd and "meaning" in cmd):
        the_voice.say_and_print("Say the word to get meaning")
        a = the_voice.listening()
        if a is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while a is not None:
                a = the_voice.listening()
                a = a.lower()
                if a == "cancel":
                    return 1
        a = a.lower()
        the_voice.say_and_print("Finding meaning...")
        tell_meaning.meaning(a)
        return 1

    elif "search google" in cmd or "find on google" in cmd or ("search" in cmd and "net" in cmd) or (
            "search" in cmd and "google" in cmd):
        the_voice.say_and_print("What do you want to search?")
        a = the_voice.listening()
        if a is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while a is not None:
                a = the_voice.listening()
                a = a.lower()
                if a == "cancel":
                    return 1
        a = a.lower()
        the_voice.say_and_print("Searching...")
        google_search.search(a)
        return 1

    elif "open site" in cmd or ("open" in cmd and "site" in cmd):
        the_voice.say_and_print("which site do you want to open?")
        a = the_voice.listening()
        if a is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while a is not None:
                a = the_voice.listening()
                a = a.lower()
                if a == "cancel":
                    return 1
        a = a.lower()
        the_voice.say_and_print("Opening Site...")
        frequent_site.site(a)
        return 1
    elif "set reminder" in cmd or ("set" in cmd and "reminder" in cmd):
        the_voice.say_and_print("What shall I remind you about?")
        a = the_voice.listening()
        if a is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while a is not None:
                a = the_voice.listening()
                a = a.lower()
                if a == "cancel":
                    return 1
        a = a.lower()
        the_voice.say_and_print("Setting reminder...")
        the_voice.say_and_print("In how many seconds you want to be reminded?")
        while True:
            temp = the_voice.listening()
            try:
                b = int(temp)
                break
            except:
                if temp.lower() == "cancel":
                    return 1
                the_voice.say_and_print("Please tell after how many seconds you want to be reminded, or say \"CANCEL\" to cancel")
        set_reminder.task(a, b)
        return 1

    elif "movies nearby" in cmd or "search movies" in cmd or ("movies" in cmd and "nearby" in cmd) or (
            "search" in cmd and "movies" in cmd):
        the_voice.say_and_print("Showing Movies Near by...")
        movies_nearby.movies("movies nearby")
        return 1

    elif "plan travel" in cmd or ("plan" in cmd and "travel" in cmd) or ("book" in cmd and "hotel" in cmd) or (
            "book" in cmd and "flight" in cmd) or ("book" in cmd and "train" in cmd) or (
            "book" in cmd and "bus" in cmd):
        the_voice.say_and_print("Plan Your Travel")
        plan_travel.travel()
        return 1

    elif "latest updates" in cmd or ("latest" in cmd and "updates" in cmd) or ("tell" in cmd and "news" in cmd):
        the_voice.say_and_print("Showing Latest Feeds...")
        news_update.news()
        return 1

    elif "cricket score" in cmd or ("cricket" in cmd and "score" in cmd) or ("live" in cmd and "cricket" in cmd):
        the_voice.say_and_print("Showing Cricket Score...")
        cricket_score.score()
        return 1

    return 0


