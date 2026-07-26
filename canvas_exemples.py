from kivy.graphics.vertex_instructions import Ellipse, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.metrics import dp
from kivy.properties import Clock
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
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_a_click(self):
        # print("Button A clicked!")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)  # Increment value in pixels
        x += dp(10)  # Move 10 pixels to the right
        # bord droit : x+w
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)
        
        
class CanvasExemple5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)  # Velocity in pixels per frame
        self.vy = dp(4)  # Velocity in pixels per frame
        with self.canvas:
            self.ball = Ellipse(pos=(self.center), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)  # Update at 60 FPS
            
    
    def on_size(self, *args):
        print("on_size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)
        
    def update(self, dt):
        # print("update")
        x, y = self.ball.pos
        
        x += self.vx
        y += self.vy
        
        if x <= 0 or x + self.ball_size >= self.width:
            self.vx = -self.vx  # Reverse horizontal direction
            x += self.vx  # Move the ball back within bounds
        if y <= 0 or y + self.ball_size >= self.height:
            self.vy = -self.vy  # Reverse vertical direction
            y += self.vy  # Move the ball back within bounds
        self.ball.pos = (x, y)
        
class CanvasExemple6(Widget):
    pass