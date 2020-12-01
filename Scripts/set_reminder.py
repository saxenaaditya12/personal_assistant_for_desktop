import time
import winsound


def task(text, a):
    try:
        total_breaks = 3
        break_count = 0
        print("\n🙄 wait 🙄")
        time.sleep(a)
        while break_count < total_breaks:
            time.sleep(2)
            dur = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, dur)
            print("\n", text)
            freq += 100
            dur += 50
            break_count = break_count + 1

    except Exception as e:
        print(e)
        print("* Error in Setting Up Reminder *")
