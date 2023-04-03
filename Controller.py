import pygame as pg
import time


class Controller(object):
    def __init__(self):
        pg.init()
        pg.joystick.init()
        self.joystick = pg.joystick.Joystick(0)
        self.joystick.init()
        print(self.joystick.get_numaxes())
        self.nonStop = True
        self.left_speed = 0
        self.right_speed = 0

    def get_event(self):
        self.nonStop = True
        while self.nonStop:
            for event in pg.event.get(pump=True):
                # print(event)
                if event.type == pg.JOYAXISMOTION:
                    self.left_speed = -round(self.joystick.get_axis(1), 2)
                    self.right_speed = round(self.joystick.get_axis(2), 2)
                elif event.type == pg.JOYBUTTONDOWN:
                    if self.joystick.get_button(6):
                        self.nonStop = False
                        break
            yield [self.left_speed, self.right_speed, self.nonStop]
# controller = Controller()
# while True:
#     print(next(controller.get_event()))
#     time.sleep(0.01)