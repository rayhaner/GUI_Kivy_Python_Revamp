from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.textfield import MDTextFieldRect


class Calculator(Screen):

    kmh_value = NumericProperty(0)
    ms_value = NumericProperty(0)
    mph_value = NumericProperty(0)

    def is_number(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def text_change(self, text, label_type):

        def convert(conversion):
            return round(float(text) * conversion, 1)

        if not self.is_number(text):
            return

        if label_type == 'kmh':
            self.ms_value = convert(1/3.6)
            self.mph_value = convert(1/1.609)

        elif label_type == 'ms':
            self.kmh_value = convert(3.6)
            self.mph_value = convert(2.237)

        elif label_type == 'mph':
            self.ms_value = convert(1/2.237)
            self.kmh_value = convert(1.609)

    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'gallery'


class ConvertTextField(MDTextFieldRect):
    def keyboard_on_key_up(self, keycode, text):
        if self.readonly and text[1] == "backspace":
            self.readonly = False
            self.do_backspace()


