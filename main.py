from kivymd.app import MDApp
from app.screens.menuscreen.menuscreen import MenuScreen
from app.screens.proteinscreen.proteinscreen import ProteinScreen

class MainApp(MDApp):
    def build(self):
        self.title = "ProtiCalc"
        
    def on_start(self):
        self.root.current = 'menu_screen'
        
if __name__ == "__main__":
    MainApp().run()
