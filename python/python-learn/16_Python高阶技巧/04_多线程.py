import threading
import time

def sing():
    while True:
        print("我在唱歌，啦啦啦...")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞，哔哔哔哔哔")
        time.sleep(1)

sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)
sing_thread.start()
dance_thread.start()
