'''
pip install pypiwin32

https://gist.github.com/mdavey/6d40a89dbc15aefcc8cd
https://msdn.microsoft.com/en-us/library/dd375731.aspx?f=255&MSPPError=-2147217396
https://www.programcreek.com/python/index/475/win32con
https://www.programcreek.com/python/example/82679/win32con.KEYEVENTF_KEYUP
'''
#
# After a post to c.l.py by Richie Hindle:
# http://groups.google.com/groups?th=80e876b88fabf6c9
#
import os
import pyautogui

import ctypes
from ctypes import wintypes
import win32con
from functools import reduce
import Hotkeys_intro

class MdHotkey():
    def __init__(self, id, keys, lambda_action):
        self.id = id
        self.keys = keys
        self.lambda_action = lambda_action
        

### Introduction ###
intro = Hotkeys_intro.hotkeys_introduction()
print(intro)

byref = ctypes.byref
user32 = ctypes.windll.user32

items = [MdHotkey(1 , (ord('G'), win32con.MOD_CONTROL, win32con.MOD_WIN) ,lambda :os.system('start chrome "https://mail.google.com/mail/u/0/#inbox" ')),
        MdHotkey(2 , (ord('Y'), win32con.MOD_CONTROL, win32con.MOD_WIN) ,lambda :os.system('start chrome "https://www.youtube.com" ')),
        MdHotkey(3 , (ord('A'), win32con.MOD_CONTROL, win32con.MOD_WIN) ,lambda :os.system('start chrome "https://www.atpworldtour.com" ')),
        MdHotkey(4 , (ord('W'), win32con.MOD_CONTROL, win32con.MOD_WIN) ,lambda :os.system('start chrome "https://www.fifa.com/worldcup/" ')),
        MdHotkey(5 , (ord('T'), win32con.MOD_CONTROL, win32con.MOD_WIN) ,lambda :os.system('start chrome "http://www.wimbledon.com/index.html" ')),

        MdHotkey(21 ,  (ord('N'), win32con.MOD_ALT) ,lambda :os.startfile(r"C:\Program Files\Notepad++\notepad++.exe")),
        MdHotkey(22 ,  (ord('S'), win32con.MOD_ALT) ,lambda :os.startfile(r'SnippingTool.exe')),
        MdHotkey(23 ,  (ord('K'), win32con.MOD_ALT) ,lambda :os.startfile(r'C:\Users\evan9\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KMPlayer.lnk')),
        MdHotkey(24 ,  (ord('P'), win32con.MOD_ALT) ,lambda :os.startfile(r'C:\Users\evan9\AppData\Local\Programs\Python\Python36\Scripts\spyder3.exe')),
        MdHotkey(25 ,  (ord('J'), win32con.MOD_ALT) ,lambda :os.startfile(r"C:\PyCodes\To_Compile\dist\Open_Jupyter_Notebook\Open_Jupyter_Notebook.exe")),

        MdHotkey(41 ,  (ord('P'), win32con.MOD_ALT, win32con.MOD_WIN) ,lambda :os.startfile(r'C:\PyCodes')),
        MdHotkey(42 ,  (ord('L'), win32con.MOD_ALT, win32con.MOD_WIN) ,lambda :os.startfile(r'C:\Users\evan9\Downloads')),
        MdHotkey(43 ,  (ord('E'), win32con.MOD_ALT, win32con.MOD_WIN) ,lambda :os.startfile(r'C:\Evan')),
        MdHotkey(44 ,  (ord('I'), win32con.MOD_ALT, win32con.MOD_WIN) ,lambda :os.startfile(r'C:\Musics')),
        
        MdHotkey(61 ,  (win32con.VK_LEFT, win32con.MOD_CONTROL) ,lambda :pyautogui.hotkey('ctrl', 'z' ,pause=0)),
        MdHotkey(62 ,  (win32con.VK_RIGHT, win32con.MOD_CONTROL) ,lambda :pyautogui.hotkey('ctrl', 'v' ,pause=0)),
        MdHotkey(63 ,  (win32con.VK_UP, win32con.MOD_CONTROL) ,lambda :pyautogui.hotkey('ctrl', 'x' ,pause=0)),
        MdHotkey(64 ,  (win32con.VK_DOWN, win32con.MOD_CONTROL) ,lambda :pyautogui.hotkey('ctrl', 'c' ,pause=0)),
        MdHotkey(65 ,  (ord('1'), win32con.MOD_ALT) ,lambda :pyautogui.press('f11')),    #F11
        MdHotkey(66 ,  (ord('2'), win32con.MOD_ALT) ,lambda :pyautogui.press('f12')),    #F12
        MdHotkey(67 ,  (ord('8'), win32con.MOD_ALT) ,lambda :pyautogui.press('f8')),     #F8
        MdHotkey(68 ,  (ord('9'), win32con.MOD_ALT) ,lambda :pyautogui.press('f9')),     #F9
        MdHotkey(69 ,  (ord('0'), win32con.MOD_ALT) ,lambda :pyautogui.press('f10')),    #F10
        
       
        MdHotkey(999 , (win32con.VK_F4, win32con.MOD_WIN), lambda : user32.PostQuitMessage(0))]
   
HOTKEYS,HOTKEY_ACTIONS = {} , {}
for e in items:    
    HOTKEYS[e.id] = e.keys
    HOTKEY_ACTIONS[e.id] = e.lambda_action

#
# RegisterHotKey takes:
#  Window handle for WM_HOTKEY messages (None = this thread)
#  arbitrary id unique within the thread
#  modifiers (MOD_SHIFT, MOD_ALT, MOD_CONTROL, MOD_WIN)
#  VK code (either ord ('x') or one of win32con.VK_*)
#
#for id, (vk, modifiers) in HOTKEYS.items ():
#  print( "Registering id", id, "for key", vk)
#  if not user32.RegisterHotKey (None, id, modifiers, vk):
#    print("Unable to register id", id)
for id, values in HOTKEYS.items ():
    vk, modifiers = values[0], reduce (lambda x, y: x | y, values[1:])
    print ("Registering id", id, "for key", vk)
    if not user32.RegisterHotKey (None, id, modifiers, vk):
        print ("Unable to register id", id)
#
# Home-grown Windows message loop: does
#  just enough to handle the WM_HOTKEY
#  messages and pass everything else along.
#
try:
    msg = wintypes.MSG ()
    while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
        if action_to_take:
            action_to_take ()
        user32.TranslateMessage (byref (msg))
        user32.DispatchMessageA (byref (msg))
finally:
    for id in HOTKEYS.keys ():
        user32.UnregisterHotKey (None, id)



