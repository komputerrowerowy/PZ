#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from settingsjson import settings_json, settings_json1
from kivy.uix.settings import SettingsWithSpinner
from kivy.uix.settings import SettingsWithNoMenu
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.settings import Settings
from kivy.properties import ListProperty, BooleanProperty
from kivy.logger import Logger

'''
Builder.load_string('''

''')
<Ustawienia>:

    id: Ustawienia
    canvas.before:
        Color:
            rgba: 0.235, 0.529, 0.572, 1
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'resources/Ustawienia.png'

    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, .3
        Label:
            size_hint: 0.15, 1
            background_color: 0.235, 0.529, 0.572, 0

        GridLayout:
            cols:1
            orientation: 'horizontal'

            Button:
                #id: label
                text: "Ustawienia"
                font_size: '25 sp'
                size_hint: 1, 0.3
                color: 1, 1, 1, 1
                background_normal: ''
                background_color: root.kolor
                on_release: app.open_settings()

            Label:
                size_hint: 1, 0.5

        Label:
            size_hint: 0.15, 1
            background_color: 0.235, 0.529, 0.572, 0
'''
#0.235, 0.529, 0.622, 0.6


class Ustawienia(BoxLayout):
    pass


class ScreensettingsApp(App, GridLayout):

    def build(self):
        self.settings_cls = SettingsWithSpinner
        self.use_kivy_settings = False

        motyw = self.config.get('wyglad', 'boolwyglad')

        if motyw == int(1):
            pass
            #Ustawienia.kolor = (0.235, 0.529, 0.622, 0.6)

        if motyw == int(0):
            pass
            #Ustawienia.kolor = (0, 0, 0, 1)

        return Ustawienia()

    def build_config(self, config):
        config.setdefaults('ekran', {
            'optionsekran': 'zawsze włączony'})

        config.setdefaults('wyglad', {'boolwyglad': False})

        config.setdefaults('nawigacja', {
            'pathnawigacja': '/some/path/'})

        config.setdefaults('nawigacja', {
            'pathnawigacja1': '/some/path'})

        config.setdefaults('glos', {
            'optionsglos1': 'zawsze włączone'})

        config.setdefaults('glos', {
            'optionsglos2': 'zawsze włączone'})

        config.setdefaults('glos', {
            'optionsglos3': 'zawsze włączone'})


    def build_settings(self, settings):
        self.textcolor = 0,0,0,0
        settings.add_json_panel('Ogólne', self.config, data=settings_json)
        settings.add_json_panel('Komunikaty Głosowe', self.config, data=settings_json1)


    def on_config_change(self, config, section, key, value):

        if section == 'ekran' and key =='optionsekran' and value == 'zawsze włączony':
            '''print self'''

        if section == 'wyglad' and key =='boolwyglad' and value == '1':
            print ('Tryb ciemny')
            #Ustawienia.kolor = (0.235, 0.529, 0.622, 0.6)

        if section == 'wyglad' and key == 'boolwyglad' and value == '0':
            print ('Tryb jasny')
            #Ustawienia.kolor = (0,0,0,1)

        if section == 'nawigacja':
            if key =='pathnawigacja':
                print()
            if key =='pathnawigacja1':
                print()

        if section == 'glos':
            if key =='optionsglos1' and value == 'zawsze włączone':
                '''print self'''
            if key =='optionsglos2' and value == 'zawsze włączone':
                '''print self'''
            if key =='optionsglos3'and value == 'zawsze włączone':
                print (self)


ScreensettingsApp().run()
