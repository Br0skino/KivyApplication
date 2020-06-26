from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
class MainWindow(BoxLayout):
    pass



class MainApp(App):
    def build(self):
        return MainWindow()
MainApp().run()