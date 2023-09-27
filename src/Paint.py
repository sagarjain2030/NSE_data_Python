import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse,Line
from kivy.uix.button import Button
from random import random
from random import randint

class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)

class PingPongBall(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (50, 50)
        self.pos = (0, 0)
        self.velocity = (4, 0)

class PaintApp(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = Color(1, 0, 0)
        self.d = 30

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            self.color = Color(random(),random(),random())
            self.d=randint(10,30)
            Ellipse(pos=(touch.x - self.d/2, touch.y - self.d/2), size=(self.d,self.d))
            print("color : " + str(int(self.color.r * 255)) + " " + str(int(self.color.g * 255)) + " " + str(int(self.color.b * 255)))
            print("d : " + str(self.d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
    
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


    def on_touch_up(self, touch):
        print("inside touch up")
        print(touch)
        with self.canvas:
            Ellipse(pos=(touch.x - self.d/2, touch.y - self.d/2), size=(self.d,self.d))



class Paint(App):

    def build(self):
        #return LoginScreen()
        #return PingPongBall()
        parent = Widget()
        self.painter = PaintApp()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    
    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    app_start = Paint()
    app_start.run()