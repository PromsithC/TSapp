from kivy.app import App
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (480,800)#(720,1280)


class ScreenMN(ScreenManager):
    pass

class HomeScreen(Screen):
    def login(self):
        self.ids.error_login.text = "wrong username or password"

class MyApp(App):
    def build(self):
        return Builder.load_file('dev01.kv')

if __name__ == "__main__":
    MyApp().run()