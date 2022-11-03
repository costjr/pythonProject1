from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton

class Demo(MDApp):
    def build(self):
        screen = Screen()
        self.l = MDLabel(text = "HI PEOPLE!", halign='center',
                         text_color=(0.5, 0, 0.5, 1),
                         font_style='Caption')

        self.n = MDTextField(text="Enter name", pos_hint={'center_x':0.5, 'center_y':0.8},
                             size_hint_x=None, width=100)
        btn = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.5, 'center_y': 0.3},
        on_release=self.btnfunc)

        screen.add_widget(self.n)
        screen.add_widget(btn)
        screen.add_widget(self.l)
        return screen
    def btnfunc(self, obj):
        self.l.text = self.n.text
        print("button is pressed!")
if __name__ == "__main__":
        Demo().run()