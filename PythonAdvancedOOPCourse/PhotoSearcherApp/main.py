from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia

Builder.load_file('front_end.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # get user query from the text input
        query = self.manager.current_screen.ids.user_query.text
        # print(query)
        # use input to search wikipedia for the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        headers = {
            'User-Agent' : 'My User Agent 1.0'
        }
        req = requests.get(self.get_image_link(), headers=headers)

        filepath = 'files/image.jpg'
        with open(filepath, 'wb') as file:
            file.write(req.content)
        return filepath

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

# img_url = wikipedia.page("Beach")
# img_url = img_url.images[0]
# req = requests.get(img_url, allow_redirects=False)
#
#
#
# headers = {'User-Agent' : 'My User Agent 1.0'}
# # headers['Referer'] = img_url
# req = requests.get(img_url, headers=headers, allow_redirects=False)
# with open('image12', 'wb') as fh:
#     fh.write(req.content)