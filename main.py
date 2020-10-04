from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helper import screen_helper
import time
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.clock import Clock
from newsapi import NewsApiClient
from kivymd.uix.label import MDLabel



from kivy.uix.screenmanager import ScreenManager, Screen
import webbrowser






class StartScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.callbackfun, 3)

    def callbackfun(self, dt):
        self.manager.current = self.manager.next()
class HomeScreen(Screen):
    pass
class NewsScreen(Screen):
    pass
class VizScreen(Screen):
    pass
class ContactScreen(Screen):    pass



sm = ScreenManager()

sm.add_widget(StartScreen(name='start'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(NewsScreen(name='news'))
sm.add_widget(ContactScreen(name='contact'))
sm.add_widget(VizScreen(name='vis'))
class SansaarApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass



    def build(self):
        self.theme_cls.primary_palette = "Teal"
        class ContentNavigationDrawer(BoxLayout):
            pass

        class DrawerList(ThemableBehavior, MDList):
            pass

        self.screen = Builder.load_string(screen_helper)


        return self.screen


    def navigate(self):

        webbrowser.open("https://team-sansaar.tribe.so/")
SansaarApp().run()

