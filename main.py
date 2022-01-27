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
    label_times.place(x=150, y=450)

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
    mem.write_int(get_pointer_address(module + 0x00130EDC, offsets), value)

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
        offsets = [0x78, 0x3C, 0x0, 0xC, 0x100, 0x0, 0x5DC]
        module = module_from_name(mem.process_handle, name_game).lpBaseOfDll
        value = int(combobox.get())
        mem.write_int(get_pointer_address(module + 0x00131878, offsets), value)
    except Exception:
        mem.write_int(get_pointer_address(module + 0x00131878, offsets), 123456789)

def hack_life(name_game, combobox):
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
        offsets = [0x114, 0xC, 0x48, 0x0, 0x5C, 0x118, 0x608]
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
window.wm_attributes("-alpha", 0.7)
window.wm_attributes("-topmost", "True")
window.wm_attributes("-toolwindow", "True")
window.configure(background="#000000")

value = IntVar()
scale_value = Scale(window, variable=value, to=10000)
scale_value.set(1000)
scale_value.config(background="#AAAAAA", foreground="black")
scale_value.place(x=50, y=50, relheight=0.7)

button_hack = Button(window, text="|         Hack         |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_money("iBomberDefensePacific.exe", scale_value))
button_hack.place(x=150, y=100)

button_hack = Button(window, text="|         Auto         |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_money_auto("iBomberDefensePacific.exe", scale_value))
button_hack.place(x=150, y=150)

value_select_score = IntVar()
myFont = Font(family="Times New Roman", size=13)
combobox_select_score = Combobox(window, textvariable=value_select_score, width=8)
combobox_select_score['values'] = (1000, 100000, 10000000, 1000000000)
combobox_select_score.set(1000)
combobox_select_score.configure(font=myFont)
combobox_select_score.place(x=150, y=250)

button_hack = Button(window, text="|         Score        |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_score("iBomberDefensePacific.exe", combobox_select_score))
button_hack.place(x=150, y=300)


value_select_life = IntVar()
myFont = Font(family="Times New Roman", size=13)
combobox_select_life = Combobox(window, textvariable=value_select_life, width=8)
combobox_select_life['values'] = (1000, 100000, 10000000, 1000000000)
combobox_select_life.set(1000)
combobox_select_life.configure(font=myFont)
combobox_select_life.place(x=150, y=350)

button_hack = Button(window, text="|         Life            |", background="#AAAAAA", foreground="black")
button_hack.config(command=lambda: hack_life("iBomberDefensePacific.exe", combobox_select_life))
button_hack.place(x=150, y=400)

button_exit = Button(window, text="|          Exit           |", background="#FFFFFF", foreground="black")
button_exit.config(command=kill_process)
button_exit.place(x=150, y=500)

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