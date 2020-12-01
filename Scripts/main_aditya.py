import store_process
import find
import set_workspace
import the_voice
import calculate


def preprocess():
    store_process.start_pro()
    find.pre_process()


def start(cmd):
    if "save workspace" in cmd or ("save" in cmd and "workspace" in cmd):
        the_voice.say_and_print("Saving workspace...")
        store_process.save_unique()
        return 1

    elif "set up workspace" in cmd or ("set" in cmd and "workspace" in cmd):
        the_voice.say_and_print("Setting workspace...")
        set_workspace.open_workspace_apps()
        return 1

    elif "search file" in cmd or ("search" in cmd and "file" in cmd):
        the_voice.say_and_print("Say the file name to search")
        temp = the_voice.listening()
        if temp is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while temp is not None:
                temp = the_voice.listening()
                temp = temp.lower()
                if temp == "cancel":
                    return 1
        temp = temp.lower()
        find.search(temp)
        return 1

    elif "open application" in cmd or ("open" in cmd and "app" in cmd):
        the_voice.say_and_print("Say the application name to open: ")
        temp = the_voice.listening()
        if temp is None:
            print("Sorry, didn't get you!")
            print("Please say the name of file to search, or \"CANCEL\" to cancel")
            while temp is not None:
                temp = the_voice.listening()
                temp = temp.lower()
                if temp == "cancel":
                    return 1
        temp = temp.lower()
        if ".exe" not in temp:
            temp = temp + ".exe"
        app_paths = find.search(temp, "endswith")
        for app_path in app_paths:
            set_workspace.open_app(app_path)
        if len(app_paths) == 0:
            the_voice.say_and_print("No such application found!")
        return 1
    elif "calculate" in cmd or ("run" in cmd and "calculator" in cmd) or ("open" in cmd and "calculator" in cmd):
        calculate.start()
        return 1

    return 0
