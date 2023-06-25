import kivy
kivy.require('1.10.0')
  
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Label
  
class HelloKivy(App):
  
    # This returns the content we want in the window
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text ="Hello !",font_size = 80)
        f.add_widget(s)
        s.add_widget(l)
        # Return a label widget with Hello Kivy
        return f
  
def main():
    helloKivy = HelloKivy()
    helloKivy.run()

if __name__ == "__main__":
    main()


