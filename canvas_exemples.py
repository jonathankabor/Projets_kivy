from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Builder 


Builder.load_file('canvas_exemples.kv')


class CanvasExemple1(Widget):
    pass

class CanvasExemple2(Widget):
    pass

class CanvasExemple3(Widget):
    pass

class CanvasExemple4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=[100, 100, 400, 500], width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            Rectangle(pos=(700, 200), size=(150, 100))