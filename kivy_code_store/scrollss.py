from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<ScrollApp>:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1, 0.12
        Button:
            text: 'Fixed Menu'
            on_press: print('This button stops working if there is a horizontal scrollview "behind"')
    BoxLayout:
        id:scroll_box
        ScrollView:
            do_scroll: False, True
            bar_width: 10
            scroll_type: ['bars', 'content']
            # size_hint: None, None
            # size: scroll_box.size
            height: scroll_box.height
            # pos: scroll_box.pos
            # pos_hint: {'top': 0.9}
            GridLayout:
                cols:1
                #orientation: 'vertical'
                size_hint: (1, None)
                height: self.minimum_height
                padding: 22, 0, 22, 50
                spacing: 50
                canvas:
                    Color:
                        rgba: .15, .15, .15, .9
                    Rectangle:
                        size: self.size
                        pos: self.pos
                Button:
                    text : 'what'
                    size_hint: None, None
                    width: 100
                    height: 100
                    on_press: print('This button does not overlap the menu above')
    
                # "ScrollViews containers"
                Custom:
                Custom:
                Custom:
                Custom:
                Custom:
    BoxLayout:  
        size_hint: 1, 0.12
        Button:
            text : 'hi'
            on_press: print("This menu at the bottom is not affected by the problem that occurs with the top one")


<Custom@BoxLayout>:
    orientation: 'vertical'
    size_hint: 1, None
    height: self.minimum_height
    Label:
        size_hint: None, None
        size: self.texture_size
        id: label
        font_size: 20
        text: 'Teste'
    ScrollView:
        do_scroll: True, False
        size_hint: 1, None
        height: 150
        GridLayout:
            id: grid
            size_hint: None, 1
            width: self.minimum_width
            spacing: 5
            cols: 3
            Button:
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
            Button:
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
            Button:
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
''')


class ScrollApp(BoxLayout):
    pass


class Test(App):
    def build(self):
        return ScrollApp()


Test().run()
