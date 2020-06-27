from kivymd.app import MDApp
from kivy.lang import Builder
KV="""
Screen:
    MDRectangleFlatButton:
        text:"Hello World Kivy"
        pos_hint:{"center_x":0.5,"center_y":0.5}
"""
class MainApp(MDApp):
    def build(self,title,theme_cls.theme_style,theme_cls.primary_palette):
        self.title="Hello Kivy"
        self.theme_cls.theme_style= "Light"#"Dark"
        self.theme_cls.primary_palette="Blue"
        return Builder.load_string(KV)
MainApp().run()