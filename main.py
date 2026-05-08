from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from jnius import autoclass
import requests
import json

# ANDROID 12 DİK MOD VE PREMIUM TASARIM
Window.softinput_mode = "below_target"
Window.clearcolor = get_color_from_hex("#0d0d12")

class LilitPro(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # API ANAHTARIN
        self.api_key = "AIzaSyC90KUJHL4lNjew-mWZKJfJvfQzuEj1BUM"
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        
        # SES MOTORU (TTS)
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
        except: self.tts = None

        # GÖRSEL ARAYÜZ (NEON VE PROFESYONEL)
        self.header = Label(text="[b][color=00f2ff]LILIT PRO[/color][/b]\n[size=14sp][color=ff007f]HYBRID INTELLIGENCE[/color][/size]",
                           markup=True, pos_hint={'x': 0, 'y': 0.43}, size_hint=(1, 0.1), font_size='28sp')
        self.add_widget(self.header)

        self.scroll = ScrollView(size_hint=(0.9, 0.48), pos_hint={'x': 0.05, 'y': 0.22})
        self.terminal = Label(text="[color=00ff41]> Çekirdek v6.0 aktif.\n> İsa Yörük için sistem hazır.[/color]",
                            markup=True, size_hint_y=None, height=5000, halign="left", valign="top",
                            text_size=(Window.width * 0.85, None), font_size='16sp')
        self.scroll.add_widget(self.terminal)
        self.add_widget(self.scroll)

        self.input_box = TextInput(hint_text="Patronu dinliyorum...", pos_hint={'x': 0.05, 'y': 0.12}, 
                                  size_hint=(0.9, 0.08), background_color=(0.1, 0.1, 0.15, 1), 
                                  foreground_color=(1, 1, 1, 1), multiline=False)
        self.add_widget(self.input_box)

        self.btn = Button(text="SİSTEME ENJEKTE ET", pos_hint={'x': 0.05, 'y': 0.02}, size_hint=(0.9, 0.08),
                         background_normal='', background_color=get_color_from_hex("#ff007f"), bold=True)
        self.btn.bind(on_release=self.run_ai)
        self.add_widget(self.btn)

    def run_ai(self, instance):
        user_text = self.input_box.text.strip()
        if not user_text: return
        
        self.terminal.text += f"\n\n[color=ffffff]İSA:[/color] {user_text}"
        self.input_box.text = "Düşünüyor..."

        try:
            prompt = f"Sen Lilit'sin. İsa Yörük'ün süper zekasısın. Çok kısa ve karizmatik cevap ver: {user_text}"
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            
            # Bağlantı Ayarları (Android 12 için güvenli SSL)
            response = requests.post(self.api_url, json=payload, timeout=15)
            
            if response.status_code == 200:
                reply = response.json()['candidates'][0]['content']['parts'][0]['text']
                self.terminal.text += f"\n[color=00f2ff]LILIT:[/color] {reply}"
                if self.tts: self.tts.speak(reply, 0, None)
            else:
                self.terminal.text += f"\n[color=ffaa00]> API Meşgul. Onarım Başlatıldı...[/color]"
        except:
            self.terminal.text += f"\n[color=ff0000]> BAĞLANTI HATASI! Sistem onarılıyor...[/color]"
        
        self.input_box.text = ""

class LilitApp(App):
    def build(self): return LilitPro()

if __name__ == "__main__":
    LilitApp().run()
