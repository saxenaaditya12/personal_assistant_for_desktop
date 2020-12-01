import ctypes
import datetime
import the_voice
import ast


def get_disp_name():
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3
    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)
    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value


class User:
    def __init__(self):
        self.name = get_disp_name()
        temp = self.name.split()
        self.first_nm = temp[0]
        self.last_nm = temp[len(temp) - 1]
        self.nicknm = self.name[:2].upper()

        self.dob = None
        self.gender = None
        self.email = None
        self.age = None

    def set_values(self, nm, nicknm, dob, gender, email, age):
        self.name = nm
        temp = self.name.split()
        self.first_nm = temp[0]
        self.last_nm = temp[len(temp) - 1]
        self.nicknm = nicknm

        self.dob = dob
        self.gender = gender
        self.email = email
        self.age = age

    def set_name(self, nm):
        if nm is not None:
            self.name = nm
            temp = self.name.split()
            self.first_nm = temp[0]
            self.last_nm = temp[len(temp) - 1]
            self.nicknm = self.name[:2].upper()

    def set_nicknm(self, nm):
        if nm is not None:
            self.nicknm = nm

    def set_dob(self, dob):
        if str(type(dob)) == "<class \'datetime.datetime\'>":
            self.dob = dob
            self.age = datetime.datetime.now().year - self.dob.year
        else:
            print("Not a proper date-time format!")

    def set_gender(self, gen):
        self.gender = gen

    def set_email(self, em):
        if em is not None and ("@" in em and "." in em):
            self.email = em
        else:
            print("Not a valid email address!")


def collect_user_data():
    the_voice.say_and_print("What's your name?")
    nm = input(">>>")
    user.set_name(nm)

    the_voice.say_and_print("What's your date of birth?")
    print("(In YYYY/MM/DD format)")
    dt = input(">>>")
    try:
        dt = dt.split("/")
        if len(dt[0]) == 4 and len(dt[1]) <= 2 and len(dt[2]) <= 2:
            yr = int(dt[0])
            mon = int(dt[1])
            date = int(dt[2])
            temp = datetime.datetime(yr, mon, date)
            user.set_dob(temp)
    except:
        print("Not a valid date format!")

    the_voice.say_and_print("What's your gender?")
    gen = input(">>>")
    user.set_gender(gen)

    the_voice.say_and_print("What's your email?")
    em = input(">>>")
    user.set_email(em)

    the_voice.say_and_print("What should I call you?")
    print("Enter nick name")
    nicknm = input(">>>")
    user.set_nicknm(nicknm)
    fw = open("data_files/user_data.txt", "w")
    fw2 = open("data_files/" + user.first_nm.lower() + "_data.txt", "w")
    fw.write(str(user.__dict__))
    fw2.write(str(user.__dict__))
    fw.close()
    fw2.close()
    the_voice.say_and_print("User data saved successfully!")
    the_voice.say_and_print("Hello " + user.nicknm + ", what are my orders?")


def set_user_data():
    try:
        fr = open("data_files/user_data.txt", "r")
    except:
        print("user_data.txt not found, setting default values!")
        return

    data = fr.read()

    try:
        data = eval(data)
        user.set_values(data['name'], data['nicknm'], data['dob'], data['gender'], data['email'], data['age'])
        fr.close()
        return
    except:
        pass

    try:
        data = ast.literal_eval(data)
        user.set_values(data['name'], data['nicknm'], data['dob'], data['gender'], data['email'], data['age'])
    except:
        print("Data in user_data.txt is corrupted, setting default values!")
    fr.close()


def edit_user_data():
    try:
        fr = open("data_files/user_data.txt", "r")
    except:
        print("user_data.txt not found!")
        return
    data = fr.read()
    try:
        data = eval(data)
        ex_nm = data['name']
        ex_nicknm = data['nicknm']
        ex_dob = data['dob']
        ex_gen = data['gender']
        ex_em = data['email']
        fr.close()
    except:
        print("data in data_files/user_data.txt is corrupted")
        fr.close()
        return

    print("Current Details:")
    print("Name:", data['name'],
          "\nNickname:", data['nicknm'],
          "\nDate of birth:", data['dob'],
          "\nGender:", data['gender'],
          "\nEmail:", data['email'],
          "\nAge:", data['age'])
    print("What's your name? (type \"Default\" for using existing value)")
    while True:
        nm = input(">>>")
        if nm is not None and nm.lower() != "default":
            user.set_name(nm)
            break
        elif nm is None:
            print("Name can not be empty!")
            print("Please enter your full name")
        else:
            nm = ex_nm
            user.set_name(nm)
            break
    print("What's your date of birth? (type \"Default\" for using existing value)")
    print("(In YYYY/MM/DD format)")
    while True:
        dt = input(">>>")
        if dt is not None and dt.lower() == "default":
            dt = ex_dob
            user.set_dob(dt)
            break
        try:
            dt = dt.split("/")
            if len(dt[0]) == 4 and len(dt[1]) <= 2 and len(dt[2]) <= 2:
                yr = int(dt[0])
                mon = int(dt[1])
                date = int(dt[2])
                temp = datetime.datetime(yr, mon, date)
                user.set_dob(temp)
                break
        except:
            print("Not a valid date format!")
            print("Please enter proper date of birth")

    print("What's your gender? (type \"Default\" for using existing value)")
    gen = input(">>>")
    if gen is not None and gen.lower()!= "default":
        user.set_gender(gen)
    else:
        gen = ex_gen
        user.set_gender(gen)

    print("What's your email? (type \"Default\" for using existing value)")
    while True:
        em = input(">>>")
        if em is not None and em.lower() != "default":
            if "@" in em and "." in em:
                user.set_email(em)
                break
            else:
                print("Not a valid email address!")
                print("Enter proper email")
        else:
            em = ex_em
            user.set_email(em)
            break

    print("What should I call you? (type \"Default\" for using existing value)")
    print("Enter nick name")
    nicknm = input(">>>")
    if nicknm is not None and nicknm.lower() != "default":
        user.set_nicknm(nicknm)
    else:
        nicknm = ex_nicknm
        user.set_nicknm(nicknm)

    fw = open("data_files/user_data.txt", "w")
    fw2 = open("data_files/" + user.first_nm.lower() + "_data.txt", "w")
    fw.write(str(user.__dict__))
    fw2.write(str(user.__dict__))
    fw.close()
    fw2.close()
    the_voice.say_and_print("User updated successfully!")
    the_voice.say_and_print("Hello " + user.nicknm + ", what are my orders?")


def change_user(fnm):
    fnm = fnm.lower()
    if user.first_nm.lower() == fnm:
        the_voice.say_and_print("That is already the current user!")
        return
    while True:
        try:
            fr = open("data_files/" + fnm + "_data.txt", "r")
            break
        except:
            print("data_files/" + fnm + "_data.txt does not exists!")
            the_voice.say_and_print("No such user found!")
            the_voice.say_and_print("Please type the first name or \"CANCEL\" to cancel")
            fnm = input(">>>")
            fnm = fnm.lower()
            if fnm == "cancel":
                return
            if user.first_nm.lower() == fnm:
                the_voice.say_and_print("That is already the current user!")
                return
    fw = open("data_files/user_data.txt", "w")
    newdata = fr.read()
    fw.write(newdata)
    fr.close()
    fw.close()
    set_user_data()
    the_voice.say_and_print("User updated successfully!")
    the_voice.say_and_print("Hello " + user.nicknm + ", what are my orders?")


user = User()
set_user_data()
