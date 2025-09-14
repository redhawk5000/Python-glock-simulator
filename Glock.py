import os
import time
import keyboard

count = 17  # starting ammo

def shoot():
    global count
    if count > 0:
        print(f"Fa Ammo: {count}")
        count -= 1
        time.sleep(0.1)
    else:
        print("Out of ammo! Press 'r' to reload.")

def reload():
    global count
    count = 17
    print("Reloading...")
    time.sleep(2)
    print("Reloaded!")

def clear_terminal():
    if os.name == 'nt':  
        _ = os.system('cls')

# Main loop
print("Press SPACE to shoot, R to reload. Press Q to quit.")
while True:
    if keyboard.is_pressed("space"):  # shoot when spacebar pressed
        shoot()
        time.sleep(0.2)  # prevent spam
    elif keyboard.is_pressed("r"):  # reload when R pressed
        reload()
    elif keyboard.is_pressed("q"):  # quit game
        clear_terminal()
        print("Are you sure you want to quit Y/N")
    elif keyboard.is_pressed("y"):
        print("Quiting...")
        time.sleep(2)
        clear_terminal()
        break
    elif keyboard.is_pressed("n"):
        print("Restarting Game...")
        time.sleep(2)
        clear_terminal
        print("Press SPACE to shoot, R to reload. Press Q to quit.")

        continue
