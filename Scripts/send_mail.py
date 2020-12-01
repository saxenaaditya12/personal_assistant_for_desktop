import the_voice
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import encryptor_decryptor


def decrypt(filename, key):
    encryptor_decryptor.decrypt(filename, key)


def encrypt(filename, key):
    encryptor_decryptor.encrypt(filename, key)


try:
    s = smtplib.SMTP(host='smtp.gmail.com', port=587 or 465)
    s.starttls()
except Exception as e:
    print("Error connecting to host or port!\nCheck Internet Connection!")
    print(e)

encryptor_decryptor.safe_key_generator()
key = encryptor_decryptor.load_key()


def send(BY, key):
    the_voice.say_and_print("Tell the name of receiver or \"CANCEL\" to cancel")
    name = the_voice.listening()
    while 1:
        try:
            name = name.lower()
            if name == "cancel":
                return
            break
        except:
            the_voice.say_and_print("Tell the name of receiver or \"CANCEL\" to cancel")
        name = the_voice.listening()

    decrypt('data_files/mycontacts.txt', key)
    with open('data_files/mycontacts.txt', mode='r', encoding='utf-8') as open_receiver:
        while 1:
            flag = 0
            for receiver in open_receiver:
                name2 = receiver.split()[0].lower().rstrip()
                if name == name2:
                    flag = 1
                    TO = receiver.split()[1].lower().rstrip()
                    TO = TO.rstrip()
            if flag == 0:
                the_voice.say_and_print("This person is not in your receiver's list!")
                the_voice.say_and_print("Add this person in list, yes or no?")
                the_voice.say_and_print("or say \"CANCEL\" to cancel")
                while 1:
                    flag = the_voice.listening()
                    while 1:
                        try:
                            flag = flag.lower()
                            if flag == "cancel":
                                encrypt('data_files/mycontacts.txt', key)
                                return
                            break
                        except:
                            print("Say yes or no, or say \"CANCEL\" to cancel")
                        flag = the_voice.listening()
                    if flag.lower() == 'yes':
                        decrypt('data_files/mycontacts.txt', key)
                        with open('data_files/mycontacts.txt', mode='a', encoding='utf-8') as receive:
                            while 1:
                                the_voice.say_and_print("Enter receiver's email address or \"CANCEL\" to cancel")
                                TO = input(">>>")
                                if type(TO) != type("abc"):
                                    print("Email address can't be empty!")
                                    print("Enter email or \"CANCEL\" to cancel")
                                    continue
                                if "@" in TO and "." in TO:
                                    L = [" \n", name, " ", TO]
                                    receive.writelines(L)
                                    break
                                elif TO.lower() == 'cancel':
                                    encrypt('data_files/mycontacts.txt', key)
                                    return
                                else:
                                    the_voice.say_and_print("Wrong email format!")
                                    the_voice.say_and_print("try again...")
                                    continue
                        encrypt('data_files/mycontacts.txt', key)
                        break
                    elif flag.lower() == 'no':
                        print("Say the name of receiver again or \"CANCEL\" to cancel")
                        name = the_voice.listening()
                        while 1:
                            try:
                                name = name.lower()
                                if name == "cancel":
                                    encrypt('data_files/mycontacts.txt', key)
                                    return
                                break
                            except:
                                print("Tell the name of receiver again or \"CANCEL\" to cancel")
                            name = the_voice.listening()
                        break
                    else:
                        print("Say \"YES\",\"NO\" or \"CANCEL\", try again")
                        continue
            else:
                break
    encrypt('data_files/mycontacts.txt', key)

    the_voice.say_and_print("connecting to host...")
    # s.starttls()  # Extending the transport layer security
    # print("information encrypted...")
    # decrypt('data_files/sender.txt', key)
    # with open('data_files/sender.txt', mode='r', encoding='utf-8') as f:
    #     for item in f:
    #         if item.split()[1].lower().rstrip() == BY:
    #             flag = 1
    #             temp = item
    #     if flag == 1:
    #         try:
    #             s.login(BY, temp.split()[2].lower().rstrip())
    #             print("login successful...\n")
    #             encrypt('data_files/sender.txt', key)
    #         except Exception as e:
    #             print("!! Something is wrong with sender credentials or other app access setting !!")
    #             print(e)
    #             return 1
    #     else:
    #         the_voice.say_and_print("Data is not written in file!!")
    #         return 1
    the_voice.say_and_print("What is the subject or say \"CANCEL\" to cancel")
    SUBJECT = the_voice.listening()
    while 1:
        try:
            SUBJECT = SUBJECT.lower()
            if SUBJECT == "cancel":
                return
            break
        except:
            print("Tell the name of receiver again or \"CANCEL\" to cancel")
        SUBJECT = the_voice.listening()

    while 1:
        the_voice.say_and_print("What is the message or say \"CANCEL\" to cancel")
        body = the_voice.listening()
        while 1:
            try:
                if body.lower() == "cancel":
                    return
                break
            except:
                print("Please tell the message or say \"CANCEL\" to cancel")
            body = the_voice.listening()

        print(body)
        the_voice.say_and_print("Is this correct yes or no?")
        while 1:
            is_it = the_voice.listening()
            while 1:
                try:
                    is_it = is_it.lower()
                    if is_it == "cancel":
                        return
                    break
                except:
                    print("Please say yes or no? Or say \"CANCEL\" to cancel")
                is_it = the_voice.listening()
            if is_it.lower() == "no":
                break
            elif is_it.lower() == "yes":
                msg = MIMEMultipart()
                msg['From'] = BY
                msg['To'] = TO
                msg['Subject'] = SUBJECT
                msg.attach(MIMEText(body, 'plain'))
                try:
                    s.send_message(msg)
                except Exception as e:
                    print("Failed to send!")
                    print(e)
                    return
                the_voice.say_and_print("Message sent successfully!")
                del msg
                s.quit()
                return
            else:
                the_voice.say_and_print("just say 'yes', 'no' or 'cancel'!")
                continue


def update_sender():
    while 1:
        the_voice.say_and_print("Name the sender or say \"CANCEL\" to cancel")
        name = the_voice.listening()
        while 1:
            try:
                name = name.lower()
                if name == "cancel":
                    return
                break
            except:
                print("Name the sender or say \"CANCEL\" to cancel")
            name = the_voice.listening()

        decrypt('data_files/sender.txt', key)
        with open('data_files/sender.txt', mode='r', encoding='utf-8') as open_sender:
            flag = 0
            for senders in open_sender:
                if name.lower() == senders.split()[0].lower().rstrip():
                    flag = 1
                    BY = senders.split()[1].lower().rstrip()
                    print("Information encrypted!")
                    try:
                        s.login(BY, senders.split()[2].lower().rstrip())
                        the_voice.say_and_print("Login successful!")
                    except Exception as e:
                        print("Something is wrong with sender credentials or account access settings!")
                        print(e)
                        return 1
                    send(BY, key)
                    break
            encrypt('data_files/sender.txt', key)
            if flag == 0:
                the_voice.say_and_print("This person is not in your sender's list!")
                while 1:
                    the_voice.say_and_print("Add this person in senders list, yes or no? Or say \"CANCEL\" to cancel.")
                    flag = the_voice.listening()
                    if type(flag) == type("abc"):
                        if flag.lower() == 'yes':
                            decrypt('data_files/sender.txt', key)
                            with open('data_files/sender.txt', mode='a', encoding='utf-8') as sender:
                                while 1:
                                    the_voice.say_and_print("Enter sender's email address or \"CANCEL\" to cancel.")
                                    while 1:
                                        BY = input(">>>")
                                        try:
                                            BY = BY.lower()
                                            if BY == "cancel":
                                                encrypt('data_files/sender.txt', key)
                                                return
                                            break
                                        except:
                                            print("Sender's email address can't be empty!")
                                            print("Enter email or \"CANCEL\" to cancel.")
                                    if '@' in BY and '.' in BY:
                                        the_voice.say_and_print("Enter password or \"CANCEL\" to cancel.")
                                        PassWord = input(">>>")
                                        while 1:
                                            try:
                                                PassWord = PassWord.lower()
                                                if PassWord == "cancel":
                                                    encrypt('data_files/sender.txt', key)
                                                    return
                                                break
                                            except:
                                                the_voice.say_and_print("Enter password or \"CANCEL\" to cancel.")
                                            PassWord = input(">>>")
                                        L = [" \n", name, " ", BY, " ", PassWord]
                                        sender.writelines(L)

                                        the_voice.say_and_print("Sender is added successfully")
                                        send(BY, key)
                                        while 1:
                                            the_voice.say_and_print(
                                                "Continue messaging from this sender, yes or no? Or say \"CANCEL\" to cancel.")
                                            flag2 = the_voice.listening()
                                            while 1:
                                                try:
                                                    flag2 = flag2.lower()
                                                    if flag2 == "cancel":
                                                        encrypt('data_files/sender.txt', key)
                                                        return
                                                    break
                                                except:
                                                    print("Say yes , no or \"CANCEL\" to cancel.")
                                                flag2 = the_voice.listening()
                                            if flag2 == 'yes':
                                                the_voice.say_and_print("Okay!")
                                                send(BY, key)
                                            elif flag2 == 'no':
                                                the_voice.say_and_print("Okay!")
                                                break
                                            else:
                                                the_voice.say_and_print("Try again!")
                                                continue
                                        break
                                    else:
                                        the_voice.say_and_print("Wrong gmail format!")
                                        the_voice.say_and_print("try again...")
                                        continue
                            encrypt('data_files/sender.txt', key)
                            break
                        elif flag.lower() == 'no':
                            break
                        else:
                            the_voice.say_and_print("Wrong input try again")
                    else:
                        the_voice.say_and_print("Try again...")
                        continue


def start():
    while 1:
        the_voice.say_and_print("Use default sender,\"python\" ? say yes, no, or \"CANCEL\" to cancel")
        use_it = the_voice.listening()
        while 1:
            try:
                use_it = use_it.lower()
                if use_it == "cancel":
                    return
                break
            except:
                print("Say yes , no, or \"CANCEL\" to cancel")
            use_it = the_voice.listening()
        if use_it == "yes":
            # using default sender python
            decrypt('data_files/sender.txt', key)
            with open('data_files/sender.txt', mode='r', encoding='utf-8') as open_sender:
                for senders in open_sender:
                    if "python" == senders.split()[0].lower().rstrip():
                        BY = senders.split()[1].lower().rstrip()

                        try:
                            s.login(BY, senders.split()[2].lower().rstrip())
                            the_voice.say_and_print("Login successful!")
                        except Exception as e:
                            print("Something is wrong with sender credentials or account access settings!")
                            print(e)
                            encrypt('data_files/sender.txt', key)
                            return
                        send(BY, key)
                    else:
                        the_voice.say_and_print("Default user data destroyed!")
                        the_voice.say_and_print("Enter new user data")
                        update_sender()
            encrypt('data_files/sender.txt', key)
        elif use_it == "cancel":
            return
        elif use_it == "no":
            the_voice.say_and_print("Choose another sender...")
            update_sender()
        else:
            the_voice.say_and_print("Invalid input")
            continue

        while 1:
            the_voice.say_and_print("Send again, yes or no ")
            flag = the_voice.listening()
            if type(flag) == type("abc"):
                if flag == 'no':
                    encrypt('data_files/mycontacts.txt', key)
                    encrypt('data_files/sender.txt', key)
                    return
                elif flag == 'yes':
                    break
                else:
                    print("Say yes or no?")
            else:
                print("Say yes or no?")

