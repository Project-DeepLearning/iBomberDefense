import tkinter
from tkinter import *
from pymem import Pymem
from pymem.process import *
from subprocess import Popen
from tkinter.font import Font
from tkinter.ttk import Combobox
import time, threading, os, win32api


def now_times(window):
    myFont = Font(family="Times New Roman", size=12)
    label_times = Label(window, background="red", foreground="black")
    label_times.configure(font=myFont)
    time_string = time.strftime('%H:%M:%S')
    label_times.place(x=150, y=480)

    def auto_time(window, label):
        try:
            while True:
                time_string = time.strftime('%H:%M:%S')
                label.config(text=f"|    {time_string}    |")
                label.update()
                time.sleep(1)
        except RuntimeError:
            kill_process()

    thread_auto_time = threading.Thread(target=auto_time, args=(window, label_times,))
    thread_auto_time.start()


def hack_money(name_game, scale):
    global locked
    locked = False
    mem = Pymem(name_game)
    win32api.Beep(1000, 100)

    def get_pointer_address(base, offsets):
        try:
            address = mem.read_int(base)
            for offset in offsets:
                if offset != offsets[-1]:
                    address = mem.read_int(address + offset)
            address = address + offsets[-1]
            return address
        except Exception:
            kill_process()

    offsets = [0x78, 0x84, 0x100, 0x100, 0xFC, 0x0, 0x5D8]
    module = module_from_name(mem.process_handle, name_game).lpBaseOfDll
    value = scale.get()
    mem.write_int(get_pointer_address(module + 0x00130EDC, offsets), value)


def hack_money_auto(name_game, scale):
    mem = Pymem(name_game)
    win32api.Beep(1000, 100)

    def get_pointer_address(base, offsets):
        try:
            address = mem.read_int(base)
            for offset in offsets:
                if offset != offsets[-1]:
                    address = mem.read_int(address + offset)
            address = address + offsets[-1]
            return address
        except Exception:
            kill_process()

    offsets = [0x78, 0x84, 0x100, 0x100, 0xFC, 0x0, 0x5D8]
    module = module_from_name(mem.process_handle, name_game).lpBaseOfDll
    value = 99999

    def auto(module, offsets, value):
        global locked
        locked = True
        while locked:
            mem.write_int(get_pointer_address(module + 0x00130EDC, offsets), value)

    thread_auto = threading.Thread(target=auto, args=(module, offsets, value,))
    thread_auto.start()


def hack_score(name_game, combobox):
    global module, offsets
    mem = Pymem(name_game)
    win32api.Beep(1000, 100)

    def get_pointer_address(base, offsets):
        try:
            address = mem.read_int(base)
            for offset in offsets:
                if offset != offsets[-1]:
                    address = mem.read_int(address + offset)
            address = address + offsets[-1]
            return address
        except Exception:
            kill_process()
    try:
        offsets = [0xC, 0x40, 0x32C, 0x118, 0x2C, 0x0, 0x5DC]
        module = module_from_name(mem.process_handle, name_game).lpBaseOfDll
        value = int(combobox.get())
        mem.write_int(get_pointer_address(module + 0x001307AC, offsets), value)
    except Exception:
        mem.write_int(get_pointer_address(module + 0x001307AC, offsets), 123456789)


def kill_process():
    win32api.Beep(1000, 100)
    win32api.Beep(1000, 100)
    win32api.Beep(1000, 100)
    os._exit(0)


window = tkinter.Tk()

window.geometry("320x720+150+150")
window.title("")
window.overrideredirect(False)
window.wm_attributes("-alpha", 0.8)
window.wm_attributes("-topmost", "True")
window.wm_attributes("-toolwindow", "True")
window.configure(background="#000000")

value = IntVar()
scale_value = Scale(window, variable=value, to=10000)
scale_value.set(2000)
scale_value.config(background="#AAAAAA", foreground="black")
scale_value.place(x=50, y=50, relheight=0.7)

button_hack = Button(window, text="|         Hack         |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_money("iBomberDefensePacific.exe", scale_value))
button_hack.place(x=150, y=100)

button_hack = Button(window, text="|         Auto         |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_money_auto("iBomberDefensePacific.exe", scale_value))
button_hack.place(x=150, y=150)

value_select = IntVar()
myFont = Font(family="Times New Roman", size=13)
combobox_select = Combobox(window, textvariable=value_select, width=8)
combobox_select['values'] = (1000, 100000, 10000000, 1000000000)
combobox_select.set(1000)
combobox_select.configure(font=myFont)
combobox_select.place(x=150, y=250)

button_hack = Button(window, text="|         Score        |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_score("iBomberDefensePacific.exe", combobox_select))
button_hack.place(x=150, y=300)

button_exit = Button(window, text="|          Exit           |", background="#FFFFFF", foreground="black")
button_exit.config(command=kill_process)
button_exit.place(x=150, y=400)

label_show = Label(window, text="|    Hack iBomber Defense Pacific    |")
label_show.config(background="red", foreground="black")
label_show.place(x=65, y=600)

label_show = Label(window, text="|                  Crack by Duke                 |")
label_show.config(background="red", foreground="black")
label_show.place(x=65, y=630)
now_times(window)

try:
    window.mainloop()
except KeyboardInterrupt:
    kill_process()
