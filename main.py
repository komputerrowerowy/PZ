# -*- coding: utf-8 -*-

import datetime
from kivy.app import App
from kivy.clock import mainthread
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from math import radians, sin, cos, acos, degrees, pi

import requests
from kivy.garden.mapview import MapLayer
from kivy.graphics.context_instructions import Translate, Scale
from kivy.graphics.transformation import Matrix
from kivy.properties import StringProperty, BooleanProperty
from plyer import call
from plyer import gps
from jnius import autoclass
from jnius import cast, PythonJavaClass, java_method
from kivy.utils import platform
from functools import partial
from os import listdir, path
from kivy.clock import Clock
from kivy.core.audio import SoundLoader, Sound
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.popup import Popup
import time
import threading
from Contact import Contact
from Group import Group
import geocoder
from plyer import sms
import sqlite3
import sys
import os
from utwor import Utwor

from math import sqrt
from math import atan

from plyer import compass

from kivy.animation import Animation
from kivy.graphics.transformation import Matrix
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Translate, Scale
from kivy.core.window import Window

from speed import Speed
from settingsjson import settings_json
import ctypes
from route import Router
from loadOsm import LoadOsm
import json

#import pyowm

#owm = pyowm.OWM('b26433c9a2c69c16c1d138cc5710fd57', language='pl')  #moj kod!!!

# 3c8792 niebieski kolor xD
print "wersja_aaa"

Hardware = autoclass('org.renpy.android.Hardware')

AcceptIncomingCall = autoclass("org.test.Phone")

TelephonyManager = autoclass('android.telephony.TelephonyManager')
Context = autoclass('android.content.Context')
activity = autoclass("org.renpy.android.PythonActivity").mActivity
Grupy = autoclass("android.provider.ContactsContract$Groups")

print "test1"
print "ugabuga"
GraphHopperAndroid = autoclass("com.graphhopper.android.GraphHopperAndroid")(activity.mPath)
GraphHopperAndroid.loadGraphStorage()
print "test2"
print GraphHopperAndroid

AcceptIncomingCall2 = activity

contacts = []
contacts2 = []
contacts3 = []
contactsGroups = {}
contactsGroups2 = {}
groups = []
sensorEnabled = False
wsp2 = 0
GrupyId = []
'''Popup odbieranie telefonu'''
Builder.load_string('''
<ConfirmPopup>:
    cols:1

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 1
        Button:
            background_normal: ''
            background_color: .22, .74, .13, 1
            size_hint_y: 0.6
            on_release: root.dispatch('on_answer','Odbierz')
            Image:
                id: sdasdaa
                center_x: (self.parent.center_x)
                center_y: (self.parent.center_y - 0)
                source: 'resources/odbierz.png'
                height: self.parent.height
                #width: self.parent.width

        Button:
            background_normal: ''
            background_color: .83, .18, .18,1
            size_hint_y: 0.4
            on_release: root.dispatch('on_answer', 'Odrzuc')
            Image:
                id: sdasdaa
                center_x: (self.parent.center_x)
                center_y: (self.parent.center_y - 0)
                source: 'resources/odrzuc.png'
                height: self.parent.height
                #width: self.parent.width


<StartScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'resources/start.jpg'
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1.0, .3
        pos: 0, self.height * 1.7
        Button:
            size_hint_x: 0.1
            size_hint_y: 0.5
            background_color: 0.235, 0.529, 0.572, 0

        Button:
            text: "Rozpocznij"
            size_hint_x: 0.8
            size_hint_y: 0.3
            color: 1, 1, 1, 1
            background_normal: ''
            background_color: 0.45, 0.11, 0.06, .6
            on_release: root.parent.remove_widget(root.parent.children[0])
            #Image:
                #id: sdasdaaqq
                #opacity: 0.8
                #center_x: (self.parent.center_x / 3.7)
                #center_y: (self.parent.center_y * 0.87)
                #source: 'resources/btn.png'
                #height: self.parent.height
                #width: self.parent.width

        Button:
            size_hint_x: 0.1
            size_hint_y: 0.5
            background_color: 0.235, 0.529, 0.572, 0
''')


#
# class AndroidSms(Sms):
#
#     def _send(self, **kwargs):
#         sms = SmsManager.getDefault()
#
#         recipient = kwargs.get('665544954')
#         message = kwargs.get('test smsa xD Syntezator przeczytał?')
#
#         if sms:
#             sms.sendTextMessage(recipient, None, message, None, None)





class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass



class StartScreen(Screen):
    pass


class ShowTime(Screen):
    popup_shown = False
    flagaCall = 1
    prev = 0

    def __init__(self, **kwargs):
        super(ShowTime, self).__init__()
        self.add_widget(StartScreen())
        #MainApp.get_running_app().root.carousel.slides[0].hide_search_bar()

    def build(self):
        pass

    def showScreenSettingsDisplay(self):
        self.clear_widgets()
        screen = ScreenSettingsDisplay()
        self.add_widget(screen)

    def showScreenSettingsAlerts(self):
        self.clear_widgets()
        screen = ScreenSettingsAlerts()
        self.add_widget(screen)

    def showScreenSettingsSocial(self):
        self.clear_widgets()
        screen = ScreenSettingsSocial()
        self.add_widget(screen)

    def showScreenSettingsSMS(self):
        self.clear_widgets()
        screen = ScreenSettingsSMS()
        self.add_widget(screen)

    def showScreenSettings(self):
        self.clear_widgets()
        show_time = ShowTime()
        self.add_widget(show_time)

    def showCallInterface(self):
        self.clear_widgets()
        show_time = ShowTime()
        self.add_widget(show_time)

    def goToScreen(self):
        c = self.carousel

        if "screenSettings" in c.current_slide.name:
            slides = c.current_slide.carousel.slides
            c.current_slide.carousel.anim_move_duration = 0
            c.current_slide.carousel.load_slide(slides[1])
            c.current_slide.carousel.anim_move_duration = 0.5

        if "callScreen" in c.current_slide.name:
            slides = c.current_slide.carousel.slides
            c.current_slide.carousel.anim_move_duration = 0
            c.current_slide.carousel.load_slide(slides[1])
            c.current_slide.carousel.anim_move_duration = 0.5

    def send_sms(self, sms_recipient, sms_message):
        # sms.send(recipient=self.sms_recipient, message=self.sms_message)
        # sms.send(self.sms_recipient, self.sms_message)
        print "SMS"
        sms.send(recipient=sms_recipient, message=sms_message)

    def callListener(self):

        print activity.number
        if activity.callState == 1 and self.popup_shown == False:
            self.popup_shown = True
            contact = activity.getContactName(activity.number)
            # activity.speaker.speak("Dzwoni: : " + contact + "!")
            if contact == "Nieznany numer":
                contact = activity.number

            content = ConfirmPopup()
            content.bind(on_answer=self._on_answer)
            self.popup = Popup(title="Dzwoni: " + contact,
                               content=content,
                               size_hint=(0.9, 0.75),
                               auto_dismiss=False)
            self.popup.open()
            
            activity.lastWord = ""
            activity.switchSearch("ODBIERZ")
            self.incoming_call_clock = Clock.schedule_interval(self.accept_call_voice, 1)
            # time.sleep(1)

    def check(self, sms_recipient, sms_message):

        print"nieWiem"
        # self.send_sms()
        self.callListener()
        self.send_sms(sms_recipient, sms_message)
        # sms2 = AndroidSms()
        # sms2.send('663889095', 'wiadomosc sms')
        
    def accept_call_voice(self, lalala):
        #print "dupa" + " " + activity.lastWord
        if activity.callState == 1:
            #print "dupa" + " " + activity.lastWord
            if activity.lastWord == "ODBIERZ" or activity.lastWord == "ODBIERZ(2)":
                print "odbierz"
                activity.lastWord = ""
                self.flagaCall = 1
                AcceptIncomingCall2.acceptCall()
                activity.switchSearch("JEDEN")

                self.incoming_call_clock.cancel()
            else:
                if activity.lastWord == "ODRZUC" or activity.lastWord == "ODRZUC(2)" or activity.lastWord == "ROZLACZ" or activity.lastWord == "ROZLACZ(2)":
                    print "odrzuc"
                    activity.lastWord = ""
                    self.flagaCall = 1
                    self.rejectIncomingCall()
                    activity.switchSearch("JEDEN")

                    self.incoming_call_clock.cancel()

    def _on_answer(self, instance, answer):
        print "USER ANSWER: ", repr(answer)
        if answer == "Odbierz":

            self.flagaCall = 1
            self.popup.dismiss()
            AcceptIncomingCall2.acceptCall()
        else:
            if answer == "Odrzuc":

                self.flagaCall = 1

                self.rejectIncomingCall()
                self.popup.dismiss()
        self.popup.dismiss()
        self.popup_shown = False

    def rejectIncomingCall(self):

        telephonyManager = activity.getSystemService(Context.TELEPHONY_SERVICE)

        telephonyService = activity.createITelephonyInstance(telephonyManager)

        telephonyService.endCall()
        # self.popup.dismiss()
    if activity.lastWord = "DALEJ" or activity.lastWord = "DALEJ(2)":
        MainApp.get_running_app().root.carousel.next_slide
        activity.lastWord = ""
    if activity.lastWord = "WSTECZ" or activity.lastWord = "WSTECZ(2)":
        MainApp.get_running_app().root.carousel.previous_slide
        activity.lastWord = ""
    if activity.Word = "POPRZEDNI" or activity.lastWord = "POPRZEDNI(2)" or activity.lastWord = "POPRZEDNIA(2)" or activity.lastWord = "POPRZEDNIA":
        backSong(self)
        activity.lastWord = ""
    if activity.Word = "NASTĘPNY" or activity.lastWord = "NASTĘPNY(2)" or activity.lastWord = "NASTĘPNA(2)" or activity.lastWord = "NASTĘPNA":
        backSong(self)
        activity.lastWord = ""
    if activity.lastWord = "STOP" or activity.lastWord = "STOP(2)" or activity.lastWord = "START(2)" or activity.lastWord = "START" or activity.lastWord = "MUZYKA" or activity.lastWord = "MUZYKA(2)":
        stopSong(self)
        activity.lastWord = ""

    def check2(self, fla):
        # pass
        if activity.isIncoming:
            if self.flagaCall == 1:
                self.flagaCall = 2
                numTel = str(activity.number)
                num = str(numTel)
                num = num.replace(" ", "")
                num = num.replace("-", "")
                if num[0] == "+":
                    num = num[-9:]

                numTel = num

                # for contact in contacts3:
                #     try:
                #         print "dane_kontaktow_test"
                #         print "name: " + str(contact.display_name)
                #         print "tel: " + str(contact.number)
                #         print "grupa: " + str(contact.group_id)
                #     except:
                #         pass

                for contact in contacts3:
                    if str(numTel) == str(contact.number):
                        GrupyId.append(contact.group_id)

                conn = sqlite3.connect('baza.db')
                c = conn.cursor()

                c.execute("SELECT REAKCJA FROM Grupy WHERE ID_GRUPY = '999'")
                dane = c.fetchall()

                try:
                    nrGrupy = contactsGroups2[contactsGroups[numTel]]
                    print nrGrupy
                except:
                    nrGrupy = 999
                    GrupyId.append(nrGrupy)
                    print "wyjatek: ", sys.exc_info()
                    # wykona sie jesli dzwoni obcy nr
                    # for x in dane:
                    #     if str(nrGrupy) == str(x[0]):
                    #         self.callListener()
                    #     else:
                    #         self.rejectIncomingCall()

                c.execute("SELECT ID_GRUPY FROM Grupy WHERE REAKCJA = '1'")
                dane = c.fetchall()

                conn.commit()
                conn.close()

                zmienna = BooleanProperty(True)
                zmienna1 = BooleanProperty(True)

                print "dane z bazy: "
                print dane
                print "==============="


                for x in dane:
                    for y in GrupyId:
                        if str(y) == str(x[0]):
                            self.callListener()
                            # AcceptIncomingCall2.acceptCall()
                            # print 'autoodebranie'
                            zmienna = False
                            print zmienna
                            # self.flagaCall = 1
                            break

                # if zmienna:
                #     for x in dane1:
                #         for y in GrupyId:
                #             if int(y) == int(x[0]):
                #                 # tutaj miejsce na wywolanie metody odrzucajacej polaczenie z wyslaniem powiadomienia SMS
                #                 self.rejectIncomingCall()
                #                 print 'odrzucenieSMS'
                #                 self.send_sms(numTel, "Jadę rowerem, oddzwonię później.")
                #                 #self.send_sms()
                #                 zmienna1 = False
                #                 print zmienna1
                #                 self.flagaCall = 1
                #                 break

                # if bool(zmienna) == bool(zmienna1):
                if bool(zmienna):
                    self.rejectIncomingCall()
                    print 'odrzucenie'
                    # print 'odrzucenieSMS'
                    # self.send_sms(numTel, "Jadę rowerem, oddzwonię później.")
                    self.flagaCall = 1

        else:
            if self.popup_shown == True:
                self.popup.dismiss()
                self.popup_shown = False
                self.flagaCall = 1


class ChooseFile(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)


class ChooseNumber(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def addNumber1(self):
        self.ids.nrTelefonu.text += self.ids.btn1.text

    def addNumber1(self):
        self.ids.nrTelefonu.text += self.ids.btn1.text

    def addNumber2(self):
        self.ids.nrTelefonu.text += self.ids.btn2.text

    def addNumber3(self):
        self.ids.nrTelefonu.text += self.ids.btn3.text

    def addNumber4(self):
        self.ids.nrTelefonu.text += self.ids.btn4.text

    def addNumber5(self):
        self.ids.nrTelefonu.text += self.ids.btn5.text

    def addNumber6(self):
        self.ids.nrTelefonu.text += self.ids.btn6.text

    def addNumber7(self):
        self.ids.nrTelefonu.text += self.ids.btn7.text

    def addNumber8(self):
        self.ids.nrTelefonu.text += self.ids.btn8.text

    def addNumber9(self):
        self.ids.nrTelefonu.text += self.ids.btn9.text

    def addNumber11(self):
        self.ids.nrTelefonu.text += self.ids.btn11.text

    def addNumber12(self):
        self.ids.nrTelefonu.text += self.ids.btn12.text

    def addNumber0(self):
        self.ids.nrTelefonu.text += self.ids.btn0.text

    def delNumber(self):
        self.ids.nrTelefonu.text = self.ids.nrTelefonu.text[:-1]

    def callPhonePopup(bt):
        Uri = autoclass('android.net.Uri')
        Intent = autoclass('android.content.Intent')
        PythonActivity = autoclass('org.renpy.android.PythonActivity')

        num = "tel:"
        num = num + bt.ids.nrTelefonu.text
        intent = Intent(Intent.ACTION_CALL)
        intent.setData(Uri.parse(num))
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(intent)


class MusicPlayer(Screen):
    directory = ''  # lokacja folderu z piosenkami
    nowPlaying = ''  # Aktualnie wybrana piosenka
    songs = []  # Lista utworów
    songs2 = []  # Lista utworów
    flaga = 1
    indeks = 0

    #funkcja wywoływana na przycisku stop/play
    def stopSong(self):
        self.flaga = 88
        self.ids.playSongg.source = "resources/play.png"
        if self.nowPlaying == '':
            #title = self.songs[0]
            self.nowPlaying = SoundLoader.load(self.songs[0].pelna_sciezka)
            self.ids.nowplay.text = self.songs[0].nazwa
            self.ids.playSongg.source = "resources/stop_music.png"
        if self.nowPlaying.state == 'stop':
            self.flaga = 5

            self.nowPlaying.play()
            if self.flaga == 5:
                self.flaga = 6
                if self.flaga == 6:
                    self.nowPlaying.bind(on_stop=self.stop_event_flaga)
                    self.ids.playSongg.source = "resources/stop_music.png"

        else:
            self.flaga = 99
            self.nowPlaying.stop()
            self.ids.playSongg.source = "resources/play.png"

    # funkcja wywoływana na przycisku Następny utwór
    def nextSong(self):
        self.flaga = 1
        if self.nowPlaying == '':
            pass
        else:
            self.nowPlaying.stop()
        print("nextkSong")
        if self.flaga == 1:
            self.nowPlaying.bind(on_stop=self.stop_event_flaga)

    # funkcja wywoływana na przycisku Poprzedni utwór
    def backSong(self):
        self.flaga = 0
        dl = len(self.songs) - 1
        if self.nowPlaying == '':
            pass
        else:
            self.nowPlaying.stop()
        print("backSong")
        if self.flaga == 0:
            self.nowPlaying.bind(on_stop=self.stop_event_flaga)

    #odczytanie ścieżki folderu z pliku
    def getpath(self):
        try:
            f = open("sav.dat", "r")
            self.ids.direct.text = str(f.readline())
            f.close()
            #self.ids.searchBtn.text = "Wybierz folder"
            self.getSongs()
        except:
            self.ids.direct.text = ''
            #jak odkomentuje wyswieli wszystkie utwory
            #self.getSongs()

    #zapisanie ścieżki folderu do pliku
    def savepath(self, path):
        f = open("sav.dat", "w")
        f.write(path)
        f.close()

    def dismiss_popup(self):
        self._popup.dismiss()

    def fileSelect(self):
        content = ChooseFile(select=self.select,
                             cancel=self.dismiss_popup)

        self._popup = Popup(title="Wybierz folder", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def select(self, path):
        self.directory = path
        #self.ids.direct.text = self.directory
        #self.ids.searchBtn.text = "Wybierz folder"
        self.savepath(self.directory)
        self.songs = []
        self.getSongs()
        self.dismiss_popup()

    # proba wyczyszczenia listy utworow po dodaniu nowego folderu
    def onPressSongs(self):
        self.fileSelect()

    #główna funkcja służąca do otwarzania muzyki i tworzenia listy utworów
    def getSongs(self):

        self.directory = self.ids.direct.text  # przypisanie katalogu z etykiety


        # sprawdza czy ścieżka katalogu kończy się znakiem '/'
        if not self.directory.endswith('/'):
            self.directory += '/'



            self.ids.status.text = ''

            self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

            # get mp3 files from directory
            print "utwory"
            for root, dirs, files in os.walk('/storage'):
                for f in files:
                    filename = os.path.join(root, f)
                    if filename.endswith('.mp3'):
                        self.songs.append(Utwor(f, filename))

            # Jeśli nie znaleziono plików mp3 w wybranym katalogu
            if self.songs == []:
                self.ids.status.text = 'Nie znaleziono muzyki!'
                self.ids.status.color = (1, 0, 0, 1)


            self.songs.sort(key=lambda song: song.nazwa)


        #funkcja uruchamiana w momencie kliknięcia utworu na liście
        def playSong(bt):
            self.flaga = 3
            licznikk = 0
            try:
                self.nowPlaying.stop()
            except:
                pass
            finally:
                nazwautworu = bt.text + '.mp3'

                for song in self.songs:
                    if song.nazwa == nazwautworu:
                        pathSong = str(song.pelna_sciezka)

                self.nowPlaying = SoundLoader.load(pathSong)
                self.nowPlaying.play()
                self.ids.nowplay.text = nazwautworu
                if self.flaga == 3:
                    self.flaga = 4
                    if self.flaga == 4:
                        self.nowPlaying.bind(on_stop=self.stop_event_flaga)
                        self.ids.playSongg.source = "resources/stop_music.png"

        #tworzenie listy utworów
        for song in self.songs:

            btn1 = Button(text=song.nazwa[:-4])
            btn = Button(text=song.nazwa[:-4], on_release=playSong)
            #icon = Button(size_hint_x=None, size_hint_y=None, background_down="ico.png", background_normal="ico.png")

            # kolorowanie elementów listy
            if self.songs.index(song) % 2 == 0:
                btn.color = (0.235, 0.529, 0.572, 0)
                #btn.background_normal = ''
                btn.background_down = "resources/playy.png"
                btn.background_normal = "resources/playy.png"
                btn.background_color = (1, 1, 1, 1)
                btn.size_hint_x = 0.18

                btn1.color = (0.235, 0.529, 0.572, 1)
                btn1.background_normal = ''
                btn1.background_down =''
                btn1.background_color = (1, 1, 1, 1)
                btn1.size_hint_x = 0.82
            else:
                btn.color = (0.235, 0.529, 0.572, 0)
                #btn.background_normal = ''
                btn.background_down = "resources/play_music.png"
                btn.background_normal = "resources/play_music.png"
                btn.background_color = (.941, .960, .960, 1)
                btn.size_hint_x = 0.18

                btn1.color = (0.235, 0.529, 0.572, 1)
                btn1.background_normal = ''
                btn1.background_down = ''
                btn1.background_color = (.941, .960, .960, 1)
                btn1.size_hint_x = 0.82

            #dodanie elementów etykiet utworów
            #self.ids.scroll.add_widget(icon)
            self.ids.scroll.add_widget(btn)
            self.ids.scroll.add_widget(btn1)

    #funkcja wywoływana w momencie gdy obecnie odtwarzany utwór się skończy
    def stop_event_flaga(self, song):
        if self.flaga == 1:
            Clock.schedule_once(partial(self.nextSong2, self.nowPlaying))
        if self.flaga == 0:
            Clock.schedule_once(partial(self.backSong2, self.nowPlaying))
        if self.flaga == 4:
            Clock.schedule_once(partial(self.nextSong2, self.nowPlaying))
        if self.flaga == 6:
            Clock.schedule_once(partial(self.nextSong2, self.nowPlaying))

    #funkcja która odtwarza kolejny utwór z listy
    def nextSong2(self, songfile, dt):
        self.flaga = 1
        self.ids.playSongg.source = "resources/stop_music.png"
        dl = len(self.songs)
        a = 0
        b = int(a)
        next2 = 0
        for song in self.songs:

            if self.songs[b].nazwa == self.ids.nowplay.text:
                next1 = b + 1
                next2 = int(next1)
                if next2 >= dl:
                    next2 = 0
                b = 0
            else:
                b += 1

        if self.nowPlaying.state == 'stop':
            pass
        else:
            self.nowPlaying.stop()
        #title = self.songs[next2]
        self.nowPlaying = SoundLoader.load(self.songs[next2].pelna_sciezka)
        self.nowPlaying.play()
        self.ids.nowplay.text = self.songs[next2].nazwa
        print("nextSong2")
        if self.flaga == 1:
            self.nowPlaying.bind(on_stop=self.stop_event_flaga)

    # funkcja która odtwarza poprzedni utwór z listy
    def backSong2(self, songfile, dt):
        self.flaga = 1
        self.ids.playSongg.source = "resources/stop_music.png"
        a = 0
        b = int(a)
        next2 = 0
        for song in self.songs:

            if self.songs[b].nazwa == self.ids.nowplay.text:
                next1 = b - 1
                next2 = int(next1)
                b = 0
            else:
                b += 1

        if self.nowPlaying.state == 'stop':
            pass
        else:
            self.nowPlaying.stop()
        #title = self.songs[next2]
        self.nowPlaying = SoundLoader.load(self.songs[next2].pelna_sciezka)
        self.nowPlaying.play()
        self.ids.nowplay.text = self.songs[next2].nazwa
        print("backSong2")
        if self.flaga == 1:
            self.nowPlaying.bind(on_stop=self.stop_event_flaga)


class GroupScreen(Screen):
    auto_center = BooleanProperty(False)
    lonGPS = ''
    latGPS = ''
    flagaGPS = 0
    previous_angle = 0
    needle_angle2 = 0
    wsp2 = 0
    znacznik3 = 0
    search_location_position_temp = -1
    search_input_position_temp = -1
    search_bar_shown = True
    czy_wyznacozno_trase = False
    route_calculated = False
    licznikTemp = False
    punkty = []
    actual_point = 0
    actual_instruction = 0
    
    '''def __init__(self, **kwargs):
        super(GroupScreen, self).__init__()
        self.licznikTemp = False'''

    def test111(self):
        print "test69"



        
        
        
    def test2(self):
        GraphHopperAndroid.loadGraphStorage()

    def show_search_bar(self):
        if self.search_bar_shown == False:
            self.ids.SearchLocation.pos[0] = self.ids.SearchLocation.pos[0] + self.height
            self.ids.SearchInput.pos[0] = self.ids.SearchInput.pos[0] + self.height
            self.search_bar_shown = True
        else:
            self.ids.SearchLocation.pos[0] = self.ids.SearchLocation.pos[0] - self.height
            self.ids.SearchInput.pos[0] = self.ids.SearchInput.pos[0] - self.height
            self.search_bar_shown = False

    def hide_search_bar(self):
        print "test1"
        #self.ids.SearchLocation.pos = self.search_location_position_temp
        #self.ids.SearchInput.pos = self.search_search_input_position_temp
        self.ids.SearchLocation.pos[0] = self.ids.SearchLocation.pos[0] - self.height
        self.ids.SearchInput.pos[0] = self.ids.SearchInput.pos[0] - self.height
        self.search_bar_shown = False

    def obliczanie_y1(self, x, y, z):
        if y == 0:
            y = 0.01
        y1 = sqrt(1 / (1 + (x * x) / (y * y)))
        if y < 0:
            y1 = -y1
        return y1

    def obliczanie_x1(self, x, y1):
        x1 = sqrt(1 - y1 * y1)
        if x < 0:
            x1 = -x1
        return x1

    def obliczanie_alpha(self, x1, y1):
        if x1 == 0:
            x1 = 0.01
        if x1 < 0:
            alpha = atan(y1 / x1) + 3.14 + 1.57
        else:
            alpha = atan(y1 / x1) + 1.57
        return alpha

    # rotacja_mapy
    def get_readings(self, dt):
        print "test_rotacjajajajajajajajaja"
        val = compass.orientation
        # x = round(int(val[0]), 2)
        # y = round(int(val[1]), 2)
        # z = round(int(val[2]), 2)

        (x, y, z) = Hardware.magneticFieldSensorReading()

        y1 = round(self.obliczanie_y1(x, y, z), 2)
        x1 = round(self.obliczanie_x1(x, y1), 2)
        alpha = round(self.obliczanie_alpha(x1, y1), 2)
        self.wsp = (alpha * 360 / 6.28 + 180) % 360
        print self.wsp

        print self.wsp

        try:
            self.wsp = (int(self.wsp) / 10) * 10
        except:
            pass
        o_ile_obrot = int(self.wsp) - ShowTime.prev

        '''if (wsp2 > self.needle_angle2):
            self.kat = wsp2 - self.needle_angle2

        if (wsp2 == self.needle_angle2):
            self.kat = wsp2 - self.needle_angle2

        if (wsp2 < self.needle_angle2):
            self.kat = self.needle_angle2 - wsp2

        if self.kat > 10:
            self.needle_angle2 = wsp2'''
        print "wsp2 = " + str(self.wsp2)

        print "o ile obrot = " + str(o_ile_obrot)

        if int(o_ile_obrot) > 10 or int(o_ile_obrot) < -10:
            scatter = MainApp.get_running_app().root.carousel.slides[0].ids["scatter2"]
            # scatter = self.ids["scatter2"]
            r = Matrix().rotate(radians(o_ile_obrot), 0, 0, 1)
            scatter.apply_transform(r, post_multiply=True,
                                    anchor=scatter.to_local(scatter.parent.center_x, scatter.parent.center_y))
        ShowTime.prev = self.wsp

        # print scatter

    def Search(self):
        test = self.ids.SearchInput.text
        g = geocoder.google(self.ids.SearchInput.text + ', PL')
        if test == '':
            pass
        else:
            lonGPS2 = g.lng
            latGPS2 = g.lat
            self.lonGPS = str(lonGPS2)
            self.latGPS = str(latGPS2)
            self.flagaGPS = 1

    def returnLon(self):
        self.Search()
        return self.lonGPS

    def returnLat(self):
        self.Search()
        return self.latGPS

    def returnFlag(self):
        self.Search()
        return self.flagaGPS

    def rotate(self):
        scatter = self.ids["scatter2"]
        r = Matrix().rotate(-radians(30), 0, 0, 1)
        scatter.apply_transform(r, post_multiply=True,
                                anchor=scatter.to_local(scatter.parent.center_x, scatter.parent.center_y))

    def center(self):
        MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(float(MainApp.lat), float(MainApp.lon))
        self.auto_center = True
        self.redraw_route()

    def centerTarget(self):
        try:
            print self.returnLon()
            lon = float(self.returnLon())
            lat = float(self.returnLat())
            MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(lat, lon)
            # self.auto_center = True
            #self.redraw_route()
            self.hide_search_bar()
            MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lat = float(self.latGPS)
            MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lon = float(self.lonGPS)
        except:
            pass

    def centerMy(self):
        if self.auto_center == False:
            if self.czy_wyznacozno_trase == True:
                self.auto_center = True
                self.ids.img_center.source = "resources/center_red.png"
            lon = float(MainApp.lon)
            lat = float(MainApp.lat)
            MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(lat, lon)
            # self.auto_center = True
            self.redraw_route()
        else:

            self.auto_center = False
            self.ids.img_center.source = "resources/center_white.png"
            lon = float(MainApp.lon)
            lat = float(MainApp.lat)
            MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(lat, lon)
            # self.auto_center = True
            self.redraw_route()


    def calculate_route_nodes_run(self):
        #self.calculate_route_nodes(self.latGPS, self.lonGPS, self.latGPS, self.lonGPS)
        try:
            GraphHopperAndroid.calcPath(float(MainApp.lat), float(MainApp.lon), float(self.latGPS), float(self.lonGPS))
            self.licznikTemp = True

            self.punkty = GraphHopperAndroid.resp.getPoints()
            self.route_calculated = True
            print self.punkty.toString()
            self.czy_wyznacozno_trase = True
            self.center()
            self.ids.img_center.source = "resources/center_red.png"
                #self.redraw_route()
            print "respInMain"
            MainApp.route_nodes = True
        except:
            pass

    def calculate_route_nodes(self, lat1, lon1, lat2, lon2):
        MainApp.cos = -1
        self.czy_wyznacozno_trase = True
        self.center()
        self.ids.img_center.source = "resources/center_red.png"

        '''potrzebne do testowania na komputerze'''
        MainApp.on_location(MainApp.get_running_app())

        for layer in MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]._layers:
            if layer.id == 'line_map_layer':
                layer.routeToGpx(lat1, lon1, lat2, lon2, "cycle", "Route", "track")
                break

    def calculate_route_nodes_run(self):
        #self.calculate_route_nodes(self.latGPS, self.lonGPS, self.latGPS, self.lonGPS)
        try:
            GraphHopperAndroid.calcPath(float(MainApp.lat), float(MainApp.lon), float(self.latGPS), float(self.lonGPS))
            self.licznikTemp = True

            self.punkty = GraphHopperAndroid.resp.getPoints()
            self.instructions = GraphHopperAndroid.resp.getInstructions()
            self.route_calculated = True
            print self.punkty.toString()
            self.czy_wyznacozno_trase = True
            self.center()
            self.ids.img_center.source = "resources/center_red.png"
                #self.redraw_route()
            print "respInMain"
            MainApp.route_nodes = True
            self.actual_point = 0
            self.actual_instruction = 0
            self.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(self.actual_instruction)
        except:
            pass

    def calculate_route_nodes(self, lat1, lon1, lat2, lon2):
        MainApp.cos = -1
        self.czy_wyznacozno_trase = True
        self.center()
        self.ids.img_center.source = "resources/center_red.png"

        '''potrzebne do testowania na komputerze'''
        MainApp.on_location(MainApp.get_running_app())

        for layer in MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]._layers:
            if layer.id == 'line_map_layer':
                layer.routeToGpx(lat1, lon1, lat2, lon2, "cycle", "Route", "track")
                break

    def calculate_distance(self, lat1, lat2, lon1, lon2):
        ap = 90.0 - lat1
        bp = 90.0 - lat2
        '''cosap = cos(ap * pi / 180)
        cosbp = cos(bp * pi / 180)
        sinap = sin(ap * pi / 180)
        sinbp = sin(bp * pi / 180)

        print lat1
        print lat2
        print ap
        print bp
        print cosap
        print cosbp
        print sinap
        print sinbp
        print degrees(cos(1.616667))
        print acos((cosap * cosbp + sinap * sinbp * cos(1.616667 * pi / 180)) * pi / 180)

        distance = acos((cosap * cosbp + sinap * sinbp * cos(1.616667 * pi / 180)) * pi / 180) * 111.1'''

        distance = sqrt(pow((lat2 - lat1), 2) + cos(lat1 * pi / 180) * pow((lon2 - lon1), 2)) * 40075.704 / 360

        return distance

    def of_the_track(self, x1, y1, x2, y2, x, y):
        print "ulamek"
        print x1
        print y1
        print x2
        print y2
        print x
        print y
        a = (y2 - y1)
        b = (x2 - x1)
        ab = a / b
        abx = ab * x
        c = x2 * y1 - x1 * y2
        d = x2 - x1
        cd = c / d

        nominator = abs(abx - y + cd)
        dominator = sqrt(pow(((y2 - y1) / x2 - x1), 2) + 1)

        z = nominator / dominator
        print z
        print "z"
        if z >= .6e-05:
            return True
        else:
            return False
                
    def redraw_route(self):
        for layer in self.ids["mapView"]._layers:
            if layer.id == 'line_map_layer':
                layer.draw_line()
                break


class CallScreen(Screen):
    kontakty = []
    telefony = []
    kontakty2 = []
    telefony2 = []
    lista = {}

    #def weather(self):
        #print 'makarena'
        #obs = owm.weather_at_coords(52, 18)
        #print obs.get_reception_time(timeformat='iso')
        #w = obs.get_weather()
        #print w
        #print w.get_clouds()
        #print w.get_rain()
        #print w.get_wind()
        #print w.get_humidity()
        #print w.get_pressure()
        #print w.get_temperature(unit='celsius')
        #MainApp.get_running_app().root.carousel.slides[5].ids["temperature_now"].text = str(5)


    def dismiss_popup(self):
        self._popup.dismiss()

    def numberSelect(self):
        content = ChooseNumber(select=self.select,
                               cancel=self.dismiss_popup)

        self._popup = Popup(title="Wybierz numer", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def select(self, path):
        # self.directory = path
        # self.ids.direct.text = self.directory
        # self.ids.searchBtn.text = "Wybierz folder"
        # self.savepath(self.directory)
        # self.songs = []
        # self.getSongs()
        self.dismiss_popup()

    # def addNum(self):
    #     def addNumber(bt):
    #         self.ids.nrTelefonu.text = bt.text

    def read_groups(self):
        content_resolver = activity.getApplicationContext()
        resolver = content_resolver.getContentResolver()

        grupa = resolver.query(Grupy.CONTENT_URI, None, None, None, None)
        group = grupa

        while (grupa.moveToNext()):

            id = group.getString(group.getColumnIndex("_id"))
            name = group.getString(group.getColumnIndex("TITLE"))
            if id not in groups:
                groups.append(Group(id, name))
        grupa.close()


    def submit_contact(self):
        if platform() == 'android':
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            ContactsContract = autoclass("android.provider.ContactsContract$Contacts")
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")

            ContentResolver = autoclass('android.content.Context')

            content_resolver = activity.getApplicationContext()

            resolver = content_resolver.getContentResolver()

            ApplicationContext = autoclass('android.app.Activity')
            # app = ApplicationContext.getApplicationContext()
            Toast = autoclass("android.widget.Toast")
            Cursor = autoclass("android.database.Cursor")
            Data = autoclass("android.provider.ContactsContract$Data")
            phones = resolver.query(Phone.CONTENT_URI, None, None, None, None)
            # phones = resolver.query(Data.CONTENT_URI, None, None, None, None)
            pho = phones

            def callPhone(bt):
                Context = autoclass('android.content.Context')
                Uri = autoclass('android.net.Uri')
                Intent = autoclass('android.content.Intent')
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
                tel = ''
                for contact in contacts:
                    if bt.text == contact.display_name:
                        tel = contact.number
                num = "tel:"
                num = num + tel
                print "to jest "
                print num
                intent = Intent(Intent.ACTION_CALL)
                intent.setData(Uri.parse(num))
                currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
                currentActivity.startActivity(intent)

            self.read_groups()

            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            projection = [GroupMembership.GROUP_ROW_ID, RawContactsColumns.CONTACT_ID]
            # projection = [GroupMembership.GROUP_ROW_ID, "contact_id"]
            Cursor = autoclass("android.database.Cursor")
            # c = resolver.query(Data.CONTENT_URI, projection, GroupMembership.GROUP_ROW_ID+"="+groups,None, None)
            a = 1
            print "cosik4"
            # while (phones.moveToNext()):
            #     name = pho.getString(pho.getColumnIndex("display_name"))
            #     phoneNumber = pho.getString(pho.getColumnIndex(Phone.NUMBER))
            #     contact_group_id = pho.getString(pho.getColumnIndex(GroupMembership.GROUP_ROW_ID))
            #     contact_group_name = -1
            #     for group in groups:
            #         if contact_group_id == group.id:
            #             contact_group_name = group.name
            #     if name == "Daniel":
            #         print contact_group_id
            #         print "przerwa"

            # if a == 3:
            #     phoneNumber2 = contact_group_id
            #     print "numerrrrrrrr"
            #     print str(phoneNumber2)
            # a = a + 1
            # if a == 4:
            #     a = 1

            # dl = len(contact_group_id)
            # if dl <= 1:
            # current_contact = Contact(str(name), str(phoneNumber), str(contact_group_id), str(contact_group_name))
            # contacts.append(current_contact)

            self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

            contacts.sort(key=lambda contact: contact.display_name)
            for contact in contacts:
                btn1 = Button(text=contact.display_name, on_release=callPhone)
                btn = Button(text=contact.display_name)
                # btn = Button(text=contact.display_name + "  " + contact.group_id + "  " +contact.number, on_release=callPhone)
                if contacts.index(contact) % 2 == 0:
                    btn1.color = (0.235, 0.529, 0.572, 0)
                    #btn1.background_normal = ''
                    btn1.background_down = "resources/ringg.png"
                    btn1.background_normal = "resources/ringg.png"
                    btn1.background_color = (1, 1, 1, 1)
                    btn1.size_hint_x=0.18

                    btn.color = (0.235, 0.529, 0.572, 1)
                    btn.background_normal = ''
                    btn.background_down = ''
                    btn.background_color = (1, 1, 1, 1)
                    btn.size_hint_x = 0.82
                else:
                    btn1.color = (0.235, 0.529, 0.572, 0)
                    #btn1.background_normal = ''
                    btn1.background_down = "resources/icon_ring.png"
                    btn1.background_normal = "resources/icon_ring.png"
                    btn1.background_color = (.941, .960, .960, 1)
                    btn1.size_hint_x = 0.18

                    btn.color = (0.235, 0.529, 0.572, 1)
                    btn.background_normal = ''
                    btn.background_down = ''
                    btn.background_color = (.941, .960, .960, 1)
                    btn.size_hint_x = 0.82

                self.ids.scroll.add_widget(btn1)
                self.ids.scroll.add_widget(btn)
                # contactsGroups[contact.number] = contact.group_id

    def submit_contact2(self):
        if platform() == 'android':
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            ContactsContract = autoclass("android.provider.ContactsContract$Contacts")
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")

            ContentResolver = autoclass('android.content.Context')

            content_resolver = activity.getApplicationContext()

            resolver = content_resolver.getContentResolver()

            ApplicationContext = autoclass('android.app.Activity')
            # app = ApplicationContext.getApplicationContext()
            Toast = autoclass("android.widget.Toast")
            Cursor = autoclass("android.database.Cursor")
            Data = autoclass("android.provider.ContactsContract$Data")
            phones = resolver.query(Phone.CONTENT_URI, None, None, None, None)
            phones2 = resolver.query(Data.CONTENT_URI, None, None, None, None)
            pho = phones
            pho2 = phones2

            self.read_groups()

            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            projection = [GroupMembership.GROUP_ROW_ID, RawContactsColumns.CONTACT_ID]
            # projection = [GroupMembership.GROUP_ROW_ID, "contact_id"]
            Cursor = autoclass("android.database.Cursor")
            # c = resolver.query(Data.CONTENT_URI, projection, GroupMembership.GROUP_ROW_ID+"="+groups,None, None)
            a = 1
            print "cosik4"
            while (phones2.moveToNext()):
                name = pho2.getString(pho2.getColumnIndex("display_name"))
                phoneNumber = pho2.getString(pho2.getColumnIndex(Phone.NUMBER))
                contact_group_id = pho2.getString(pho2.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name

                # dl = len(contact_group_id)
                try:
                    if contact_group_id is not None:
                        dl = len(contact_group_id)
                        print "test1"
                        print contact_group_id
                        if dl <= 1:
                            current_contact = Contact(str(name), str(phoneNumber), str(contact_group_id),
                                                      str(contact_group_name))
                            contacts2.append(current_contact)

                            if name == "Daniel":
                                print name
                                print phoneNumber
                                print "przerwa2"
                except:
                    pass

            while (phones.moveToNext()):
                name = pho.getString(pho.getColumnIndex("display_name"))
                phoneNumber = pho.getString(pho.getColumnIndex(Phone.NUMBER))
                contact_group_id = pho.getString(pho.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name
                if name == "Daniel":
                    print name
                    print phoneNumber
                    print "przerwa"

                # if a == 3:
                #     phoneNumber2 = contact_group_id
                #     print "numerrrrrrrr"
                #     print str(phoneNumber2)
                # a = a + 1
                # if a == 4:
                #     a = 1

                # dl = len(contact_group_id)
                # if dl <= 1:

                num = str(phoneNumber)
                num = num.replace(" ", "")
                num = num.replace("-", "")
                if num[0] == "+":
                    num = num[-9:]

                current_contact = Contact(str(name), str(num), str(contact_group_id), str(contact_group_name))
                contacts.append(current_contact)

            contacts.sort(key=lambda contact: contact.display_name)
            contacts2.sort(key=lambda contact: contact.display_name)

            for contact in contacts:
                contactsGroups[contact.number] = contact.display_name
            for contact in contacts2:
                contactsGroups2[contact.display_name] = contact.number

    def submit_contact3(self):
        if platform() == 'android':
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            ContactsContract = autoclass("android.provider.ContactsContract$Contacts")
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")

            ContentResolver = autoclass('android.content.Context')

            content_resolver = activity.getApplicationContext()

            resolver = content_resolver.getContentResolver()

            ApplicationContext = autoclass('android.app.Activity')
            # app = ApplicationContext.getApplicationContext()
            Toast = autoclass("android.widget.Toast")
            Cursor = autoclass("android.database.Cursor")
            Data = autoclass("android.provider.ContactsContract$Data")
            phones = resolver.query(Phone.CONTENT_URI, None, None, None, None)
            phones2 = resolver.query(Data.CONTENT_URI, None, None, None, None)
            pho = phones
            pho2 = phones2

            self.read_groups()

            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            projection = [GroupMembership.GROUP_ROW_ID, RawContactsColumns.CONTACT_ID]
            # projection = [GroupMembership.GROUP_ROW_ID, "contact_id"]
            Cursor = autoclass("android.database.Cursor")
            # c = resolver.query(Data.CONTENT_URI, projection, GroupMembership.GROUP_ROW_ID+"="+groups,None, None)
            a = 1
            print "cosik4"
            while (phones2.moveToNext()):
                name = pho2.getString(pho2.getColumnIndex("display_name"))
                phoneNumber = pho2.getString(pho2.getColumnIndex(Phone.NUMBER))
                contact_group_id = pho2.getString(pho2.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name

                # dl = len(contact_group_id)
                try:
                    if contact_group_id is not None:
                        dl = len(contact_group_id)
                        if dl <= 1:
                            current_contact = Contact(str(name), str(contact_group_id), str(contact_group_id),
                                                      str(contact_group_name))
                            contacts2.append(current_contact)

                            if name == "Daniel":
                                print name
                                print phoneNumber
                                print "przerwa2"
                except:
                    pass

            while (phones.moveToNext()):
                name = pho.getString(pho.getColumnIndex("display_name"))
                phoneNumber = pho.getString(pho.getColumnIndex(Phone.NUMBER))
                contact_group_id = pho.getString(pho.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name
                if name == "Test":
                    print name
                    print phoneNumber
                    print "przerwa"

                # if a == 3:
                #     phoneNumber2 = contact_group_id
                #     print "numerrrrrrrr"
                #     print str(phoneNumber2)
                # a = a + 1
                # if a == 4:
                #     a = 1

                # dl = len(contact_group_id)
                # if dl <= 1:

                num = str(phoneNumber)
                num = num.replace(" ", "")
                num = num.replace("-", "")
                if num[0] == "+":
                    num = num[-9:]
                current_contact = Contact(str(name), str(num), str(contact_group_id), str(contact_group_name))
                contacts.append(current_contact)

            contacts.sort(key=lambda contact: contact.display_name)
            contacts2.sort(key=lambda contact: contact.display_name)

            for contact in contacts:
                contactsGroups[contact.number] = contact.display_name
            for contact in contacts2:
                contactsGroups2[contact.display_name] = contact.number
                for contact2 in contacts:
                    if (contact.display_name == contact2.display_name):
                        current_contact = Contact(str(contact.display_name), str(contact2.number), str(contact.number),
                                                  str(contact_group_name))
                        contacts3.append(current_contact)

                        for contact in contacts3:
                            try:
                                print "dane_kontaktow_test"
                                print "name: " + str(contact.display_name)
                                print "tel: " + str(contact.number)
                                print "grupa: " + str(contact.group_id)
                            except:
                                pass
                                # print contactsGroups2[contactsGroups["881689020"]]


class Speedometer(Screen):
    gps_speed=1
    def build(self):


        pass

class Weather(Screen):
    def ustal_pogode(self):
        print 'makarena'
        #obs = owm.weather_at_coords(52, 18)
        #print obs.get_reception_time(timeformat='iso')
        #w = obs.get_weather()
        #print w
        #print w.get_clouds()
        #print w.get_rain()
        #print w.get_wind()
        #print w.get_humidity()
        #print w.get_pressure()
        #print w.get_temperature(unit='celsius')
        search_template="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b26433c9a2c69c16c1d138cc5710fd57"
        search_url=search_template.format(53.01,18.53)
        data=requests.get(search_url).json()

        print "pobieranie prognozy"
        search_template_forecast="http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=b26433c9a2c69c16c1d138cc5710fd57"
        search_url_forecast=search_template_forecast.format(53.01,18.53)
        data_forecast=requests.get(search_url_forecast).json()
        print "koniec pobierania prognozy"

        #{u'clouds': {u'all': 20}, u'name': u'Wielka Nieszawka', u'visibility': 10000,
        #u'sys': {u'country': u'PL', u'sunset': 1492191908, u'message': 0.0067000000000000002, u'type': 1, u'id': 5345,
        #         u'sunrise': 1492141678},
        #u'weather': [{u'main': u'Clouds', u'id': 801, u'icon': u'02d', u'description': u'few clouds'}],
        #u'coord': {u'lat': 53.009999999999998, u'lon': 18.530000000000001}, u'base': u'stations', u'dt': 1492178400,
        #u'main': {u'pressure': 1010, u'temp_min': 283.14999999999998, u'temp_max': 283.14999999999998,
        #         u'temp': 283.14999999999998, u'humidity': 66}, u'id': 3082287,
        #u'wind': {u'speed': 6.2000000000000002, u'deg': 300}, u'cod': 200}


        #{u'city': {u'country': u'PL', u'population': 1000, u'id': 3082287,
        #           u'coord': {u'lat': 52.996200000000002, u'lon': 18.509699999999999}, u'name': u'Wielka Nieszawka'},
        # u'message': 0.0020999999999999999, u'list': [
        #    {u'clouds': {u'all': 80}, u'rain': {u'3h': 0.035000000000000003}, u'sys': {u'pod': u'n'},
        #     u'dt_txt': u'2017-04-14 18:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10n', u'description': u'light rain'}],
        #     u'dt': 1492192800,
        #     u'main': {u'temp_kf': 2.5499999999999998, u'temp': 282.38999999999999, u'grnd_level': 1014.83,
        #               u'temp_max': 282.38999999999999, u'sea_level': 1025.3599999999999, u'humidity': 87,
        #               u'pressure': 1014.83, u'temp_min': 279.84500000000003},
        #     u'wind': {u'speed': 4.5599999999999996, u'deg': 278.00099999999998}},
        #    {u'clouds': {u'all': 88}, u'rain': {u'3h': 0.30499999999999999}, u'sys': {u'pod': u'n'},
        #     u'dt_txt': u'2017-04-14 21:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10n', u'description': u'light rain'}],
        #     u'dt': 1492203600, u'main': {u'temp_kf': 1.7, u'temp': 280.38, u'grnd_level': 1014.71, u'temp_max': 280.38,
        #                                  u'sea_level': 1025.23, u'humidity': 91, u'pressure': 1014.71,
        #                                  u'temp_min': 278.685},
        #     u'wind': {u'speed': 3.9700000000000002, u'deg': 244.506}},
        #    {u'clouds': {u'all': 88}, u'rain': {u'3h': 0.98999999999999999}, u'sys': {u'pod': u'n'},
        #     u'dt_txt': u'2017-04-15 00:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10n', u'description': u'light rain'}],
        #     u'dt': 1492214400,
        #     u'main': {u'temp_kf': 0.84999999999999998, u'temp': 279.75999999999999, u'grnd_level': 1013.62,
        #               u'temp_max': 279.75999999999999, u'sea_level': 1024.1300000000001, u'humidity': 95,
        #               u'pressure': 1013.62, u'temp_min': 278.90899999999999},
        #     u'wind': {u'speed': 4.4900000000000002, u'deg': 250.50299999999999}},
        #    {u'clouds': {u'all': 92}, u'rain': {u'3h': 0.82499999999999996}, u'sys': {u'pod': u'n'},
        #     u'dt_txt': u'2017-04-15 03:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10n', u'description': u'light rain'}],
        #     u'dt': 1492225200, u'main': {u'temp_kf': 0, u'temp': 279.18700000000001, u'grnd_level': 1012.55,
        #                                  u'temp_max': 279.18700000000001, u'sea_level': 1023.12, u'humidity': 96,
        #                                  u'pressure': 1012.55, u'temp_min': 279.18700000000001},
        #     u'wind': {u'speed': 3.5899999999999999, u'deg': 245.00200000000001}},
        #    {u'clouds': {u'all': 92}, u'rain': {u'3h': 0.95499999999999996}, u'sys': {u'pod': u'd'},
        #     u'dt_txt': u'2017-04-15 06:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10d', u'description': u'light rain'}],
        #     u'dt': 1492236000, u'main': {u'temp_kf': 0, u'temp': 279.71100000000001, u'grnd_level': 1011.98,
        #                                  u'temp_max': 279.71100000000001, u'sea_level': 1022.5599999999999,
        #                                  u'humidity': 99, u'pressure': 1011.98, u'temp_min': 279.71100000000001},
        #     u'wind': {u'speed': 4.21, u'deg': 256.00299999999999}},
        #    {u'clouds': {u'all': 92}, u'rain': {u'3h': 0.35999999999999999}, u'sys': {u'pod': u'd'},
        #     u'dt_txt': u'2017-04-15 09:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10d', u'description': u'light rain'}],
        #     u'dt': 1492246800, u'main': {u'temp_kf': 0, u'temp': 280.48399999999998, u'grnd_level': 1011.03,
        #                                  u'temp_max': 280.48399999999998, u'sea_level': 1021.46, u'humidity': 100,
        #                                  u'pressure': 1011.03, u'temp_min': 280.48399999999998},
        #     u'wind': {u'speed': 4.0599999999999996, u'deg': 244.00299999999999}},
        #    {u'clouds': {u'all': 92}, u'rain': {u'3h': 0.40999999999999998}, u'sys': {u'pod': u'd'},
        #     u'dt_txt': u'2017-04-15 12:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10d', u'description': u'light rain'}],
        #     u'dt': 1492257600,
        #     u'main': {u'temp_kf': 0, u'temp': 281.892, u'grnd_level': 1008.6799999999999, u'temp_max': 281.892,
        #               u'sea_level': 1019.15, u'humidity': 100, u'pressure': 1008.6799999999999, u'temp_min': 281.892},
        #     u'wind': {u'speed': 5.0700000000000003, u'deg': 222.50200000000001}},
        #    {u'clouds': {u'all': 92}, u'rain': {u'3h': 1.5700000000000001}, u'sys': {u'pod': u'd'},
        #     u'dt_txt': u'2017-04-15 15:00:00',
        #     u'weather': [{u'main': u'Rain', u'id': 500, u'icon': u'10d', u'description': u'light rain'}],
        #     u'dt': 1492268400, u'main': {u'

        print 'zxzxzx'
        print data_forecast['list'][1]
        temp=data['main']['temp']-273.15
        temp_forecast=data_forecast['list'][1]['main']['temp']-273.15
        print 'koniec zxzxzx'
        #location=(data['sys']['country'],data['name'])
        MainApp.get_running_app().root.carousel.slides[5].ids["temperature_now"].text = str(temp)+str('°C')
        MainApp.get_running_app().root.carousel.slides[5].ids["temperature_forecast"].text = str(temp_forecast) + str('°C')

class ScreenSettings(Screen):
    def build(self):
        pass


class ScreenSettingsDisplay(Widget):
    pass


class ScreenSettingsAlerts(Widget):
    pass


class ScreenSettingsSocial(Widget):
    pass


class ScreenSettingsSMS(Widget):
    pass


class ScreenMusic(Widget):
    pass


class ScreenContacts(Widget):
    pass


'''poczatek'''


class CallInterface(BoxLayout):
    pass


class DialCallButton(Button):
    def dial(self, *args):
        call.dialcall()


class MakeCallButton(Button):
    tel = StringProperty()

    def call(self, *args):
        call.makecall(tel=self.tel)


'''koniec'''


class LineMapLayer(MapLayer):
    id = 'line_map_layer'

    def __init__(self, **kwargs):
        super(LineMapLayer, self).__init__()
        self.zoom = 0

    '''Funkcja odpowiadajaca za stworzenie wierzcholkow grafu, ktory jest nasza droga'''

    def parseJSON(self, points):
        response = self.downloadJSON(points)
        i = response.text.find('"coordinates":')
        s = ""
        close_bracket_count = 0
        for index in xrange(i + 15, len(response.text)):
            # s.__add__(response.text[index])

            if response.text[index] == "]":
                if close_bracket_count == 1:
                    break
                close_bracket_count += 1
            else:
                close_bracket_count = 0
            s += response.text[index]
        s = s.encode('utf-8')
        slist = s.split('],[')
        slist[0] = slist[0].replace('[', '')
        slist[len(slist) - 1] = slist[len(slist) - 1].replace(']', '')
        i = 0
        a = []
        for item in slist:
            a.append(item.split(','))
            i += 1

        self.count = 0
        self.parent.node = []
        for item in a:
            self.parent.node.append(item)
            self.count += + 1

    def downloadJSON(self, points):
        my_url = 'https://api.mapbox.com/directions/v5/mapbox/cycling/' + points + '?access_token=pk.eyJ1Ijoid2lsY3plazUwMyIsImEiOiJjaXowNnAyMjcwMDE4MzNsd2xvbTd5ZnY0In0.WiuRsomVkCrkN1j78JJ7Aw&overview=full&geometries=geojson'
        response = requests.get(my_url)
        return response

    def routeToGpx(self, lat1, lon1, lat2, lon2, transport, description="", style="track"):
        points = str(MainApp.lon) + ',' + str(MainApp.lat) + ';' + str(lon2) + ',' + str(lat2)
        self.parseJSON(points)

        # '''Wersja offline'''
        #
        # data = LoadOsm(transport)
        #
        # # data = LoadOsm('cycle')
        # #data = LoadOsm('car')
        # node1 = data.findNode(float(MainApp.lat), float(MainApp.lon))
        # node2 = data.findNode(float(lat2), float(lon2))
        #
        # router = Router(data)
        # result, route = router.doRoute(node1, node2)
        # if result != 'success':
        #     return
        # # self.count = 0
        # self.parent.node = []
        # if (style == 'track'):
        #     self.count = 0
        #     for i in route:
        #         self.parent.node.append(data.rnodes[i])
        #         self.count = self.count + 1
        #
        #
        # elif (style == 'route'):
        #     self.count = 0
        #     for i in route:
        #         self.parent.node.append(data.rnodes[i])
        #         self.count = self.count + 1
        MainApp.route_nodes = True

    '''W momencie przemieszczenia mapy przerysowujemy linie'''

    def reposition(self):
        mapview = self.parent
        if (self.zoom != mapview.zoom and MainApp.route_nodes == True):
            self.draw_line()

    '''Funkcja rysowania linii'''

    def draw_line(self):
        if MainApp.get_running_app().root.carousel.slides[0].route_calculated == True:
            mapview = self.parent
            print "testparent"
            group_screen = self.parent.parent.parent.parent.parent
            self.zoom = mapview.zoom

            '''Na ten moment ustawiamy stale wspolrzedne'''
            geo_dom = [52.9828, 18.5729]
            geo_wydzial = [53.0102, 18.5946]

            point_list = []
            '''Wywolujemy funkcje ktora zwraca nam wspolrzedne trasy o danych wspolzednych poczatkowych i koncowych (Gdzie to przeniesc???)'''
            # self.routeToGpx(float(geo_dom[0]), float(geo_dom[1]), float(geo_wydzial[0]), float(geo_wydzial[1]))

            print "lista punktow"
            '''for j in xrange(len(self.parent.node) - 1):
                point_list.extend(
                    # wersja online:
                    mapview.get_window_xy_from(float(self.parent.node[j][1]), float(self.parent.node[j][0]), mapview.zoom))
                    # wersja offline:
                    # mapview.get_window_xy_from(float(self.parent.node[j][0]), float(self.parent.node[j][1]), mapview.zoom))
                print str(self.parent.node[j][1])
                print str(self.parent.node[j][0])'''
            print float(group_screen.punkty.getLat(10))
            punkty_size = group_screen.punkty.getSize()
            print punkty_size
            point_list.extend(mapview.get_window_xy_from(float(MainApp.lat), float(MainApp.lon), mapview.zoom))
            for j in xrange(group_screen.actual_point, punkty_size - 1):
                lat = float(group_screen.punkty.getLat(j))
                lon = float(group_screen.punkty.getLon(j))
                #print lat
                lat1 = round(group_screen.punkty.getLat(j), 4)
                #print lat1
                point_list.extend(mapview.get_window_xy_from(lat, lon, mapview.zoom))

            print "dupa1"
            print point_list
            
            scatter = mapview._scatter
            x, y, s = scatter.x, scatter.y, scatter.scale

            with self.canvas:
                self.canvas.clear()
                Scale(1 / s, 1 / s, 1)
                Translate(-x, -y)
                Color(0, 0, 255, .6)
                Line(points=point_list, width=3, joint="bevel")


class ZoneList():

    ListaNazw = []
    ListaId = []

    activity = autoclass("org.renpy.android.PythonActivity").mActivity
    Grupy = autoclass("android.provider.ContactsContract$Groups")
    content_resolver = activity.getApplicationContext()
    resolver = content_resolver.getContentResolver()

    grupa = resolver.query(Grupy.CONTENT_URI, None, None, None, None)
    group = grupa

    ListaNazw.append("Numery spoza grup")
    ListaId.append('999')

    while (grupa.moveToNext()):

        g = group.getString(group.getColumnIndex("TITLE"))
        id = group.getString(group.getColumnIndex("_id"))

        if g not in ListaNazw:
            ListaNazw.append(g)
            ListaId.append(id)

    grupa.close()

    conn = sqlite3.connect('baza.db')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Grupy (ID_GRUPY INTEGER, REAKCJA INTEGER)")
    c.execute("SELECT * FROM Grupy")
    baza = c.fetchall()

    if baza == []:
        for x in xrange(0, len(ListaNazw)):
            c.execute("INSERT INTO Grupy VALUES (?, ?)", (ListaId[x], 0))

    else:
        c.execute("SELECT ID_GRUPY FROM Grupy")
        idBaza = c.fetchall()
        c.execute("SELECT REAKCJA FROM Grupy")
        reakcjaBaza = c.fetchall()
        c.execute("DELETE FROM Grupy")

        for x in ListaId:
            c.execute("INSERT INTO Grupy VALUES (?, ?)", (x, 0))

            if unicode(x) in unicode(idBaza):
                for y in xrange(0, len(idBaza)):
                    if "("+x+",)" == str(idBaza[y]):
                        if str(reakcjaBaza[y]) == "(1,)":
                            c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, x))
                            break


    conn.commit()
    conn.close()


class ZoneElements(GridLayout):
    if len(ZoneList.ListaNazw) < 5:
        linia = .01
    else:
        linia = .03


class ZoneCheckBoxes(ToggleButtonBehavior, GridLayout):
    _instance_count = -1
    _zoneNames = ZoneList.ListaNazw
    Window.clearcolor = (1, 1, 1, 1)

    def __init__(self, **kwargs):
        super(ZoneCheckBoxes, self).__init__(**kwargs)
        ZoneCheckBoxes._instance_count += 1

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()

        c.execute("SELECT REAKCJA FROM Grupy")
        dane = c.fetchall()

        ZoneCheckBoxes.kolor = (.235, .529, .572, 1)

        if dane[ZoneCheckBoxes._instance_count] == (0,):
            ZoneCheckBoxes.odrzuc = True
            ZoneCheckBoxes.decyduj = False

        elif dane[ZoneCheckBoxes._instance_count] == (1,):
            ZoneCheckBoxes.odrzuc = False
            ZoneCheckBoxes.decyduj = True

        conn.commit()
        conn.close()

    def odrzucenie(self, x):

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        for i in range(0, len(ZoneList.ListaNazw)):
            if ZoneList.ListaNazw[i] == x[5:len(x)]:
                c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (0, ZoneList.ListaId[i]))

        conn.commit()
        conn.close()

    def decyzja(self, x):

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        for i in range(0, len(ZoneList.ListaNazw)):
            if ZoneList.ListaNazw[i] == x[5:len(x)]:
                c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, ZoneList.ListaId[i]))

        conn.commit()
        conn.close()


class ZoneButton(Button):
    _instance_count = -1
    _zoneNames = ZoneList.ListaNazw
    
    def __init__(self, **kwargs):
        super(ZoneButton, self).__init__(**kwargs)
        ZoneButton._instance_count += 1


class ZoneLayout(BoxLayout):
    if len(ZoneList.ListaNazw) < 5:
        rozmiar = .3
    elif 5 >= len(ZoneList.ListaNazw) < 10:
        rozmiar = .5
    elif 10 >= len(ZoneList.ListaNazw) < 15:
        rozmiar = 1
    else:
        rozmiar = 1.5

    def __init__(self, **kwargs):
        super(ZoneLayout, self).__init__(**kwargs)

        for i in range(len(ZoneList.ListaNazw)):
            self.add_widget(ZoneElements())


class MainApp(App):
    gps_speed = 0.00
    highest_speed = 0.00
    highest_speed_float = 0.00
    gps_status = StringProperty('Click Start to get GPS location updates')
    lat = 53.0102
    lon = 18.5946
    flagCenter = True
    # screensettings.kv tymczasowo zakomentowany w pliku main.kv
    Builder.load_file("screensettings.kv")
    Builder.load_file("groupscreen.kv")
    Builder.load_file("callscreen.kv")
    Builder.load_file("musicplayer.kv")
    Builder.load_file("grupy.kv")
    Builder.load_file("speedometer.kv")
    Builder.load_file("weather.kv")
    znacznik = 0
    route_nodes = BooleanProperty(False)
    prev_time = datetime.datetime.now().time()
    gr = GroupScreen()
    # try:
    #     gr.do_toggle()
    # except:
    #     pass

    def build(self):
        show_time = ShowTime()
        try:
            Hardware.magneticFieldSensorEnable(True)
        except:
            print "nie masz kompasu"
        callS = CallScreen()
        # callS.submit_contact2()
        callS.submit_contact3()
        music = MusicPlayer()
        music.getpath()
        # modyfikacja 3
        gr = GroupScreen()


        Clock.schedule_interval(show_time.check2, 1)
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            self.start(1000, 0)
        except NotImplementedError:
            self.gps_status = 'GPS is not implemented for your platform'

        
        activity.runRecognizerSetup();
            
        return show_time

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, speed, **kwargs):
        duration = (
            datetime.datetime.combine(datetime.date.today(),
                                      datetime.datetime.now().time()) - datetime.datetime.combine(
                datetime.date.today(), MainApp.prev_time)).total_seconds()
        if duration >= 1:
            self.gps_location = '\n'.join([
                                              '{}={}'.format(k, v) for k, v in kwargs.items()])
            for k, v in kwargs.items():
                if k == "lat":
                    MainApp.lat = float(v)
                else:
                    if k == "lon":
                        MainApp.lon = float(v)
            '''W karuzeli dodajemy layer wraz z nasza utworzona klasa LineMapLayer'''
            print "---------------------"
            # label = MainApp.get_running_app().root.carousel.slides[0].ids["label1"]
            # label.text = str(int(label.text) + 1)

            '''Nie jestem pewien czy usuniecie tego nie bedzie powodowalo problemow'''
            '''if MainApp.znacznik > 0:
                for layer in MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]._layers:
                    if layer.id == 'line_map_layer':
                        MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]._layers.remove(layer)
                        break
            #MainApp.znacznik = 1'''

            speed = Speed(float(speed))
            if speed > self.highest_speed_float:
                self.highest_speed_float = speed
            self.gps_speed = speed
            self.highest_speed = self.highest_speed_float
            print "blblbl"
            print self.gps_speed
            self.gps_speed=self.gps_speed*18/5
            self.gps_speed=round(self.gps_speed,2)
            self.highest_speed = self.highest_speed * 18 / 5
            self.highest_speed = round(self.highest_speed, 2)
            MainApp.get_running_app().root.carousel.slides[4].ids["label_speed"].text = str(self.gps_speed)
            MainApp.get_running_app().root.carousel.slides[4].ids["label_max_speed"].text = str(self.highest_speed)

            mapview = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
            if MainApp.znacznik == 0:
                mapview.add_layer(LineMapLayer(), mode="scatter")
                MainApp.znacznik = 1

            group = GroupScreen()
            try:
                group.get_readings(1)
            except:
                pass

            # flaga_gps = group.returnFlag()
            # lat_2 = group.returnLat()
            # lon_2 = group.lonGPS

            # print "test_gps"
            # print lat_2
            # print lon_2fes
            # print flaga_gps

            MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lat = float(MainApp.lat)
            MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lon = float(MainApp.lon)

            punkty = MainApp.get_running_app().root.carousel.slides[0].punkty
            #punkty.setNode(0, float(MainApp.lat), float(MainApp.lon))

            group_screen = MainApp.get_running_app().root.carousel.slides[0]

            #obliczenie odleglosci miedzy aktualnym punktem a najblizszym punktem w nawigacji do ktorego zmierzamy
            if group_screen.route_calculated == True:
                x1 = punkty.getLat(group_screen.actual_point)
                y1 = punkty.getLon(group_screen.actual_point)
                x2 = punkty.getLat(group_screen.actual_point + 1)
                y2 = punkty.getLon(group_screen.actual_point + 1)
                x = MainApp.lat
                y = MainApp.lon

                if group_screen.of_the_track(x1, y1, x2, y2, x, y):
                    group_screen.calculate_route_nodes_run()

                distance1 = group_screen.calculate_distance(float(MainApp.lat), float(punkty.getLat(group_screen.actual_point)), float(MainApp.lon), float(punkty.getLon(group_screen.actual_point)))
                distance2 = group_screen.calculate_distance(float(MainApp.lat), float(punkty.getLat(group_screen.actual_point + 1)), float(MainApp.lon), float(punkty.getLon(group_screen.actual_point + 1)))

                print "dystans"
                print distance1
                print distance2

                #sprawdzenie czy nie ominelismy najblizszego punktu

                instruction_points = GraphHopperAndroid.getInstructionPoints(group_screen.actual_instruction)

                if distance2 > distance1:
                    if distance1 < 0.01:
                        #sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje
                        if instruction_points.getLatitude(0) == punkty.getLat(group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(group_screen.actual_point):
                            group_screen.actual_instruction += 1
                        group_screen.actual_point += 1

                        print "instrukcje"
                        print instruction_points.getLatitude(0)
                        print instruction_points.getLongitude(0)

                        if group_screen.actual_point == (punkty.getSize() - 1):
                            group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."


                    MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lat = float(group_screen.punkty.getLat(group_screen.actual_point))
                    MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lon = float(group_screen.punkty.getLon(group_screen.actual_point))

                    MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lat = float(group_screen.punkty.getLat(group_screen.actual_point + 1))
                    MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lon = float(group_screen.punkty.getLon(group_screen.actual_point + 1))


                else:
                    #sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje
                    if instruction_points.getLatitude(0) == punkty.getLat(group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(group_screen.actual_point):
                        group_screen.actual_instruction += 1
                    group_screen.actual_point += 1
                    print "instrukcje"
                    print instruction_points.getLatitude(0)
                    print instruction_points.getLongitude(0)
                    if group_screen.actual_point == (punkty.getSize() - 1):
                        group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."

                group_screen.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(group_screen.actual_instruction)

            # if flaga_gps == 1:
            #     MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lat = lat_2
            #     MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lon = lat_2

            if MainApp.get_running_app().root.carousel.slides[0].auto_center:
                mapview.center_on(float(MainApp.lat), float(MainApp.lon))
                MainApp.get_running_app().root.carousel.slides[0].redraw_route()

            if self.flagCenter == True:
                mapview.center_on(float(MainApp.lat), float(MainApp.lon))
                MainApp.get_running_app().root.carousel.slides[0].redraw_route()
                self.flagCenter = False
            MainApp.cos = 0
            MainApp.prev_time = datetime.datetime.now().time()

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)


pass

if __name__ == '__main__':
    MainApp().run()
