# from pynput import keyboard
# from readsettingsfile import Keyswitch, FileRead
# from logic import Movement
# import time


# Key = keyboard.Key


# print(FileRead().ReadStr('LOOKINGFORKEYS'))



# import tkinter as tk

# def update_label():
#     label.config(text="Nowa treść etykiety")

# def start_thread():
#     # Symulacja wątku
#     import threading
#     thread = threading.Thread(target=update_label)
#     thread.start()

# root = tk.Tk()
# label = tk.Label(root, text="Początkowa treść etykiety")
# label.pack()

# button = tk.Button(root, text="Uruchom wątek", command=start_thread)
# button.pack()

# root.mainloop()

# import tkinter as tk
# import tkinter.simpledialog

# def get_user_input():
#     result = tkinter.simpledialog.askstring("Input", "Podaj coś:")
#     if result is not None:
#         print("Wprowadzono:", result)
#     else:
#         print("Anulowano")

# root = tk.Tk()
# button = tk.Button(root, text="Pobierz dane od użytkownika", command=get_user_input)
# button.pack()
# root.mainloop()

print('x \u2208 \u2115+')


# print(type(Key))
# print(Keyswitch().Delate_L_R(Key.alt_l))

# activeKeys = set()
# def on_key_press(key):
#     if(not type(key) == keyboard.KeyCode):
#         match key:
#             case Key.shift_l | Key.shift_r:
#                 activeKeys.add(Key.shift)
#             case Key.ctrl_l | Key.ctrl_r:
#                 activeKeys.add(Key.ctrl)
#             case Key.alt_l | Key.alt_r:
#                 activeKeys.add(Key.alt)
#             case Key.cmd_l | Key.cmd_r:
#                 activeKeys.add(keyboard.KeyCode.from_char(Key.cmd))
#             case _:
#                 activeKeys.add(keyboard.KeyCode.from_char(key))
#     else:
#         activeKeys.add(key)
#     print(f'{key}, {type(key)}, {key.name} - {activeKeys}')
        
# def on_key_release(key):
#     if(not type(key) == keyboard.KeyCode):
#         match key:
#             case Key.shift_l | Key.shift_r:
#                 activeKeys.discard(Key.shift)
#             case Key.ctrl_l | Key.ctrl_r:
#                 activeKeys.discard(keyboard.KeyCode.from_char(Key.ctrl))
#             case Key.alt_l | Key.alt_r:
#                 activeKeys.discard(keyboard.KeyCode.from_char(Key.alt))
#             case Key.cmd_l | Key.cmd_r:
#                 activeKeys.discard(keyboard.KeyCode.from_char(Key.cmd))
#             case _:
#                 activeKeys.discard(keyboard.KeyCode.from_char(key))
#     else:
#         activeKeys.discard(key)

# listener = keyboard.Listener(
#     on_press=on_key_press, 
#     on_release=on_key_release)

# listener.start()
# # while(True):
#     # keyboard.Controller().press(keyboard.KeyCode.from_char('a'))
#     # Movement().KeyboardPress()
#     # time.sleep(1)
# listener.join()


#Write
# def Write(LOOKINGFORKEYS: set):

#     Keys = str()

#     for i in LOOKINGFORKEYS:
#         match i.char:
#             case '\x11':
#                 Keys += 'q'
#             case '\x17':
#                 Keys += 'w'
#             case '\x05':
#                 Keys += 'e'
#             case '\x12':
#                 Keys += 'r'
#             case '\x14':
#                 Keys += 't' 
#             case '\x19':
#                 Keys += 'y'
#             case '\x15':
#                 Keys += 'u'
#             case '\t':
#                 Keys += 'i'
#             case '\x0f':
#                 Keys += 'o'
#             case '\x10':
#                 Keys += 'p'
#             case '\x1b':
#                 Keys += '['
#             case '\x1d':
#                 Keys += ']'
#             case '\x01':
#                 Keys += 'a'
#             case '\x13':
#                 Keys += 's'
#             case '\x04':
#                 Keys += 'd'
#             case '\x06':
#                 Keys += 'f'
#             case '\x07':
#                 Keys += 'g'
#             case '\x08':
#                 Keys += 'h'
#             case '\n':
#                 Keys += 'j'
#             case '\x0b':
#                 Keys += 'k'
#             case '\x0c':
#                 Keys += 'l'
#             case '\x1d':
#                 Keys += ';'
#             case '\x1a':
#                 Keys += 'z' 
#             case '\x18':
#                 Keys += 'x' 
#             case '\x03':
#                 Keys += 'c'
#             case '\x16':
#                 Keys += 'v'
#             case '\x02':
#                 Keys += 'b'
#             case '\x0e':
#                 Keys += 'n'
#             case '\r':
#                 Keys += 'm'
#             case '\x1f':
#                 Keys += '-'
#             case '\x1c':
#                     Keys += "\\"
#             case None:
#                 match i.vk:
#                     case 48:
#                         Keys += '0'
#                     case 49:
#                         Keys += '1'
#                     case 50:
#                         Keys += '2'
#                     case 51:
#                         Keys += '3'
#                     case 52:
#                         Keys += '4'
#                     case 53:
#                         Keys += '5'
#                     case 54:
#                         Keys += '6'
#                     case 55:
#                         Keys += '7'
#                     case 56:
#                         Keys += '8'
#                     case 57:
#                         Keys += '9'
#                     case 187:
#                         Keys += '+'
#                     case 188:
#                         Keys += ','
#                     case 190:
#                         Keys += '.'
#                     case 191:
#                         Keys += '/'
#                     case 192:
#                         Keys += '`'
#                     case 222:
#                         Keys += "\'"
#                     case _:
#                         Keys += 'Error'
#             case _:
#                 Keys += i.char
#         Keys += '+'

#     Keys = Keys[:-1]
#     Keys = Keys.replace('Key.', '')

#     with open('test.txt', 'w') as f:
#         f.write(f'LOOKINGFORKEYS = {Keys}')
#         f.close()

# #read
# def Read() -> set:
#     LOOKINGFORKEYS = str()

#     with open('test.txt', 'r') as f:
#         for line in f:
#             name, value = line.strip().split(' = ')
#             LOOKINGFORKEYS = value
#             # if(hasattr(self, name)):
#             #     setattr(self, name, value)
#             # else:
#             #     print(f'There is no variable named: {name}')
        
#     LOOKINGFORKEYS.lower()
#     answear = set()

#     if len(LOOKINGFORKEYS) == 0:
#         answear.add(Key.space)

#     if not LOOKINGFORKEYS.rfind('+++') == -1:
#         if LOOKINGFORKEYS.rfind('ctrl') == -1:
#             answear.add(keyboard.KeyCode.from_char('+'))
#         else:
#             answear.add(keyboard.KeyCode.from_vk(187))
#         LOOKINGFORKEYS = LOOKINGFORKEYS.replace('+++', '+')

#     if not LOOKINGFORKEYS.rfind('++') == -1:
#         if LOOKINGFORKEYS.startswith('++') or LOOKINGFORKEYS.endswith('++'):
#             if LOOKINGFORKEYS.rfind('ctrl') == -1:
#                 answear.add(keyboard.KeyCode.from_char('+'))
#             else:
#                 answear.add(keyboard.KeyCode.from_vk(187))
#             LOOKINGFORKEYS = LOOKINGFORKEYS.replace('++', '')

#     if LOOKINGFORKEYS == '+':
#         answear.add(Key.space)
#         return answear

#     ks = Keyswitch()

#     ctrl = False
#     if not LOOKINGFORKEYS.rfind('ctrl') == -1:
#         ctrl = True
#     while(len(LOOKINGFORKEYS)):
#         x = LOOKINGFORKEYS.rpartition('+')
#         answear.add(ks.Str2Key(x[2], ctrl))

#         if len(x[0]) == 0 and x[1] == '+':
#             answear.add(Key.space)
#         LOOKINGFORKEYS = LOOKINGFORKEYS[:-1-len(x[2])]

#     return answear


# # Write({keyboard.KeyCode.from_char(Key.ctrl), keyboard.KeyCode.from_char('w')})

# for x in Read():
#     print(f'{x} {type(x)}')

# def handle_hotkey():
#     print("Skrót Ctrl + F7 został spełniony!")

# # Definiujemy sekwencję klawiszy, którą chcemy monitorować
# hotkey_sequence = "<ctrl>+<f7>"

# # Tworzymy obiekt HotKey, który reprezentuje nasz skrót
# hotkey = keyboard.HotKey(keyboard.HotKey.parse(hotkey_sequence), handle_hotkey)

# # Rozpoczynamy nasłuchiwanie na nasz skrót
# hotkey.start()

# # Oczekujemy na zakończenie programu (możesz dodać dowolny kod tutaj)
# keyboard.wait("esc")

# # Zatrzymujemy nasłuchiwanie po zakończeniu programu
# hotkey.stop()

# Parsowanie przycisku funkcyjnego F7
# hotkey_str = "<f7>"
# hotkey = keyboard.HotKey.parse(hotkey_str)

# # Teraz możesz użyć obiektu hotkey do obsługi skrótu klawiszowego
# def on_hotkey_pressed():
#     print("Przycisk funkcyjny F7 został naciśnięty!")

# hotkey.register(on_hotkey_pressed)

# # Rozpoczęcie nasłuchiwania na skrót klawiszowy
# with keyboard.Listener() as listener:
#     listener.join()


# print(keyboard.HotKey.parse('<f7>'))


# def on_activate():
#     print('Global hotkey activated!')

# def for_canonical(f):
#     return lambda k: f(l.canonical(k))

# hotkey = keyboard.HotKey(
#     keyboard.HotKey.parse('<ctrl>+<alt>+h'),
#     on_activate)
# with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release),
#         suppress=True) as l:
#     l.join()


# try:
#     x = int(input("Podaj liczbę: "))
#     result = 10 / x
#     print(f"Wynik dzielenia: {result}")
# except ZeroDivisionError:
#     print("Błąd: Dzielenie przez zero.")
#     # # Alternatywne działanie lub obsługa błędu
#     # result = None
#     # # Możesz kontynuować program dalej
#     # print(f"Wynik: {result}")
# except ValueError:
#     print("Błąd: To nie jest liczba całkowita.")
#     # Alternatywne działanie lub obsługa błędu
#     # result = None
#     # # Możesz kontynuować program dalej
#     # print(f"Wynik: {result}")
# print('dalej')

# try:
#     x = int(input("Podaj liczbę: "))
#     result = 10 / x
#     print(f"Wynik dzielenia: {result}")
# except ZeroDivisionError:
#     print("Błąd: Dzielenie przez zero.")
#     # Nie obsługujemy błędu, więc program zostanie zatrzymany natychmiast
# except ValueError:
#     print("Błąd: To nie jest liczba całkowita.")
#     # Nie obsługujemy błędu, więc program zostanie zatrzymany natychmiast
# print('dalej')

# from settings import COLORS

# def checkcolorchange():
#     COLORS['BG0'] = 'red'
#     print(f"Done BG0 is now {COLORS['BG0']}")

# MOUSEMODE = (1, 0)
# line = 'MOUSEMODE = (0, 3)'

# name, value = line.strip().split(' = ')
                
# MOUSEMODE = value


# try:
#     MOUSEMODE = MOUSEMODE.replace('(', '')
#     MOUSEMODE = MOUSEMODE.replace(',', '')
#     MOUSEMODE = MOUSEMODE.replace(' ', '')
#     MOUSEMODE = MOUSEMODE.replace(')', '')
#     MOUSEMODE = list(MOUSEMODE)
#     MOUSEMODE[0] = int(MOUSEMODE[0])
#     MOUSEMODE[1] = int(MOUSEMODE[1])
#     MOUSEMODE = tuple(MOUSEMODE)
# except ValueError:
#     print('While changing Variable MOUSEMODE occured unexpected error, setting to (1, 0)')
#     MOUSEMODE = (1, 0)
# if MOUSEMODE[0] not in [0, 1]:
#     print('First part of variable MOUSEMODE is nighter 0 nor 1, setting to 1')
#     MOUSEMODE[0] = 1   
# if MOUSEMODE[1] not in [0, 1, 2, 3]:
#     print('First part of variable MOUSEMODE is nighter 0 nor 1, 2, 3, setting to 0')
#     MOUSEMODE[1] = 0


# print(f'Type: {type(MOUSEMODE)} = ({MOUSEMODE[0]} type: {type(MOUSEMODE[0])}, {MOUSEMODE[1]} type: {type(MOUSEMODE[1])})')

# lista = ['ananas', 'bambola voodo', 'szymon', 'IL MIMO', 'test']

# print(lista)


# import threading, time

# def checkloop():
#     while(True):
#         print('a')
#         time.sleep(0.1)

# t = threading.Thread(target=checkloop)
# t.start()

# while(True):
#     print('b')
#     time.sleep(0.1)



"""
TIMES = 1         
TIME = 10          
TIMECOOLDOWN = 100 
FPS = 60         
RANGE = 100        
RANDOMNESS = 100   
MOUSEMODE = (1, 0)  
CLICKNUMBER = 1    
COOLDOWN = 10      
KEYS = ['w', 's', 'a', 'd']
RESETTIME = 20
RESETTIMERAND = 10
KEYBOARDIF = 0
"""



# import tkinter as tk # Python 3
# root = tk.Tk()
# # The image must be stored to Tk or it will be garbage collected.
# root.image = tk.PhotoImage(file='Img/keyboard.png')
# label = tk.Label(root, image=root.image, bg='white')
# root.overrideredirect(True)
# root.geometry("+250+250")
# root.lift()
# # root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop()



# class KlasaNadrzedna:
#     def __init__(self):
#         self.zmienna = 1

# class KlasaPodklasa(KlasaNadrzedna):
#     def zmien_zmienna(self, nowa_wartosc):
#         self.zmienna = nowa_wartosc

# # Tworzenie instancji klasy KlasaPodklasa
# inst_podklasa = KlasaPodklasa()
# print(inst_podklasa.zmienna)  # Wyświetli: 1

# # Zmiana zmiennej w instancji KlasaPodklasa
# inst_podklasa.zmien_zmienna(99)
# print(inst_podklasa.zmienna)  # Wyświetli: 99

# # Tworzenie nowej instancji klasy KlasaNadrzedna
# inst_nadrzedna = KlasaNadrzedna()
# print(inst_nadrzedna.zmienna)  # Wyświetli: 1 (nie została zmieniona)


# x = 'test'
# vars()[x] = 12
# print(test) 


# class sample(object):
#     def __init__(self):
#         vars(self)['a'] = 10

# s = sample()
# print(s.a)