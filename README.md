# AntyAFK

My old project for as name implies antyAFK

Written in python

---
# How to run

## Linux (kinda works (made it for windows))

1. `sudo apt install python3-tk`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip3 install customtkinter`
5. `pip3 install pillow`
6. `pip3 install pynput`
7. in main.py line 22: `self.iconbitmap(IMAGES['ICON'])` should be commented/deleted

## Windows

1. install python
    - if you going to use venv probably you should enable running scripts (run this line in elevated powershell): `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
2. `python3 -m venv .venv`
3. `.\.venv\Scripts\activate`
4. `pip3 install customtkinter`
5. `pip3 install pillow`
6. `pip3 install pynput`

---

# Credits

- Mouse icon by [Freepik](https://www.flaticon.com/free-icon/mouse_3249525)
- Mouse icon by [Freepik](https://www.flaticon.com/free-icon/mouse_1786973)
- Keyboard icon by [Freepik](https://www.flaticon.com/free-icon/keyboard_2182669)
- On/Off button icon by [Freepik](https://www.flaticon.com/free-icon/onoff-button_1228?term=onoff&page=1&position=1&origin=search&related_id=1228)
- Color palette from [Aquaverse](https://lospec.com/palette-list/aquaverse)


---

# MIT License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
