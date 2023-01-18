from pynput.keyboard import Key,Listener,Controller
Keyboard = Controller()

def testKeyboardVirtually():
    Keyboard.press(Key.media_volume_up)
    Keyboard.release(Key.media_volume_down)
    Keyboard.press(Key.media_volume_down)
    Keyboard.release(Key.media_volume_down)


def onPress(key):
    # A loop that never ends can be used to prank friends but disatrous when runned always.
    testKeyboardVirtually()


#Setup a Keyboard listener to listen on Keyboard events  
with Listener(on_press=onPress) as listener:
    listener.join()



