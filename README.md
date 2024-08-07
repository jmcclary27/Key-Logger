For educational purposes only.

# Basic Keylogger


Tracks user's keystrokes, saves keystrokes into text file, then periodically sends text file from designated email to target emails.

## Tools Used


- Imports pynput library to allow keyboard input operation
- Utilizes smptd module to send emails via simple Mail Transfer Protocol server
- Navigates operating system pathways using os import

## Building Process


- Initializes self as instance of Key Logger object, assumes caps lock is intially false
- 'if __name__ == __main__' begins running code
- Variable `current` tracks time since program has started
- keyPressed function checks if 3600 seconds have passed after a key is pressed and sends key logs to target emails accordingly
- New `current` variable is created after text file is sent, resetting counter for 3600 seconds to pass
- Try-except statement catches common keys that cannot be logged using pynput

## Important Details


- Program only checks how much time has elapsed after a key is pressed; if there is no activty for an hour, no text file will be sent
- Email that is sending keyfile must have two-step authentification activated
- Variable `email_password` must be the personalized sixteen-digit passcode Google provides when two step authentification is live
- Target emails do not require authorization
- Timer that automatically sends email can be changed but must be done cautiously as lag occurs when timer is shorter




