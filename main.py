from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from calculator import Calculator
from incorrect import Incorrect
from gallery import Gallery
from stopwatch import Stopwatch


class Login(Screen):
    def do_login(self, login_text, password_text):
        app = MDApp.get_running_app()

        app.username = login_text
        app.password = password_text

        self.manager.transition = SlideTransition(direction="left")

        if app.username == "Roboto" and app.password == "123":
            self.manager.current = 'gallery'
        else:
            self.manager.current = 'incorrect'

    def reset_form(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class LoginApp(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Incorrect(name='incorrect'))
        manager.add_widget(Gallery(name='gallery'))
        manager.add_widget(Stopwatch(name='stopwatch'))
        manager.add_widget(Calculator(name='calculator'))

        return manager


if __name__ == '__main__':
    LoginApp().run()
