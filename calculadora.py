import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.input_box = TextInput(multiline=False, readonly=True, font_size=40, halign='right')
        self.add_widget(self.input_box)

        grid = GridLayout(cols=4, spacing=3, size_hint_y=None, height=300)

        grid.add_widget(Button(text='7', on_press=self.append_input))
        grid.add_widget(Button(text='8', on_press=self.append_input))
        grid.add_widget(Button(text='9', on_press=self.append_input))
        grid.add_widget(Button(text='+', on_press=self.append_input))
        
        grid.add_widget(Button(text='4', on_press=self.append_input))
        grid.add_widget(Button(text='5', on_press=self.append_input))
        grid.add_widget(Button(text='6', on_press=self.append_input))
        grid.add_widget(Button(text='-', on_press=self.append_input))

        grid.add_widget(Button(text='1', on_press=self.append_input))
        grid.add_widget(Button(text='2', on_press=self.append_input))
        grid.add_widget(Button(text='3', on_press=self.append_input))
        grid.add_widget(Button(text='*', on_press=self.append_input))
        
        grid.add_widget(Button(text='Del', on_press=self.delete_input))
        grid.add_widget(Button(text='C', on_press=self.clear_input))
        grid.add_widget(Button(text='0', on_press=self.append_input))
        grid.add_widget(Button(text='=', on_press=self.calculate_result))
        grid.add_widget(Button(text='/', on_press=self.append_input))

        self.add_widget(grid)

        self.input_buffer = ''

    def append_input(self, button):
        self.input_buffer += button.text
        self.input_box.text = self.input_buffer

    def clear_input(self, button):
        self.input_buffer = ''
        self.input_box.text = ''

    def delete_input(self, button):
        self.input_buffer = self.input_buffer[:-1]
        self.input_box.text = self.input_buffer

    def calculate_result(self, button):
        try:
            result = str(eval(self.input_buffer))
            self.input_box.text = result
            self.input_buffer = result
        except:
            self.input_box.text = 'Error'
            self.input_buffer = ''


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()