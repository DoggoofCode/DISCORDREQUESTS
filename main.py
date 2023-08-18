import requests
import time
import threading

print(
    "  ____ ___ ____  ____   _    __  __  __     ___ \n|  _ \_ _/ ___||  _ \ / \  |  \/  | \ \   / / | \n| | | | |\___ \| |_) / _ \ | |\/| |  \ \ / /| | \n| |_| | | ___) |  __/ ___ \| |  | |   \ V / | |\n|____/___|____/|_| /_/   \_\_|  |_|    \_(_)|_|")


# https://discord.com/api/v9/channels/938037132059082782/messages
def sendmsg(CHANNELID='CHALLENID', MSG="hello my frindky man"):
    start = time.perf_counter()

    payload = {
        "content": MSG
    }

    headers = {
        "Authorization": "ENTER DISCORD TOKEN"
    }

    channelID = CHANNELID

    r = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", data=payload, headers=headers)

    finish = time.perf_counter()
    print(f"Completed in: {round(finish - start, 2)} sec")
    # return f"Completed in: {round(finish - start, 2)} sec"


def threadsing(channelID, message, repetition):
    threads = []

    totalStart = time.perf_counter()

    for _ in range(repetition):
        t = threading.Thread(target=sendmsg, args=[channelID, message])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    totalEND = time.perf_counter()

    print(f"Completed the Script in: {round(totalEND - totalStart, 2)} secs")


playing = True
CHANNELIDENTIFICATION = None
message = None
while playing:
    if CHANNELIDENTIFICATION is None:
        CHANNELIDENTIFICATION = input("Enter the Channel ID: ")
        if CHANNELIDENTIFICATION == '':
            CHANNELIDENTIFICATION = 'Channel id'
    if message is None:
        message = input("Enter the Message: ")
        if message == '':
            message = 'get spammed on!'

    repetition = int(input("How Many Times Do you want to repeat it? : "))

    threadsing(CHANNELIDENTIFICATION, message, repetition)
