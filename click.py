from pynput.mouse import Controller,Button
import time
mouse = Controller()

while True:
    mouse.click(Button.left,1)
    print('clicked')
    mouse.move(50, 50)
    time.sleep(3)
    mouse.move(-50, -50)
    time.sleep(5)
	

