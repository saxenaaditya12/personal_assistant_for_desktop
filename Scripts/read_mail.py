import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import encryptor_decryptor
import the_voice


def decrypt(filename, key):
    encryptor_decryptor.decrypt(filename, key)


def encrypt(filename, key):
    encryptor_decryptor.encrypt(filename, key)


def read(BY, key):
    print("connecting to host....")
    try:
        imap = imaplib.IMAP4_SSL(host='imap.gmail.com', port=993)
    except Exception as e:
        print("Error connecting to host or port!")
        print(e)
        return
    print("information encrypted successfully ")
    try:
        imap.starttls()  # Extending the transport layer security
    except Exception as e:
        print("Transfer Layer Security is denied by server")
        pass
    decrypt('data_files/sender.txt', key)
    with open('data_files/sender.txt', mode='r', encoding='utf-8') as f:
        flag = 0
        for item in f:
            if item.split()[1].lower().rstrip() == BY:
                flag = 1
                temp = item
        if flag == 1:
            try:
                imap.login(BY, temp.split()[2].lower().rstrip())
                print("login successful")
                encrypt('data_files/sender.txt', key)
            except Exception as e:
                print("!! Something is wrong with sender credentials or other app access setting !!")
                print(e)
                exit()
        else:
            print("Data is not written in file!!")
            exit()
    status, messages = imap.select(mailbox='inbox', readonly=True)
    messages = int(messages[0])
    the_voice.say_and_print("How many emails you want to read")
    N = int(the_voice.listening())

    for i in range(messages, messages - N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(message_set=str(i),
                              message_parts="(RFC822)")  # msg gets tuple of message envelope and content
        # print(msg)
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])  # Message parser
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][
                    0]  # subject is a list of one tuple, first in tuple is our real subject
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
                from_ = msg.get("From")
                print("Subject:", subject)
                print("From:", from_)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        # ***
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            print("There are some attachments also")
                            # download attachment
                            filename = part.get_filename()  # **
                            if filename:
                                if not os.path.isdir('C:/File Attachments'):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir('C:/File Attachments')
                                    print(" Attachment file is downloaded in C:/File Attachments")
                                elif os.path.isdir('C:/File Attachments'):
                                    print("The attachment file is already downloaded in C:/File Attachments")
                                filepath = os.path.join('C:/File Attachments/', filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                if content_type == "text/html":
                    print("There is html attachment")
                    # if it's HTML, create a new HTML file and open it in browser
                    if not os.path.isdir('C:/html_attach'):
                        # make a folder for this email (named after the subject)
                        try:
                            os.mkdir('C:/html_attach')
                        except Exception as e:
                            print(e)
                            pass
                    filename = f"{subject[:50]}.html"
                    filepath = os.path.join('C:/html_attach/', filename)  # os.path.join(path, *paths)
                    # write the file
                    try:
                        open(filepath, "w").write(body)
                        # open in the chrome browser
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(filepath)
                    except Exception as e:
                        print(e)
                        pass

                print("=" * 100)
    imap.close()
    imap.logout()


def start():
    encryptor_decryptor.safe_key_generator()
    key = encryptor_decryptor.load_key()
    while 1:
        while 1:
            the_voice.say_and_print("Name of user whose inbox is to be opened")
            name = the_voice.listening()
            decrypt('data_files/sender.txt', key)
            with open('data_files/sender.txt', mode='r', encoding='utf-8') as open_sender:
                flag = 0
                for senders in open_sender:
                    if name.lower() == senders.split()[0].lower().rstrip():
                        BY = senders.split()[1].lower().rstrip()
                        flag = 1
                        read(BY, key)
                        break
                encrypt('data_files/sender.txt', key)
                if flag == 0:
                    the_voice.say_and_print("This person is not in your user's list")
                    while 1:
                        the_voice.say_and_print("Add this person in list yes or no ?")

                        flag = the_voice.listening()
                        b = type("h")
                        if type(flag) == b:
                            if flag.lower() == 'yes':
                                decrypt('data_files/sender.txt', key)
                                with open('data_files/sender.txt', mode='a', encoding='utf-8') as sender:
                                    while 1:
                                        the_voice.say_and_print("Tell user's email address")
                                        BY = the_voice.listening()
                                        if '@gmail.com' in BY or '@juitsolan.in' in BY:
                                            L = [" \n", name, " ", BY, " "]
                                            sender.writelines(L)
                                            the_voice.say_and_print("Tell password: ")
                                            sender.write(the_voice.listening())
                                            read(BY, key)
                                            while 1:
                                                the_voice.say_and_print("Continue with this user yes or no ?")
                                                flag = "none"
                                                flag = the_voice.listening()
                                                if flag == 'yes':
                                                    read(BY, key)
                                                    break
                                                elif flag == 'no':
                                                    the_voice.say_and_print("Okay")
                                                    break
                                                else:
                                                    the_voice.say_and_print("Try again")
                                            break
                                        else:
                                            the_voice.say_and_print("Wrong gmail format")
                                            the_voice.say_and_print("Try again")
                                encrypt('data_files/sender.txt', key)
                                break
                            elif flag.lower() == 'no':
                                break
                            else:
                                the_voice.say_and_print("Try again")
                        else:
                            the_voice.say_and_print("Try again")
            while 1:
                the_voice.say_and_print("Read again yes or no ?")
                flag = the_voice.listening()
                b = type("h")
                if type(flag) == b:
                    if flag.lower() == 'yes':
                        break
                    elif flag.lower() == 'no':
                        the_voice.say_and_print("See you again ")
                        return 1
                    else:
                        the_voice.say_and_print("Try again")
                else:
                    the_voice.say_and_print("Try again")
