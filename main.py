#from tkinter.ttk import Button
from kivy.app import App
from kivy.uix.image import Image
from kivy.metrics import dp







        


class MyApp(App):
    def build(self):
        return Image(source="images/donut.gif")
class LeLabApp(App):
    pass


LeLabApp().run()

