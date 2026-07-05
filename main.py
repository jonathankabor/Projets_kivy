#from tkinter.ttk import Button
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

class MainWidget(Widget):
    pass

class WidgetsExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    slider_label_text = StringProperty("1")
    
    def on_button_click(self):
        print("Button click")
        
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)
        
    def on_toggle_button_state(self, widget):
        if widget.state == "down":
            print("Toggle button ON")
            widget.text = "ON"
            self.compteur_actif = True
        else:
            print("Toggle button OFF")
            widget.text = "OFF"
            self.compteur_actif = False
            
    def on_switch_active(self, widget):
        if widget.active:
            print("Switch ON")
            self.compteur_actif = True
        else:
            print("Switch OFF")
            self.compteur_actif = False
            
    def on_slider_value(self, widget):
        print("Slider value: " + str(int(widget.value)))
        self.compteur = int(widget.value)
        self.mon_texte = str(self.compteur)
        self.slider_label_text = str(int(widget.value))

class GridLayoutExemple(GridLayout):
    pass

class StackLayoutExemple(StackLayout):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)

class AnchorLayoutExemple(AnchorLayout):
    pass

class BoxLayoutExemple(BoxLayout):
    pass

"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class LeLabApp(App):
    pass

LeLabApp().run()

