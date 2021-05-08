
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.extras.highlight import KivyLexer
from kivy.lang.parser import ParserException
from kivy.properties import StringProperty

import os
import openai
import threading

from prompts import prompt
from utils import fix_indent

openai.api_key = os.getenv("OPENAI_API_KEY")

class InfoLabel(MDLabel):
    _color= StringProperty("Gray")

class Demo(MDApp):

    def build(self):
        x = Builder.load_file("test.kv")
        self.app_root = x
        return x
    
    def add_new(self, text, btn):
        btn.disabled = True
        query = (
            "Input: {}\n".format(text)+
            "Output:"
        )
        copy_prompt = prompt+query
        t = threading.Thread(
            target = self.get_response, args=(copy_prompt, btn)
        )
        t.start()
    
    def get_response(self, prompt, btn):
        response = openai.Completion.create(
            engine="curie-instruct-beta",
            prompt=prompt,
            temperature=0.8,
            max_tokens=250,
            top_p=1,
            best_of=5,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"] 
            )

        new_kv = fix_indent(response.choices[0].text)
        print(new_kv)
        result_layout = self.app_root.ids.result_layout
        code_input = self.app_root.ids.code_input
        code_input.lexer = KivyLexer()
        
        result_layout.clear_widgets()
        try:
            code_input.text = new_kv+"\n"
            new_widget = Builder.load_string(new_kv)
            result_layout.add_widget(new_widget)
        except Exception as e:
            print(e) 
            info_label = InfoLabel()
            info_label.text = str(e)
            info_label._color = "Red"
            info_label.font_style = "H5"
            result_layout.add_widget(info_label)
        btn.disabled = False

Demo().run()
