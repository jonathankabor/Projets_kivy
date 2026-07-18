from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
import sys


Builder.load_file("widget_exemples.kv")




class WidgetsExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    slider_label_text = StringProperty("1")
    text_input_text = StringProperty("Jo Le Magicien")
    
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
    
    def ProgressBar_value(self, widget):
        print("ProgressBar value: " + str(int(widget.value)))
        self.compteur = int(widget.value)
        self.mon_texte = str(self.compteur)
        self.slider_label_text = str(int(widget.value))
        
    def on_text_validate(self, widget):
        print("TextInput validate: " + widget.text)
        self.text_input_text = widget.text
