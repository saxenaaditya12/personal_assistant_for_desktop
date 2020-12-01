import the_voice
import requests

# import json
# import encryptor_decryptor
#
# def decrypt(filename, key):
#     encryptor_decryptor.decrypt(filename, key)
#
# def encrypt(filename, key):
#     encryptor_decryptor.encrypt(filename, key)
# def print(a):
#     import sys, time, playsound
#     # w = wave.open("e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3", "r")
#     for i in a:
#         sys.stdout.write(i)
#         sys.stdout.flush()
#
#         # playsound.playsound('s4.mp3', True)
#         time.sleep(0.02)
#     sys.stdout.write('\n')
# encryptor_decryptor.safe_key_generator()
# key = encryptor_decryptor.load_key()
# decrypt('api.txt', key)
# with open('api.txt', mode='r', encoding='utf-8') as f:
#     for items in f:
flag = 1
try:
    api_key = 'f27d414ff043465cfa57c77e880eef1e'
# api_key = "Your_API_Key"
except Exception as e:
    print(e)
    print("Check your api key")
    flag = 0
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather():
    global flag
    if flag == 0:
        print("Check your api key")
        return
    while 1:
        the_voice.say_and_print("Tell city name")
        while True:
            city_name = the_voice.listening()
            try:
                city_name = city_name.lower()
                if city_name == "cancel":
                    return
                break
            except:
                print("Please tell the city name or \"CANCEL\" to cancel")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            the_voice.say_and_print("Here is the report")
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            the_voice.say_and_print(" Temperature (in celsius) = " +
                                    str(current_temperature - 273) +
                                    "\n atmospheric pressure (in hPa unit) = " +
                                    str(current_pressure) +
                                    "\n humidity (in percentage) = " +
                                    str(current_humidiy) +
                                    "\n description = " +
                                    str(weather_description))
            print("\n")
            while 1:
                print('Another city?(yes/no): ')
                the_voice.say('Another city? yes or no')
                while True:
                    flag = the_voice.listening()
                    try:
                        flag = flag.lower()
                        break
                    except:
                        print("Please say that again...")
                if flag == 'no':
                    return
                elif flag == 'yes':
                    break
                else:
                    print("wrong choice try again")
                    the_voice.say("wrong choice try again")
        else:
            print(" City Not Found ")
            the_voice.say("city not found")
