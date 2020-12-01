import encryptor_decryptor
import the_voice
from twilio.rest import Client


def decrypt(filename, key):
    encryptor_decryptor.decrypt(filename, key)


def encrypt(filename, key):
    encryptor_decryptor.encrypt(filename, key)


def add_contact(name, key):
    decrypt('data_files/phone_book.txt', key)
    with open('data_files/phone_book.txt', mode='a', encoding='utf-8') as phone:
        print("Enter whatsapp number along with country code(eg.+91 for india): ")
        the_voice.say("Enter whatsapp number along with country code")
        while True:
            number = input(">>>")
            if '+' not in number:
                print("Invalid number(Enter country code also)\nTry again")
                the_voice.say("Invalid number Enter country code also\n Try again")
            else:
                break
        L = [" \n", name, " ", number]
        phone.writelines(L)
        the_voice.say_and_print("Do you want to send a message to this number, yes or no?")
        while True:
            flag2 = the_voice.listening()
            try:
                flag2 = flag2.lower()
                if flag2 == 'yes':
                    break
                elif flag2 == 'no':
                    encrypt('data_files/phone_book.txt', key)
                    return
                else:
                    the_voice.say_and_print("Please say Yes or No!")
            except:
                print("Sorry, didn't get what you said, please try again")
        RECEIVER = number
        print("Sending to:", RECEIVER)
        the_voice.say("Sending to " + RECEIVER)
        send(RECEIVER, key)
    encrypt('data_files/phone_book.txt', key)


def start():
    encryptor_decryptor.safe_key_generator()
    key = encryptor_decryptor.load_key()
    while 1:
        the_voice.say_and_print("Who is the receiver?")
        while True:
            name = the_voice.listening()
            try:
                name = name.lower()
                if name == "cancel":
                    return
                break
            except:
                print("Sorry didn't get you, please tell the name or \"CANCEL\" to cancel")
        print("Receiver:", name)
        decrypt('data_files/phone_book.txt', key)
        with open('data_files/phone_book.txt', mode='r', encoding='utf-8') as contacts_file:
            flag = 0
            for contacts in contacts_file:
                name2 = contacts.split()[0]
                name2 = name2.lower()
                if name2 == name:
                    flag = 1
                    RECEIVER = contacts.split()[1]
                    RECEIVER = RECEIVER.rstrip()
                    print("sending to: ", RECEIVER)
                    encrypt('data_files/phone_book.txt', key)
                    send(RECEIVER, key)
        if flag == 0:
            the_voice.say_and_print("Given name is not in your contact list!")
            while 1:
                the_voice.say_and_print("Enter this in contact list, yes or no?")
                flag = the_voice.listening()
                try:
                    flag = flag.lower()
                    if flag == 'yes':
                        add_contact(name, key)
                        break
                    elif flag == 'no':
                        break
                    else:
                        the_voice.say_and_print("Please say Yes or No!")
                except:
                    print("Sorry, didn't get what you said, please try again")

            the_voice.say_and_print("Send again, yes or no?")

        while True:
            flag3 = the_voice.listening()
            try:
                flag3 = flag3.lower()
                if flag3 == 'yes':
                    break
                elif flag3 == 'no':
                    return
                else:
                    the_voice.say_and_print("Please say Yes or No!")
            except:
                print("Sorry, didn't get what you said, please try again")


def send(RECEIVER, key):
    decrypt('data_files/sid-token.txt', key)
    with open('data_files/sid-token.txt', mode='r', encoding='utf-8') as id:
        for items in id:
            account_sid = items.split()[0]
            auth_token = items.split()[1]
    encrypt('data_files/sid-token.txt', key)

    client = Client(account_sid, auth_token)
    while True:
        the_voice.say_and_print("Enter message:")
        waap_message = the_voice.listening()
        while True:
            try:
                waap_message.lower()
                break
            except:
                print("Sorry didn't get you, please say again!")
            waap_message = the_voice.listening()
        print("Send?(yes/no)")
        the_voice.say("Send, yes or no")
        while 1:
            flag = the_voice.listening()
            try:
                flag = flag.lower()
                if flag == 'yes':
                    the_voice.say_and_print("Sending...")
                    break
                elif flag == 'no':
                    break
                else:
                    the_voice.say_and_print("Please say Yes or No!")
            except:
                print("Sorry didn't get what you said, please say again")
        if flag == 'yes':
            decrypt('data_files/sid-token.txt', key)
            with open('data_files/sid-token.txt', mode='r', encoding='utf-8') as id:
                for items in id:
                    sandbox_number = items.split()[2]
            encrypt('data_files/sid-token.txt', key)
            try:
                message = client.messages.create(from_='whatsapp:' + sandbox_number, body=waap_message,
                                                 to='whatsapp:' + RECEIVER)
                print(message)
                the_voice.say_and_print("Message sent successfully!")
            except Exception as e:
                print(e)
                print("Message not send!")
            return
        elif flag == 'no':
            the_voice.say_and_print("Do you wish to \"EDIT\" the message, or \"CANCEL\"")
            while True:
                ch = the_voice.listening()
                try:
                    ch = ch.lower()
                    if "edit" in ch:
                        break
                    elif "cancel" in ch:
                        return
                    else:
                        print("Please say \"EDIT\" or \"CANCEL\"")
                except:
                    print("Sorry, didn't get you please say \"EDIT\" or \"CANCEL\"")
