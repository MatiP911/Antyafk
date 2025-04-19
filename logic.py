from pynput import mouse, keyboard
import random
import time
from readsettingsfile import FileRead, FileWrite
import threading
from readsettingsfile import Keyswitch

# from screeninfo import get_monitors

Mouse = mouse.Controller()
ButtonMouse = mouse.Button

Key = keyboard.Key

# variables
STATE = False
ACTIVELOOP = False
ACTIVECHANGER = False


class Movement(FileRead):
    def __init__(self):
        super().__init__()
        self.KEYS = list(self.KEYS)

    def Loop(self):
        super().__init__()
        for _ in range(self.TIMES):
            self.randomMouse()
            self.KeyboardPress()

    def randomMouse(self):
        if (self.MOUSEMODE[0] == 1):
            randx = random.randint(1, self.RANDOMNESS)
            randy = random.randint(1, self.RANDOMNESS)

            xsign = random.choice([1, -1])
            ysign = random.choice([1, -1])

            steps_x = (self.RANGE*xsign + randx*xsign)/self.FPS
            steps_y = (self.RANGE*ysign + randy*ysign)/self.FPS

            for __ in range(self.FPS):
                Mouse.move(steps_x, steps_y)
                time.sleep(self.TIME / self.FPS / 1000)

        if (self.MOUSEMODE[1] == 1):
            Mouse.click(ButtonMouse.left, self.CLICKNUMBER)
        if (self.MOUSEMODE[1] == 2):
            Mouse.click(ButtonMouse.right, self.CLICKNUMBER)
        if (self.MOUSEMODE[1] == 3):
            for __ in range(self.CLICKNUMBER):
                Mouse.press(ButtonMouse.left)
                Mouse.press(ButtonMouse.right)
                Mouse.release(ButtonMouse.left)
                Mouse.release(ButtonMouse.right)
        time.sleep(self.TIMECOOLDOWN / 1000)

    def KeyboardPress(self):
        ks = Keyswitch()
        if self.KEYBOARDIF:
            self.button = random.choice(self.KEYS)
            if type(self.button) == keyboard.KeyCode:
                keyboard.Controller().press(ks.Key2Str(self.button))
                time.sleep(self.TIME/1000)
                keyboard.Controller().release(ks.Key2Str(self.button))
            else:
                keyboard.Controller().press(self.button)
                time.sleep(self.TIME/1000)
                keyboard.Controller().release(self.button)


class MainLogic():
    def __init__(self) -> None:
        pass

    def WhatState(self) -> bool:
        return STATE

    def ChangeState(self) -> None:
        global STATE
        STATE = not STATE
        if (STATE):
            self.INFLoop()

    def INFLoop(self) -> None:
        move = Movement()

        def Loop():
            time.sleep(move.INITIALCOOLDOWN)
            while (STATE):
                move.Loop()
                time.sleep(
                    move.RESETTIME + random.randint(move.RESETTIMERAND*-1, move.RESETTIMERAND))
            global ACTIVELOOP
            ACTIVELOOP = False

        if not ACTIVELOOP:
            t = threading.Thread(target=Loop)
            t.start()

    def INFLoopKeyCheck(self) -> None:
        activeKeys = set()
        ks = Keyswitch()

        def on_key_press(key):
            LOOKINGFORKEYS = FileRead().LOOKINGFORKEYS
            if ACTIVECHANGER:
                return
            if (not type(key) == keyboard.KeyCode):
                activeKeys.add(ks.Delate_L_R(key))
            else:
                activeKeys.add(ks.SpecialShift(key))

            if activeKeys == LOOKINGFORKEYS:
                self.ChangeState()

        def on_key_release(key):
            if ACTIVECHANGER:
                return
            if (not type(key) == keyboard.KeyCode):
                activeKeys.discard(ks.Delate_L_R(key))
            else:
                activeKeys.discard(ks.SpecialShift(key))
                activeKeys.discard(ks.SpecialShift(key))

        listener = keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release,
        )

        listener.start()

    def ChangeKey(self, destroy) -> None:
        global ACTIVECHANGER
        ACTIVECHANGER = True

        activeKeys = set()
        setKeys = set()
        ks = Keyswitch()

        def on_key_press(key):
            if key == Key.esc:
                global ACTIVECHANGER
                ACTIVECHANGER = False

                listener.stop()
                destroy()
                return
            if (not type(key) == keyboard.KeyCode):
                activeKeys.add(ks.Delate_L_R(key))
                setKeys.add(ks.Delate_L_R(key))
            else:
                activeKeys.add(key)
                setKeys.add(key)

        def on_key_release(key):
            if (not type(key) == keyboard.KeyCode):
                activeKeys.discard(ks.Delate_L_R(key))
            else:
                activeKeys.discard(key)

            if not activeKeys:
                global ACTIVECHANGER

                FileWrite().Write(LOOKINGFORKEYS=setKeys)
                ACTIVECHANGER = False

                destroy()
                listener.stop()

        listener = keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release)

        listener.start()


if __name__ == '__main__':
    # m = MainLogic()
    # m.INFLoopKeyCheck()
    # Movement().KeyboardPress()
    t = Movement()
    print(t.COOLDOWN)
    while True:
        time.sleep(1)
    pass
