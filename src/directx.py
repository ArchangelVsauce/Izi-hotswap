import time
import keyboard
import customtkinter

from pydirectinput import (
    keyDown,
    keyUp,
    leftClick,
    move,
    moveTo,
    mouseUp,
    mouseDown,
    RIGHT,
    press,
)  
from loguru import logger

def press_and_hold_key(key: str, seconds: float):
    logger.debug(f'press key "{key}" {seconds} seconds')

    keyDown(key)
    time.sleep(seconds)
    keyUp(key)

def hotswap(): #end on izi, 6 shots max - no ammo # takes 6.25 seconds to run 36, 37.5 total
        

        keyDown("r")
        time.sleep(1.1)
        keyUp("r")

        press("3")
        mouseDown(button=RIGHT)
        time.sleep(0.5)
        leftClick()
        time.sleep(0.18)

        press("1")
        time.sleep(0.8)
        leftClick()
        mouseUp(button=RIGHT)

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x250")

def stop():
       exit()

def playback2():
        time.sleep(5)
        hotswap()
        hotswap()
        hotswap()
        hotswap()
        hotswap()
        hotswap()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Izi Cocket Swap")
label.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Start", command=playback2)
button1.pack(pady=16, padx=12)

button2 = customtkinter.CTkButton(master=frame, text="End", command=stop)
button2.pack(pady=16, padx=12)

root.mainloop()