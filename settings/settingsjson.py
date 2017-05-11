#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json

settings_json = json.dumps([

    {'type': 'title',
     'title': 'Wygląd'},

    {'type': 'bool',
     'title': 'Tryb ciemny',
     'desc': 'Zmiana trybu kolorystycznego',
     'section': 'wyglad',
     'key': 'boolwyglad'},


    {'type': 'title',
     'title': 'Ekran'},

    {'type': 'options',
     'title': 'Tryb wygaszania ekranu',
     'section': 'ekran',
     'key': 'optionsekran',
     'options': ['zawsze włączony', 'przygaszony, \ngdy nieaktywny']},


    {'type': 'title',
     'title': 'Nawigacja'},

    {'type': 'path',
     'title': 'Zapis plików GPX',
     'desc': 'Folder do zapisu plików GPX',
     'section': 'nawigacja',
     'key': 'pathnawigacja'},

    {'type': 'path',
     'title': 'Mapy offline',
     'desc': 'Folder z mapami offline',
     'section': 'nawigacja',
     'key': 'pathnawigacja1'}])


settings_json1 = json.dumps([

    {'type': 'options',
     'title': "Wiadomość SMS",
     'desc': "Czytanie przychodzących wiadomości SMS",
     'section': 'glos',
     'key': 'optionsglos1',
     'options': ['zawsze włączone', 'tylko w słuchawkach', 'nigdy']},

    {'type': 'options',
     'title': 'Powiadomienia o burzach',
     'section': 'glos',
     'key': 'optionsglos2',
     'options': ['zawsze włączone', 'tylko w słuchawkach', 'nigdy']},

    {'type': 'options',
     'title': 'Nazwa dzwoniącego',
     'desc': 'Wypowiadanie nazwy kontaktu przychodzącego połączenia',
     'section': 'glos',
     'key': 'optionsglos3',
     'options': ['zawsze włączone', 'tylko w słuchawkach', 'nigdy']}])

