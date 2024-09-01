from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

class CustomFloatLayout(MDFloatLayout):
    pass

class SectionBoxLayout(MDBoxLayout):
    section_name = StringProperty()
    
class GradientSeparator(MDBoxLayout):
    pass
