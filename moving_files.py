from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

folder_to_track = '/Users/moonmoonbird/Documents/moonmoonbird/1'
folder_destination = '/Users/moonmoonbird/Documents/moonmoonbird/2'

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "new_name_" + str(self.i) + '.txt'
        for filename in os.listdir(folder_to_track):
            file_exist = os.path.isfile(folder_destination + '/' +new_name)
            while file_exist:
                self.i += 1
                new_name = "new_name_" + str(self.i) + '.txt'
                file_exist = os.path.isfile(folder_destination + '/' + new_name)
            src = folder_to_track + '/' + filename
            dest = folder_destination + '/' + new_name
            os.rename(src, dest)

handler = MyHandler()
observer = Observer()
observer.schedule(handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
        print('1111')
except KeyboardInterrupt:
    observer.stop()
print(2222)
observer.join()