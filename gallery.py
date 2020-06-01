from kivy.uix.screenmanager import Screen, SlideTransition


class Gallery(Screen):
    # def get_info(self, id):
    #     print(id)

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').reset_form()

    def open_stopwatch(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'stopwatch'

    def open_calculator(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'calculator'
