# Basic Keylogger


Tracks user's keystrokes, saves keystrokes into text file, then periodically sends text file from designated email to target emails.

## Tools Used


- Imports pynput library to allow keyboard input operation
- Utilizes smptd module to send emails via simple Mail Transfer Protocol server

## Important Details
- Variable `email_password` must be a Google App Password to allow program to access sender email
- Target emails do not require authorization
- In generated text file, Caps Lock is assumed to be initially unactivated





