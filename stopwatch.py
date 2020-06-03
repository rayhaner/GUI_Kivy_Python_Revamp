from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen, SlideTransition


class Stopwatch(Screen):
    millisec = NumericProperty(0)
    time = StringProperty("00:00:00:000")
    running = False

    # Helper Methods
    def convert(self, ms):
        sec = ms // 1000
        ms = ms % 1000
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        return "{:02d}:{:02d}:{:02d}:{:03d}".format(int(hours), int(mins), int(sec), ms)

    def run_clock(self, *args):
        self.millisec += 10
        self.time = self.convert(self.millisec)

    # Button Methods
    def start(self):
        if not self.running:
            self.clock_event = Clock.schedule_interval(self.run_clock, 0.01)
            self.running = True

    def stop(self):
        if self.running:
            Clock.unschedule(self.clock_event)
            self.running = False

    def reset(self):
        self.stop()
        self.millisec = 0
        self.time = "00:00:00:000"

    def back(self):
        self.reset()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'gallery'
