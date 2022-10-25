from file_sharer import FileSharer
from kivy.core.clipboard import Clipboard
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import os
import time
import webbrowser

Builder.load_file('front_end.kv')

class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        # pass

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        # pass

    def capture(self):
        """Creates a filename with the current time, then captures
         and saves a photo image under that filename"""
        time_stamp = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{time_stamp}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath
        # pass

class ImageScreen(Screen):

    def create_link(self):
        """Accesses the the photo filepath, uploads it to the web,
        then inserts the link into the label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        # try will first try this and only if that causes an error will it do the exception case
        try:
            Clipboard.copy(self.url)
        except:
            self.create_link()
            Clipboard.copy(self.url)

    def open_link(self):
        """Open link with default browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.create_link()
            webbrowser.open(self.url)

    def return_to_main(self):
        self.manager.current = 'camera_screen'



class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()



MainApp().run()