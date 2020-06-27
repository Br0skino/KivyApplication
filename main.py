from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton,MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.lang import Builder
Window.size=(300,500)
screen_settings="""
Screen:
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:"DrugNet"

            
            halign:"center"
            left_action_items: [["menu", lambda x: app.callback()]]
            
        MDLabel:



"""

class DemoApp(MDApp):




    def build(self):
        self.theme_cls.primary_palette="Purple"
        self.theme_cls.theme_style="Light"
        screen=Builder.load_string(screen_settings)
        Bottone=MDTextField(text="Username",pos_hint={"center_x":0.5,"center_y":0.5},size_hint_x=0.5)
        Button=MDRectangleFlatButton(text="LOGIn",pos_hint={"center_x":0.50,"center_y":0.43})
        screen.add_widget(Bottone)
        screen.add_widget(Button)

        
        return screen
DemoApp().run()
