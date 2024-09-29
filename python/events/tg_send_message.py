import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''
directory_to_watch = '.'

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        print(f"New file created: {file_path}")

        time.sleep(1)

        try:
            with open(file_path, 'rb') as file:
                files = {'photo': (os.path.basename(file_path), file, 'image/jpg')}
                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto?chat_id={TELEGRAM_CHAT_ID}"
                response = requests.post(url, files=files)

                if response.ok:
                    print("Photo sent successfully!")
                else:
                    print(f"Failed to send photo. Telegram API response: {response.text}")

        except Exception as e:
            print(f"Error processing file: {e}")

if __name__ == '__main__':
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=True)

    print(f"Watching directory: {directory_to_watch}")

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()