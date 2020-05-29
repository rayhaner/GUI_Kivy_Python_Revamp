from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.app import MDApp


class Stopwatch(Screen):
    milisec = NumericProperty(0)
    time = StringProperty("00:00:00:00")
    running = False

    # Helper Methods
    def convert(self, ms):
        sec = ms // 100
        ms = ms % 100
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        return "{:02d}:{:02d}:{:02d}:{:02d}".format(int(hours), int(mins), int(sec), ms)

    def run_clock(self, *args):
        self.milisec += 1
        self.time = self.convert(self.milisec)

    # Button Methods
    def start(self):
        self.clock_event = Clock.schedule_interval(self.run_clock, 0.01)
        self.running = True

    def stop(self):
        if self.running:
            Clock.unschedule(self.clock_event)
            self.running = False

    def reset(self):
        self.stop()
        self.milisec = 0
        self.time = "00:00:00:00"

    def back(self):
        self.reset()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'gallery'
