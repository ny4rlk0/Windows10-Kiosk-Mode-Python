#!/usr/bin/python
#https://github.com/ny4rlk0/Windows10-Kiosk-Mode-Python/
#Run as administrator!
#Wtf is this and why did i write this? lol.
#Ara ara? I remember now. I wanted a transparent screen lock.
#Wait this does not look like it does that.
#Well F*** it. It should do similiar thing to Kiosk mode (Lockdown mode for windows.) for python. 
#ESC= Disable input + Enter Kiosk mode
#TAB= Enable input + Exit Kiosk mode
#Altho i said kiosk mode it still lets user shut down computer after CTRL+ALT+DEL But user cant do anything except that as long as it runs.
#It also hides options in CTRL+ALT+DEL Security Attention Sequence. (Which turn back to normal when you press TAB.)
#Still couldn't figure it out a way to block SAS completely. (Probably it has something to do with Gina.dll)
#Wait do i want to do that tho?
from ctypes import *;import time;from pynput import keyboard;import sys;
from pynput.keyboard import Key;import keyboard as kk;
from threading import Thread as core;import subprocess as sp
runonce=True
lockdown=False
ny4='rlk0'
###RegeditValues###
rega='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f'
rega1='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /f'
rega2='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies" /f'
rega3='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f'
rega4='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "SoftwareSASGeneration" /t REG_DWORD /d 0 /f'
rega5='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /t REG_DWORD /d 1 /f'
rega6='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableLockWorkStation" /t REG_DWORD /d 1 /f'
rega7='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "NoLogoff" /t REG_DWORD /d 1 /f'
rega8='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableChangePassword" /t REG_DWORD /d 1 /f'
rega9='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "HideFastUserSwitching" /t REG_DWORD /d 1 /f'
rega10='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableCAD" /t REG_DWORD /d 1 /f'
rega11='reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout" /v "Scancode Map" /t REG_BINARY /d 0000000000000000030000004de01de04be01d0000000000 /f'
regd='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "SoftwareSASGeneration" /t REG_DWORD /d 0 /f'
regd1='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /t REG_DWORD /d 0 /f'
regd2='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableLockWorkStation" /t REG_DWORD /d 0 /f'
regd3='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v "NoLogoff" /t REG_DWORD /d 0 /f'
regd4='reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableChangePassword" /t REG_DWORD /d 0 /f'
regd5='reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "HideFastUserSwitching" /t REG_DWORD /d 0 /f'
regd6='reg delete "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies" /f'
regd7='reg delete "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout" /v "Scancode Map" /f'
regd8='reg delete "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout" /v "SoftwareSASGeneration" /f'
regListEnable=[rega,rega1,rega2,rega3,rega4,rega5,rega6,rega7,rega8,rega9,rega10,rega11]
regListDisable=[regd,regd1,regd2,regd3,regd4,regd5,regd6,regd7,regd8]
###RegeditValues###
combo={keyboard.Key.ctrl_l,keyboard.Key.alt_l,keyboard.Key.delete}
combo1={keyboard.Key.ctrl_r,keyboard.Key.alt_l,keyboard.Key.delete}
combo2={keyboard.Key.ctrl_l,keyboard.Key.alt_r,keyboard.Key.delete}
combo3={keyboard.Key.ctrl_l,keyboard.Key.alt_gr,keyboard.Key.delete}
combo4={keyboard.Key.ctrl_r,keyboard.Key.alt_gr,keyboard.Key.delete}
combo5={keyboard.Key.ctrl_l,keyboard.Key.shift_l,keyboard.Key.esc}
combo6={keyboard.Key.ctrl_r,keyboard.Key.shift_l,keyboard.Key.esc}
combo7={keyboard.Key.ctrl_r,keyboard.Key.shift_r,keyboard.Key.esc}
current=set()
def blockInput(Value):
    if Value==True and lockdown==True:
        windll.user32.BlockInput(True)
    elif lockdown==False:windll.user32.BlockInput(False)
def disableTaskManager(Value):
    n=sp.DEVNULL
    if Value==True:
        for r in regListEnable:
            try:sp.Popen(r,stdout=n,stderr=n,stdin=n)
            except Exception as e:print(e);continue
    elif Value==False:
        for r in regListDisable:
            try:sp.Popen(r,stdout=n,stderr=n,stdin=n)
            except Exception as e:print(e);continue
def on_press(key):
    global lockdown
    if key==keyboard.Key.tab:lockdown=False;disableTaskManager(False)
    if key==keyboard.Key.esc:lockdown=True;disableTaskManager(True)
    if key in combo or key in combo1 or key in combo2 or key in combo3 or key in combo4 or key in combo5 or key in combo6 or key in combo7 and key not in current:
        current.add(key)
        if all (k in current for k in combo) or all (k in current for k in combo2) or all (k in current for k in combo3) or all (k in current for k in combo4) or all (k in current for k in combo5) or all (k in current for k in combo6) or all (k in current for k in combo7):
            print('Dangerious Key Combo Detected!')
            time.sleep(0.1)
            kk.press_and_release('Enter')
            kk.press_and_release('Enter')
def on_release(key):
    try:
        if key in current:current.remove(key);print("Removed "+str(key)+".")
    except:pass
def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
while True:
    if runonce:
        runonce=False
        a=core(target=listen);a.daemon=True;a.start()
    blockInput(True)
    time.sleep(0.2)
