import ast
import subprocess
import the_voice


def open_workspace_apps():
    try:
        fr = open("data_files/workspace.txt", 'r')
    except:
        print("workspace.txt does not exist!")
        return
    w_list = ast.literal_eval(fr.read())
    for i in w_list:
        try:
            subprocess.Popen(w_list[i])
            print(i, "opened successfully!")
        except:
            print(i, "can't be opened!")
    fr.close()
    the_voice.say_and_print("Success!")


def open_app(app_path):
    try:
        subprocess.Popen(app_path)
        print(app_path, "opened successfully!")
    except:
        print(app_path, "can't be opened!")
