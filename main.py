from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import hashlib

def generate_main_license(hwid, client_count, mode_type):
    if not hwid or len(hwid) < 3:
        return 'En attente de HWID...'
    try:
        count = int(client_count)
    except:
        count = 0
    calc_mode = 'stock' if mode_type == 'none' else mode_type
    suffix = 'rest_book_key' if calc_mode == 'restaurant' else 'acc_book_key'
    salted_id = f'pro_v2_{hwid}_server_clients_{count}_{suffix}'
    return hashlib.sha256(salted_id.encode()).hexdigest()

def generate_mobile_key(device_id):
    if not device_id or len(device_id) < 3:
        return 'En attente ID Mobile...'
    salt = f'magpro_mobile_v6_{device_id}_secure_key'
    return hashlib.sha256(salt.encode()).hexdigest()

def generate_mobile_resto_key(device_id):
    if not device_id or len(device_id) < 3:
        return 'En attente ID Mobile...'
    salt = f'magpro_resto_mobile_v6_{device_id}_secure_key'
    return hashlib.sha256(salt.encode()).hexdigest()

def generate_feature_key(hwid, feature_code):
    if not hwid or len(hwid) < 3:
        return 'En attente de HWID...'
    if feature_code == 'none':
        return ''
    salt = f'magpro_feature_{hwid}_{feature_code}_secret_v1'
    return hashlib.sha256(salt.encode()).hexdigest()

class LoginScreen(Screen):

    def numpad_press(self, value):
        inp = self.ids.pass_input
        lbl = self.ids.error_label
        if value == 'C':
            inp.text = ''
            lbl.text = ''
        elif value == 'OK':
            if inp.text == '2022':
                self.manager.current = 'main'
                inp.text = ''
                lbl.text = ''
            else:
                lbl.text = 'Code Incorrect !'
                inp.text = ''
        else:
            if len(inp.text) < 4:
                inp.text += value
            lbl.text = ''

class MainScreen(Screen):
    pass

KV_CODE = "\n<SectionHeader@Label>:\n    markup: True\n    font_size: '16sp'\n    color: 0.0, 0.48, 0.8, 1\n    size_hint_y: None\n    height: '40dp'\n    canvas.before:\n        Color:\n            rgba: 0.15, 0.15, 0.15, 1\n        Rectangle:\n            pos: self.pos\n            size: self.size\n\n<PriceButton@Button>:\n    markup: True\n    halign: 'center'\n    valign: 'middle'\n    text_size: self.size\n    font_size: '14sp'\n    size_hint_y: None\n    height: '60dp'\n    background_normal: ''\n    background_color: 0.25, 0.25, 0.25, 1\n\n<ModeButton@ToggleButton>:\n    markup: True\n    size_hint_y: None\n    height: '50dp'\n    font_size: '13sp'\n    halign: 'center'\n    valign: 'middle'\n\n<NumButton@Button>:\n    font_size: '22sp'\n    bold: True\n    background_normal: ''\n    background_color: 0.2, 0.2, 0.2, 1\n    color: 1, 1, 1, 1\n\nScreenManager:\n    LoginScreen:\n        name: 'login'\n    MainScreen:\n        name: 'main'\n\n<LoginScreen>:\n    canvas.before:\n        Color:\n            rgba: 0.05, 0.05, 0.05, 1\n        Rectangle:\n            pos: self.pos\n            size: self.size\n    \n    BoxLayout:\n        orientation: 'vertical'\n        padding: '20dp'\n        spacing: '10dp'\n        \n        Label:\n            text: '[b]SÉCURITÉ[/b]'\n            markup: True\n            font_size: '24sp'\n            size_hint_y: None\n            height: '40dp'\n            color: 0, 0.73, 0.83, 1\n\n        TextInput:\n            id: pass_input\n            hint_text: '----'\n            password: True\n            readonly: True\n            multiline: False\n            halign: 'center'\n            font_size: '30sp'\n            size_hint_y: None\n            height: '60dp'\n            background_color: 0.15, 0.15, 0.15, 1\n            foreground_color: 1, 1, 1, 1\n            cursor_color: 0, 0, 0, 0\n\n        Label:\n            id: error_label\n            text: ''\n            color: 1, 0.2, 0.2, 1\n            font_size: '14sp'\n            size_hint_y: None\n            height: '30dp'\n\n        # --- لوحة الأرقام ---\n        GridLayout:\n            cols: 3\n            spacing: '10dp'\n            size_hint_y: 1\n            padding: [20, 0, 20, 0]\n            \n            NumButton:\n                text: '7'\n                on_release: root.numpad_press('7')\n            NumButton:\n                text: '8'\n                on_release: root.numpad_press('8')\n            NumButton:\n                text: '9'\n                on_release: root.numpad_press('9')\n            \n            NumButton:\n                text: '4'\n                on_release: root.numpad_press('4')\n            NumButton:\n                text: '5'\n                on_release: root.numpad_press('5')\n            NumButton:\n                text: '6'\n                on_release: root.numpad_press('6')\n            \n            NumButton:\n                text: '1'\n                on_release: root.numpad_press('1')\n            NumButton:\n                text: '2'\n                on_release: root.numpad_press('2')\n            NumButton:\n                text: '3'\n                on_release: root.numpad_press('3')\n\n            NumButton:\n                text: 'C'\n                color: 1, 0.5, 0.5, 1\n                on_release: root.numpad_press('C')\n            NumButton:\n                text: '0'\n                on_release: root.numpad_press('0')\n            NumButton:\n                text: 'OK'\n                color: 0.5, 1, 0.5, 1\n                on_release: root.numpad_press('OK')\n\n<MainScreen>:\n    ScrollView:\n        canvas.before:\n            Color:\n                rgba: 0.1, 0.1, 0.1, 1\n            Rectangle:\n                pos: self.pos\n                size: self.size\n\n        BoxLayout:\n            orientation: 'vertical'\n            size_hint_y: None\n            height: self.minimum_height\n            padding: '15dp'\n            spacing: '10dp'\n\n            Label:\n                text: '[b]KeygenPro v1.1.0[/b]'\n                markup: True\n                font_size: '26sp'\n                size_hint_y: None\n                height: '60dp'\n                color: 1, 1, 1, 1\n\n            Label:\n                text: '[b]ID Matériel / Mobile:[/b]'\n                markup: True\n                color: 0, 0.73, 0.83, 1\n                size_hint_y: None\n                height: '30dp'\n                halign: 'left'\n                text_size: self.size\n            \n            BoxLayout:\n                size_hint_y: None\n                height: '45dp'\n                spacing: '5dp'\n                \n                TextInput:\n                    id: hwid_input\n                    hint_text: 'Coller ID ici...'\n                    multiline: False\n                    background_color: 0.2, 0.2, 0.2, 1\n                    foreground_color: 1, 1, 1, 1\n                    on_text: app.update_calculation()\n\n                Button:\n                    text: '[b]COLLER[/b]'\n                    markup: True\n                    size_hint_x: None\n                    width: '80dp'\n                    background_normal: ''\n                    background_color: 0.3, 0.8, 0.5, 1\n                    on_release: app.paste_hwid()\n\n            SectionHeader:\n                text: '[b]  1. Logiciels (Base)[/b]'\n\n            GridLayout:\n                cols: 1\n                size_hint_y: None\n                height: self.minimum_height\n                spacing: '5dp'\n\n                ModeButton:\n                    text: '[b]PC: Stock[/b]  [color=#00ff7f][b][25000 DA][/b][/color]'\n                    group: 'mode'\n                    state: 'down'\n                    on_press: \n                        app.current_mode = 'stock'\n                        app.active_source = 'main'\n                        app.update_calculation()\n\n                ModeButton:\n                    text: '[b]PC: Resto[/b]  [color=#00ff7f][b][35000 DA][/b][/color]'\n                    group: 'mode'\n                    on_press: \n                        app.current_mode = 'restaurant'\n                        app.active_source = 'main'\n                        app.update_calculation()\n\n                ModeButton:\n                    text: '[b]Mobile: Stock[/b]  [color=#00ff7f][b][20000 DA][/b][/color]'\n                    group: 'mode'\n                    on_press: \n                        app.current_mode = 'mobile'\n                        app.active_source = 'mobile'\n                        app.update_calculation()\n\n                ModeButton:\n                    text: '[b]Mobile: Resto[/b]  [color=#00ff7f][b][15000 DA][/b][/color]'\n                    group: 'mode'\n                    on_press: \n                        app.current_mode = 'mobile_resto'\n                        app.active_source = 'mobile_resto'\n                        app.update_calculation()\n\n            BoxLayout:\n                size_hint_y: None\n                height: '40dp'\n                \n                Label:\n                    text: '[b]Postes Clients (PC):[/b]'\n                    markup: True\n                    halign: 'left'\n                    text_size: self.size\n                    valign: 'middle'\n                \n                Label:\n                    text: '[color=#00ff7f][b]10000 DA[/b][/color]'\n                    markup: True\n                    size_hint_x: None\n                    width: '80dp'\n                    halign: 'right'\n                    valign: 'middle'\n                    text_size: self.size\n\n            BoxLayout:\n                size_hint_y: None\n                height: '40dp'\n                spacing: '10dp'\n                \n                Label:\n                    text: 'Nombre: ' + '[color=#ffd700][b]' + str(int(client_slider.value)) + '[/b][/color]'\n                    markup: True\n                    size_hint_x: None\n                    width: '100dp'\n                    halign: 'left'\n                    text_size: self.size\n\n                Slider:\n                    id: client_slider\n                    min: 0\n                    max: 50\n                    value: 0\n                    step: 1\n                    cursor_size: '25dp', '25dp'\n                    on_value: \n                        app.client_count = int(self.value)\n                        app.active_source = 'main'\n                        app.update_calculation()\n\n            SectionHeader:\n                text: '[b]  2. Options (Modules)[/b]'\n\n            GridLayout:\n                cols: 2\n                size_hint_y: None\n                height: self.minimum_height\n                spacing: '8dp'\n\n                PriceButton:\n                    text: '[b]Fidélité[/b]\\n[color=#00ff7f][b][5000 DA][/b][/color]'\n                    on_release: app.select_feature('fidelity')\n                \n                PriceButton:\n                    text: '[b]Série/Garantie[/b]\\n[color=#00ff7f][b][5000 DA][/b][/color]'\n                    on_release: app.select_feature('serials')\n                \n                PriceButton:\n                    text: '[b]Facture Live[/b]\\n[color=#00ff7f][b][5000 DA][/b][/color]'\n                    on_release: app.select_feature('live_display')\n                \n                PriceButton:\n                    text: '[b]Écran Promo[/b]\\n[color=#00ff7f][b][5000 DA][/b][/color]'\n                    on_release: app.select_feature('secondary_screen')\n                \n                PriceButton:\n                    text: '[b]Vérif. Prix[/b]\\n[color=#00ff7f][b][10000 DA][/b][/color]'\n                    on_release: app.select_feature('price_check')\n                \n                PriceButton:\n                    text: '[b]Balance[/b]\\n[color=#00ff7f][b][10000 DA][/b][/color]'\n                    on_release: app.select_feature('scale')\n\n                PriceButton:\n                    text: '[b]Pointage[/b]\\n[color=#00ff7f][b][10000 DA][/b][/color]'\n                    on_release: app.select_feature('attendance')\n\n            Label:\n                size_hint_y: None\n                height: '20dp'\n\n            Label:\n                text: '[b]' + app.result_title + '[/b]'\n                markup: True\n                font_size: '14sp'\n                color: 0.6, 0.6, 0.6, 1\n                size_hint_y: None\n                height: '25dp'\n\n            TextInput:\n                id: result_box\n                text: app.generated_key\n                font_size: '16sp'\n                readonly: True\n                background_color: 0.15, 0.15, 0.15, 1\n                foreground_color: 1, 0.8, 0, 1\n                size_hint_y: None\n                height: '55dp'\n                halign: 'center'\n                multiline: False\n\n            Button:\n                text: '[b]COPIER LA CLÉ[/b]'\n                markup: True\n                background_normal: ''\n                background_color: 0, 0.48, 0.8, 1\n                font_size: '16sp'\n                size_hint_y: None\n                height: '60dp'\n                on_release: app.copy_key()\n\n            Label:\n                text: app.status_msg\n                font_size: '13sp'\n                color: 0, 1, 0, 1\n                size_hint_y: None\n                height: '30dp'\n"

class KeygenApp(App):
    generated_key = StringProperty('')
    result_title = StringProperty('Clé Générée:')
    status_msg = StringProperty('Prêt.')
    current_mode = StringProperty('stock')
    client_count = 0
    active_source = StringProperty('main')
    selected_feature = StringProperty('none')

    def build(self):
        return Builder.load_string(KV_CODE)

    def paste_hwid(self):
        try:
            content = Clipboard.paste()
            main_screen = self.root.get_screen('main')
            if content:
                main_screen.ids.hwid_input.text = content
                self.update_calculation()
        except:
            pass

    def select_feature(self, feature_code):
        self.selected_feature = feature_code
        self.active_source = 'feature'
        self.update_calculation()

    def update_calculation(self, *args):
        try:
            main_screen = self.root.get_screen('main')
            hwid = main_screen.ids.hwid_input.text.strip()
            key = ''
            if self.active_source == 'mobile_resto' or self.current_mode == 'mobile_resto':
                key = generate_mobile_resto_key(hwid)
                self.result_title = 'Clé Mobile (Resto):'
            elif self.active_source == 'mobile' or self.current_mode == 'mobile':
                key = generate_mobile_key(hwid)
                self.result_title = 'Clé Mobile (Stock):'
            elif self.active_source == 'main':
                calc_mode = 'stock'
                if self.current_mode == 'restaurant':
                    calc_mode = 'restaurant'
                key = generate_main_license(hwid, self.client_count, calc_mode)
                self.result_title = f'Licence PC ({calc_mode.upper()}):'
            elif self.active_source == 'feature':
                key = generate_feature_key(hwid, self.selected_feature)
                self.result_title = f'Option ({self.selected_feature}):'
            self.generated_key = key
            self.status_msg = 'Généré.' if 'En attente' not in key else 'En attente de données...'
        except:
            pass

    def copy_key(self):
        if self.generated_key and 'En attente' not in self.generated_key:
            Clipboard.copy(self.generated_key)
            self.status_msg = 'Copié !'

if __name__ == '__main__':
    KeygenApp().run()
