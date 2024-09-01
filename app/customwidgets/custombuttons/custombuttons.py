from kivy.uix.button import Button
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.properties import ColorProperty, StringProperty

class GradientButton(RectangularRippleBehavior, Button):
    text = StringProperty('Button')
    text_color = ColorProperty('white')
    
class ColoredButton(RectangularRippleBehavior, Button):
    text = StringProperty('Button')
    text_color = ColorProperty('white')
    bg_color = StringProperty('#25aae1')