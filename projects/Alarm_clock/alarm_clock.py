from tkinter import *
import datetime
import time
import sys
from threading import Thread

# Conditionally import winsound
if sys.platform == "win32":
    import winsound
else:
    winsound = None

def alarm_logic(set_alarm_time, play_sound_function):
    """Alarm logic separated from GUI code."""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            if play_sound_function:
                play_sound_function("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)

def create_gui():
    root = Tk()
    root.geometry("400x200")

    hour = StringVar(root)
    minute = StringVar(root)
    second = StringVar(root)

    def start_alarm_thread():
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        play_sound_function = winsound.PlaySound if winsound else None
        alarm_thread = Thread(target=alarm_logic, args=(set_alarm_time, play_sound_function))
        alarm_thread.start()

    Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
    Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

    frame = Frame(root)
    frame.pack()

    OptionMenu(frame, hour, *[f'{i:02}' for i in range(24)]).pack(side=LEFT)
    OptionMenu(frame, minute, *[f'{i:02}' for i in range(60)]).pack(side=LEFT)
    OptionMenu(frame, second, *[f'{i:02}' for i in range(60)]).pack(side=LEFT)

    Button(root, text="Set Alarm", font=("Helvetica 15"), command=start_alarm_thread).pack(pady=20)

    return root, hour, minute, second

if __name__ == "__main__":
    root, _, _, _ = create_gui()
    root.mainloop()
