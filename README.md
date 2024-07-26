This is made for educational purposes only and should not be used with any sort of malicious intent

# Basic Keylogger


Tracks user's keystrokes, saves keystrokes into text file, then periodically sends text file from designated email to target emails.

## Tools Used


- Imports pynput library to allow keyboard input operation
- Utilizes smptd module to send emails via simple Mail Transfer Protocol server
- Navigates operating systems pathways using os import

## Building Process


- The code starts with creating a class called Key Logger, setting up the program to be built with object oriented programming
- We then use the initializer method, defining self and caps to ensure starting with caps lock won't mess up our key strokes
- 'if __name__ = __main__' is used at the bottom of the file to start the code
- A variable, current, is created with the current time, and the keypressed function gets called every time a key is pressed
- After every keystroke, the function checks if 3600 seconds, or one hour, has passed, and if it has, it sends the key logs to your desired email using the smptd module
- It is important to note the code only checks how much time has elapsed after a key is pressed, so if there is no activty for an hour, no text file will be sent
- When the text file is sent, a new 'current' variable is created with the current time, resetting the counter for 3600 seconds to pass
- After a key is pressed, a try except statement is used, since there are certain keys that cannot be logged using pynput
- The except statement logs edge cases that normally cannot be logged with a simple 'key.char' line of code

## Important Details


- The email that is sending the keyfile has to have two step authentification activated
- Variable `email_password` must be the personalized sixteen digit passcode google gives when two step authentification is live
- Target emails do not require authorization
- The counter to send the email can be shortened to less than an hour, but the shorter the counter is, the more likely there is lag the targets computer making the keylogger more likely to be discovered




