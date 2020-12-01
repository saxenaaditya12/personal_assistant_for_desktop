import wmi
import ast
import the_voice


def start_pro():
    f = wmi.WMI()
    pre_file = open("data_files/start-processes.txt", "w")
    pre = dict()
    for process in f.Win32_Process():
        pre[process.Name] = process.ExecutablePath
    pre_file.write(str(pre))
    pre_file.close()


def crr_pro():
    f = wmi.WMI()
    post_file = open("data_files/crr-processes.txt", "w")
    post = dict()
    for process in f.Win32_Process():
        post[process.Name] = process.ExecutablePath
    post_file.write(str(post))
    post_file.close()
    return post


def save_unique():
    try:
        fr = open("data_files/start-processes.txt", "r")
    except:
        print("Start Processes not found!")
        return
    post = crr_pro()
    try:
        pre = ast.literal_eval(fr.read())
    except:
        print("Invalid data in start-processes.txt!")
        fr.close()
        return
    uni = dict()
    for i in post:
        if i not in pre:
            uni[i] = post[i]
    temp = list()
    # filtering
    for i in uni:
        if i in temp:
            del uni[i]
        else:
            if uni[i] is not None and "windows\\" not in uni[i].lower() and "windows\\\\" not in uni[i].lower():
                temp.append(i)
    fw = open("data_files/workspace.txt", 'w')
    fw.write(str(uni))
    fr.close()
    fw.close()
    the_voice.say_and_print("Success!")

