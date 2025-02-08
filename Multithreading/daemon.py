import threading
import time

def background_task():
    while True:
        time.sleep(1)
        print("Background task runnibg...")

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

time.sleep(3)
print("Main Thread is Dead.")
