import pyHook 
from threading import Timer
import win32gui
import logging

class blockInput():
    def OnKeyboardEvent(self,event):
        return False

    def unblock(self):
        logging.info(" -- Unblock!")
        if self.t.is_alive():
            self.t.cancel()
        try: self.hm.UnhookKeyboard()
        except: pass
       
    def block(self, timeout = 10, keyboard = True):
        self.t = Timer(timeout, self.unblock)
        self.t.start()

        logging.info(" -- Block!")

        if keyboard:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()
        win32gui.PumpWaitingMessages()

    def _init_(self):
        self.hm = pyHook.HookManager()