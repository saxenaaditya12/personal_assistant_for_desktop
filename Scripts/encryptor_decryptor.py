from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("data_files/key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("data_files/key.key", "rb").read()

def encrypt(filename, key):
    with open(filename, mode='r', encoding='utf-8') as t:
        flag = 0
        for items in t:
            if ' ' in items:
                flag = 1
                break
    if flag == 1:
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

def decrypt(filename, key):
    with open(filename, mode='r', encoding='utf-8') as t:
        flag = 0
        for items in t:
            if ' ' not in items:
                flag = 1
                break
    if flag == 1:
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)

def safe_key_generator():
    flag = 0
    with open('data_files/key.key', mode='r', encoding='utf-8') as k:
        data = k.read()
    if len(data) > 0:
        # all the file which is using encryptor(here all the txt files) needs to add here as follows >>>>>>>
        key = load_key()
        # try:
        decrypt('data_files/mycontacts.txt', key)
        decrypt('data_files/phone_book.txt', key)
        decrypt('data_files/sender.txt', key)
        decrypt('data_files/sid-token.txt', key)
        # decrypt('api.txt', key)
        flag = 1
        # except Exception as e:
        #     print(e,"\n** key changed probably and database is lost **\n Use Backup Database")
        #     quit()
    else:
        print("** key lost WARNING **")
        print("If any of your file was encrypted you lost the data along with the key :(\n** kindly use backup **")
        flag = 0
    if flag == 1:
        write_key()  # make sure no file is left encrypted before this point
        # now encrypting all the file with new key

        key = load_key()
        encrypt('data_files/mycontacts.txt', key)
        encrypt('data_files/phone_book.txt', key)
        encrypt('data_files/sender.txt', key)
        encrypt('data_files/sid-token.txt', key)
        # encrypt('api.txt', key)


key = load_key()
# decrypt('data_files/sid-token.txt', key)
# decrypt("data_files/mycontacts.txt", key)
decrypt('data_files/sender.txt', key)
# decrypt('data_files/phone_book.txt', key)

# encrypt('data_files/mycontacts.txt', key)
# encrypt('data_files/phone_book.txt', key)
# encrypt('data_files/sender.txt', key)
# encrypt('data_files/sid-token.txt', key)