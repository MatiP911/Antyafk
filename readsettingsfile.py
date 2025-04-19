import tkinter as tk
from tkinter.filedialog import askopenfilename
from pynput import keyboard
from typing import Union
from settings import Variables

Key = keyboard.Key

PATH = 'variables.txt'

#Reads From File
class FileRead():
    def __init__(self):
        v = Variables()
        
        #inicialize
        self.TIMES = v.Deafult('TIMES')                          #ilość ruchów >=0
        self.TIME = v.Deafult('TIME')                            #czas jednej iterakcji w ms >0
        self.TIMECOOLDOWN = v.Deafult('TIMECOOLDOWN')            #czas pomiędzy interkacjami w ms >0
        self.RESETTIME = v.Deafult('RESETTIME')                  #czas resetowania interakcji s>0
        self.RESETTIMERAND = v.Deafult('RESETTIMERAND')          #losowość resetowania interakcji s >=0
        self.FPS = v.Deafult('FPS')                              #fps-y interkacji >0
        self.RANGE = v.Deafult('RANGE')                          #odległość ruchu należy do N
        self.RANDOMNESS = v.Deafult('RANDOMNESS')                #losowość ruchu >0
        self.MOUSEMODE = v.Deafult('MOUSEMODE')                  #(ruch,przycisk) (0-nic 1-ruch, 0-nic 1-LMB 2-RMB 3-BMB)
        self.CLICKNUMBER = v.Deafult('CLICKNUMBER')              #ilość kliknięć należy do N
        self.COOLDOWN = v.Deafult('COOLDOWN')                    #czas pomiędzy odpaleniami iterakcji w s >0
        self.KEYBOARDIF = v.Deafult('KEYBOARDIF')                #czy włączać klawiature
        self.KEYS = v.Deafult('KEYS')                            #przyciski z szansą naciśnięcia podczas włączonej klawiatury
        self.INITIALCOOLDOWN = v.Deafult('INITIALCOOLDOWN')      #cooldown po uruchomieniu skryptu w s>0
        self.LOOKINGFORKEYS = v.Deafult('LOOKINGFORKEYS')        #przycisk ON/OFF

        #read
        self.Read()
        self.VarChangeCheck()

    def Read(self):
        try: 
            with open(PATH, 'r') as file:
                for line in file:
                    if not line.strip().rfind(' = ') == -1:
                        name, value = line.strip().split(' = ')
                        
                        if(hasattr(self, name)):
                            setattr(self, name, value)
                        else:
                            print(f'There is no variable named: {name}')
                    else:
                        print('There was error while reading from file, make sure that all \'=\' are surrounded with singular spaces')
        except FileNotFoundError:
            print('File not found.')

    def VarChangeCheck(self):
        v = Variables()

        #TIMES
        try:
            self.TIMES = int(self.TIMES)
        except ValueError:
            print(f'Variable TIMES is not int, setting to {v.Deafult("TIMES")}')
            self.TIME = v.Deafult("TIMES")
        if self.TIMES < 0:
            print(f'Variable TIMES < 0, setting to {v.Deafult("TIMES")}')
            self.TIME = v.Deafult("TIMES")

        #TIME
        try:
            self.TIME = int(self.TIME)
        except ValueError:
            print(f'Variable TIME is not int, setting to {v.Deafult("TIME")}')
            self.TIME = v.Deafult("TIME")
        if self.TIME <= 0:
            print(f'Variable TIME <= 0, setting to {v.Deafult("TIME")}')
            self.TIME = v.Deafult("TIME")

        #TIMECOOLDOWN
        try:
            self.TIMECOOLDOWN = int(self.TIMECOOLDOWN)
        except ValueError:
            print(f'Variable TIMECOOLDOWN is not int, setting to {v.Deafult("TIMECOOLDOWN")}')
            self.TIMECOOLDOWN = v.Deafult("TIMECOOLDOWN")
        if self.TIMECOOLDOWN <= 0:
            print(f'Variable TIMECOOLDOWN <= 0, setting to {v.Deafult("TIMECOOLDOWN")}')
            self.TIMECOOLDOWN = v.Deafult("TIMECOOLDOWN")

        #FPS
        try:
            self.FPS = int(self.FPS)
        except ValueError:
            print(f'Variable FPS is not int, setting to {v.Deafult("FPS")}')
            self.FPS = v.Deafult("FPS")
        if self.FPS <= 0:
            print(f'Variable FPS <= 0, setting to {v.Deafult("FPS")}')
            self.FPS = v.Deafult("FPS")

        #RANGE
        try:
            self.RANGE = int(self.RANGE)
        except ValueError:
            print(f'Variable RANGE is not int, setting to {v.Deafult("RANGE")}')
            self.RANGE = v.Deafult("RANGE")
        if self.RANGE <= 0:
            print(f'Variable RANGE <= 0, setting to {v.Deafult("RANGE")}')
            self.RANGE = v.Deafult("RANGE")

        #RANDOMNESS
        try:
            self.RANDOMNESS =  int(self.RANDOMNESS)
        except ValueError:
            print(f'Variable RANDOMNESS is not int, setting to {v.Deafult("RANDOMNESS")}')
            self.RANDOMNESS = v.Deafult("RANDOMNESS")
        if self.RANDOMNESS < 0:
            print(f'Variable RANDOMNESS < 0, setting to {v.Deafult("RANDOMNESS")}')
            self.RANDOMNESS = v.Deafult("RANDOMNESS")

        #MOUSEMODE
        try:
            if(type(self.MOUSEMODE) == str):
                self.MOUSEMODE = self.MOUSEMODE.replace('(', '')
                self.MOUSEMODE = self.MOUSEMODE.replace(',', '')
                self.MOUSEMODE = self.MOUSEMODE.replace(' ', '')
                self.MOUSEMODE = self.MOUSEMODE.replace(')', '')
                self.MOUSEMODE = list(self.MOUSEMODE)
                self.MOUSEMODE[0] = int(self.MOUSEMODE[0])
                self.MOUSEMODE[1] = int(self.MOUSEMODE[1])
                if self.MOUSEMODE[0] not in [0, 1]:
                    print(f'First part of variable MOUSEMODE is nighter 0 nor 1, setting to {v.Deafult("MOUSEMODE")[0]}')
                    self.MOUSEMODE[0] = v.Deafult("MOUSEMODE")[0]   
                if self.MOUSEMODE[1] not in [0, 1, 2, 3]:
                    print(f'First part of variable MOUSEMODE is nighter 0 nor 1, 2, 3, setting to {v.Deafult("MOUSEMODE")[1]}')
                    self.MOUSEMODE[1] = v.Deafult("MOUSEMODE")[1]
            self.MOUSEMODE = tuple(self.MOUSEMODE)
        except ValueError:
            print(f'While changing Variable MOUSEMODE occured unexpected error, setting to {v.Deafult("MOUSEMODE")}')
            self.MOUSEMODE = v.Deafult("MOUSEMODE")

        #CLICKNUMBER
        try:
            if(type(self.CLICKNUMBER) == str):
                if '.' in self.CLICKNUMBER:
                    self.CLICKNUMBER =  float(self.CLICKNUMBER)
                else:
                    self.CLICKNUMBER =  int(self.CLICKNUMBER)
        except ValueError:
            print(f'Variable CLICKNUMBER is not int, setting to {v.Deafult("CLICKNUMBER")}')
            self.CLICKNUMBER = v.Deafult("CLICKNUMBER")
        if self.CLICKNUMBER < 0:
            print(f'Variable CLICKNUMBER < 0, setting to {v.Deafult("CLICKNUMBER")}')
            self.CLICKNUMBER = v.Deafult("CLICKNUMBER")

        #COOLDOWN
        try:
            if(type(self.COOLDOWN) == str):
                if '.' in self.COOLDOWN:
                    self.COOLDOWN =  float(self.COOLDOWN)
                else:
                    self.COOLDOWN =  int(self.COOLDOWN)
        except ValueError:
            print(f'Variable COOLDOWN is nighter int nor float, setting to {v.Deafult("COOLDOWN")}')
            self.COOLDOWN = v.Deafult("COOLDOWN")
        if self.COOLDOWN <= 0:
            print(f'Variable COOLDOWN < 0, setting to {v.Deafult("COOLDOWN")}')
            self.COOLDOWN = v.Deafult("COOLDOWN")

        #KEYBOARDIF
        try:
            self.KEYBOARDIF =  int(self.KEYBOARDIF)
        except ValueError:
            print(f'Variable KEYBOARDIF is not int, setting to {v.Deafult("KEYBOARDIF")}')
            self.KEYBOARDIF = v.Deafult("KEYBOARDIF")
        if not self.KEYBOARDIF in [0, 1]:
            print(f'Variable KEYBOARDIF is nighter 0 nor 1, setting to {v.Deafult("KEYBOARDIF")}')
            self.KEYBOARDIF = v.Deafult("KEYBOARDIF")

        #RESETTIME = 20     
        try:
            self.RESETTIME =  int(self.RESETTIME)
        except ValueError:
            print('Variable RESETTIME is not int, setting to {v.Deafult("RESETTIME")}')
            self.RESETTIME = v.Deafult("RESETTIME")
        if self.RESETTIME <= 0:
            print('Variable RESETTIME is <= 0, setting to {v.Deafult("RESETTIME")}')
            self.RESETTIME = v.Deafult("RESETTIME")

        #RESETTIMERAND 
        try:
            self.RESETTIMERAND =  int(self.RESETTIMERAND)
        except ValueError:
            print(f'Variable RESETTIMERAND is not int, setting to {v.Deafult("RESETTIMERAND")}')
            self.RESETTIMERAND = v.Deafult("RESETTIMERAND")
        if self.RESETTIMERAND < 0:
            print(f'Variable RESETTIMERAND is < 0, setting to {v.Deafult("RESETTIMERAND")}')
            self.RESETTIMERAND = v.Deafult("RESETTIMERAND")
        if self.RESETTIMERAND > self.RESETTIME:
            print('Variable RESETTIMERAND is > RESETTIME, setting to 0')
            self.RESETTIMERAND = 0

        #INITIALCOOLDOWN
        try:
            self.INITIALCOOLDOWN = int(self.INITIALCOOLDOWN)
        except ValueError:
            print(f'Variable INITIALCOOLDOWN is not int, setting to {v.Deafult("INITIALCOOLDOWN")}')
            self.INITIALCOOLDOWN = v.Deafult("INITIALCOOLDOWN")
        if self.INITIALCOOLDOWN < 0:
            print(f'Variable INITIALCOOLDOWN < 0, setting to {v.Deafult("INITIALCOOLDOWN")}')
            self.INITIALCOOLDOWN = v.Deafult("INITIALCOOLDOWN")

        #KEYS
        try:
            if type(self.KEYS) == str:
                self.KEYS = self.SpecialVarCheck(str(self.KEYS))
        except ValueError:
            print(f'Variable KEYS is declared wrongly, using {v.Deafult("KEYS")} instead')
            self.KEYS = self.SpecialVarCheck(v.Deafult("KEYS"))
        
        #LOOKINGFORKEYS
        try:
            if type(self.LOOKINGFORKEYS) == str:
                self.LOOKINGFORKEYS = self.SpecialVarCheck(str(self.LOOKINGFORKEYS))
        except ValueError:
            print(f'Variable LOOKINGFORKEYS is declared wrongly, using {v.Deafult("LOOKINGFORKEYS")} instead')
            self.LOOKINGFORKEYS = self.SpecialVarCheck(v.Deafult("LOOKINGFORKEYS"))

    def SpecialVarCheck(self, var: str) -> set:
        var.lower()
        answear = set()
        ks = Keyswitch()

        if len(var) == 0:
            answear.add(Key.space)

        if not var.rfind('+++') == -1:
            if var.rfind('ctrl') == -1:
                answear.add(keyboard.KeyCode.from_char('+'))
            else:
                answear.add(keyboard.KeyCode.from_vk(187))
            var = var.replace('+++', '+')

        if not var.rfind('++') == -1:
            if var.startswith('++') or var.endswith('++'):
                if var.rfind('ctrl') == -1:
                    answear.add(keyboard.KeyCode.from_char('+'))
                else:
                    answear.add(keyboard.KeyCode.from_vk(187))
                var = var.replace('++', '')

        if var == '+':
            answear.add(Key.space)
            return answear

        ctrl = False
        if not var.rfind('ctrl') == -1:
            ctrl = True
        
        while(len(var)):
            x = var.rpartition('+')
            answear.add(ks.Str2Key(x[2], ctrl))

            if len(x[0]) == 0 and x[1] == '+':
                answear.add(Key.space)
            var = var[:-1-len(x[2])]

        return answear

    def ReadStr(self, name: str) -> Union[str, tuple, int]:
        self.Read()
        self.VarChangeCheck()
        match name:
            case 'TIMES':
                return  self.TIMES
            case 'TIME':
                return self.TIME
            case 'TIMECOOLDOWN':
                return self.TIMECOOLDOWN
            case 'RESETTIME':
                return self.RESETTIME
            case 'RESETTIMERAND':
                return self.RESETTIMERAND
            case 'FPS':
                return self.FPS
            case 'RANGE':
                return self.RANGE
            case 'RANDOMNESS':
                return self.RANDOMNESS
            case 'MOUSEMODE':
                return  self.MOUSEMODE
            case 'CLICKNUMBER':
                return self.CLICKNUMBER
            case 'COOLDOWN':
                return self.COOLDOWN
            case 'KEYBOARDIF':
                return self.KEYBOARDIF
            case 'KEYS':
                return FileWrite().SpecialVarSet2Str(self.KEYS)
            case 'INITIALCOOLDOWN':
                return self.INITIALCOOLDOWN
            case 'LOOKINGFORKEYS':
                return FileWrite().SpecialVarSet2Str(FileRead().LOOKINGFORKEYS)

#Opens Explorer and reads file
class FileWindow():
    def __init__(self):
        self.SettingsFilePatch = tk.StringVar()
        tk.Tk().withdraw()
        self.SettingsFilePatch = askopenfilename()

    def GetPatch(self):
        return self.SettingsFilePatch

#Saving settings
class FileWrite(FileRead):
    def __init__(self):
        super().__init__()

    def Write(self, **kwargs) -> None:
        super().__init__()

        self.MOUSE0 = self.MOUSEMODE[0]
        self.MOUSE1 = self.MOUSEMODE[1]

        #save kwargs
        for key, value in kwargs.items():
            if(hasattr(self, key)):
                    setattr(self, key, value)
                    
                        
            self.VarChangeCheck()

        #writing
        try:
            with open(PATH, 'w') as file:
                file.write(f'TIMES = {str(self.TIMES)} \n')
                file.write(f'TIME = {str(self.TIME)} \n')
                file.write(f'TIMECOOLDOWN = {str(self.TIMECOOLDOWN)} \n')
                file.write(f'RESETTIME = {str(self.RESETTIME)} \n')  
                file.write(f'RESETTIMERAND = {str(self.RESETTIMERAND)} \n')
                file.write(f'FPS = {str(self.FPS)} \n')     
                file.write(f'RANGE = {str(self.RANGE)} \n')  
                file.write(f'RANDOMNESS = {str(self.RANDOMNESS)} \n')
                file.write(f'MOUSEMODE = ({str(self.MOUSE0)},{str(self.MOUSE1)}) \n')
                file.write(f'CLICKNUMBER = {str(self.CLICKNUMBER)} \n')
                file.write(f'COOLDOWN = {str(self.COOLDOWN)} \n')
                file.write(f'KEYBOARDIF = {str(self.KEYBOARDIF)} \n')  
                file.write(f'KEYS = {self.SpecialVarSet2Str(self.KEYS).lower()} \n')
                file.write(f'LOOKINGFORKEYS = {self.SpecialVarSet2Str(self.LOOKINGFORKEYS).lower()}')
                file.close()
        except FileNotFoundError:
            print('File not found.')

    def SpecialVarSet2Str(self, var:set) -> str:
        Keys = str()
        ks = Keyswitch()
        for i in var:
            Keys += ks.Key2Str(i)
            Keys += '+'

        Keys = Keys[:-1]
        Keys = Keys.upper()
        Keys = Keys.replace('KEY.', '')

        return Keys

    def WriteStr(self, name:str, val) -> None:
        match name:
            case 'TIMES':
                self.Write(TIMES = val)
            case 'TIME':
                self.Write(TIME = val)
            case 'TIMECOOLDOWN':
                self.Write(TIMECOOLDOWN = val)
            case 'RESETTIME':
                self.Write(RESETTIME = val)
            case 'RESETTIMERAND':
                self.Write(RESETTIMERAND = val)
            case 'FPS':
                self.Write(FPS = val)
            case 'RANGE':
                self.Write(RANGE = val)
            case 'RANDOMNESS':
                self.Write(RANDOMNESS = val)
            case 'MOUSEMODE':
                self.Write(MOUSEMODE = val)
            case 'CLICKNUMBER':
                self.Write(CLICKNUMBER = val)
            case 'COOLDOWN':
                self.Write(COOLDOWN = val)
            case 'KEYBOARDIF':
                self.Write(KEYBOARDIF = val)
            case 'KEYS':
                self.Write(KEYS = val)
            case 'INITIALCOOLDOWN':
                self.Write(INITIALCOOLDOWN = val)
            case 'LOOKINGFORKEYS':
                self.Write(LOOKINGFORKEYS = val)
            
#Keyswitch
class Keyswitch():
    def __init__(self) -> None:
        pass
    
    def Key2Str(self, i: Union[keyboard.KeyCode, Key]) -> str:
        #Switches KeyCode and Key to Str
        if type(i) == Key:
            return i.name
        match i.char:
            case '\x11':
                return 'q'
            case '\x17':
                return 'w'
            case '\x05':
                return 'e'
            case '\x12':
                return 'r'
            case '\x14':
                return 't' 
            case '\x19':
                return 'y'
            case '\x15':
                return 'u'
            case '\t':
                return 'i'
            case '\x0f':
                return 'o'
            case '\x10':
                return 'p'
            case '\x1b':
                return '['
            case '\x1d':
                return ']'
            case '\x01':
                return 'a'
            case '\x13':
                return 's'
            case '\x04':
                return 'd'
            case '\x06':
                return 'f'
            case '\x07':
                return 'g'
            case '\x08':
                return 'h'
            case '\n':
                return 'j'
            case '\x0b':
                return 'k'
            case '\x0c':
                return 'l'
            case '\x1d':
                return ';'
            case '\x1a':
                return 'z' 
            case '\x18':
                return 'x' 
            case '\x03':
                return 'c'
            case '\x16':
                return 'v'
            case '\x02':
                return 'b'
            case '\x0e':
                return 'n'
            case '\r':
                return 'm'
            case '\x1f':
                return '-'
            case '\x1c':
                    return "\\"
            case None:
                match i.vk:
                    case 48:
                        return '0'
                    case 49:
                        return '1'
                    case 50:
                        return '2'
                    case 51:
                        return '3'
                    case 52:
                        return '4'
                    case 53:
                        return '5'
                    case 54:
                        return '6'
                    case 55:
                        return '7'
                    case 56:
                        return '8'
                    case 57:
                        return '9'
                    case 187:
                        return '+'
                    case 188:
                        return ','
                    case 190:
                        return '.'
                    case 191:
                        return '/'
                    case 192:
                        return '`'
                    case 222:
                        return "\'"
                    case _:
                        return 'Error'
            case _:
                return i.char

    def Str2Key(self, i: str, ctrl: bool) -> Union[keyboard.KeyCode, Key]:
        match i:
            case 'shift':
                return Key.shift
            case 'ctrl':
                return Key.ctrl
            case 'alt':
                return Key.alt
            case 'cmd':
                return Key.cmd
            case '' | ' ':
                return Key.space
            case 'tab':
                return Key.tab
            case 'tab':
                return Key.tab
            case 'up':
                return Key.up
            case 'down':
                return Key.down
            case 'left':
                return Key.left
            case 'right':
                return Key.right
            case 'tab':
                return Key.tab
            case 'scroll_lock':
                return Key.scroll_lock
            case 'print_screen':
                return Key.print_screen
            case 'pause':
                return Key.pause
            case 'page_up':
                return Key.page_up
            case 'page_down':
                return Key.page_down
            case 'num_lock':
                return Key.num_lock
            case 'menu':
                return Key.menu
            case 'media_volume_up':
                return Key.media_volume_up
            case 'media_volume_mute':
                return Key.media_volume_mute
            case 'media_volume_down':
                return Key.media_volume_down
            case 'media_previous':
                return Key.media_previous
            case 'media_play_pause':
                return Key.media_play_pause
            case 'media_next':
                return Key.media_next
            case 'insert':
                return Key.insert
            case 'home':
                return Key.home
            case 'f1':
                return Key.f1
            case 'f2':
                return Key.f2
            case 'f3':
                return Key.f3
            case 'f4':
                return Key.f4
            case 'f5':
                return Key.f5
            case 'f6':
                return Key.f6
            case 'f7':
                return Key.f7
            case 'f8':
                return Key.f8
            case 'f9':
                return Key.f9
            case 'f10':
                return Key.f10
            case 'f11':
                return Key.f11
            case 'f12':
                return Key.f12
            case 'f13':
                return Key.f13
            case 'f14':
                return Key.f14
            case 'f15':
                return Key.f15
            case 'f16':
                return Key.f16
            case 'f17':
                return Key.f17
            case 'f18':
                return Key.f18
            case 'f19':
                return Key.f19
            case 'f20':
                return Key.f20
            case 'esc':
                return Key.esc
            case 'enter':
                return Key.enter
            case 'end':
                return Key.end
            case 'delete':
                return Key.delete
            case 'caps_lock':
                return Key.caps_lock
            case 'backspace':
                return Key.backspace
            case 'q':
                return keyboard.KeyCode.from_char('\x11')
            case 'w':
                return keyboard.KeyCode.from_char('\x17')
            case 'e':
                return keyboard.KeyCode.from_char('\x05')
            case 'r':
                return keyboard.KeyCode.from_char('\x12')
            case 't':
                return keyboard.KeyCode.from_char('\x14')
            case 'y':
                return keyboard.KeyCode.from_char('\x19')
            case 'u':
                return keyboard.KeyCode.from_char('\x15')
            case 'i':
                return keyboard.KeyCode.from_char('\t')
            case 'o':
                return keyboard.KeyCode.from_char('\x0f')
            case 'p':
                return keyboard.KeyCode.from_char('\x10')
            case '[':
                return keyboard.KeyCode.from_char('\x1b')
            case ']':
                return keyboard.KeyCode.from_char('\x1d')
            case 'a':
                return keyboard.KeyCode.from_char('\x01')
            case 's':
                return keyboard.KeyCode.from_char('\x13')
            case 'd':
                return keyboard.KeyCode.from_char('\x04')
            case 'f':
                return keyboard.KeyCode.from_char('\x06')
            case 'g':
                return keyboard.KeyCode.from_char('\x07')
            case 'h':
                return keyboard.KeyCode.from_char('\x08')
            case 'j':
                return keyboard.KeyCode.from_char('\n')
            case 'k':
                return keyboard.KeyCode.from_char('\x0b')
            case 'l':
                return keyboard.KeyCode.from_char('\x0c')
            case ';':
                return keyboard.KeyCode.from_char('\x1d')
            case 'z':
                return keyboard.KeyCode.from_char('\x1a') 
            case 'x':
                return keyboard.KeyCode.from_char('\x18') 
            case 'c':
                return keyboard.KeyCode.from_char('\x03')
            case 'v':
                return keyboard.KeyCode.from_char('\x16')
            case 'b':
                return keyboard.KeyCode.from_char('\x02')
            case 'n':
                return keyboard.KeyCode.from_char('\x0e')
            case 'm':
                return keyboard.KeyCode.from_char('\r')
            case '-':
                return keyboard.KeyCode.from_char('\x1f')
            case "\\":
                    return keyboard.KeyCode.from_char('\x1c')
            case '0':
                return keyboard.KeyCode.from_vk(48)
            case '1':
                return keyboard.KeyCode.from_vk(49)
            case '2':
                return keyboard.KeyCode.from_vk(50)
            case '3':
                return keyboard.KeyCode.from_vk(51)
            case '4':
                return keyboard.KeyCode.from_vk(52)
            case '5':
                return keyboard.KeyCode.from_vk(53)
            case '6':
                return keyboard.KeyCode.from_vk(54)
            case '7':
                return keyboard.KeyCode.from_vk(55)
            case '8':
                return keyboard.KeyCode.from_vk(56)
            case '9':
                return keyboard.KeyCode.from_vk(57)
            case ',':
                return keyboard.KeyCode.from_vk(188)
            case '.':
                return keyboard.KeyCode.from_vk(190)
            case '/':
                return keyboard.KeyCode.from_vk(191)
            case '`':
                return keyboard.KeyCode.from_vk(192)
            case "\'":
                return keyboard.KeyCode.from_vk(222)
            case _:
                return keyboard.KeyCode.from_char(i)

    def Delate_L_R(self, i: Key) -> Key:
        match i:
            case Key.shift_l | Key.shift_r:
                return Key.shift
            case Key.ctrl_l | Key.ctrl_r:
                return Key.ctrl
            case Key.alt_l | Key.alt_r:
                return Key.alt
            case Key.cmd_l | Key.cmd_r:
                return Key.cmd
            case _:
                return i

    def SpecialShift(self, i: keyboard.KeyCode) -> keyboard.KeyCode:
        i = self.Key2Str(i)
        i = i.lower()
        return self.Str2Key(i, True)

if __name__ == '__main__':
    # f = FileWrite()
    # f.Write(RANGE = 50)
    print(f'{FileRead().LOOKINGFORKEYS} - {type(FileRead().LOOKINGFORKEYS)}')
    for i in FileRead().LOOKINGFORKEYS:
        print(f'{i} - {type(i)}')
        print(f'{i.name} - {type(i.name)}')
    pass