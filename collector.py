# For collecting the data
import keyboard, pyscreenshot, uuid, os, threading
from hook import Hook, KeyboardEvent


'''           !!!!!!!!!!!  IMPORTANT  !!!!!!!!!!!!
              PLAY THE GAME IN FIRST PERSON PERSPECTIVE WITH BONET VISIBLE      '''

class capture_all():

    def __init__(self):

        self.set1_dirs()
        self.set2_dirs()
        self.set3_dirs()

    def set1_dirs(self):
        ''' Checks the directories of set1 '''

        print("checking for set1, w, s and space directories")
        
        if not (os.path.isdir("./set1") and os.path.isdir("./set1/w") and os.path.isdir("./set1/s") and os.path.isdir("./set1/space")):
            
            try:
                os.mkdir("./set1")
                print("set1 directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set1/w")
                print("w directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set1/s")
                print("s directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set1/space")
                print("space directory not found, creating one")
            except: pass
    
    def set2_dirs(self):
        ''' Checks the directories of Set2 '''

        print("checking for set2, a and d directories")
        
        if not (os.path.isdir("./set2") and os.path.isdir("./set2/a") and os.path.isdir("./set2/d")):
            
            try:
                os.mkdir("./set2")
                print("set2 directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set2/a")
                print("a directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set2/d")
                print("d directory not found, creating one")
            except: pass

    def set3_dirs(self):
        ''' Checks the directories of Set3 '''

        print("checking for set3, N20 and No20 directories")
        
        if not (os.path.isdir("./set3") and os.path.isdir("./set3/N20") and os.path.isdir("./set3/No20")):
            
            try:
                os.mkdir("./set3")
                print("set3 directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set3/N20")
                print("N20 directory not found, creating one")
            except: pass

            try:
                os.mkdir("./set3/No20")
                print("No20 directory not found, creating one")
            except: pass

    def set1_events(self, args):
        ''' Function that takes care of capturing the frames when acceleration or front/rear break is used '''
        
        if isinstance(args, KeyboardEvent):
            
            if 'W' in args.pressed_key:
                pyscreenshot.grab(bbox=(0, 155, 1920, 1080)).save(f"./set1/w/{uuid.uuid1().hex}.png")
                print(f"Saved to set1/w/")
            
            elif 'S' in args.pressed_key:
                pyscreenshot.grab(bbox=(0, 155, 1920, 1080)).save(f"./set1/s/{uuid.uuid1().hex}.png")
                print(f"Saved to set1/s/")

            elif 'Space' in args.pressed_key:
                pyscreenshot.grab(bbox=(0, 155, 1920, 1080)).save(f"./set1/space/{uuid.uuid1().hex}.png")
                print("Saved to set1/space")
    
    def set2_events(self, args):
        ''' Function that takes care of capturing the frames for left or right turns '''
        
        if isinstance(args, KeyboardEvent):
            
            if 'A' in args.pressed_key:
                pyscreenshot.grab(bbox=(0, 155, 1920, 1080)).save(f"./set2/a/{uuid.uuid1().hex}.png")
                print(f"Saved to set2/a/")
            
            elif 'D' in args.pressed_key:
                pyscreenshot.grab(bbox=(0, 155, 1920, 1080)).save(f"./set2/d/{uuid.uuid1().hex}.png")
                print(f"Saved to set2/d/")

    def set3_events(self, args):
        ''' Function that takes care of capturing the frames when nitro is used '''
        
        if isinstance(args, KeyboardEvent):
            
            if 'F' in args.pressed_key:
                pyscreenshot.grab(bbox=( 1434, 662, 1920, 1080)).save(f"./set3/N20/{uuid.uuid1().hex}.png")
                print(f"Saved to set3/N20/")

    def start_threads(self):

        hk1 = Hook()
        hk1.handler = self.set1_events
        thread1 = threading.Thread(target=hk1.hook)
        thread1.start()

        # hk2 = Hook()
        # hk2.handler = self.set2_events
        # thread2 = threading.Thread(target=hk2.hook)
        # thread2.start()

        # hk3 = Hook()
        # hk3.handler = self.set3_events
        # thread3 = threading.Thread(target=hk3.hook)
        # thread3.start()

if __name__ == '__main__':

    print("Checking for \"data\" directory")

    try:
        os.chdir("./data/")
        print("\"data\" directory found")
    except:
        print("\"data\" directory not found, creating one")
        os.mkdir("./data/")
        os.chdir("./data")

    starter = capture_all()
    starter.start_threads()


def capture_screen(name, cord):
    '''
    the road cords:
    x1,y1,x2,y2 ==> (0, 155, 1920, 1080)

    nitro cords:
    (1434, 662, 1920, 1080)
    '''
    image = pyscreenshot.grab(bbox=cord)
    # print(cord)
    image.save(name)
    print(f"{name} saved")


def capture_set2():
    ''' Function that takes care of capturing the frames for left or right turns '''

    if not (os.path.isdir("./set2") and os.path.isdir("./set1/a") and os.path.isdir("./set1/d")):
        
        try:
            os.mkdir("./set2")
            print("set2 directory not found, creating one")
        except:
            pass

        try:
            os.mkdir("./set2/a")
            print("a directory not found, creating one")
        except:
            pass

        try:
            os.mkdir("./set2/d")
            print("d directory not found, creating one")
        except:
            pass
    
    def a():
        capture_screen(f"./set2/a/{uuid.uuid1().hex}.png", cord=(0, 155, 1920, 1080))

    def d():
        capture_screen(f"./set2/d/{uuid.uuid1().hex}.png", cord=(0, 155, 1920, 1080))
    
    keyboard.add_hotkey('a', lambda: a())
    keyboard.add_hotkey('d', lambda: d())
    keyboard.wait()
# capture_set2()

def capture_set3():
    
    '''
    Function that takes care of capturing the frames for nitro
    Capture Nitro and No nitro seperately two different times
    '''

    if not os.path.isdir("./set3"):
        os.mkdir("./set3")
    elif not os.path.isdir("./set3/N20"):
        os.mkdir("./set3/N20")
    elif not os.path.isdir("./set3/No20"):
        os.mkdir("./set3/No20")
    
    def N20():
        capture_screen(f"./set3/N20/{uuid.uuid1().hex}.png", cord=(1434, 662, 1920, 1080))
    def No20():
        capture_screen(f"./set3/No20/{uuid.uuid1().hex}.png", cord=(1434, 662, 1920, 1080))
    
    '''
    keyboard.add_hotkey('f', lambda: N20())
    keyboard.wait()
    No20()
    '''

'''
from ctypes import windll, Structure, c_long, byref
def capture_cord():
    class POINT(Structure):
        _fields_ = [("x", c_long), ("y", c_long)]
    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        # return { "x": pt.x, "y": pt.y}
        return (pt.x,pt.y)

    pos = queryMousePosition()
    print(pos)
    return pos

def map_vars():
    global lx,ly
    lx,ly = capture_cord()

# For simulating the key presses
# import pyautogui # https://pyautogui.readthedocs.io/en/latest/keyboard.html
def press_key():    
    pyautogui.hotkey()

def capture_key():
    keyboard.add_hotkey('w', lambda: capture_screen(uuid.uuid1().hex, cord=(0, 155,1920, 1080)))
    # keyboard.add_hotkey('c', lambda: map_vars())
    keyboard.add_hotkey('a', lambda: print('a pressed'))
    keyboard.add_hotkey('s', lambda: print('s pressed'))
    keyboard.add_hotkey('d', lambda: print('d pressed'))
    keyboard.add_hotkey('f', lambda: print('f pressed'))
    keyboard.add_hotkey('space', lambda: print('space pressed'))
    keyboard.wait()
'''