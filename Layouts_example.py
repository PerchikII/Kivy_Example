#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('Layouts_example.kv')

class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flag = True  # с помощью этого бросаю виджеты то в левую колонку, то в правую
        posess_y1 = 1216  # максимальная высота левой колонки
        posess_y2 = 1216  # то же, только правой
        for i in range(16):  # случайным образом выставляю высоту виджета(кнопки)
            num = random.random()
            if num == 1:
                my_height = 150
            else:
                my_height = 100
            if self.flag:  # значит кидаем виджет в левую колонку
                posess_y1 -= (my_height + 2)  # нужно помнить, что в kivy рисование
                # происходит с левого нижнего угла, координаты которого 0 и 0
                # значит нужно отступить от верхней границы на выстоту кнопки с отступом в 2 пикселя
                # перед тем как задать позицию и размер виджета нужно дать ему size_hint=(None,None),
                # а потом вручную задать позицию и размер, с необходимыми отступами
                self.ids.my_box.add_widget(
                    Button(text=str(i + 1), size_hint=(None, None), height=my_height, width=(Window.width / 2) - 10,
                           pos=(0, posess_y1)))
                self.flag = False
            else:
                posess_y2 -= (my_height + 2)
                self.ids.my_box.add_widget(
                    Button(text=str(i + 1), size_hint=(None, None), height=my_height, width=(Window.width / 2) - 10,
                           pos=(Window.width / 2, posess_y2)))
                self.flag = True


class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Third(Screen):
    def __init__(self, **kwargs):
        # эти размеры нужны для того чтобы виджет не выходил за пределы экрана
        # создаю обязательно до super, иначе у меня не работает
        # в разметке всем виджетам задаю size_hint:None,None
        # а потом размещаю как мне нужно с заданными размерами
        self.my_height = Window.height
        self.my_width = Window.width
        super().__init__(**kwargs)


class Fourth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            'None', '0', 'None',
        ]
        for i in self.list_buttons:
            self.ids.this_layout.add_widget(Button(text=i, on_press=self.pressing))

    def pressing(self, instance):
        print(instance.text)
        self.manager.current = 'first'


class Layouts_exampleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='first'))
        sm.add_widget(Second(name='second'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        return sm


if __name__ == "__main__":
    Layouts_exampleApp().run()
