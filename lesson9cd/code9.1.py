"""from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def built(self):
        return MDLabel(tetx="Hello, World", halign="centre")
MainApp().run()"""

from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDIconButton(
                    icon="language-python",
                    pos_hint={'centre_x': 0.5, "centre_y": 0.5},
                    size_hint=(0.8,0.8)
                )
            )
        )
Example().run()

#from kivy.app import MDApp
#from kivymd.uix.label import MDLabel
#from kivymd.uix.screen import Screen
#from kivymd.uix.textfield import MDTextField
#from kivymd.uix.button import MDRectangleFlatbutton