from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class Grid(GridLayout):
    pass


class AbdoApp(App):
    def build(self):
        Builder.load_file('main.kv')
        return Grid()


if __name__ == '__main__':
    AbdoApp().run()
