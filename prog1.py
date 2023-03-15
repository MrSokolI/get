from kivymd.app import MDApp
from kivy.lang import Builder
import openai

openai.api_key = "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"

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        id: output_label
        text: "Вас приветствует бот!"
     
        valign: 'top'
    BoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: input_text
            hint_text: "Введите текст"
            size_hint_y: None
        MDRaisedButton:
            text: "Отправить"
            size_hint_y: None
            on_release: app.update_output()
'''

class MyApp(MDApp):

    def build(self):
        self.root = Builder.load_string(KV)
        return self.root

    def update_output(self):
        input_text = self.root.ids.input_text.text
        Anser = AI(input_text)
        self.root.ids.output_label.text = Anser
        self.root.ids.input_text.text = ""
def AI(text):
  response = openai.Completion.create(model="text-davinci-003",prompt=text,temperature=0.1,max_tokens=4000,top_p=1,frequency_penalty=0,presence_penalty=0)
  return text + '\n'+response['choices'][0]['text']


if __name__ == '__main__':
    MyApp().run()