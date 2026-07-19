#from tkinter.ttk import Button
from kivy.app import App
from kivy.uix.image import Image
from kivy.metrics import dp
from navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty



class MyscreenManager(NavigationScreenManager):
    pass

class MyApp(App):
    def build(self):
        return Image(source="images/donut.gif")
    
class LeLabApp(App):
    manager = ObjectProperty(None)
    
    
    def build(self):
        self.manager = MyscreenManager()
        return self.manager
    


LeLabApp().run()

