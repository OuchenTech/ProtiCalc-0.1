from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivy.core.window import Window
from app.customwidgets.custombuttons.custombuttons import GradientButton

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        Window.bind(on_request_close=self.exit_app)
        
    def open_popup(self):
        """
        Opens the exit confirmation popup.
        
        This method creates an instance of the `ExitPopup`, opens it,
        and binds the 'yes' button to the `exit_app` method.
        """
        model_inst = Factory.ExitPopup()
        yes_button= model_inst.ids.yes_button
        model_inst.open()
        yes_button.bind(on_release=self.exit_app)
        
    def exit_app(self, *args):
        """
        Exits the application.
        
        Stops the running of the Kivy app and closes the window.
        
        Args:
            *args: Additional arguments passed from the event binding.
        """
        App.get_running_app().stop()
        Window.close()