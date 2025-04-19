from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import time
import threading

from settings import *
from readsettingsfile import FileRead, FileWrite, FileWindow
from logic import MainLogic

class App(ctk.CTk):
    def __init__(self, title, size):
        
        #window
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        # self.minsize(size[0],size[1])
        self.configure(fg_color= COLORS['BG0'])
        ctk.set_appearance_mode("dark")
        self.iconbitmap(IMAGES['ICON'])

        #Global variables
        global SettingsFilePatch
        SettingsFilePatch = tk.StringVar(value = '/C...')

        #Grid
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1), weight = 2, uniform = 'a')
        #self.rowconfigure(1, weight = 2, uniform = 'a')
        self.rowconfigure(2, weight = 4, uniform = 'a')

        #Wigets
        self.settings = Settings(self)
        self.settings.grid(row = 0, column = 0, sticky = 'nswe')
        
        self.options = Options(self)
        self.options.grid(row = 1, column = 0, sticky = 'nswe')

        self.bottom = Bottom(self)
        self.bottom.grid(row = 2, column = 0, sticky = 'nswe')

        #run
        self.mainloop()

    def ChangeKey(self):
        self.ChangeKeyFrame = ChangeKeyFrame(self)
        self.ChangeKeyFrame.place(anchor = 'nw', relwidth = 1, relheight = 1)
        self.ChangeKeyFrame.lift()

        MainLogic().ChangeKey(self.ChangeKeyFrame.destroy)

#Top segment
class Settings(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color=TOP['BG'])

        #Grid
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 8, uniform = 'a')
        self.columnconfigure(2, weight = 1, uniform = 'a')
        self.columnconfigure(3, weight = 4, uniform = 'a')
        self.columnconfigure(4, weight = 1, uniform = 'a')
        self.columnconfigure(5, weight = 12, uniform = 'a')
        self.columnconfigure(6, weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2), weight = 2, uniform = 'a')

    #Wigets
        #File patch
        self.file_patch = FilePatch(self)
        self.file_patch.grid(row = 1, column = 1, sticky = 'nswe')

        #On/Off Button
        self.on_off_button = OnOffButton(self)
        self.on_off_button.grid(row = 0, column = 3, rowspan = 3)

        #On/Off KeyButton
        self.on_off_keybutton = OnOffKeyButton(self)
        self.on_off_keybutton.grid(row = 1, column = 5, sticky = 'nswe', rowspan = 2)

        #Names
        self.txt1 = StickBottomTxtFrame(self, 'Settings File', TOP['STICKBOTTOMTXTFRAME']['SETTING']['FONT'] , TOP['STICKBOTTOMTXTFRAME']['SETTING']['PADX'])
        self.txt2 = StickBottomTxtFrame(self, 'On/Off Key', TOP['STICKBOTTOMTXTFRAME']['ONOFFKEY']['FONT'], TOP['STICKBOTTOMTXTFRAME']['ONOFFKEY']['PADX'])

        self.txt1.grid(row = 0, column = 1, sticky = 'nswe')
        self.txt2.grid(row = 0, column = 4, columnspan = 3, sticky = 'nswe')

    def ChangeKey(self):
        self.parent.ChangeKey()

class FilePatch(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(fg_color = TOP['FILEPATCH']['BG'], corner_radius = TOP['FILEPATCH']['CORNERRADIUS'])

    #Wigets
        #Patch    
        self.file_patch_entry = ctk.CTkEntry(self)
        self.file_patch_entry.configure(textvariable = SettingsFilePatch,
        text_color = TOP['FILEPATCH']['PATCH']['TXTCOL'],
        font = TOP['FILEPATCH']['PATCH']['FONT'],
        fg_color = TOP['FILEPATCH']['PATCH']['BG'],
        state="normal", ################################################disabled
        border_width = TOP['FILEPATCH']['PATCH']['BORDERWIDTH'])

        self.file_patch_entry.place(relx = 0.04, rely = 0, anchor = 'nw', relwidth = 0.745, relheight = 0.99)

        #Button
        self.fliepatchbutton = ctk.CTkButton(self)
        self.fliepatchbutton.configure(text = '...', 
        command = self.ButtonPress,
        corner_radius = TOP['FILEPATCH']['PATCH']['BUTTON']['CORNERRADIUS'],
        font = TOP['FILEPATCH']['PATCH']['BUTTON']['FONT'],
        fg_color = TOP['FILEPATCH']['PATCH']['BUTTON']['BG'],
        text_color = TOP['FILEPATCH']['PATCH']['BUTTON']['TXTCOL'])
    
        self.fliepatchbutton.place(relx = 0.8, rely = 0.2, anchor = 'nw', relwidth = 0.14, relheight = 0.6)

    def ButtonPress(self):
        self.filewindow = FileWindow()
        SettingsFilePatch.set(self.filewindow.GetPatch())
        print(SettingsFilePatch)

class OnOffButton(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__(parent)
        #IMG
        self.img0 = ctk.CTkImage(dark_image = Image.open(IMAGES['ONOFFBUTTON0']), size = TOP['ONOFFBUTTON']['IMGSIZE'])
        self.img1 = ctk.CTkImage(dark_image = Image.open(IMAGES['ONOFFBUTTON1']), size = TOP['ONOFFBUTTON']['IMGSIZE'])
        

        self.configure(corner_radius = TOP['ONOFFBUTTON']['CORNERRADIUS'], 
                       command = self.ChangeState, 
                    #    image = self.img0, 
                       text = '', 
                    #    fg_color = TOP['ONOFFBUTTON']['OFF']['BG'], 
                    #    hover_color = TOP['ONOFFBUTTON']['OFF']['HOVER'],
                       height = 100)

        self.clsState = MainLogic()
        self.state0 = self.clsState.WhatState() #Last state
        self.SetState()

        #Thred loop
        def CheckLoop():
            while(True):
                state1 = self.clsState.WhatState()
                if not self.state0 == state1:
                    self.state0 = state1
                    self.SetState()
                time.sleep(0.1)

        t1 = threading.Thread(target = CheckLoop)
        t1.start()

    def ChangeState(self):
        self.clsState.ChangeState()
        self.SetState()
    
    def SetState(self):
        state = self.clsState.WhatState()
        if state:
            self.configure(image = self.img1, fg_color = TOP['ONOFFBUTTON']['ON']['BG'], hover_color = TOP['ONOFFBUTTON']['ON']['HOVER'])            
        else:
            self.configure(image = self.img0, fg_color = TOP['ONOFFBUTTON']['OFF']['BG'], hover_color = TOP['ONOFFBUTTON']['OFF']['HOVER'])

class OnOffKeyButton(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(corner_radius = TOP['ONOFFKEY']['CORNERRADIUS'], 
                       command = self.Input, 
                       fg_color = TOP['ONOFFKEY']['BG'], 
                       hover_color = TOP['ONOFFKEY']['HOVER'],
                       font = TOP['ONOFFKEY']['FONT'],
                       text_color = TOP['ONOFFKEY']['TXTCOL'])
        
        MainLogic().INFLoopKeyCheck()

        #Checking if LOOKINGFORKEYS changed
        self.configure(text = FileRead().ReadStr('LOOKINGFORKEYS'))
        def CheckLoop():
            oldtxt = FileRead().ReadStr('LOOKINGFORKEYS')
            while(True):
                newtxt = FileRead().ReadStr('LOOKINGFORKEYS')
                if not oldtxt == newtxt:
                    self.configure(text = newtxt)
                    oldtxt = newtxt
                time.sleep(0.1)

        t2 = threading.Thread(target = CheckLoop)
        t2.start()

    def txt(self):
            self.configure(text = 'test')#FileRead().ReadStr('LOOKINGFORKEYS'))
            
    def Input(self):
        self.parent.ChangeKey()

class ChangeKeyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color = OTHERS['CHANGEKEY']['BG'])

        self.esc()
        self.ClickKey()
        
    def esc(self):
        self.esc = ctk.CTkLabel(self, text = 'Press ESC to leave', font = OTHERS['CHANGEKEY']['FONT0'], text_color = OTHERS['CHANGEKEY']['TXTCOL'])
        self.esc.place(anchor = 'nw', relx=0.01, rely=0)

    def ClickKey(self):
        self.ClickKey = ctk.CTkLabel(self, text = '...Press any button...', font = OTHERS['CHANGEKEY']['FONT1'], text_color = OTHERS['CHANGEKEY']['TXTCOL'])
        self.ClickKey.place(anchor = 'center', relx=0.5, rely=0.45)

class StickBottomTxtFrame(ctk.CTkFrame):
    def __init__(self, parent, txt, font, padx = 0):
        super().__init__(parent)
        self.configure(fg_color = TOP['STICKBOTTOMTXTFRAME']['BG'])

        self.label = ctk.CTkLabel(self, text = txt, font = font, text_color = TOP['STICKBOTTOMTXTFRAME']['TXTCOL'], padx = padx)

        if(padx != 0 ):
            self.label.pack(side = 'bottom', anchor = 'sw')
        else:
            self.label.pack(side = 'bottom')

#Middle segment
class Options(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color = MID['BG'])

        #Grid
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1)

        #Wigets
        self.MouseMove = Option(self, 'MouseMove')
        self.MouseMove.grid(row = 0, column = 0)

        self.MouseButton = Option(self, 'MouseButton')
        self.MouseButton.grid(row = 0, column = 1)

        self.Keyboard = Option(self, 'Keyboard')
        self.Keyboard.grid(row = 0, column = 2)

class Option(ctk.CTkButton):
    def __init__(self, parent, option):
        super().__init__(parent)
        self.Writing = FileWrite()
        self.configure(text = '', corner_radius = MID['OPTION']['CORNERRADIUS'])

        match option:
            case 'MouseMove':
                self.MouseMove()
            case 'MouseButton':
                self.MouseButton()
            case 'Keyboard':
                self.Keyboard()
            case _:
                print('Wrong Option')

    #Mouse Move
    def MouseMove(self):
        self.configure(command = self.MouseMoveClick)

        self.img0 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEMOVE0']), size = MID['OPTION']['IMGSIZE'])
        self.img1 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEMOVE1']), size = MID['OPTION']['IMGSIZE'])
        
        read = FileRead()
        self.WigetState = read.MOUSEMODE[0]
        self.MouseClick()

    def MouseMoveClick(self):
        self.WigetState += 1
        self.WigetState %= 2
        self.MouseClick()
        self.Writing.Write(MOUSE0 = self.WigetState)

    #Mouse button
    def MouseButton(self):
        self.configure(command = self.MouseButtonClick)

        self.img0 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEBUTTON0']), size = MID['OPTION']['IMGSIZE'])
        self.img1 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEBUTTON1']), size = MID['OPTION']['IMGSIZE'])
        self.img2 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEBUTTON2']), size = MID['OPTION']['IMGSIZE'])
        self.img3 = ctk.CTkImage(dark_image = Image.open(IMAGES['MOUSEBUTTON3']), size = MID['OPTION']['IMGSIZE'])
        
        read = FileRead()
        self.WigetState = read.MOUSEMODE[1]
        self.MouseClick()

    def MouseButtonClick(self):
        self.WigetState += 1
        self.WigetState %= 4
        self.MouseClick()
        self.Writing.Write(MOUSE1 = self.WigetState)

    #Keyboard
    def Keyboard(self):
        self.configure(command = self.KeyboardClick)

        self.img0 = ctk.CTkImage(dark_image = Image.open(IMAGES['KEYBOARD0']), size = MID['OPTION']['IMGSIZE'])
        self.img1 = ctk.CTkImage(dark_image = Image.open(IMAGES['KEYBOARD1']), size = MID['OPTION']['IMGSIZE'])
        
        read = FileRead()
        self.WigetState = read.KEYBOARDIF
        self.MouseClick()

    def KeyboardClick(self):
        self.WigetState += 1
        self.WigetState %= 2
        self.MouseClick()
        self.Writing.Write(KEYBOARDIF = self.WigetState)

    def MouseClick(self):

        match self.WigetState:
            case 0:
                self.configure(fg_color = MID['OPTION']['OFF']['BG'], image = self.img0, hover_color = MID['OPTION']['OFF']['HOVER'])
            case 1:
                self.configure(fg_color = MID['OPTION']['ON']['BG'], image = self.img1, hover_color = MID['OPTION']['ON']['HOVER'])
            case 2:
                self.configure(fg_color = MID['OPTION']['ON']['BG'], image = self.img2, hover_color = MID['OPTION']['ON']['HOVER'])
            case 3:
                self.configure(fg_color = MID['OPTION']['ON']['BG'], image = self.img3, hover_color = MID['OPTION']['ON']['HOVER'])

#Bottom segment
class Bottom(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color = BOTTOM['BG'])

        #Grid
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 8, uniform = 'a')
        self.columnconfigure(2, weight = 1, uniform = 'a')
        self.columnconfigure(3, weight = 8, uniform = 'a')
        self.columnconfigure(4, weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')

        #Switchers
        self.Times = Switcher(self, name = 'TIMES')
        self.Time = Switcher(self, name = 'TIME')
        self.TimeCooldown = Switcher(self, name = 'TIMECOOLDOWN')
        self.ResetTime = Switcher(self, name = 'RESETTIME')
        self.ResetTimeRand = Switcher(self, name = 'RESETTIMERAND')
        self.FPS = Switcher(self, name = 'FPS')
        self.Range = Switcher(self, name = 'RANGE')
        self.Randomness = Switcher(self, name = 'RANDOMNESS')
        self.ClickNumber = Switcher(self, name = 'CLICKNUMBER')
        self.Cooldown = Switcher(self, name = 'COOLDOWN')
        self.Keys = Switcher(self, name = 'KEYS')
        self.InicialCooldown = Switcher(self, name = 'INITIALCOOLDOWN')


        def CheckLoop():
            while(True):
                self.Times.ReadVar()
                self.Time.ReadVar()
                self.TimeCooldown.ReadVar()
                self.ResetTime.ReadVar()
                self.ResetTimeRand.ReadVar()
                self.FPS.ReadVar()
                self.Range.ReadVar()
                self.Randomness.ReadVar()
                self.ClickNumber.ReadVar()
                self.Cooldown.ReadVar()
                self.Keys.ReadVar()
                self.InicialCooldown.ReadVar()
                time.sleep(0.1)

        t3 = threading.Thread(target = CheckLoop)
        t3.start()

        self.Times.grid(column = 1, row = 0, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.Time.grid(column = 1, row = 1, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.TimeCooldown.grid(column = 1, row = 2, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.ResetTime.grid(column = 1, row = 3, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.ResetTimeRand.grid(column = 1, row = 4, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.FPS.grid(column = 1, row = 5, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.Range.grid(column = 3, row = 0, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.Randomness.grid(column = 3, row = 1, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.ClickNumber.grid(column = 3, row = 2, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.Cooldown.grid(column = 3, row = 3, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.Keys.grid(column = 3, row = 4, sticky = 'nswe', pady = BOTTOM['PADY'])
        self.InicialCooldown.grid(column = 3, row = 5, sticky = 'nswe', pady = BOTTOM['PADY'])

class Switcher(ctk.CTkFrame):
    def __init__(self, parent, name: str) -> None:
        super().__init__(parent)
        self.v = Variables()
        self.r = FileRead()
        self.w = FileWrite()

        self.name = name

        self.configure(fg_color = BOTTOM['SWITCHER']['BG'])
        #Grid
        self.columnconfigure(0, weight = 8, uniform = 'a')
        self.columnconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(2, weight = 8, uniform = 'a')
        self.rowconfigure(0, weight = 1)

        #wigets
        self.Label = ctk.CTkLabel(self, text = name.title(), 
                                  fg_color = BOTTOM['SWITCHER']['LABEL']['BG'],
                                  text_color = BOTTOM['SWITCHER']['LABEL']['TXTCOL'],
                                  corner_radius = BOTTOM['SWITCHER']['LABEL']['CORNERRADIUS'])

        self.Button = ctk.CTkButton(self, 
                                    fg_color = BOTTOM['SWITCHER']['BUTTON']['BG'],
                                    hover_color = BOTTOM['SWITCHER']['BUTTON']['HOVER'],
                                    text_color = BOTTOM['SWITCHER']['BUTTON']['TXTCOL'],
                                    corner_radius = BOTTOM['SWITCHER']['BUTTON']['CORNERRADIUS'],
                                    command = self.Input)
        
        self.ReadVar()
        
        self.Label.grid(row = 0, column = 0, sticky = 'nswe')
        self.Button.grid(row = 0, column = 2, sticky = 'nswe')

    def Input(self) -> None:
        self.dialog = ctk.CTkInputDialog(
                                        text = f'{self.v.Explanations(self.name)}\n{self.v.Requirements(self.name)}', 
                                        fg_color = BOTTOM['SWITCHER']['DIALOGBOX']['BG'],
                                        button_fg_color = BOTTOM['SWITCHER']['DIALOGBOX']['BUTTON']['BG'],
                                        button_hover_color = BOTTOM['SWITCHER']['DIALOGBOX']['BUTTON']['HOVER'],
                                        button_text_color = BOTTOM['SWITCHER']['DIALOGBOX']['BUTTON']['TXT'],
                                        entry_fg_color = BOTTOM['SWITCHER']['DIALOGBOX']['ENTRY']['BG'],
                                        entry_border_color = BOTTOM['SWITCHER']['DIALOGBOX']['ENTRY']['BORDER'],
                                        entry_text_color = BOTTOM['SWITCHER']['DIALOGBOX']['ENTRY']['TXT'],
                                        title = self.name)
        
        #Checking if pressed Cancel, if so do nothing
        ans = self.dialog.get_input()
        if not ans == None:
            self.w.WriteStr(self.name, ans)

    def ReadVar(self) -> None:
        self.Button.configure(text = self.r.ReadStr(self.name))
        time.sleep(0.1)

#Startups
App(TITLE, SIZE)