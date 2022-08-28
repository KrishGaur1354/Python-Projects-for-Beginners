import time
from plyer import notification

if __name__== "__main__":
    while True:
        notification.notify(
            title = "WELCOME!!" ,
            message = "This is Krish's PC" ,
            timeout = 10
         )
        time.sleep(3600)
