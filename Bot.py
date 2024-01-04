from pynput.keyboard import *
from pynput.mouse import Button, Controller
import time

class Bot:
    def _init_(self, mouse, running, OpArea_XL, OpArea_XR, OpArea_YU, OpArea_YL):
        self.mouse = Controller()
        self.running = False
        self.No_limit = True #if True, program works no matter where mouse is located.
    
        self.OpArea_XL =  0 #limit of operation area, left X axis
        self.OpArea_XR =  0 # || || right X axis
        self.OpArea_YU =  0 # || || upper Y axis
        self.OpArea_YL =  0 # || || lower Y axis

    def Is_in_OpSquare():
        return False
        #get mouse position, returns true if in set operation square.

    def Run(self):
        if self.No_limit == False:
            if Is_in_OpSquare():
                self.running = True
                Clicker(running)
            else:
                self.running = False
                Clicker(running)
        elif self.running:
            self.running = False
            Clicker(running)
        else:
            self.running = True
            Clicker(running)

    def Stop_bot(self):
        self.running = False
        return self.running

    def Clicker(turner):
        while turner:
            mouse.click(Button.left, 1)
            time.sleep(0.001)
            
    def Limiter_mode():
        return 0
    
class Imputer:
    def press_on(key):
        print('Press ON: {}'.format(key))
    def press_off(key):
        print('Press OFF: {}'.format(key))
        if key == Key.esc:
            print('Script Finalized')
            return Bot.Stop_bot()
        elif key.char == ('s'):
            Bot.Run()
    with Listener(on_press = press_on, on_release = press_off) as listener:
        listener.join()
