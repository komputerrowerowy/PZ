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
from kivy.uix.image import Image
from math import radians, sin, cos, acos, degrees, pi, asin

import requests
from kivy.garden.mapview import MapLayer
from kivy.garden.mapview import MapView, MapMarker
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
from kivy.uix.label import Label
from SOAPpy import WSDL
#from os import *
from time import gmtime, strftime, localtime
import unicodedata
import linecache
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial
from kivy.uix.gridlayout import GridLayout
from settingsjson import settings_json, settings_json1
from kivy.uix.settings import SettingsWithSpinner
from kivy.uix.settings import SettingsWithNoMenu
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.settings import Settings
from kivy.properties import ListProperty, BooleanProperty
from kivy.logger import Logger
from kivy.garden.qrcode import QRCodeWidget

from collections import namedtuple
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, BooleanProperty, \
    NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Line
from jnius import autoclass, PythonJavaClass, java_method, cast
from android.runnable import run_on_ui_thread
import random

# preload java classes


#import pyowm

#owm = pyowm.OWM('b26433c9a2c69c16c1d138cc5710fd57', language='pl')  #moj kod!!!

# 3c8792 niebieski kolor xD
print "wersja_aaafghjkl"

Hardware = autoclass('org.renpy.android.Hardware')

AcceptIncomingCall = autoclass("org.test.Phone")

TelephonyManager = autoclass('android.telephony.TelephonyManager')
Context = autoclass('android.content.Context')
activity = autoclass("org.renpy.android.PythonActivity").mActivity
Grupy = autoclass("android.provider.ContactsContract$Groups")

GraphHopperAndroid = autoclass("com.graphhopper.android.GraphHopperAndroid")(activity.mPath)
GraphHopperAndroid.loadGraphStorage()

AcceptIncomingCall2 = activity

System = autoclass('java.lang.System')
System.loadLibrary('iconv')
PythonActivity = autoclass('org.renpy.android.PythonActivity')
Camera = autoclass('android.hardware.Camera')
ImageScanner = autoclass('net.sourceforge.zbar.ImageScanner')
Config = autoclass('net.sourceforge.zbar.Config')
SurfaceView = autoclass('android.view.SurfaceView')
LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
Image = autoclass('net.sourceforge.zbar.Image')
ImageFormat = autoclass('android.graphics.ImageFormat')
LinearLayout = autoclass('android.widget.LinearLayout')
Symbol = autoclass('net.sourceforge.zbar.Symbol')
JSONObject = autoclass("org.json.JSONObject")

navi_path = '/sdcard'

contacts = []
contacts2 = []
contacts3 = []
contactsFavorite = []

contactsGroups = {}
contactsGroups2 = {}
contactsGroupsFavorite = {}
groups = []
sensorEnabled = False
wsp2 = 0
GrupyId = []

accountName = activity.getUsername()

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
<StormPopup>:
    cols:1
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 1
        Image:
            size_hint_y: .2
            canvas.before:
                Color:
                    rgba: root.color
                Rectangle:
                    pos: self.pos
                    size: self.size
            center_x: self.parent.center_x
            source: root.grzmot
            height: self.parent.height*2
            width: self.parent.width*2
        Image:
            size_hint_y: .6
            canvas.before:
                Color:
                    rgba: root.color
                Rectangle:
                    pos: self.pos
                    size: self.size
            center_x: self.parent.center_x
            background_color: 1,1,0,0
            source: 'resources/radarN.png'
            height: self.parent.height*6
            width: self.parent.width*6
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



class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

class StormPopup(GridLayout):
    text = StringProperty()
    ktory_radar=''
    grzmot='resources/cloud-and-thunder.png'
    color=(1,0,0,1)

    def __init__(self, **kwargs):
        self.register_event_type('on_answer2')
        super(StormPopup, self).__init__(**kwargs)

    def on_answer2(self, *args):
        pass

class StartScreen(Screen):
    pass



class ShowTime(Screen):
    popup_shown = False
    flagaCall = 1
    prev = 0
    powtorka=0
    nrTel = 000000000
    aktualny_miesiac=5
    aktualny_dzien = 15
    aktualna_godzina = 17
    aktualna_minuta = 30
    minutnik=0
    if_night=False
    group_members_names = []
    group_members_lat = []
    group_members_lon = []

    def __init__(self, **kwargs):
        super(ShowTime, self).__init__()
        self.add_widget(StartScreen())

    def build(self):
        pass




    def MapNormal(self):
        MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.height = ((self.height * self.height) + (
        self.width * self.width)) ** 0.5
        MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.width = ((self.height * self.height) + (
        self.width * self.width)) ** 0.5
        MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.pos = (-(
        (((self.height * self.height) + (self.width * self.width)) ** 0.5) - self.width)) / 2, (-(
        (((self.height * self.height) + (self.width * self.width)) ** 0.5) - self.height)) / 2



    def MapCut(self, touch):
        print 'ciecie mapy'

        indeks = MainApp.get_running_app().root.carousel.index
        if indeks == 0:
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.height = self.height
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.width = self.width
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.pos = self.pos
        else:
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.height = ((self.height * self.height) + (self.width * self.width))**0.5
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.width = ((self.height * self.height) + (self.width * self.width))**0.5
            MainApp.get_running_app().root.carousel.slides[0].ids.relativeMap.pos = (-((((self.height * self.height) + (self.width * self.width))**0.5) - self.width))/2, (-((((self.height * self.height) + (self.width * self.width))**0.5) - self.height))/2

        # self1 = MainApp.get_running_app().root.carousel
        #
        # if not self1.touch_mode_change:
        #     if self1.ignore_perpendicular_swipes and \
        #                     self1.direction in ('top', 'bottom'):
        #         if abs(touch.oy - touch.y) < self1.scroll_distance:
        #             if abs(touch.ox - touch.x) > self1.scroll_distance:
        #                 self1._change_touch_mode()
        #                 self1.touchModeChange = True
        #     elif self1.ignore_perpendicular_swipes and \
        #                     self1.direction in ('right', 'left'):
        #         if abs(touch.ox - touch.x) < self1.scroll_distance:
        #             if abs(touch.oy - touch.y) > self1.scroll_distance:
        #                 self._change_touch_mode()
        #                 self1.touchModeChange = True




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
        print "SMS"
        print(self.nrTel)
        sms.send(recipient=sms_recipient, message=sms_message)

    def callListener(self):

        print activity.number
        self.nrTel = activity.number
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
            activity.actual_search = "ODBIERZ";
            activity.switchSearch("ODBIERZ")
            self.incoming_call_clock = Clock.schedule_interval(self.accept_call_voice, 1)
            # time.sleep(1)

    def stormListener(self):
        content = StormPopup()
        content.bind(on_answer=self._on_answer2)
        self.popup2 = Popup(title="Ostrzezenie o burzy: ",
                           content=content,
                           size_hint=(0.9, 0.75),
                           auto_dismiss=True)
        self.popup2.open()



    def accept_call_voice(self, lalala):
        #print "dupa" + " " + activity.lastWord
        if activity.callState == 1:
            #print "dupa" + " " + activity.lastWord
            if activity.lastWord == "ODBIERZ" or activity.lastWord == "ODBIERZ2":
                print "odbierz"
                activity.lastWord = ""
                self.flagaCall = 1
                AcceptIncomingCall2.acceptCall()
                activity.actual_search = "";
                activity.switchSearch("BIKOM")

                self.incoming_call_clock.cancel()
            else:
                if activity.lastWord == "ODRZUC" or activity.lastWord == "ODRZUC2" or activity.lastWord == "ROZLACZ" or activity.lastWord == "ROZLACZ(2)":
                    print "odrzuc"
                    activity.lastWord = ""
                    self.flagaCall = 1
                    self.rejectIncomingCall()
                    activity.actual_search = "";
                    activity.switchSearch("BIKOM")

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
        #self.popup_shown = False
        self.ShowSmsAnswer()

    def _on_answer2(self, instance, answer):
        print "USER ANSWER2: ", repr(answer)
        if answer == "Odbierz":

            #self.flagaCall = 1
            self.popup2.dismiss()
            #AcceptIncomingCall2.acceptCall()
        else:
            if answer == "Odrzuc":

                #self.flagaCall = 1

                #self.rejectIncomingCall()
                self.popup2.dismiss()
        self.popup2.dismiss()
        self.popup_shown = False

    def rejectIncomingCall(self):

        telephonyManager = activity.getSystemService(Context.TELEPHONY_SERVICE)

        telephonyService = activity.createITelephonyInstance(telephonyManager)

        telephonyService.endCall()
        #self.ShowSmsAnswer()
        # self.popup.dismiss()

    def day_or_night(self,year,month,day,hour,minute,lat,lon):
        R=year
        M=month
        D=day
        Lat=52
        Long=18
        Req=-0.833
        J=367*R-int(7*(R+int((M+9)/12))/4)+int(275*M/9)+D-730531.5
        Cent=J/36525
        L=(4.8949504201433+628.331969753199*Cent)%6.28318530718
        G=(6.2400408+628.331969753199*Cent)%6.28318530718
        O=0.409093-0.0002269*Cent
        F=0.033423*sin(G)+0.00034907*sin(2*G)
        E=0.0430398*sin(2*(L+F))-0.00092502*sin(4*(L+F))-F
        A=asin(sin(O)*sin(L+F))
        C=(sin(0.017453293*Req)-sin(0.017453293*Lat)*sin(A))/(cos(0.017453293*Lat)*cos(A))
        Wsch=(pi-(E+0.017453293*Long+1*acos(C)))*57.29577951/15
        Zach = (pi - (E + 0.017453293 * Long - 1 * acos(C))) * 57.29577951 / 15
        godzina_wschodu=int(Wsch)
        print "godzina wschodu"
        print godzina_wschodu
        minuta_wschodu=int((Wsch-int(Wsch))*60)
        print "minuta wschodu"
        print minuta_wschodu
        godzina_zachodu=int(Zach)
        print "godzina zachodu"
        print godzina_zachodu
        minuta_zachodu=int((Zach-int(Zach))*60)
        print "minuta zachodu"
        print minuta_zachodu
        #poprawka na czas polski
        godzina_wschodu=godzina_wschodu+2
        godzina_zachodu=godzina_zachodu+2
        if hour<godzina_zachodu and hour>godzina_wschodu:
            return False
        if hour==godzina_wschodu and minute>minuta_wschodu:
            return False
        if hour==godzina_zachodu and minute<minuta_zachodu:
            return False
        return True






    def check(self, fla):
        # pass
        mapview = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
        group_screen = MainApp.get_running_app().root.carousel.slides[0]

        messageList = activity.client.messageList
        print "odczytane wiadomosci"
        if not messageList.isEmpty():
            for i in xrange(messageList.size()):

                nazwa_konta = ""
                komorka = []
                tytul = ""
                lat = 0.0
                lon = 0.0

                message = messageList.get(i)
                message = message.replace("{", "")
                message = message.replace("}", "")
                message_split = message.split(",")
                print message_split

                komorka.append(message_split.pop().split("="))
                komorka.append(message_split.pop().split("="))
                komorka.append(message_split.pop().split("="))
                komorka.append(message_split.pop().split("="))

                print komorka

                for i in komorka:
                    wartosc = i.pop()
                    klucz = i.pop()

                    print klucz
                    print wartosc
                    wartosc = wartosc.replace(" ", "")
                    klucz = klucz.replace(" ", "")

                    if klucz == "id":
                        nazwa_konta = wartosc
                    elif klucz == "title":
                        tytul = wartosc
                    elif klucz == "lat":
                        lat = float(wartosc)
                    elif klucz == "lon":
                        lon = float(wartosc)

                if nazwa_konta != activity.getUsername():
                    print "kupa"
                    print nazwa_konta
                    print tytul
                    if str(tytul) == 'TitleCarDown':
                        group_screen.sendAlertCarDown()
                    elif str(tytul) == 'TitleCarUp':
                        group_screen.sendAlertCarUp()
                    elif str(tytul) == 'TitleStart':
                        group_screen.sendAlertStart()
                    elif str(tytul) == 'TitleStop':
                        group_screen.sendAlertStop()
                    elif str(tytul) == "AktualPosition":
                        if nazwa_konta not in self.group_members_names:
                            self.group_members_names.append(str(nazwa_konta))
                            self.group_members_lat.append(float(lat))
                            self.group_members_lon.append(float(lon))

                            '''print self.group_members_names

                            index = len(self.group_members_lat) - 1
                            marker = "marker_group_" + str(index + 1)
                            print marker

                            marker_group = MainApp.get_running_app().root.carousel.slides[0].ids[marker]
                            self.group_update_marker(marker_group, lat, lon)'''
                        else:
                            index = self.group_members_names.index(str(nazwa_konta))
                            self.group_members_lat[index] = lat
                            self.group_members_lon[index] = lon

                            '''marker = "marker_group_" + str(index + 1)
                            print marker
                            #lat: 52.9828
                            #lon: 18.5729

                            marker_group = MainApp.get_running_app().root.carousel.slides[0].ids[marker]
                            self.group_update_marker(marker_group, lat, lon)'''


            messageList.clear()

        if self.minutnik%60==0:
            print datetime.datetime.today()
            dt = datetime.datetime.now()
            tt = dt.timetuple()
            self.aktualny_rok=tt[0]
            self.aktualny_miesiac=tt[1]
            self.aktualny_dzien = tt[2]
            self.aktualna_godzina = tt[3]
            self.aktualna_minuta = tt[4]
            print self.aktualny_miesiac
            print self.aktualny_dzien
            print self.aktualna_godzina
            print self.aktualna_minuta

            self.if_night=self.day_or_night(self.aktualny_rok,self.aktualny_miesiac,self.aktualny_dzien,self.aktualna_godzina,self.aktualna_minuta,MainApp.lat,MainApp.lon)
        self.minutnik=self.minutnik+1

        print "czy mamy noc?"
        print str(self.if_night)
        Weather.czy_noc=self.if_night
        print str(Weather.czy_noc)


        print "plusik"
        print activity.keyPressed
        if activity.keyPressed == "prawo":
            print activity.keyPressed
            MainApp.get_running_app().root.carousel.load_next(mode='next')
            activity.keyPressed = ""
            print "po plusiku"
        elif activity.keyPressed == "lewo":
            MainApp.get_running_app().root.carousel.load_previous()
            activity.keyPressed = ""
            print activity.keyPressed

            print "po plusiku"


        print('LonZmapview', mapview.globalLon)
        print('LatZmapview', mapview.globalLat)

        if mapview.globalLon >= 0 and mapview.globalLat >= 0:



            MainApp.get_running_app().root.carousel.slides[0].latGPS = mapview.globalLat
            MainApp.get_running_app().root.carousel.slides[0].lonGPS = mapview.globalLon
            MainApp.get_running_app().root.carousel.slides[0].calculate_route_nodes_run_add()
            # MainApp.get_running_app().root.carousel.slides[0].centerTarget()

            mapview.globalLat = -1
            mapview.globalLon = -1



        if activity.lastWord != '':
            music_screen = MainApp.get_running_app().root.carousel.slides[3]
            commands = activity.lastWord.split(" ")
            if commands[0] == "DALEJ":
                MainApp.get_running_app().root.carousel.load_next(mode = 'next')
                activity.lastWord = ""
            if commands[0] == "WSTECZ":
                MainApp.get_running_app().root.carousel.load_previous()
                activity.lastWord = ""
            if commands[0] == "POPRZEDNI" or activity.lastWord == "POPRZEDNIA":
                music_screen.backSong()
                activity.lastWord = ""
            if commands[0] == "NASTĘPNY" or activity.lastWord == "NASTĘPNA":
                music_screen.nextSong()
                activity.lastWord = ""
            if commands[0] == "STOP" or activity.lastWord == "START" or activity.lastWord == "MUZYKA":
                music_screen.stopSong()
                activity.lastWord = ""

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
                    print "wyjatek kontaktow: "
                    GrupyId.append(nrGrupy)
                    print "wyjatek: ", sys.exc_info()

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

        print "Tutaj sprawdzam Weather.czy_burza=" + str(Weather.czy_burza)
        if Weather.czy_burza==1 and self.powtorka==0:
            self.powtorka=1
            self.stormListener()

    def dismiss_popupSmsAnswer(self):
        self._popupSmsAnswer.dismiss()
        self.popup_shown = False

    def ShowSmsAnswer(self):
        content = PopupSmsAnswer(SmsOdp1=self.SmsOdp1,
                                 SmsOdp2=self.SmsOdp2,
                                 SmsOdp3=self.SmsOdp3,
                             cancelSmsAnswer=self.dismiss_popupSmsAnswer)

        self._popupSmsAnswer = Popup(title="Odpowiedzi sms", content=content,
                            size_hint=(0.9, 0.8))
        self._popupSmsAnswer.open()

    def SmsOdp1(self):
        self.send_sms(self.nrTel, "Jadę rowerem. Odezwę się później.")
        self.dismiss_popupSmsAnswer()
        self.popup_shown = False

    def SmsOdp2(self):
        self.send_sms(self.nrTel, "Jadę rowerem. Nie mogę teraz rozmawiać.")
        self.dismiss_popupSmsAnswer()
        self.popup_shown = False

    def SmsOdp3(self):
        self.send_sms(self.nrTel, "Jadę rowerem. Zadzwoń później.")
        self.dismiss_popupSmsAnswer()
        self.popup_shown = False


class ChooseFile(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

class PopupSmsAnswer(FloatLayout):
    SmsOdp1 = ObjectProperty(None)
    SmsOdp2 = ObjectProperty(None)
    SmsOdp3 = ObjectProperty(None)
    cancelSmsAnswer = ObjectProperty(None)


class PopupGroupConect(FloatLayout):
    createGroupConect = ObjectProperty(None)
    joinGroupConect = ObjectProperty(None)
    cancelGroupConect = ObjectProperty(None)

class PopupAlert(FloatLayout):
    cancelAlert = ObjectProperty(None)
    sendCarDown = ObjectProperty(None)
    sendCarUp = ObjectProperty(None)
    sendStart = ObjectProperty(None)
    sendStop = ObjectProperty(None)


class PopupAlertCarDown(FloatLayout):
    cancelAlertCarDown = ObjectProperty(None)

class PopupAlertCarUp(FloatLayout):
    cancelAlertCarUp = ObjectProperty(None)

class PopupAlertStop(FloatLayout):
    cancelAlertStop = ObjectProperty(None)

class PopupAlertStart(FloatLayout):
    cancelAlertStart = ObjectProperty(None)

class PopupShowPin(FloatLayout):
    cancelShowPin = ObjectProperty(None)



class PopupPutPin(FloatLayout):
    cancelPutPin = ObjectProperty(None)
    selectPutPin = ObjectProperty(None)
    def goToGroup(self):
        topic3 = self.ids.PinInput.text
        print(str(topic3))
        gr = GroupScreen()

        gr.change_topic_add(str(topic3))
        gr.dismiss_popupPutPin()


class ChooseBicomTras(FloatLayout):
    selectTras = ObjectProperty(None)
    cancelTras = ObjectProperty(None)


class PopupGPX(FloatLayout):
    selectGpx = ObjectProperty(None)
    cancelGpx = ObjectProperty(None)

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
    songsLoaded = False

    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__()
        self.songsLoaded = False

    def MusicPlayerNextCarousel(self):
        MainApp.get_running_app().root.carousel.load_next(mode='next')

    def MusicPlayerPreviousCarousel(self):
        MainApp.get_running_app().root.carousel.load_previous()

    #funkcja wywoływana na przycisku stop/play
    def stopSong(self):
        if self.songsLoaded:
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
        if self.songsLoaded:
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
        if self.songsLoaded:
            self.flaga = 0
            dl = len(self.songs) - 1
            if self.nowPlaying == '':
                pass
            else:
                self.nowPlaying.stop()
            print("backSong")
            if self.flaga == 0:
                self.nowPlaying.bind(on_stop=self.stop_event_flaga)



    #główna funkcja służąca do otwarzania muzyki i tworzenia listy utworów
    def getSongs(self):

        self.directory = self.ids.direct.text  # przypisanie katalogu z etykiety

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

        if len(self.songs) > 0:
            self.songsLoaded = True


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
        if self.songsLoaded:
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
        if self.songsLoaded:
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
    punkty22 = []
    instructions = []
    actual_point = 0
    actual_instruction = 0
    actual_instruction2 = 0
    punkty_aktualne2 = []
    punkty_aktualne = []
    instructions_aktualne = []
    flagaPunktow = 0
    TymczasoweLat = 0
    TymczasoweLon = 0
    PunktyKontrolneLon = []
    PunktyKontrolneLat = []
    travelled_points = 0
    route_size = []
    list_points_shown = True
    Nawiguj = False
    removeFlag = False
    TypeBike = 'bike'
    directory = ''
    recordPosition = False
    cityPoint = ''
    streetPoint = ''
    geoFlaga = True
    NawigationMode = False
    PathBicomTras = "/sdcard/Bicom/BicomTrasa.txt"
    FkagaPunktowSymulatora = False
    punktyTrasyLat = []
    punktyTrasyLon = []
    punktySymulacjiLat = []
    punktySymulacjiLon = []
    GpxPath = "/sdcard/Bicom/Moje_trasy/"
    simulationFlag = True
    connectGroup = False

    # def __init__(self, **kwargs):
    #     super(GroupScreen, self).__init__()
    #     self.ids.scatter2.bbox = ((0, 0), (self.width, self.height))


    def sfinxof(self):
        if activity.ignore_sphinx == True:
            activity.ignore_sphinx = False
            MainApp.get_running_app().root.carousel.slides[0].ids.label_instruction_distance.background_color = (0.235, 0.529, 0.572, 0.9)
        else:
            activity.ignore_sphinx = True
            MainApp.get_running_app().root.carousel.slides[0].ids.label_instruction_distance.background_color = (0.235, 0.529, 0.572, 0.8)


    def send_string(self, klucz1, wartosc1, klucz2, wartosc2, klucz3, wartosc3, tytul):
        json = JSONObject()
        info = JSONObject()

        json.put("to", "/topics/" + activity.actualTopic)
        info.put("title", tytul)
        info.put(klucz1, wartosc1)
        info.put(klucz2, wartosc2)
        info.put(klucz3, wartosc3)
        json.put("data", info);
        print 'tu wpisuje jsona xD'
        print json.toString()

        activity.sendJSON(json)

    def change_topic(self):
        # MainApp.get_running_app().root.carousel.slides[0].ids['PinLabel'].text = str(topic)
        # PopupShowPin.ids.PinLabel.text = str(topic)
        activity.subscribeTopic(str(MainApp.topicLabel))
        # activity.subscribeTopic("ugabuga")

    def change_topic_add(self, topic):
        activity.subscribeTopic(str(topic))

    def simulationRoute(self):
        if self.simulationFlag == False:
            self.simulationFlag = True
            self.ids.img_sim.source = "resources/recred.png"
        else:
            self.simulationFlag = False
            self.ids.img_sim.source = "resources/recwhite.png"


    def GroupScreenNextCarousel(self):
        MainApp.get_running_app().root.carousel.load_next(mode='next')

    def GroupScreenPreviousCarousel(self):
        MainApp.get_running_app().root.carousel.load_previous()

    def saveToBicom(self, lat, lon):
        f = open("/sdcard/Bicom/BicomTrasa.txt", "a")
        f.write(str(lat) + " " + str(lon))
        f.close()

    def loadFromBicom(self, path, nr):
        wiersz = linecache.getline(path, nr)





    def savepath(self, path):
        f = open("/sdcard/Bicom/path/sav.dat", "w")
        f.write(path)
        f.close()
        print"zapisSciezki"
        print MainApp.navi_path

    def dismiss_popupAlert(self):
        self._popupAlert.dismiss()

    def sendAlert(self):
        content = PopupAlert(cancelAlert=self.dismiss_popupAlert, sendCarDown=self.sendCarDownMessage, sendCarUp=self.sendCarUpMessage , sendStop =self.sendStop , sendStart =self.sendStart)

        self._popupAlert = Popup(title="Wyślij komunikat", content=content,
                            size_hint=(0.8, 0.7))
        self._popupAlert.open()

    def sendCarDownMessage(self):
        self.send_string('id', accountName, 'KeyCarDown', 'CarDown', 'KeyCarDown2', 'CarDown2', 'TitleCarDown')
        self.dismiss_popupAlert()

    def sendCarUpMessage(self):
        self.send_string('id', accountName, 'KeyCarUp', 'CarUp', 'KeyCarUp2', 'CarUp2', 'TitleCarUp')
        self.dismiss_popupAlert()

    def sendStop(self):
        self.send_string('id', accountName, 'KeyStop', 'Stop', 'KeyStop2', 'Stop2', 'TitleStop')
        self.dismiss_popupAlert()

    def sendStart(self):
        self.send_string('id', accountName, 'KeyStart', 'Start', 'KeyStart2', 'Start2', 'TitleStart')
        self.dismiss_popupAlert()

    def sendMainLocation(self):
        self.send_string('id', accountName, 'lat', str(MainApp.lat), 'lon', str(MainApp.lon), 'AktualPosition')

    def dismiss_popupAlertCarDown(self):
        self._popupAlertCarDown.dismiss()

    def sendAlertCarDown(self):
        content = PopupAlertCarDown(cancelAlertCarDown=self.dismiss_popupAlertCarDown)

        self._popupAlertCarDown = Popup(title="Komunikat", content=content,
                            size_hint=(0.8, 0.5))
        self._popupAlertCarDown.open()

    def dismiss_popupAlertCarUp(self):
        self._popupAlertCarUp.dismiss()

    def sendAlertCarUp(self):
        content = PopupAlertCarUp(cancelAlertCarUp=self.dismiss_popupAlertCarUp)

        self._popupAlertCarUp = Popup(title="Komunikat", content=content,
                                        size_hint=(0.8, 0.5))
        self._popupAlertCarUp.open()

    def dismiss_popupAlertStop(self):
        self._popupAlertStop.dismiss()

    def sendAlertStop(self):
        content = PopupAlertStop(cancelAlertStop=self.dismiss_popupAlertStop)

        self._popupAlertStop = Popup(title="Komunikat", content=content,
                                        size_hint=(0.8, 0.5))
        self._popupAlertStop.open()


    def dismiss_popupAlertStart(self):
        self._popupAlertStart.dismiss()

    def sendAlertStart(self):
        content = PopupAlertStart(cancelAlertStart=self.dismiss_popupAlertStart)

        self._popupAlertStart = Popup(title="Komunikat", content=content,
                                        size_hint=(0.8, 0.5))
        self._popupAlertStart.open()

    def dismiss_popupShowPin(self):
        self._popupShowPin.dismiss()

    def ShowPin(self):
        content = PopupShowPin(cancelShowPin=self.dismiss_popupShowPin)

        #actualDate = strftime("%Y-%m-%d %H:%M:%S", localtime())
        # self._popupShowPin.ids.qr.data = actualDate

        # MainApp.topicLabel = random.randrange(1000, 10000, 2)
        content.ids.PinLabel.text = str(MainApp.topicLabel)



        self._popupShowPin = Popup(title="Komunikat", content=content,
                                        size_hint=(0.8, 0.4))


        self._popupShowPin.open()

    def dismiss_popupPutPin(self):
        print 'wypisz ten topic'

        #self._popupPutPin.dismiss()


    def PutPin(self):
        content = PopupPutPin(cancelPutPin=self.dismiss_popupPutPin, selectPin=self.selectPutPin)


        self._popupPutPin = Popup(title="Dołącz do grupy", content=content,
                                        size_hint=(0.8, 0.6))


        self._popupPutPin.open()

    def selectPutPin(self):
        pass





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
        self.savepath(self.directory)

        self.dismiss_popup()

    def ComunicationGroups(self):
        if self.connectGroup == False:
            self.ShowGroupConect()
        else:
            self.sendAlert()




    def dismiss_popupGroupConect(self):
        self._popupGroupConect.dismiss()

    def ShowGroupConect(self):
        content = PopupGroupConect(createGroupConect=self.createGroupConectAlert,
                                   joinGroupConect=self.joinGroupConectAlert,
                             cancelGroupConect=self.dismiss_popupGroupConect)

        self._popupGroupConect = Popup(title="Ekran tworzenia grup", content=content,
                            size_hint=(0.9, 0.6))
        self._popupGroupConect.open()

    def joinGroupConectAlert(self):
        self.PutPin()
        #self.send_string()
        #elf.change_topic_add(self.topicLabel)
        self.dismiss_popupGroupConect()
        MainApp.get_running_app().root.carousel.slides[0].ids.img_groupConect.source = 'resources/alert.png'
        self.connectGroup = True

    def createGroupConectAlert(self):
        self.dismiss_popupGroupConect()
        self.ShowPin()
        self.change_topic()
        MainApp.get_running_app().root.carousel.slides[0].ids.img_groupConect.source = 'resources/alert.png'
        self.connectGroup = True

    def dismiss_popupTras(self):
        self._popupTras.dismiss()

    def fileSelectTras(self):
        content = ChooseBicomTras(selectTras=self.selectTras,
                             cancelTras=self.dismiss_popupTras)

        self._popupTras = Popup(title="Wybierz trase do zaimportowania", content=content,
                            size_hint=(0.9, 0.9))
        self._popupTras.open()

    def selectTras(self, path, filename):
        print "wyswietl_error"
        localPtah = os.path.join(path, filename[0])
        file = str(filename[0])
        localPtahSymuluj = str('/sdcard/Bicom/Zapisane_trasy/Symulacja/' + str(file[-23:]))

        print "wyswietl_error2"
        print (str(localPtahSymuluj))
        print (str(filename[0]))
        #localPtah = path
        self.removeFlag = False

        scren = MainApp.get_running_app().root.carousel.slides[0]

        count = len(open(localPtah, 'rU').readlines())
        countSymuluj = len(open(localPtahSymuluj, 'rU').readlines())

        localSize = len(self.PunktyKontrolneLon)

        self.ZerujTrase()

        print "test_odczytu"
        print (count)
        linecache.clearcache()
        wiersz = linecache.getline(localPtah, 1)
        if float(wiersz[:7]) == float(123.123):
            self.TypeBike = 'bike'
        elif float(wiersz[:7]) == float(456.456):
            self.TypeBike = 'mtb'
        # self.TypeBike = str(wiersz)
        print(str(wiersz[:7]))
        linecache.clearcache()
        wiersz = linecache.getline(localPtah, 2)
        try:
            MainApp.lon = float(wiersz[-14:])
            MainApp.lat = float(wiersz[:13])
        except:
            try:
                MainApp.lon = float(wiersz[-12:])
                MainApp.lat = float(wiersz[:11])
            except:
                print "nie wczytalo"

        try:
            MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(MainApp.lat, MainApp.lon)
            MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lat = float(MainApp.lat)
            MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lon = float(MainApp.lon)

        except:
            pass
        try:
            self.redraw_route()
        except:
            pass

        for nr in xrange(3, count + 1):
            linecache.clearcache()
            wiersz = linecache.getline(localPtah, nr)

            try:

                self.lonGPS = float(wiersz[-14:])
                self.latGPS = float(wiersz[:13])
                print('test_przejscia_13')
                print(str(wiersz[-14:]))
                print(str(wiersz[:13]))
                print"======================="
                map = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
                mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
                map.add_marker(mark)
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)
                self.calculate_route_nodes_run_add()

            except:

                try:
                    self.lonGPS = float(wiersz[-12:])
                    self.latGPS = float(wiersz[:11])
                    print('test_przejscia_11')
                    print(str(wiersz[-12:]))
                    print(str(wiersz[:11]))
                    print"======================="
                except:
                    print"wyjatekkkkkkkkk"


        for nr in xrange(2, countSymuluj + 1):
            linecache.clearcache()
            wierszSymuluj = linecache.getline(localPtahSymuluj, nr)

            try:

                self.punktySymulacjiLon.append(float(wierszSymuluj[-14:]))
                self.punktySymulacjiLat.append(float(wierszSymuluj[:13]))
                print('test_przejscia_133')
                print(str(wierszSymuluj[-14:]))
                print(str(wierszSymuluj[:13]))
                print"======================="


            except:

                try:
                    self.punktySymulacjiLon.append(float(wierszSymuluj[-12:]))
                    self.punktySymulacjiLat.append(float(wierszSymuluj[:11]))
                    print('test_przejscia_12')
                    print(str(wierszSymuluj[-12:]))
                    print(str(wierszSymuluj[:11]))
                    print"======================="

                except:
                    print"wyjatekkkkkkkkkrrrrrrrrrr"



        self.dismiss_popupTras()

    def changeGpxPath(self, path):
        self.GpxPath = path

    def dismiss_popupGpx(self):
        self._popupGpx.dismiss()

    def saveToGpx(self):
        content = PopupGPX(selectGpx=self.selectGpx,
                             cancelGpx=self.dismiss_popupGpx)

        self._popupGpx = Popup(title="Zapis do GPX", content=content,
                            size_hint=(0.9, 0.4))
        self._popupGpx.open()

    def selectGpx(self):
        # wersja z -2h czas UTC
        # actualDate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        actualDate = strftime("%Y-%m-%d %H:%M:%S", localtime())

        print "abbbbbbbbbb"

        self.GpxPath + actualDate + ".gpx"

        #GraphHopperAndroid.saveActualPositionListToGPX("/sdcard/Bicom/trasa1.gpx", str(actualDate))
        GraphHopperAndroid.saveActualPositionListToGPX(str(self.GpxPath), str(actualDate))



        self.dismiss_popupGpx()

    def saveGraphhopperTras(self):
        if len(self.PunktyKontrolneLon) >= 2:
            actualDate = strftime("%Y-%m-%d %H:%M:%S", localtime())
            ff = open("/sdcard/Bicom/Zapisane_trasy/" + actualDate + ".txt", "w")
            if str(self.TypeBike) == 'bike':
                ff.write(str('123.123') + "\n")
            elif str(self.TypeBike) == 'mtb':
                ff.write(str('456.456') + "\n")
            ff.close()
            f = open("/sdcard/Bicom/Zapisane_trasy/" + actualDate + ".txt", "a")
            # if str(self.TypeBike) == 'bike':
            #     f.write(str('123.123') + "\n")
            # elif str(self.TypeBike) == 'mtb':
            #     f.write(str('456.456') + "\n")
            print("test_zapisu")
            print(str(self.TypeBike))
            for j in xrange(0, len(self.PunktyKontrolneLon)):
                f.write(str(self.PunktyKontrolneLat[j]) + " " + str(self.PunktyKontrolneLon[j]) + "\n")
            f.write("Koniec\n")
            f.close()

            # tylko do zpisuu punktów na symulacje
            self.zapiszPunktyTrasy(actualDate)

    def zapiszPunktyTrasy(self, actualDate):
        if len(self.punktyTrasyLon) >= 2:
            ff = open("/sdcard/Bicom/Zapisane_trasy/ZapisanaTrasa" + actualDate + ".txt", "w")
            if str(self.TypeBike) == 'bike':
                ff.write(str('123.123') + "\n")
            elif str(self.TypeBike) == 'mtb':
                ff.write(str('456.456') + "\n")
            ff.close()
            f = open("/sdcard/Bicom/Zapisane_trasy/ZapisanaTrasa" + actualDate + ".txt", "a")
            print("test_zapisu")
            for j in xrange(0, len(self.punktyTrasyLon)):
                f.write(str(self.punktyTrasyLat[j]) + " " + str(self.punktyTrasyLon[j]) + "\n")
            f.close()

    localPtah = "/sdcard/Bicom/BicomTrasa.txt"

    def loadFromBicomNonDynamic(self):
        self.removeFlag = False

        scren = MainApp.get_running_app().root.carousel.slides[0]
        localPtah = "/sdcard/Bicom/BicomTrasa.txt"
        count = len(open(localPtah, 'rU').readlines())

        localSize = len(self.PunktyKontrolneLon)

        self.ZerujTrase()

        print "test_odczytu"
        print (count)
        linecache.clearcache()
        wiersz = linecache.getline(localPtah, 1)
        if float(wiersz[:7]) == float(123.123):
            self.TypeBike = 'bike'
        elif float(wiersz[:7]) == float(456.456):
            self.TypeBike = 'mtb'
        # self.TypeBike = str(wiersz)
        print(str(wiersz[:7]))
        for nr in xrange(2, count):
            linecache.clearcache()
            wiersz = linecache.getline(localPtah, nr)

            try:
                print(str(wiersz[-13:]))
                print(str(wiersz[:13]))
                self.lonGPS = float(wiersz[-13:])
                self.latGPS = float(wiersz[:13])
                print('test_przejscia_13')
                print(str(self.lonGPS))
                print(str(self.latGPS))
                map = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
                mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
                map.add_marker(mark)
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)
                self.calculate_route_nodes_run_add()

            except:
                print(str(wiersz[11:]))
                print(str(wiersz[:11]))
                print(' ')
                print(' ')
                print(' ')
                try:
                    self.lonGPS = float(wiersz[11:])
                    self.latGPS = float(wiersz[:11])
                    print('test_przejscia_11')
                    print(str(self.lonGPS))
                    print(str(self.latGPS))
                except:
                    print"wyjatekkkkkkkkk"

                map = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
                mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
                map.add_marker(mark)
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)
                self.calculate_route_nodes_run_add()

    def test2(self):
        GraphHopperAndroid.loadGraphStorage()

    def show_search_bar(self):
        if self.search_bar_shown == False:
            self.ids.SearchInputShow.pos[0] = self.ids.SearchInputShow.pos[0] + self.height
            self.ids.SearchLayout.pos[0] = self.ids.SearchLayout.pos[0] + self.height
            self.search_bar_shown = True
        else:
            self.hide_list_points()
            self.ids.SearchInputShow.pos[0] = self.ids.SearchInputShow.pos[0] - self.height
            self.ids.SearchLayout.pos[0] = self.ids.SearchLayout.pos[0] - self.height
            self.search_bar_shown = False

    def hide_search_bar(self):
        if self.search_bar_shown == True:
            self.hide_list_points()
            self.ids.SearchInputShow.pos[0] = self.ids.SearchInputShow.pos[0] - self.height
            self.ids.SearchLayout.pos[0] = self.ids.SearchLayout.pos[0] - self.height
            self.search_bar_shown = False



    def show_list_points(self):
        if self.list_points_shown == False:
            self.ids.scrollPoints.pos[0] = self.ids.scrollPoints.pos[0] + self.height
            self.list_points_shown = True
        else:
            self.ids.scrollPoints.pos[0] = self.ids.scrollPoints.pos[0] - self.height
            self.list_points_shown = False

    def hide_list_points(self):
        print "test1"
        if self.list_points_shown == True:
            self.ids.scrollPoints.pos[0] = self.ids.scrollPoints.pos[0] - self.height
            self.list_points_shown = False

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

    def navi(self):
        if self.NawigationMode == False and len(self.PunktyKontrolneLon)>=2:
            self.NawigationMode = True
            group_screen = MainApp.get_running_app().root.carousel.slides[0]
            group_screen.ids.mapView.zoom = 18
            self.center()
            self.ids.img_navi.source = "resources/map.png"
            group_screen.recordPosition = True
        else:
            self.NawigationMode = False
            group_screen = MainApp.get_running_app().root.carousel.slides[0]
            self.ZerujTrase()
            self.ids.img_navi.source = "resources/route.png"
            group_screen.recordPosition = False
            #GraphHopperAndroid.saveActualPositionListToGPX("/sdcard/Bicom/trasa1.gpx", "trasa1")
            #self.saveToGpx()

    def center(self):
        MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(float(MainApp.lat), float(MainApp.lon))
        self.auto_center = True
        self.route_calculated = True
        self.Nawiguj = True
        self.hide_search_bar()
        self.ids.img_center.source = "resources/center_red.png"
        self.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(self.actual_instruction)
        self.redraw_route()

    def centerTarget(self):
        try:
            print self.returnLon()
            lon = float(self.returnLon())
            lat = float(self.returnLat())
            self.latGPS = float(self.returnLat())
            self.lonGPS = float(self.returnLon())
            map = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
            MainApp.get_running_app().root.carousel.slides[0].ids["mapView"].center_on(lat, lon)

            mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
            map.add_marker(mark)
            MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)

            self.calculate_route_nodes_run_add()
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


    def TypeBikeBike(self):
        self.TypeBike = 'bike'
        self.recalculate_route()

    def TypeBikeMtb(self):
        self.TypeBike = 'mtb'
        self.recalculate_route()

    def calculate_route_nodes_run_add(self):

        if self.removeFlag == True:
            self.TymczasoweLat = self.PunktyKontrolneLat[(len(self.PunktyKontrolneLon) - 1)]
            self.TymczasoweLon = self.PunktyKontrolneLon[(len(self.PunktyKontrolneLon) - 1)]
            self.removeFlag = False

        if self.flagaPunktow == 0:
            GraphHopperAndroid.calcPath(True, self.TypeBike, float(MainApp.lat), float(MainApp.lon), float(self.latGPS),
                                        float(self.lonGPS))
            self.punkty = GraphHopperAndroid.resp.getPoints()
            if self.FkagaPunktowSymulatora == False:
                self.punkty22 = GraphHopperAndroid.resp.getPoints()
            self.instructions = GraphHopperAndroid.instructionList
            self.PunktyKontrolneLat.append(float(MainApp.lat))
            self.PunktyKontrolneLon.append(float(MainApp.lon))
            self.PunktyKontrolneLat.append(float(self.latGPS))
            self.PunktyKontrolneLon.append(float(self.lonGPS))
            self.route_size.append(self.punkty.getSize())
            if self.list_points_shown == True:
                self.hide_list_points
        else:
            GraphHopperAndroid.calcPath(False, self.TypeBike, float(self.TymczasoweLat), float(self.TymczasoweLon), float(self.latGPS),
                                        float(self.lonGPS))
            self.punkty_aktualne = GraphHopperAndroid.resp.getPoints()
            punkty_size = self.punkty_aktualne.getSize()
            self.punkty.removeLast()
            for j in xrange(0, punkty_size):
                lat = float(self.punkty_aktualne.getLat(j))
                lon = float(self.punkty_aktualne.getLon(j))
                ele = float(self.punkty_aktualne.getEle(j))

                self.punkty.add(lat, lon, ele)
                if self.FkagaPunktowSymulatora == False:
                    self.punkty22.add(lat, lon, ele)


            GraphHopperAndroid.connectInstructions()
            self.instructions = GraphHopperAndroid.instructionList
            self.PunktyKontrolneLat.append(float(self.latGPS))
            self.PunktyKontrolneLon.append(float(self.lonGPS))
            self.route_size.append(self.punkty.getSize() - 1)
            self.route_size.append(punkty_size)

        self.licznikTemp = True

        self.route_calculated = True
        # print('wypisane punkty')
        # print self.punkty.toString()
        self.czy_wyznacozno_trase = True
        # self.center()
        # self.ids.img_center.source = "resources/center_red.png"
        self.redraw_route()
        # print "respInMain"
        MainApp.route_nodes = True
        self.actual_point = 0
        self.actual_instruction = 0
        self.actual_instruction2 = 0
        if self.auto_center == True:
            self.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(self.actual_instruction)
        self.flagaPunktow += 1
        self.TymczasoweLat = self.latGPS
        self.TymczasoweLon = self.lonGPS

        self.ids.scrollPoints.clear_widgets(children=None)

        def SearchAdres(latAdd, lonAdd):
            g = geocoder.google([latAdd, lonAdd], method='reverse')
            city = g.city
            print "citycitycity"
            street = g.street
            print "streetstreet"
            # print str(city)
            # print str(street)
            MomentCity = g.city
            MomentStreet = g.street
            try:
                self.cityPoint = MomentCity.encode('utf-8')
            except:
                self.cityPoint = str(latAdd) + ', ' + str(lonAdd)
            try:
                self.streetPoint = MomentStreet .encode('utf-8')
                self.geoFlaga = True
            except:
                self.streetPoint = ''
                self.geoFlaga = False
            # print self.cityPoint

        # def saveGraphhopperTras(bt):
        #     if len(self.PunktyKontrolneLon) >= 2:
        #         ff = open("/sdcard/Bicom/BicomTrasa.txt", "w")
        #         ff.write("")
        #         ff.close()
        #         f = open("/sdcard/Bicom/BicomTrasa.txt", "a")
        #         if str(self.TypeBike) == 'bike':
        #             f.write(str('123.123') + "\n")
        #         elif str(self.TypeBike) == 'mtb':
        #             f.write(str('456.456') + "\n")
        #         print("test_zapisu")
        #         print(str(self.TypeBike))
        #         for j in xrange(0, len(self.PunktyKontrolneLon) - 1):
        #             f.write(str(self.PunktyKontrolneLat[j]) + " " + str(self.PunktyKontrolneLon[j]) + "\n")
        #         f.close()
        #
        # localPtah = "/sdcard/Bicom/BicomTrasa.txt"
        #
        # def loadFromBicomNonDynamic(bt):
        #
        #     scren = MainApp.get_running_app().root.carousel.slides[0]
        #     localPtah = "/sdcard/Bicom/BicomTrasa.txt"
        #     count = len(open(localPtah, 'rU').readlines())
        #     localSize = len(self.PunktyKontrolneLon)
        #
        #     self.ZerujTrase()
        #
        #     print "test_odczytu"
        #     print (count)
        #     wiersz = linecache.getline(localPtah, 1)
        #     if float(wiersz[:7]) == float(123.123):
        #         self.TypeBike = 'bike'
        #     elif float(wiersz[:7]) == float(456.456):
        #         self.TypeBike = 'mtb'
        #     #self.TypeBike = str(wiersz)
        #     print(str(wiersz[:3]))
        #     for nr in xrange(2, count + 1):
        #         wiersz = linecache.getline(localPtah, nr)
        #         if(nr == 2):
        #             # self.PunktyKontrolneLat.append(float(wiersz[11:]))
        #             # self.PunktyKontrolneLon.append(float(wiersz[:11]))
        #             self.lonGPS = float(wiersz[11:])
        #             self.latGPS = float(wiersz[:11])
        #             if float(wiersz[11:]) != MainApp.lon and float(wiersz[:11]) != MainApp.lat:
        #                 print "tttggggggggggggggg"
        #                 print(float(wiersz[11:]))
        #                 print(float(wiersz[:11]))
        #                 self.calculate_route_nodes_run_add()
        #                 map = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
        #                 mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
        #                 map.add_marker(mark)
        #                 MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)
        #                 print "ttt"
        #                 print(float(wiersz[11:]))
        #                 print(float(wiersz[:11]))
        #         else:
        #             # self.PunktyKontrolneLat.append(float(wiersz[13:]))
        #             # self.PunktyKontrolneLon.append(float(wiersz[:13]))
        #             try:
        #                 self.lonGPS = float(wiersz[13:])
        #                 self.latGPS = float(wiersz[:13])
        #             except:
        #                 self.lonGPS = float(wiersz[11:])
        #                 self.latGPS = float(wiersz[:11])
        #             mark = MapMarker(lon=float(self.lonGPS), lat=float(self.latGPS))
        #             map.add_marker(mark)
        #             MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.append(mark)
        #             # print "ttt"
        #             # print(float(wiersz[13:]))
        #             # print(float(wiersz[:13]))
        #             self.calculate_route_nodes_run_add()


        def addPointList(bt):
            self.ids.scrollPoints.clear_widgets(children=None)
            for indeks in xrange(0, len(self.PunktyKontrolneLon)):
                SearchAdres(float(self.PunktyKontrolneLat[indeks]), float(self.PunktyKontrolneLon[indeks]))
                if self.geoFlaga == True:
                    tekst = '' + self.streetPoint + ', ' + str(self.cityPoint)
                else:
                    tekst = '' + str(self.cityPoint)
                # tekst = '' + str(self.PunktyKontrolneLat[indeks]) + ', ' + str(self.PunktyKontrolneLon[indeks])

                btn3 = Button(text='x', on_release=removePoint)
                btn2 = Button(text='V', on_release=downPoint)
                btn1 = Button(text='^', on_release=upPoint)
                btn = Button(text=tekst)
                if indeks > 0:
                    btn3.id = 'BtnXX' + str(indeks)
                    btn3.color = (1, 1, 1, 0)
                    # btn3.background_normal = ''
                    btn3.text = str(indeks)
                    btn3.background_down = "resources/removeA.png"
                    btn3.background_normal = "resources/remove30.png"
                    btn3.background_color = (1, 1, 1, 1)
                    btn3.size_hint_x = 0.1

                    btn1.id = 'BtnG' + str(indeks)
                    btn1.color = (1, 1, 1, 0)
                    # btn1.background_normal = ''
                    btn1.text = str(indeks)
                    btn1.background_down = "resources/upA.png"
                    btn1.background_normal = "resources/up30.png"
                    btn1.background_color = (1, 1, 1, 1)
                    btn1.size_hint_x = 0.1

                    btn2.id = 'BtnD' + str(indeks)
                    btn2.color = (1, 1, 1, 0)
                    # btn2.background_normal = ''
                    btn2.text = str(indeks)
                    btn2.background_down = "resources/downA.png"
                    btn2.background_normal = "resources/down30.png"
                    btn2.background_color = (1, 1, 1, 1)
                    btn2.size_hint_x = 0.1

                    btn.id = 'BtnT' + str(indeks)
                    btn.color = (1, 1, 1, 1)
                    btn.background_normal = ''
                    btn.background_down = ''
                    btn.background_color = (0, 0, 0, .3)
                    btn.size_hint_x = 0.7
                    btn.font_size = self.height / 50
                else:

                    btn3.id = 'BtnXX' + str(indeks)
                    btn3.color = (1, 1, 1, 0)
                    btn3.background_normal = ''
                    btn3.text = str(indeks)
                    # btn3.background_down = "resources/remove.png"
                    # btn3.background_normal = "resources/remove.png"
                    btn3.background_color = (0, 0, 0, .3)
                    btn3.size_hint_x = 0.1

                    btn1.id = 'BtnG' + str(indeks)
                    btn1.color = (1, 1, 1, 0)
                    btn1.background_normal = ''
                    btn1.text = str(indeks)
                    # btn1.background_down = "resources/up2.png"
                    # btn1.background_normal = "resources/up2.png"
                    btn1.background_color = (0, 0, 0, .3)
                    btn1.size_hint_x = 0.1

                    btn2.id = 'BtnD' + str(indeks)
                    btn2.color = (1, 1, 1, 0)
                    btn2.background_normal = ''
                    btn2.text = str(indeks)
                    # btn2.background_down = "resources/down2.png"
                    # btn2.background_normal = "resources/down2.png"
                    btn2.background_color = (0, 0, 0, .3)
                    btn2.size_hint_x = 0.1

                    btn.id = 'BtnT' + str(indeks)
                    btn.color = (1, 1, 1, 1)
                    btn.background_normal = ''
                    btn.background_down = ''
                    btn.background_color = (0, 0, 0, .3)
                    btn.size_hint_x = 0.7
                    btn.font_size = self.height / 50

                self.ids.scrollPoints.add_widget(btn3)
                self.ids.scrollPoints.add_widget(btn1)
                self.ids.scrollPoints.add_widget(btn2)
                self.ids.scrollPoints.add_widget(btn)

            # btn4 = Button(text='z', on_release=saveGraphhopperTras)
            # btn6 = Button(text='w', on_release=loadFromBicomNonDynamic)
            # btn5 = Button(text='')
            # btn7 = Button(text='')
            #
            # btn4.id = 'BtnXX' + str(indeks)
            # btn4.color = (1, 1, 1, 1)
            # # btn3.background_normal = ''
            # #btn4.text = str(indeks)
            # btn4.background_down = ""
            # btn4.background_normal = ""
            # btn4.background_color = (0, 0, 0, .3)
            # btn4.size_hint_x = 0.1
            #
            # btn5.id = 'BtnG' + str(indeks)
            # btn5.color = (1, 1, 1, 0)
            # # b5n1.background_normal = ''
            # btn5.text = str(indeks)
            # btn5.background_down = ""
            # btn5.background_normal = ""
            # btn5.background_color = (0, 0, 0, .3)
            # btn5.size_hint_x = 0.1
            #
            # btn6.id = 'BtnD' + str(indeks)
            # btn6.color = (1, 1, 1, 1)
            # # b6n2.background_normal = ''
            # #btn6.text = str(indeks)
            # btn6.background_down = ""
            # btn6.background_normal = ""
            # btn6.background_color = (0, 0, 0, .3)
            # btn6.size_hint_x = 0.1
            #
            # btn7.id = 'BtnT' + str(indeks)
            # btn7.color = (1, 1, 1, 1)
            # btn7.background_normal = ''
            # btn7.background_down = ''
            # btn7.background_color = (0, 0, 0, .3)
            # btn7.size_hint_x = 0.7
            # btn7.font_size = self.height / 50
            #
            # self.ids.scrollPoints.add_widget(btn4)
            # self.ids.scrollPoints.add_widget(btn5)
            # self.ids.scrollPoints.add_widget(btn6)
            # self.ids.scrollPoints.add_widget(btn7)


        def upPoint(bt):
            indeks = int(bt.text)


            if indeks > 1:
                TymLon = self.PunktyKontrolneLon[indeks]
                TymLat = self.PunktyKontrolneLat[indeks]
                TymSize = self.route_size[indeks]
                self.PunktyKontrolneLon[indeks] = self.PunktyKontrolneLon[indeks - 1]
                self.PunktyKontrolneLat[indeks] = self.PunktyKontrolneLat[indeks - 1]
                self.route_size[indeks] = self.route_size[indeks - 1]
                self.PunktyKontrolneLon[indeks - 1] = TymLon
                self.PunktyKontrolneLat[indeks - 1] = TymLat
                self.route_size[indeks - 1] = TymSize
                TymMark = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks - 1]
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks - 1] = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks -2]
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks - 2] = TymMark

                addPointList(bt)
                self.recalculate_route()

        def downPoint(bt):
            indeks = int(bt.text)

            if indeks < (len(self.PunktyKontrolneLon) - 1):
                TymLon = self.PunktyKontrolneLon[indeks]
                TymLat = self.PunktyKontrolneLat[indeks]
                TymSize = self.route_size[indeks]
                TymMark = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks - 1]
                self.PunktyKontrolneLon[indeks] = self.PunktyKontrolneLon[indeks + 1]
                self.PunktyKontrolneLat[indeks] = self.PunktyKontrolneLat[indeks + 1]
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks - 1] = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks]
                self.route_size[indeks] = self.route_size[indeks + 1]
                self.PunktyKontrolneLon[indeks + 1] = TymLon
                self.PunktyKontrolneLat[indeks + 1] = TymLat
                self.route_size[indeks + 1] = TymSize
                MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list[indeks] = TymMark

                addPointList(bt)

                self.recalculate_route()

        def removePoint(bt):
            indeks = str(bt.text)
            indeks2 = -1

            if int(indeks) > 0:
                print('tttttttttttttttt', int(indeks))


                for i in xrange(0, len(self.PunktyKontrolneLon)):
                    if str(i) == str(indeks):
                        indeks2 = int(i)

                self.removeFlag = True
                Marker = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.pop(indeks2-1)

                map = MapView()
                map.remove_marker(Marker)


                self.PunktyKontrolneLon.pop(int(indeks2))
                self.PunktyKontrolneLat.pop(int(indeks2))
                self.route_size.pop(int(indeks2 - 1))

                if len(self.PunktyKontrolneLon) == 1:
                    self.PunktyKontrolneLon.pop(0)
                    self.PunktyKontrolneLat.pop(0)
                    self.flagaPunktow = 0
                    self.route_calculated = False
                    self.czy_wyznacozno_trase = False
                    MainApp.route_nodes = False
                    self.licznikTemp = False
                    self.auto_center = False
                    self.Nawiguj = False
                    self.removeFlag = False
                    self.ids.scrollPoints.clear_widgets(children=None)
                    for layer in self.ids["mapView"]._layers:
                        if layer.id == 'line_map_layer':
                            layer.czysc_trase()
                            break

                addPointList(bt)

                self.recalculate_route()

        addPointList(self)



    def finishRoute(self):
        self.route_calculated = False
        self.czy_wyznacozno_trase = False
        MainApp.route_nodes = False
        self.licznikTemp = False
        self.auto_center = False
        self.Nawiguj = False


    def ZerujTrase(self):
        self.flagaPunktow = 0
        self.route_calculated = False
        self.czy_wyznacozno_trase = False
        MainApp.route_nodes = False
        self.licznikTemp = False
        self.auto_center = False
        self.Nawiguj = False
        self.actual_point = 0
        self.FkagaPunktowSymulatora = True

        self.ids.scrollPoints.clear_widgets(children=None)
        self.ids.img_center.source = "resources/center_white.png"
        self.ids.label_instruction.text = ''
        MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lat = -82
        MainApp.get_running_app().root.carousel.slides[0].ids["marker2"].lon = 112

        localSize = len(self.PunktyKontrolneLon)
        localSizeSymulacja= len(self.punktySymulacjiLon)

        for i in xrange(1, localSizeSymulacja):
            self.punktySymulacjiLon.pop()
            self.punktySymulacjiLat.pop()

        for i in xrange(1, localSize):
            Marker = MainApp.get_running_app().root.carousel.slides[0].ids.mapView.marker_list.pop()

            map = MapView()
            map.remove_marker(Marker)


        for i in xrange(1, localSize):
            indeks = localSize - i

            self.PunktyKontrolneLon.pop(indeks)
            self.PunktyKontrolneLat.pop(indeks)
            self.route_size.pop(indeks-1)

        try:
            self.PunktyKontrolneLon.pop(0)
            self.PunktyKontrolneLat.pop(0)
        except:
            pass
        # self.recalculate_route()

        for layer in self.ids["mapView"]._layers:
            if layer.id == 'line_map_layer':
                layer.czysc_trase()
                break




    def recalculate_route(self):
        try:
            print 'test usuwania tras'

            GraphHopperAndroid.calcPath(True, self.TypeBike, float(MainApp.lat), float(MainApp.lon),
                                        float(self.PunktyKontrolneLat[self.travelled_points + 1]),
                                        float(self.PunktyKontrolneLon[self.travelled_points + 1]))
            self.punkty = GraphHopperAndroid.resp.getPoints()
            self.instructions = GraphHopperAndroid.instructionList

            self.route_size[self.travelled_points + 1] = (self.punkty.getSize())

            self.actual_point = 0
            self.actual_instruction = 0
            self.actual_instruction2 = 0
            if self.auto_center == True:
                self.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(self.actual_instruction)



            if (self.travelled_points + 1) < (len(self.PunktyKontrolneLat)-1):
                for i in xrange(self.travelled_points + 1, len(self.PunktyKontrolneLat) - 1):
                    GraphHopperAndroid.calcPath(False, self.TypeBike, float(self.PunktyKontrolneLat[i]),
                                                             float(self.PunktyKontrolneLon[i]),
                                                             float(self.PunktyKontrolneLat[i + 1]),
                                                             float(self.PunktyKontrolneLon[i + 1]))
                    self.punkty_aktualne = GraphHopperAndroid.resp.getPoints()
                    punkty_size = self.punkty_aktualne.getSize()
                    self.punkty.removeLast()
                    for j in xrange(0, punkty_size):
                        lat = float(self.punkty_aktualne.getLat(j))
                        lon = float(self.punkty_aktualne.getLon(j))
                        ele = float(self.punkty_aktualne.getEle(j))

                        self.punkty.add(lat, lon, ele)

                    self.route_size[i + 1] = punkty_size

                    GraphHopperAndroid.connectInstructions()
                    # self.punkty.removeLast()

            self.route_calculated = True
            self.czy_wyznacozno_trase = True
            MainApp.route_nodes = True
            self.redraw_route()


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

        distance = sqrt(pow((lat2 - lat1), 2) + pow(cos(lat1 * pi / 180) * (lon2 - lon1), 2)) * 40075.704 / 360

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
        if b == 0:
            ab = 0
        else:
            ab = a / b
        abx = ab * x
        c = x2 * y1 - x1 * y2
        d = x2 - x1
        if d == 0:
            cd = 0
        else:
            cd = c / d

        nominator = abs(abx - y + cd)
        dominator = sqrt(pow(((y2 - y1) / x2 - x1), 2) + 1)

        z = nominator / dominator
        print z
        print "z"
        if z >= .4e-05:
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


    def CallScreenNextCarousel(self):
        MainApp.get_running_app().root.carousel.load_next(mode='next')

    def CallScreenPreviousCarousel(self):
        MainApp.get_running_app().root.carousel.load_previous()

    def dismiss_popup(self):
        self._popup.dismiss()

    def numberSelect(self):
        content = ChooseNumber(cancel=self.dismiss_popup)

        self._popup = Popup(title="Wybierz numer", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


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


    def view_contact(self):
        if platform() == 'android':
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")

            content_resolver = activity.getApplicationContext()

            resolver = content_resolver.getContentResolver()
            phones = resolver.query(Phone.CONTENT_URI, None, None, None, None)

            def callPhone(bt):
                Uri = autoclass('android.net.Uri')
                Intent = autoclass('android.content.Intent')
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
                tel = ''
                for contact in contactsFavorite:
                    if bt.text == contact.display_name:
                        tel = contact.number
                num = "tel:"
                num = num + tel
                intent = Intent(Intent.ACTION_CALL)
                intent.setData(Uri.parse(num))
                currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
                currentActivity.startActivity(intent)

            self.read_groups()

            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

            contactsFavorite.sort(key=lambda contact: contact.display_name)
            for contact in contactsFavorite:
                btn1 = Button(text=contact.display_name, on_release=callPhone)
                btn = Button(text=contact.display_name)
                if contactsFavorite.index(contact) % 2 == 0:
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



    def download_contact(self):
        if platform() == 'android':
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")

            content_resolver = activity.getApplicationContext()

            resolver = content_resolver.getContentResolver()
            Data = autoclass("android.provider.ContactsContract$Data")
            phones = resolver.query(Phone.CONTENT_URI, None, None, None, None)
            phones2 = resolver.query(Data.CONTENT_URI, None, None, None, None)
            phonesFav = resolver.query(Phone.CONTENT_URI, None, "starred=1", None, None)
            # phones2 = resolver.query(Data.CONTENT_URI, None, "starred=1", None, None)
            pho = phones
            pho2 = phones2
            phoFav = phonesFav

            self.read_groups()

            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            print "cosik4"
            while (phones2.moveToNext()):
                name = pho2.getString(pho2.getColumnIndex("display_name"))
                phoneNumber = pho2.getString(pho2.getColumnIndex(Phone.NUMBER))
                contact_group_id = pho2.getString(pho2.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name

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

                num = str(phoneNumber)
                num = num.replace(" ", "")
                num = num.replace("-", "")
                if num[0] == "+":
                    num = num[-9:]
                current_contact = Contact(str(name), str(num), str(contact_group_id), str(contact_group_name))
                contacts.append(current_contact)

            while(phonesFav.moveToNext()):
                name = phoFav.getString(phoFav.getColumnIndex("display_name"))
                phoneNumber = phoFav.getString(phoFav.getColumnIndex(Phone.NUMBER))
                contact_group_id = phoFav.getString(phoFav.getColumnIndex(GroupMembership.GROUP_ROW_ID))
                contact_group_name = -1
                for group in groups:
                    if contact_group_id == group.id:
                        contact_group_name = group.name

                num = str(phoneNumber)
                num = num.replace(" ", "")
                num = num.replace("-", "")
                if num[0] == "+":
                    num = num[-9:]
                current_contact = Contact(str(name), str(num), str(contact_group_id), str(contact_group_name))
                contactsFavorite.append(current_contact)

            contacts.sort(key=lambda contact: contact.display_name)
            contacts2.sort(key=lambda contact: contact.display_name)
            contactsFavorite.sort(key=lambda contact: contact.display_name)

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


class Speedometer(Screen):
    gps_speed=1
    def build(self):


        pass

class Weather(Screen):
    czy_burza = 0.5
    miejscowosc = ''
    czy_noc=BooleanProperty()
    niebieski=(0.235, 0.529, 0.572, 1)
    czerwony=(0.86, 0.08, 0.23, 1)
    kolor1=(0,0,0,0)

    def WeatherNextCarousel(self):
        MainApp.get_running_app().root.carousel.load_next(mode='next')

    def WeatherPreviousCarousel(self):
        MainApp.get_running_app().root.carousel.load_previous()

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
        search_url=search_template.format(MainApp.lat, MainApp.lon)
        data=requests.get(search_url).json()

        print "pobieranie prognozy"
        search_template_forecast="http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=b26433c9a2c69c16c1d138cc5710fd57"
        search_url_forecast=search_template_forecast.format(MainApp.lat, MainApp.lon)
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
        print data_forecast
        print data_forecast['list'][1]
        print data_forecast['city']['name']
        self.miejscowosc=data_forecast['city']['name']

        print self.miejscowosc
        print Weather.miejscowosc
        print Weather().miejscowosc
        temp = data_forecast['list'][0]['main']['temp'] - 273.15
        temp_forecast=data_forecast['list'][1]['main']['temp']-273.15
        temp=round(temp,2)
        temp_forecast=round(temp_forecast,2)

        print "czy mamy noc?2"
        print str(self.czy_noc)
        print "sprawdzam obrazek 1"
        if data_forecast['list'][0]['clouds']['all'] >= 0 and data_forecast['list'][0]['clouds'][
            'all'] < 15 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/sunny.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 0 and data_forecast['list'][0]['clouds'][
            'all'] < 15 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/night.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 15 and data_forecast['list'][0]['clouds'][
            'all'] < 30 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids[
                "obrazek_pogody"].source = 'resources/partialy-cloudy.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 15 and data_forecast['list'][0]['clouds'][
            'all'] < 30 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/dark-night.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 30 and data_forecast['list'][0]['clouds'][
            'all'] < 70 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids[
                "obrazek_pogody"].source = 'resources/cloud-with-sun.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 30 and data_forecast['list'][0]['clouds'][
            'all'] < 70 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/dark-night.png'
        elif data_forecast['list'][0]['clouds']['all'] >= 70 and data_forecast['list'][0]['clouds']['all'] <= 100:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/cloudly.png'
        print "sprawdzam obrazek 2"
        if data_forecast['list'][1]['clouds']['all'] >= 0 and data_forecast['list'][1]['clouds'][
            'all'] < 15 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/sunny.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 0 and data_forecast['list'][1]['clouds'][
            'all'] < 15 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/night.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 15 and data_forecast['list'][1]['clouds'][
            'all'] < 30 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids[
                "obrazek_pogody2"].source = 'resources/partialy-cloudy.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 15 and data_forecast['list'][1]['clouds'][
            'all'] < 30 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/dark-night.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 30 and data_forecast['list'][1]['clouds'][
            'all'] < 70 and self.czy_noc == False:
            MainApp.get_running_app().root.carousel.slides[4].ids[
                "obrazek_pogody2"].source = 'resources/cloud-with-sun.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 30 and data_forecast['list'][1]['clouds'][
            'all'] < 70 and self.czy_noc == True:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/dark-night.png'
        elif data_forecast['list'][1]['clouds']['all'] >= 70 and data_forecast['list'][1]['clouds']['all'] <= 100:
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/cloudly.png'
        print "sprawdzam obrazek 3"
        try:
            rain = data_forecast['list'][0]['rain']['3h']
            rain = round(rain, 2)
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody"].source = 'resources/opady.png'
        except:
            rain = 0
        print "sprawdzam obrazek 4"
        try:
            rain_forecast = data_forecast['list'][1]['rain']['3h']
            rain_forecast = round(rain_forecast, 2)
            MainApp.get_running_app().root.carousel.slides[4].ids["obrazek_pogody2"].source = 'resources/opady.png'
        except:
            rain_forecast = 0

        humidity = data_forecast['list'][0]['main']['humidity']
        humidity_forecast = data_forecast['list'][1]['main']['humidity']

        #place=data_forecast['city']['coord']['name']
        #name=data_forecast['list'][0]['weather']['main']

        wind = data_forecast['list'][0]['wind']['speed']
        wind=round(wind,2)
        wind_forecast = data_forecast['list'][1]['wind']['speed']
        wind_forecast=round(wind_forecast,2)

        kier=data_forecast['list'][0]['wind']['speed']
        if kier<=22.5 or kier>337.5:
            kierunek='N'
        if kier <= 67.5 and kier > 22.5:
            kierunek = 'NE'
        if kier <= 112.5 and kier > 67.5:
            kierunek = 'E'
        if kier <= 157.5 and kier > 112.5:
            kierunek = 'SE'
        if kier <= 202.5 and kier > 157.5:
            kierunek = 'S'
        if kier <= 247.5 and kier > 202.5:
            kierunek = 'SW'
        if kier <= 292.5 and kier > 247.5:
            kierunek = 'W'
        if kier <= 337.5 and kier > 292.5:
            kierunek = 'NW'

        kier_forecast=data_forecast['list'][1]['wind']['speed']
        if kier_forecast<22.5 or kier_forecast>=337.5:
            kierunek_forecast='N'
        if kier_forecast < 67.5 and kier_forecast >= 22.5:
            kierunek_forecast = 'NE'
        if kier_forecast < 112.5 and kier_forecast >= 67.5:
            kierunek_forecast = 'E'
        if kier_forecast < 157.5 and kier_forecast >= 112.5:
            kierunek_forecast = 'SE'
        if kier_forecast < 202.5 and kier_forecast >= 157.5:
            kierunek_forecast = 'S'
        if kier_forecast < 247.5 and kier_forecast > 202.5:
            kierunek_forecast = 'SW'
        if kier_forecast < 292.5 and kier_forecast >= 247.5:
            kierunek_forecast = 'W'
        if kier_forecast < 337.5 and kier_forecast >= 292.5:
            kierunek_forecast = 'NW'

        print 'koniec zxzxzx'
        #location=(data['sys']['country'],data['name'])
        MainApp.get_running_app().root.carousel.slides[4].ids["label_temperatura"].text = str(temp)+str('°C')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_opady"].text = str(rain) + str(' mm')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_wilgotnosc"].text = str(humidity) + str('%')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_wiatr"].text = str(kierunek) + " " + str(
            wind) + str(' m/s ')
        #MainApp.get_running_app().root.carousel.slides[5].ids["label_miejscowosc"].text = str(place)
        #MainApp.get_running_app().root.carousel.slides[5].ids["label_czas"].text = str(time)
        #MainApp.get_running_app().root.carousel.slides[5].ids["label_nazwa_pogody"].text = str(name)

        MainApp.get_running_app().root.carousel.slides[4].ids["label_forecast_temperatura"].text = str(temp_forecast) + str('°C')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_forecast_opady"].text = str(rain_forecast) + str(
            ' mm')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_forecast_wilgotnosc"].text = str(humidity_forecast) + str(
            '%')
        MainApp.get_running_app().root.carousel.slides[4].ids["label_forecast_wiatr"].text = str(wind_forecast) + str(
            'm/s ') + str(kierunek_forecast)
        return data_forecast['city']['name']

    def burze_api(self,key, wsdl_file, city, range_detect):
        server = WSDL.Proxy(wsdl_file)
        xy = server.miejscowosc(city, key)
        ostrzezenia = server.ostrzezenia_pogodowe(xy['y'], xy['x'], key)
        burza = server.szukaj_burzy(xy['y'], xy['x'], range_detect, key)
        return [ostrzezenia, burza]

    def print_burza(self,burza):
        print "=== Wykrywanie burzy ==="
        if burza['liczba'] == 0:
            Weather.czy_burza=1
            print "Weather().czy_burza="+str(self.czy_burza)
            print "whahahaha mamy radarN"
            StormPopup.ktory_radar = "resources/radarN.png"
            StormPopup.background_color = (1, 1, 0, 1)
            #self.czy_burza = 0
            #MainApp.get_running_app().root.carousel.slides[0].ids["label_burza"].color = (0, 1, 0, 0.3)
            print "Brak burzy"
        else:
            Weather.czy_burza=0
            print "Weather().czy_burza=" + str(Weather().czy_burza)
            print "Uwaga! Wyladowania atmosferyczne w odleglosci ", str(burza['odleglosc']), "km"
            print "Kierunek: ", str(burza['kierunek'])
            if str(burza['kierunek'])=='N':
                print "whahahaha mamy radarN"
                if burza['odleglosc']>=50:
                    StormPopup.background_color = (1, 1, 0, 1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarN.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: N"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: Północy")
            elif str(burza['kierunek'])=='NE':
                print "whahahaha mamy radarNE"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarNE.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: NE"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: Północy wschód")
            elif str(burza['kierunek'])=='E':
                print "whahahaha mamy radarE"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarE.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: E"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: wschodni")
            elif str(burza['kierunek'])=='SE':
                print "whahahaha mamy radarSE"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarSE.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: SE"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: południowo wschodni")
            elif str(burza['kierunek'])=='S':
                print "whahahaha mamy radarS"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarS.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: S"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: południowy")
            elif str(burza['kierunek'])=='SW':
                print "whahahaha mamy radarSW"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarSW.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: SW"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: południowo zachodni")
            elif str(burza['kierunek'])=='W':
                print "whahahaha mamy radarW"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarW.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: W"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: zachodni")
            elif str(burza['kierunek'])=='NW':
                print "whahahaha mamy radarNW"
                if burza['odleglosc']>=50:
                    StormPopup.color=(1,1,0,.1)
                elif burza['odleglosc']>=20 and burza['odleglosc']<50:
                    StormPopup.color=(1,.5,0,.3)
                else:
                    StormPopup.color=(1,0,0,.3)
                StormPopup.ktory_radar = "resources/radarNW.png"
                StormPopup.text = "Uwaga!\nBurze w odleglosci "+str(burza['odleglosc'])+"km\nKierunek: NW"
                print "wykonal sie popup"
                activity.readStormAlerts("Uwaga! Burze w odleglosci "+str(burza['odleglosc'])+"km. Kierunek: północno zachodni")
                print "powinno przeczytac"
            print "Liczba: ", str(burza['liczba'])
            print "Odleglosc: ", str(burza['odleglosc']), "km"
            print "Okres: ", str(burza['okres']), "min"

    def print_ostrzezenia(self,ostrzezenia):
        print "=== Ostrzezenia pogodowe==="
        print "Mroz: {0} {1} {2}".format(ostrzezenia['mroz'], ostrzezenia['mroz_od_dnia'], ostrzezenia['mroz_od_dnia'])
        print "Upal: {0} {1} {2}".format(ostrzezenia['upal'], ostrzezenia['upal_od_dnia'], ostrzezenia['upal_od_dnia'])
        print "Wiatr: {0} {1} {2}".format(ostrzezenia['wiatr'], ostrzezenia['wiatr_od_dnia'],
                                          ostrzezenia['wiatr_od_dnia'])
        print "Opad: {0} {1} {2}".format(ostrzezenia['opad'], ostrzezenia['opad_od_dnia'], ostrzezenia['opad_od_dnia'])
        print "Burza: {0} {1} {2}".format(ostrzezenia['burza'], ostrzezenia['burza_od_dnia'],
                                          ostrzezenia['burza_od_dnia'])
        print "Traba: {0} {1} {2}".format(ostrzezenia['traba'], ostrzezenia['traba_od_dnia'],
                                          ostrzezenia['traba_od_dnia'])


class ScreenSettings(Screen):





    #motyw = self.config.get('wyglad', 'boolwyglad')

    # if motyw == int(1):
    #     pass
    #     # Ustawienia.kolor = (0.235, 0.529, 0.622, 0.6)
    #
    # if motyw == int(0):
    #     pass

    #return Ustawienia()

    pass







class LineMapLayer(MapLayer):
    id = 'line_map_layer'

    def __init__(self, **kwargs):
        super(LineMapLayer, self).__init__()
        self.zoom = 0



    '''W momencie przemieszczenia mapy przerysowujemy linie'''

    def reposition(self):
        mapview = self.parent
        if (self.zoom != mapview.zoom and MainApp.route_nodes == True):
            self.draw_line()

    '''Funkcja rysowania linii'''

    def czysc_trase(self):
        self.canvas.clear()

    def draw_line(self):
        if MainApp.get_running_app().root.carousel.slides[0].route_calculated == True:
            mapview = self.parent
            group_screen = self.parent.parent.parent.parent.parent
            self.zoom = mapview.zoom

            point_list = []
            '''Wywolujemy funkcje ktora zwraca nam wspolrzedne trasy o danych wspolzednych poczatkowych i koncowych (Gdzie to przeniesc???)'''

            punkty_size = group_screen.punkty.getSize()
            print punkty_size
            point_list.extend(mapview.get_window_xy_from(float(MainApp.lat), float(MainApp.lon), mapview.zoom))
            for j in xrange(group_screen.actual_point, punkty_size - 1):
                lat = float(group_screen.punkty.getLat(j))
                lon = float(group_screen.punkty.getLon(j))
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

    Kontakty = []

    def __init__(self, **kwargs):
        super(ZoneButton, self).__init__(**kwargs)
        ZoneButton._instance_count += 1

    def pop(self, tytul):
        pass

        '''if platform() == 'android':
            activity = autoclass("org.renpy.android.PythonActivity").mActivity
            GroupMembership = autoclass("android.provider.ContactsContract$CommonDataKinds$GroupMembership")
            Phone = autoclass("android.provider.ContactsContract$CommonDataKinds$Phone")
            Data = autoclass("android.provider.ContactsContract$Data")
            RawContactsColumns = autoclass("android.provider.ContactsContract$RawContactsColumns")
            content_resolver = activity.getApplicationContext()
            resolver = content_resolver.getContentResolver()

            for i in range(0, len(ZoneList.ListaNazw)):
                if tytul == ZoneList.ListaNazw[i]:
                    groupID = ZoneList.ListaId[i]
                    break

            projection = [RawContactsColumns.CONTACT_ID, GroupMembership.GROUP_ROW_ID]

            grupa = resolver.query(Data.CONTENT_URI, projection, GroupMembership.GROUP_ROW_ID + "=" + groupID, None,
                                   None)
            group = grupa

            while (grupa.moveToNext()):
                id = group.getString(group.getColumnIndex("CONTACT_ID"))

                grupa2 = resolver.query(Phone.CONTENT_URI, None, Phone.CONTACT_ID + "=" + id, None, None)
                group2 = grupa2

                while (grupa2.moveToNext()):
                    nazwa = group2.getString(group2.getColumnIndex("DISPLAY_NAME"))
                    if nazwa not in ZoneButton.Kontakty:
                        ZoneButton.Kontakty.append(nazwa)

                grupa2.close()
            grupa.close()

        popup = Popup(title=tytul, title_color=(.235, .529, .572, 1), title_align='center',
                      separator_color=(.235, .529, .572, 1),
                      # background= 'atlas://data/images/defaulttheme/filechooser_selected',
                      auto_dismiss=False,
                      size_hint=(None, None),
                      size=(400, 400))

        layout1 = StackLayout(orientation='lr-bt')

        zamknij = Button(text='Zamknij', background_color=(.235, .529, .572, 1), size_hint_y=None, height=40)
        zamknij.bind(on_release=popup.dismiss)

        scrlv = ScrollView(size_hint=(1, 0.86))

        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))

        # groupID = '1'

        if len(ZoneButton.Kontakty) < 1:
            ZoneButton.Kontakty = []
            ZoneButton.Kontakty.append("Brak kontaktów w tej grupie.")

            for i in range(0, len(ZoneButton.Kontakty)):
                btn = Button(text=ZoneButton.Kontakty[i],
                             color=(.235, .529, .572, 1),
                             size_hint_y=None,
                             height=200,
                             width=200,
                             valign='middle',
                             halign='center',
                             font_size=20)

                btn.text_size = (btn.size)
                btn.background_color = (.941, .941, .937, 0)
                layout2.add_widget(btn)

        elif int(groupID) == int(999):
            ZoneButton.Kontakty = []
            ZoneButton.Kontakty.append(
                "Ta grupa przeznaczona jest dla nieznanych numerów i nie zawiera żadnego kontaktu.")

            for i in range(0, len(ZoneButton.Kontakty)):
                btn = Button(text=ZoneButton.Kontakty[i],
                             color=(.235, .529, .572, 1),
                             size_hint_y=None,
                             height=200,
                             width=200,
                             valign='middle',
                             halign='center',
                             font_size=20)

                btn.text_size = (btn.size)
                btn.background_color = (.941, .941, .937, 0)
                layout2.add_widget(btn)
        else:
            for i in range(0, len(ZoneButton.Kontakty)):
                btn = Button(text=ZoneButton.Kontakty[i],
                             color=(.235, .529, .572, 1),
                             size_hint_y=None,
                             height=40,
                             width=200,
                             valign='middle',
                             halign='center',
                             font_size=20)

                btn.text_size = (btn.size)
                btn.background_color = (.941, .941, .937, 0)
                layout2.add_widget(btn)

        scrlv.add_widget(layout2)
        layout1.add_widget(zamknij)
        layout1.add_widget(scrlv)
        popup.content = layout1
        popup.open()

        ZoneButton.Kontakty = []

    def scroll_change(self, scrlv, instance, value):
        scrlv.scroll_y = value'''




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


class PreviewCallback(PythonJavaClass):
    '''Interface used to get back the preview frame of the Android Camera
    '''
    __javainterfaces__ = ('android.hardware.Camera$PreviewCallback',)

    def __init__(self, callback):
        super(PreviewCallback, self).__init__()
        self.callback = callback

    @java_method('([BLandroid/hardware/Camera;)V')
    def onPreviewFrame(self, data, camera):
        self.callback(camera, data)


class SurfaceHolderCallback(PythonJavaClass):
    '''Interface used to know exactly when the Surface used for the Android
    Camera will be created and changed.
    '''

    __javainterfaces__ = ('android.view.SurfaceHolder$Callback',)

    def __init__(self, callback):
        super(SurfaceHolderCallback, self).__init__()
        self.callback = callback

    @java_method('(Landroid/view/SurfaceHolder;III)V')
    def surfaceChanged(self, surface, fmt, width, height):
        self.callback(fmt, width, height)

    @java_method('(Landroid/view/SurfaceHolder;)V')
    def surfaceCreated(self, surface):
        pass

    @java_method('(Landroid/view/SurfaceHolder;)V')
    def surfaceDestroyed(self, surface):
        pass


class AndroidWidgetHolder(Widget):
    '''Act as a placeholder for an Android widget.
    It will automatically add / remove the android view depending if the widget
    view is set or not. The android view will act as an overlay, so any graphics
    instruction in this area will be covered by the overlay.
    '''

    view = ObjectProperty(allownone=True)
    '''Must be an Android View
    '''

    def __init__(self, **kwargs):
        self._old_view = None
        from kivy.core.window import Window
        self._window = Window
        kwargs['size_hint'] = (None, None)
        super(AndroidWidgetHolder, self).__init__(**kwargs)

    def on_view(self, instance, view):
        if self._old_view is not None:
            layout = cast(LinearLayout, self._old_view.getParent())
            layout.removeView(self._old_view)
            self._old_view = None

        if view is None:
            return

        activity = PythonActivity.mActivity
        activity.addContentView(view, LayoutParams(*self.size))
        view.setZOrderOnTop(True)
        view.setX(self.x)
        view.setY(self._window.height - self.y - self.height)
        self._old_view = view

    def on_size(self, instance, size):
        if self.view:
            params = self.view.getLayoutParams()
            params.width = self.width
            params.height = self.height
            self.view.setLayoutParams(params)
            self.view.setY(self._window.height - self.y - self.height)

    def on_x(self, instance, x):
        if self.view:
            self.view.setX(x)

    def on_y(self, instance, y):
        if self.view:
            self.view.setY(self._window.height - self.y - self.height)


class AndroidCamera(Widget):
    '''Widget for controling an Android Camera.
    '''

    index = NumericProperty(0)

    __events__ = ('on_preview_frame',)

    def __init__(self, **kwargs):
        self._holder = None
        self._android_camera = None
        super(AndroidCamera, self).__init__(**kwargs)
        self._holder = AndroidWidgetHolder(size=self.size, pos=self.pos)
        self.add_widget(self._holder)

    @run_on_ui_thread
    def stop(self):
        if self._android_camera is None:
            return
        self._android_camera.setPreviewCallback(None)
        self._android_camera.release()
        self._android_camera = None
        self._holder.view = None

    @run_on_ui_thread
    def start(self):
        if self._android_camera is not None:
            return

        self._android_camera = Camera.open(self.index)

        # create a fake surfaceview to get the previewCallback working.
        self._android_surface = SurfaceView(PythonActivity.mActivity)
        surface_holder = self._android_surface.getHolder()

        # create our own surface holder to correctly call the next method when
        # the surface is ready
        self._android_surface_cb = SurfaceHolderCallback(self._on_surface_changed)
        surface_holder.addCallback(self._android_surface_cb)

        # attach the android surfaceview to our android widget holder
        self._holder.view = self._android_surface

    def _on_surface_changed(self, fmt, width, height):
        # internal, called when the android SurfaceView is ready
        # FIXME if the size is not handled by the camera, it will failed.
        params = self._android_camera.getParameters()
        params.setPreviewSize(width, height)
        self._android_camera.setParameters(params)

        # now that we know the camera size, we'll create 2 buffers for faster
        # result (using Callback buffer approach, as described in Camera android
        # documentation)
        # it also reduce the GC collection
        bpp = ImageFormat.getBitsPerPixel(params.getPreviewFormat()) / 8.
        buf = '\x00' * int(width * height * bpp)
        self._android_camera.addCallbackBuffer(buf)
        self._android_camera.addCallbackBuffer(buf)

        # create a PreviewCallback to get back the onPreviewFrame into python
        self._previewCallback = PreviewCallback(self._on_preview_frame)

        # connect everything and start the preview
        self._android_camera.setPreviewCallbackWithBuffer(self._previewCallback);
        self._android_camera.setPreviewDisplay(self._android_surface.getHolder())
        self._android_camera.startPreview();

    def _on_preview_frame(self, camera, data):
        # internal, called by the PreviewCallback when onPreviewFrame is
        # received
        self.dispatch('on_preview_frame', camera, data)
        # reintroduce the data buffer into the queue
        self._android_camera.addCallbackBuffer(data)

    def on_preview_frame(self, camera, data):
        pass

    def on_size(self, instance, size):
        if self._holder:
            self._holder.size = size

    def on_pos(self, instance, pos):
        if self._holder:
            self._holder.pos = pos


class ZbarQrcodeDetector(AnchorLayout):
    '''Widget that use the AndroidCamera and zbar to detect qrcode.
    When found, the `symbols` will be updated
    '''
    camera_size = ListProperty([320, 240])

    symbols = ListProperty([])

    # XXX can't work now, due to overlay.
    show_bounds = BooleanProperty(False)

    Qrcode = namedtuple('Qrcode',
                        ['type', 'data', 'bounds', 'quality', 'count'])

    def __init__(self, **kwargs):
        super(ZbarQrcodeDetector, self).__init__(**kwargs)
        self._camera = AndroidCamera(
            size=self.camera_size,
            size_hint=(None, None))
        self._camera.bind(on_preview_frame=self._detect_qrcode_frame)
        self.add_widget(self._camera)

        # create a scanner used for detecting qrcode
        self._scanner = ImageScanner()
        self._scanner.setConfig(0, Config.ENABLE, 0)
        self._scanner.setConfig(Symbol.QRCODE, Config.ENABLE, 1)
        self._scanner.setConfig(0, Config.X_DENSITY, 3)
        self._scanner.setConfig(0, Config.Y_DENSITY, 3)

    def start(self):
        self._camera.start()

    def stop(self):
        self._camera.stop()

    def _detect_qrcode_frame(self, instance, camera, data):
        # the image we got by default from a camera is using the NV21 format
        # zbar only allow Y800/GREY image, so we first need to convert,
        # then start the detection on the image
        parameters = camera.getParameters()
        size = parameters.getPreviewSize()
        barcode = Image(size.width, size.height, 'NV21')
        barcode.setData(data)
        barcode = barcode.convert('Y800')

        result = self._scanner.scanImage(barcode)

        if result == 0:
            self.symbols = []
            return

        # we detected qrcode! extract and dispatch them
        symbols = []
        it = barcode.getSymbols().iterator()
        while it.hasNext():
            symbol = it.next()
            qrcode = ZbarQrcodeDetector.Qrcode(
                type=symbol.getType(),
                data=symbol.getData(),
                quality=symbol.getQuality(),
                count=symbol.getCount(),
                bounds=symbol.getBounds())
            symbols.append(qrcode)

        self.symbols = symbols

    '''
    # can't work, due to the overlay.
    def on_symbols(self, instance, value):
        if self.show_bounds:
            self.update_bounds()

    def update_bounds(self):
        self.canvas.after.remove_group('bounds')
        if not self.symbols:
            return
        with self.canvas.after:
            Color(1, 0, 0, group='bounds')
            for symbol in self.symbols:
                x, y, w, h = symbol.bounds
                x = self._camera.right - x - w
                y = self._camera.top - y - h
                Line(rectangle=[x, y, w, h], group='bounds')
    '''


class MainApp(App):
    gps_speed = 0.00
    highest_speed = 0.00
    highest_speed_float = 0.00
    distance = 0.00
    calories = 0.00
    gps_status = StringProperty('Click Start to get GPS location updates')
    lat = 52.9828
    lon = 18.5729
    flagCenter = True
    # screensettings.kv tymczasowo zakomentowany w pliku main.kv
    Builder.load_file("screensettings.kv")
    Builder.load_file("groupscreen.kv")
    Builder.load_file("callscreen.kv")
    Builder.load_file("musicplayer.kv")
    Builder.load_file("grupy.kv")
    # Zakomentowane w pliku main.kv
    # Builder.load_file("speedometer.kv")
    Builder.load_file("weather.kv")
    znacznik = 0
    route_nodes = BooleanProperty(False)
    prev_time = datetime.datetime.now().time()
    gr = GroupScreen()
    lastInstruction = ''
    flagaWygladu = True
    flagaWykonania = True
    tabela_speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # nie smiac sie! ;)
    licz = 0
    wystarczy = 0
    avg_speed = 0.00
    suma = 0
    licz2 = 0
    all = True
    timeNow = 0.0
    timeLast = 0.0
    LastLat = 0
    LastLon = 0
    distanceSpeed = 0
    TimeSpeed = 0
    licznikSpeed = 0
    FlagaLicznik = False
    navi_path = '/sdcard/Bicom/Mapy'
    readSmsState = 2
    readStormState = 2
    distLabel = 0
    FlagaWysylania = 0
    topicLabel = random.randrange(1000, 10000, 2)
    ostatnie_predkosci = [0, 0, 0, 0, 0, 0]
    j = 0
    k = 0
    skrzyzowanieLat = [53.008887, 53.008887, 53.011923,53.011923, 53.011923, 53.011923,53.011923, 53.011880, 53.011880,53.011880,53.011880,53.011880,53.009383,
                       53.009383]
    skrzyzowanieLon = [18.585147, 18.585147, 18.585732, 18.585732, 18.585732, 18.585732, 18.585732, 18.596178,18.596178,18.596178,18.596178,18.596178,18.593510,18.593510]



    def build(self):
        show_time = ShowTime()
        try:
            Hardware.magneticFieldSensorEnable(True)
        except:
            print "nie masz kompasu"
        callS = CallScreen()
        callS.download_contact()

        # słuzy do zmiany flagi co godzinę, wykorzystywane przy pobieraniu pogody
        def UstawFlage(self):
            self.flagaWygladu = True



        Clock.schedule_interval(show_time.check, 1)
        Clock.schedule_interval(UstawFlage, 3600)
        Clock.schedule_interval(self.on_location_symuluj, 1)
        Clock.schedule_interval(self.group_update_marker, 1)
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            self.start(1000, 0)
        except NotImplementedError:
            self.gps_status = 'GPS is not implemented for your platform'


        activity.runRecognizerSetup();

        self.settings_cls = SettingsWithSpinner
        self.use_kivy_settings = False

        print 'znacznik'

        MainApp.navi_path = self.config.get('nawigacja', 'pathnawigacja1')

        MainApp.readSmsState = self.config.get('glos', 'optionsglos1').encode('ascii', 'ignore')
        MainApp.readStormState = self.config.get('glos', 'optionsglos2').encode('ascii', 'ignore')
        zawsze = 'zawsze wczone'
        sluchawki = 'tylko w suchawkach'
        nigdy = 'nigdy'


        print zawsze
        print type(MainApp.readSmsState)
        print MainApp.readSmsState

        if MainApp.readSmsState == zawsze:
            activity.readSmsState = 1
        elif MainApp.readSmsState == sluchawki:
            activity.readSmsState = 2
        elif MainApp.readSmsState == nigdy:
            activity.readSmsState = 3

        if MainApp.readStormState == zawsze:
            activity.readStormState = 1
        elif MainApp.readStormState == sluchawki:
            activity.readStormState = 2
        elif MainApp.readStormState == nigdy:
            activity.readStormState = 3
        print 'znacznik2'
        return show_time

    def build_config(self, config):
        config.setdefaults('ogolne', {
            'optionsplec': 'mężczyzna'})

        config.setdefaults('ogolne', {
            'waga': 70})

        config.setdefaults('ekran', {
            'optionsekran': 'zawsze włączony'})

        config.setdefaults('wyglad', {'boolwyglad': False})

        config.setdefaults('nawigacja', {
            'pathnawigacja': '/sdcard/Bicom/Moje_trasy/'})

        config.setdefaults('nawigacja', {
            'pathnawigacja1': '/sdcard/Bicom/Mapy/'})

        config.setdefaults('glos', {
            'optionsglos1': 'tylko w słuchawkach'})

        config.setdefaults('glos', {
            'optionsglos2': 'tylko w słuchawkach'})

        config.setdefaults('glos', {
            'optionsglos3': 'tylko w słuchawkach'})


    def build_settings(self, settings):
        self.textcolor = 0, 0, 0, 0
        settings.add_json_panel('Ogólne', self.config, data=settings_json)
        settings.add_json_panel('Komunikaty Głosowe', self.config, data=settings_json1)

    def on_config_change(self, config, section, key, value):

        gr = GroupScreen()
        print "zmieniloSie"
        print key
        if section == 'ekran' and key == 'optionsekran' and value == 'zawsze włączony':
            '''print self'''

        if section == 'wyglad' and key == 'boolwyglad' and value == '1':
            print ('Tryb ciemny')
            # Ustawienia.kolor = (0.235, 0.529, 0.622, 0.6)

        if section == 'wyglad' and key == 'boolwyglad' and value == '0':
            print ('Tryb jasny')
            # Ustawienia.kolor = (0,0,0,1)

        if section == 'nawigacja':
            print('nawigacja')
            if key == 'pathnawigacja':
                print('pathnawigacja')
                MainApp.navi_path = value
                gr.changeGpxPath(value)

            if key == 'pathnawigacja1':
                print 'pathnawigacja1'
                MainApp.navi_path = value
                gr.savepath(value)

        if section == 'glos':
            if key == 'optionsglos1':
                if value.encode('ascii', 'ignore') == 'zawsze wczone':
                    activity.readSmsState = 1
                if value.encode('ascii', 'ignore') == 'tylko w suchawkach':
                    activity.readSmsState = 2
                if value.encode('ascii', 'ignore') == 'nigdy':
                    activity.readSmsState = 3

            if key == 'optionsglos2':
                if value.encode('ascii', 'ignore') == 'zawsze wczone':
                    activity.readStormState = 1
                if value.encode('ascii', 'ignore') == 'tylko w suchawkach':
                    activity.readStormState = 2
                if value.encode('ascii', 'ignore') == 'nigdy':
                    activity.readStormState = 3
            if key == 'optionsglos3' and value.encode('ascii', 'ignore') == 'zawsze wczone':
                print (self)

            print 'znacznik3'
            print value.encode('ascii', 'ignore')
            print activity.readSmsState

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    def loadScreen(self):
        MainApp.get_running_app().root.carousel.load_previous()

    @mainthread
    def group_update_marker(self, a):
        show_time = MainApp.get_running_app().root

        for index in xrange(0, len(show_time.group_members_lat)):
            marker = "marker_group_" + str(index + 1)

            print "testMarker"

            marker_group = show_time.carousel.slides[0].ids[marker]
            MainApp.get_running_app().root.carousel.slides[0].ids[marker].lat = float(
                show_time.group_members_lat[index])
            MainApp.get_running_app().root.carousel.slides[0].ids[marker].lon = float(
                show_time.group_members_lon[index])

            #gr = GroupScreen()
            #gr.centerMy()

            print "wszystkiewarstwy"
            for layer in MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]._layers:
                # if layer.id == 'line_map_layer':
                #     layer.czysc_trase()
                #     break
                layer.reposition()
                break
                #print layer

    @mainthread
    def on_location_symuluj(self, clock):

        group_screen = MainApp.get_running_app().root.carousel.slides[0]




        if self.FlagaWysylania >= 4:

            self.FlagaWysylania = 0
            try:
                if group_screen.connectGroup == True:
                    group_screen.sendMainLocation()
            except:
                print"brak polaczenia z grupa"
        else:
            self.FlagaWysylania = self.FlagaWysylania + 1
        if group_screen.simulationFlag == True:
            duration = (
                datetime.datetime.combine(datetime.date.today(),
                                          datetime.datetime.now().time()) - datetime.datetime.combine(
                    datetime.date.today(), MainApp.prev_time)).total_seconds()

            if duration >= 1:
                # self.gps_location = '\n'.join([
                #                                   '{}={}'.format(k, v) for k, v in kwargs.items()])
                # Symulator jazdy, tylko do pozorowania trasy
                punkty2 = MainApp.get_running_app().root.carousel.slides[0].punkty
                punktySymulacjiLon2 = MainApp.get_running_app().root.carousel.slides[0].punktySymulacjiLon
                punktySymulacjiLat2 = MainApp.get_running_app().root.carousel.slides[0].punktySymulacjiLat

                if group_screen.route_calculated == True and group_screen.Nawiguj == True and self.licz2 < len(
                        punktySymulacjiLat2) - 1:
                    # MainApp.lat = punkty2.getLat(self.licz2)
                    # MainApp.lon = punkty2.getLon(self.licz2)
                    MainApp.lat = punktySymulacjiLat2[self.licz2]
                    MainApp.lon = punktySymulacjiLon2[self.licz2]
                    self.licz2 = self.licz2 + 1
                    self.FlagaLicznik = True

                elif group_screen.route_calculated == True and group_screen.Nawiguj == True and self.licz2 < punkty2.getSize() - 1:
                    MainApp.lat = punkty2.getLat(self.licz2)
                    MainApp.lon = punkty2.getLon(self.licz2)
                    self.licz2 = self.licz2 + 1
                    self.FlagaLicznik = True
                else:
                    self.FlagaLicznik = False
                    self.licz2 = 0
                    self.distance = 0.00
                    self.calories = 0.00

                # koniec symulatora

                # Prawidłowy kod
                # for k, v in kwargs.items():
                #     if k == "lat":
                #         MainApp.lat = float(v)
                #     else:
                #         if k == "lon":
                #             MainApp.lon = float(v)

                # konic komenatrza prawidłowego kodu

                print "licznik_predkosci"
                if self.licz2 > 0:
                    print MainApp.lat
                    print MainApp.LastLat
                    print MainApp.lon
                    print MainApp.LastLon
                    print self.LastLat
                    print self.LastLon
                    self.distanceSpeed = group_screen.calculate_distance(float(MainApp.lat),
                                                                         float(MainApp.LastLat),
                                                                         float(MainApp.lon),
                                                                         float(MainApp.LastLon))
                    # self.distanceSpeed = self.distanceSpeed / 10000
                    self.timeNow = time.time()
                    self.TimeSpeed = self.timeNow - self.timeLast
                    # self.TimeSpeed = self.TimeSpeed / 60

                    print"++++++++++"
                    print (str(self.distanceSpeed))
                    print (str(self.TimeSpeed))
                    self.timeLast = self.timeNow
                    MainApp.LastLat = MainApp.lat
                    MainApp.LastLon = MainApp.lon
                    self.LastLat = MainApp.lat
                    self.LastLon = MainApp.lon
                else:
                    MainApp.LastLat = MainApp.lat
                    MainApp.LastLon = MainApp.lon
                    self.LastLat = MainApp.lat
                    self.LastLon = MainApp.lon
                    self.distanceSpeed = 0
                    self.TimeSpeed = 0

                self.licznikSpeed += 1

                # speed = Speed(float(speed))
                # # if speed<4.0:
                # #   speed=0
                # if speed > self.highest_speed_float:
                #     self.highest_speed_float = speed
                # # self.distance=self.distance+speed
                # # self.distance=round(self.distance,2)
                # self.gps_speed = speed
                if self.FlagaLicznik == False:
                    self.gps_speed = 0
                else:
                    try:
                        self.gps_speed = float(self.distanceSpeed * 3600) / float(self.TimeSpeed)
                        print "000000000000000000000000000000000"
                        print (self.gps_speed)
                        print "00000000000000000000000000000"
                    except:
                        pass
                self.tabela_speed[self.licz] = self.gps_speed
                if self.wystarczy == 1:
                    for i in self.tabela_speed:
                        self.suma = self.suma + i
                    self.avg_speed = self.suma / 20
                if self.licz == 19:
                    self.licz = 0
                    self.wystarczy = 1
                self.licz = self.licz + 1
                # self.highest_speed = self.highest_speed_float
                # print "blblbl"
                # print self.gps_speed
                # self.gps_speed = self.gps_speed * 18 / 5
                # self.gps_speed = round(self.gps_speed, 2)
                # self.highest_speed = self.highest_speed * 18 / 5
                # self.highest_speed = round(self.highest_speed, 2)
                # self.distance = self.distance + (self.gps_speed / 1000.00) aaaaaaaaaaaaaaa
                self.distance = self.distance + self.distanceSpeed
                if self.gps_speed <= 9 and self.gps_speed > 6:
                    self.calories = self.calories + 70 * 0.06 / 60.00
                elif self.gps_speed > 9 and self.gps_speed <= 13:
                    self.calories = self.calories + 70 * 0.114 / 60.00
                elif self.gps_speed > 13 and self.gps_speed <= 16:
                    self.calories = self.calories + 70 * 0.13 / 60.00
                elif self.gps_speed > 16 and self.gps_speed <= 19:
                    self.calories = self.calories + 70 * 0.149 / 60.00
                elif self.gps_speed > 19:
                    self.calories = self.calories + 70 * 0.168 / 60.00
                self.calories2 = round(self.calories, 1)
                self.distance2 = round(self.distance, 2)
                self.gps_speed2 = round(self.gps_speed, 1)
                if self.j == 6:
                    self.j = 0
                if self.j < 6:
                    self.ostatnie_predkosci[self.j] = self.gps_speed2
                    self.j = self.j + 1
                    sumka = self.ostatnie_predkosci[0] + self.ostatnie_predkosci[1] + self.ostatnie_predkosci[2] + \
                            self.ostatnie_predkosci[3] + self.ostatnie_predkosci[4] + self.ostatnie_predkosci[5]
                    self.gps_speed2 = round(sumka / 6, 1)
                # MainApp.get_running_app().root.carousel.slides[4].ids["label_speed"].text = str(self.gps_speed)
                # MainApp.get_running_app().root.carousel.slides[4].ids["label_max_speed"].text = str(self.highest_speed)

                MainApp.get_running_app().root.carousel.slides[0].ids["label_speed2"].text = str(self.gps_speed2)
                # MainApp.get_running_app().root.carousel.slides[0].ids["label_max_speed2"].text = str(self.highest_speed)
                MainApp.get_running_app().root.carousel.slides[0].ids["label_distance"].text = str(self.distance2)
                MainApp.get_running_app().root.carousel.slides[0].ids["label_calories"].text = str(self.calories2)
                if self.wystarczy == 1:
                    self.avg_speed2 = round(self.avg_speed, 1)
                    # MainApp.get_running_app().root.carousel.slides[0].ids["label_avg_speed"].text = str(self.avg_speed2)

                mapview = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
                if MainApp.znacznik == 0:
                    mapview.add_layer(LineMapLayer(), mode="scatter")
                    MainApp.znacznik = 1

                group = GroupScreen()
                try:
                    group.get_readings(1)
                except:
                    pass


                # Automatyczne wyświetlenei listy z kontakatami na screanie kontaktów
                if self.flagaWykonania == True:
                    MainApp.get_running_app().root.carousel.slides[1].view_contact()
                    # MainApp.get_running_app().root.carousel.slides[3].getSongs()
                    MainApp.get_running_app().root.carousel.index = 1
                    MainApp.get_running_app().root.carousel.load_previous()
                    self.flagaWykonania = False
                # wykonywane co godzine, pobieranie pogodty itd
                if self.flagaWygladu == True:

                    try:




                        self.flagaWygladu = False
                        # Weather().ustal_pogode()
                        print "przesledzam pogode"
                        miej = Weather().ustal_pogode()
                        print "przesledzilem pogode"
                        wsdl_file = 'https://burze.dzis.net/soap.php?WSDL'
                        key = '52873aebc20c11a47eacdd6f81f8b905d11a90af'
                        print "MIejscowoscc sprawdzana"
                        print str(miej)

                        city = str(miej)
                        # city="Mediolan"
                        range_detect = 70
                        print "Wykonuje burze_api"
                        ostrzezenia, burza = Weather().burze_api(key, wsdl_file, city, range_detect)
                        print "Wykonalem burze_api111"
                        Weather().print_burza(burza)
                        print "Wykonalem burze_api2"
                        Weather().print_ostrzezenia(ostrzezenia)
                        print "Wykonalem burze_api3"
                        # MusicPlayer().getSongs()
                        # self.flagaWygladu = False
                        print "daty daty daty"
                        # print datetime.date.today()
                        # abc = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        # print(str(abc))
                        # abcc = str(datetime.datetime.now())
                        # print(str(abcc))
                        # Czyszczenie cache, prototyp
                        # try:
                        #     for root, dirs, files in os.walk('/sdcard/Bicom/Mapy'):
                        #         for f in files:
                        #             print "czysci cache"
                        #             filename = os.path.join(root, f)
                        #             spr = float(path.getmtime('/sdcard/Bicom/cacheclear.dat')) - float(path.getctime(filename))
                        #             if float(spr) > 86400:
                        #                 os.remove(filename)
                        # except:
                        #     pass

                    except:
                        pass
                        # self.flagaWygladu = False
                        # Weather().ustal_pogode()
                        # MusicPlayer().getSongs()


                MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lat = float(MainApp.lat)
                MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lon = float(MainApp.lon)



                punkty = MainApp.get_running_app().root.carousel.slides[0].punkty
                # punkty.setNode(0, float(MainApp.lat), float(MainApp.lon))

                # group_screen = MainApp.get_running_app().root.carousel.slides[0]

                # obliczenie odleglosci miedzy aktualnym punktem a najblizszym punktem w nawigacji do ktorego zmierzamy
                if group_screen.route_calculated == True and group_screen.Nawiguj == True:
                    x1 = punkty.getLat(group_screen.actual_point)
                    y1 = punkty.getLon(group_screen.actual_point)
                    if group_screen.actual_point == punkty.getSize() - 1:
                        x2 = x1
                        y2 = y1
                    else:
                        x2 = punkty.getLat(group_screen.actual_point + 1)
                        y2 = punkty.getLon(group_screen.actual_point + 1)
                    x = MainApp.lat
                    y = MainApp.lon

                    # if group_screen.of_the_track(x1, y1, x2, y2, x, y):
                    #     group_screen.recalculate_route()
                    print "co tu jest?1"
                    print float(MainApp.lat)
                    print float(punkty.getLat(group_screen.actual_point))
                    print float(MainApp.lon)
                    print float(punkty.getLon(group_screen.actual_point))
                    distance1 = group_screen.calculate_distance(float(MainApp.lat),
                                                                float(punkty.getLat(group_screen.actual_point)),
                                                                float(MainApp.lon),
                                                                float(punkty.getLon(group_screen.actual_point)))
                    if x1 == x2 and y1 == y2:
                        distance2 = distance1
                    else:
                        print "co tu jest?2"
                        print float(MainApp.lat)
                        print float(punkty.getLat(group_screen.actual_point+1))
                        print float(MainApp.lon)
                        print float(punkty.getLon(group_screen.actual_point+1))
                        distance2 = group_screen.calculate_distance(float(MainApp.lat),
                                                                    float(punkty.getLat(group_screen.actual_point + 1)),
                                                                    float(MainApp.lon),
                                                                    float(punkty.getLon(group_screen.actual_point + 1)))

                    print "dystans"
                    print distance1
                    print distance2

                    # sprawdzenie czy nie ominelismy najblizszego punktu

                    instruction_points = GraphHopperAndroid.getInstructionPoints(group_screen.actual_instruction)
                    licznikInstrukcji = group_screen.actual_instruction + 1
                    try:
                        instruction_points2 = GraphHopperAndroid.getInstructionPoints(int(licznikInstrukcji))
                    except:
                        instruction_points2 = GraphHopperAndroid.getInstructionPoints(group_screen.actual_instruction)
                        print 'wywalilo instrukcje'

                    group_screen.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(
                        group_screen.actual_instruction2)
                    print "hhhhhhhhhhhhhhhhhhhhhh"
                    print self.distLabel

                    if group_screen.actual_instruction2 == 0 and self.distLabel>200:
                        self.distLabel2=round(float(self.distLabel)/1000.0,1)
                        group_screen.ids.label_instruction_distance.text = 'przez: ' + str(self.distLabel2) + ' km'
                    elif group_screen.actual_instruction2 == 0 and self.distLabel <= 200:
                        self.distLabel2=int(self.distLabel/10)*10
                        group_screen.ids.label_instruction_distance.text = 'przez: ' + str(self.distLabel2) + ' m'
                    elif group_screen.actual_instruction2 != 0 and self.distLabel>200:
                        self.distLabel2 = round(float(self.distLabel) / 1000.0, 1)
                        group_screen.ids.label_instruction_distance.text = 'za: ' + str(self.distLabel2) + ' km'
                    elif group_screen.actual_instruction2 != 0 and self.distLabel <= 200:
                        self.distLabel2 = int(self.distLabel / 10) * 10
                        group_screen.ids.label_instruction_distance.text = 'za: ' + str(self.distLabel2) + ' m'

                    print "co tu jest?3"
                    print float(MainApp.lat)
                    print float(instruction_points2.getLatitude(0))
                    print float(MainApp.lon)
                    print float(instruction_points2.getLongitude(0))

                    distanceIns = group_screen.calculate_distance(float(self.skrzyzowanieLat[self.k]),
                                                                  float(MainApp.lat),
                                                                  float(self.skrzyzowanieLon[self.k]),
                                                                  float(MainApp.lon))
                    print "dystansssssss"
                    print distanceIns
                    distanceMeters = distanceIns * 1000
                    self.distLabel = int(distanceMeters)
                    if distance2 > distance1:
                        if distance1 < 0.01:
                            # sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje


                            if instruction_points.getLatitude(0) == punkty.getLat(
                                    group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(
                                    group_screen.actual_point):
                                group_screen.actual_instruction += 1
                            print 'dystans instrukcji'
                            print str(distanceIns)
                            if float(distanceIns) < 0.4:

                                self.k = self.k + 1
                                group_screen.actual_instruction2 = group_screen.actual_instruction
                            else:
                                group_screen.actual_instruction2 = 0
                            group_screen.actual_point += 1

                            print "instrukcje"
                            print instruction_points.getLatitude(0)
                            print instruction_points.getLongitude(0)

                            if group_screen.actual_point == (punkty.getSize() - 1):
                                group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."
                                group_screen.saveToGpx()
                                group_screen.Nawiguj = False
                                self.licz2 = 0

                        # pomocnicze markery zawierajace 2 najblizsze punkty
                        '''MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lat = float(group_screen.punkty.getLat(group_screen.actual_point))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lon = float(group_screen.punkty.getLon(group_screen.actual_point))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lat = float(group_screen.punkty.getLat(group_screen.actual_point + 1))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lon = float(group_screen.punkty.getLon(group_screen.actual_point + 1))'''


                    else:
                        # sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje
                        if instruction_points.getLatitude(0) == punkty.getLat(
                                group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(
                                group_screen.actual_point):
                            group_screen.actual_instruction += 1
                        if float(distanceIns) < 0.2:

                            group_screen.actual_instruction2 = group_screen.actual_instruction
                        else:
                            group_screen.actual_instruction2 = 0
                        group_screen.actual_point += 1
                        print "instrukcje"
                        print instruction_points.getLatitude(0)
                        print instruction_points.getLongitude(0)

                        if group_screen.actual_point == (punkty.getSize() - 1):
                            group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."
                            group_screen.saveToGpx()
                            group_screen.Nawiguj = False
                            self.licz2 = 0

                    if self.lastInstruction != group_screen.ids.label_instruction.text:
                        activity.speaker.speak(group_screen.ids.label_instruction.text)
                        self.lastInstruction = group_screen.ids.label_instruction.text

                    if group_screen.actual_point >= group_screen.route_size[group_screen.travelled_points]:
                        group_screen.travelled_points += 1

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

                group_screen = MainApp.get_running_app().root.carousel.slides[0]
                if group_screen.recordPosition == True:
                    actualDate2 = strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
                    GraphHopperAndroid.addActualPosition(float(MainApp.lat), float(MainApp.lon), str(actualDate2))
                    group_screen.punktyTrasyLat.append(float(MainApp.lat))
                    group_screen.punktyTrasyLon.append(float(MainApp.lon))


    @mainthread
    def on_location(self, speed, **kwargs):



        group_screen = MainApp.get_running_app().root.carousel.slides[0]
        if self.FlagaWysylania >= 4:
            self.FlagaWysylania = 0

            try:
                if group_screen.connectGroup == True:
                    group_screen.sendMainLocation()
            except:
                print"brak polaczenia z grupa"
        else:
            self.FlagaWysylania = self.FlagaWysylania + 1
        if group_screen.simulationFlag == False:
            duration = (
                datetime.datetime.combine(datetime.date.today(),
                                          datetime.datetime.now().time()) - datetime.datetime.combine(
                    datetime.date.today(), MainApp.prev_time)).total_seconds()



            if duration >= 1:
                self.gps_location = '\n'.join([
                                                  '{}={}'.format(k, v) for k, v in kwargs.items()])


                # Prawidłowy kod
                for k, v in kwargs.items():
                    if k == "lat":
                        MainApp.lat = float(v)
                    else:
                        if k == "lon":
                            MainApp.lon = float(v)

                # konic komenatrza prawidłowego kodu


                speed = Speed(float(speed))
                # if speed<4.0:
                #   speed=0
                if speed > self.highest_speed_float:
                    self.highest_speed_float = speed
                # self.distance=self.distance+speed
                # self.distance=round(self.distance,2)
                self.gps_speed = speed

                self.tabela_speed[self.licz] = self.gps_speed
                if self.wystarczy == 1:
                    for i in self.tabela_speed:
                        self.suma = self.suma + i
                    self.avg_speed = self.suma / 20
                if self.licz == 19:
                    self.licz = 0
                    self.wystarczy = 1
                self.licz = self.licz + 1
                self.highest_speed = self.highest_speed_float
                print "blblbl"
                print self.gps_speed
                self.gps_speed = self.gps_speed * 18 / 5
                self.gps_speed = round(self.gps_speed, 2)
                self.highest_speed = self.highest_speed * 18 / 5
                self.highest_speed = round(self.highest_speed, 2)
                self.distance = self.distance + (self.gps_speed / 1000.00)
                if self.gps_speed <= 9 and self.gps_speed > 6:
                    self.calories = self.calories + 70 * 0.06 / 60.00
                elif self.gps_speed > 9 and self.gps_speed <= 13:
                    self.calories = self.calories + 70 * 0.114 / 60.00
                elif self.gps_speed > 13 and self.gps_speed <= 16:
                    self.calories = self.calories + 70 * 0.13 / 60.00
                elif self.gps_speed > 16 and self.gps_speed <= 19:
                    self.calories = self.calories + 70 * 0.149 / 60.00
                elif self.gps_speed > 19:
                    self.calories = self.calories + 70 * 0.168 / 60.00
                self.calories2 = round(self.calories, 1)
                self.distance2 = round(self.distance, 2)
                self.gps_speed2 = round(self.gps_speed, 1)
                # MainApp.get_running_app().root.carousel.slides[4].ids["label_speed"].text = str(self.gps_speed)
                # MainApp.get_running_app().root.carousel.slides[4].ids["label_max_speed"].text = str(self.highest_speed)

                MainApp.get_running_app().root.carousel.slides[0].ids["label_speed2"].text = str(self.gps_speed2)
                # MainApp.get_running_app().root.carousel.slides[0].ids["label_max_speed2"].text = str(self.highest_speed)
                MainApp.get_running_app().root.carousel.slides[0].ids["label_distance"].text = str(self.distance2)
                MainApp.get_running_app().root.carousel.slides[0].ids["label_calories"].text = str(self.calories2)
                if self.wystarczy == 1:
                    self.avg_speed2 = round(self.avg_speed, 1)
                    # MainApp.get_running_app().root.carousel.slides[0].ids["label_avg_speed"].text = str(self.avg_speed2)

                mapview = MainApp.get_running_app().root.carousel.slides[0].ids["mapView"]
                if MainApp.znacznik == 0:
                    mapview.add_layer(LineMapLayer(), mode="scatter")
                    MainApp.znacznik = 1

                group = GroupScreen()
                try:
                    group.get_readings(1)
                except:
                    pass


                # Automatyczne wyświetlenei listy z kontakatami na screanie kontaktów
                if self.flagaWykonania == True:
                    MainApp.get_running_app().root.carousel.slides[1].view_contact()
                    # MainApp.get_running_app().root.carousel.slides[3].getSongs()
                    MainApp.get_running_app().root.carousel.index = 1
                    MainApp.get_running_app().root.carousel.load_previous()
                    self.flagaWykonania = False
                # wykonywane co godzine, pobieranie pogodty itd
                if self.flagaWygladu == True:

                    try:




                        self.flagaWygladu = False
                        # Weather().ustal_pogode()
                        print "przesledzam pogode"
                        miej = Weather().ustal_pogode()
                        print "przesledzilem pogode"
                        wsdl_file = 'https://burze.dzis.net/soap.php?WSDL'
                        key = '52873aebc20c11a47eacdd6f81f8b905d11a90af'
                        print "MIejscowoscc sprawdzana"
                        print str(miej)

                        #city = str(miej)
                        city="Innsbruck"
                        range_detect = 70
                        print "Wykonuje burze_api"
                        ostrzezenia, burza = Weather().burze_api(key, wsdl_file, city, range_detect)
                        print "Wykonalem burze_api111"
                        Weather().print_burza(burza)
                        print "Wykonalem burze_api2"
                        Weather().print_ostrzezenia(ostrzezenia)
                        print "Wykonalem burze_api3"
                        # MusicPlayer().getSongs()
                        # self.flagaWygladu = False
                        print "daty daty daty"
                        # print datetime.date.today()
                        # abc = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        # print(str(abc))
                        # abcc = str(datetime.datetime.now())
                        # print(str(abcc))
                        # Czyszczenie cache, prototyp
                        # try:
                        #     for root, dirs, files in os.walk('/sdcard/Bicom/Mapy'):
                        #         for f in files:
                        #             print "czysci cache"
                        #             filename = os.path.join(root, f)
                        #             spr = float(path.getmtime('/sdcard/Bicom/cacheclear.dat')) - float(path.getctime(filename))
                        #             if float(spr) > 86400:
                        #                 os.remove(filename)
                        # except:
                        #     pass

                    except:
                        pass
                        # self.flagaWygladu = False
                        # Weather().ustal_pogode()
                        # MusicPlayer().getSongs()


                MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lat = float(MainApp.lat)
                MainApp.get_running_app().root.carousel.slides[0].ids["marker"].lon = float(MainApp.lon)

                punkty = MainApp.get_running_app().root.carousel.slides[0].punkty
                # punkty.setNode(0, float(MainApp.lat), float(MainApp.lon))

                # group_screen = MainApp.get_running_app().root.carousel.slides[0]

                # obliczenie odleglosci miedzy aktualnym punktem a najblizszym punktem w nawigacji do ktorego zmierzamy
                if group_screen.route_calculated == True and group_screen.Nawiguj == True:
                    x1 = punkty.getLat(group_screen.actual_point)
                    y1 = punkty.getLon(group_screen.actual_point)
                    if group_screen.actual_point == punkty.getSize() - 1:
                        x2 = x1
                        y2 = y1
                    else:
                        x2 = punkty.getLat(group_screen.actual_point + 1)
                        y2 = punkty.getLon(group_screen.actual_point + 1)
                    x = MainApp.lat
                    y = MainApp.lon

                    # if group_screen.of_the_track(x1, y1, x2, y2, x, y):
                    #     group_screen.recalculate_route()

                    distance1 = group_screen.calculate_distance(float(MainApp.lat),
                                                                float(punkty.getLat(group_screen.actual_point)),
                                                                float(MainApp.lon),
                                                                float(punkty.getLon(group_screen.actual_point)))
                    if x1 == x2 and y1 == y2:
                        distance2 = distance1
                    else:
                        distance2 = group_screen.calculate_distance(float(MainApp.lat),
                                                                    float(punkty.getLat(group_screen.actual_point + 1)),
                                                                    float(MainApp.lon),
                                                                    float(punkty.getLon(group_screen.actual_point + 1)))

                    print "dystans"
                    print distance1
                    print distance2

                    # sprawdzenie czy nie ominelismy najblizszego punktu

                    instruction_points = GraphHopperAndroid.getInstructionPoints(group_screen.actual_instruction)
                    licznikInstrukcji = group_screen.actual_instruction + 1
                    try:
                        instruction_points2 = GraphHopperAndroid.getInstructionPoints(int(licznikInstrukcji))
                    except:
                        instruction_points2 = GraphHopperAndroid.getInstructionPoints(group_screen.actual_instruction)
                        print 'wywalilo instrukcje'

                    group_screen.ids.label_instruction.text = GraphHopperAndroid.getTurnDescription(
                        group_screen.actual_instruction2)
                    if group_screen.actual_instruction2 == 0 and self.distLabel>200:
                        self.distLabel2=round(float(self.distLabel)/1000.0,1)
                        group_screen.ids.label_instruction_distance.text = 'przez: ' + str(self.distLabel2) + ' km'
                    elif group_screen.actual_instruction2 == 0 and self.distLabel <= 200:
                        self.distLabel2=int(self.distLabel/10)*10
                        group_screen.ids.label_instruction_distance.text = 'przez: ' + str(self.distLabel2) + ' m'
                    elif group_screen.actual_instruction2 != 0 and self.distLabel>200:
                        self.distLabel2 = round(float(self.distLabel) / 1000.0, 1)
                        group_screen.ids.label_instruction_distance.text = 'za: ' + str(self.distLabel2) + ' km'
                    elif group_screen.actual_instruction2 != 0 and self.distLabel <= 200:
                        self.distLabel2 = int(self.distLabel / 10) * 10
                        group_screen.ids.label_instruction_distance.text = 'za: ' + str(self.distLabel2) + ' m'

                    distanceIns = group_screen.calculate_distance(float(instruction_points2.getLatitude(0)),
                                                                  float(MainApp.lat),
                                                                  float(instruction_points2.getLongitude(0)),
                                                                  float(MainApp.lon))
                    distanceMeters = distanceIns * 1000
                    self.distLabel = int(distanceMeters)
                    if distance2 > distance1:
                        if distance1 < 0.01:
                            # sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje


                            if instruction_points.getLatitude(0) == punkty.getLat(
                                    group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(
                                    group_screen.actual_point):
                                group_screen.actual_instruction += 1
                            print 'dystans instrukcji'
                            print str(distanceIns)
                            if float(distanceIns) < 0.8:

                                group_screen.actual_instruction2 = group_screen.actual_instruction
                            else:
                                group_screen.actual_instruction2 = 0
                            group_screen.actual_point += 1

                            print "instrukcje"
                            print instruction_points.getLatitude(0)
                            print instruction_points.getLongitude(0)

                            if group_screen.actual_point == (punkty.getSize() - 1):
                                group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."
                                group_screen.saveToGpx()
                                group_screen.Nawiguj = False
                                self.licz2 = 0

                        # pomocnicze markery zawierajace 2 najblizsze punkty
                        '''MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lat = float(group_screen.punkty.getLat(group_screen.actual_point))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_1"].lon = float(group_screen.punkty.getLon(group_screen.actual_point))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lat = float(group_screen.punkty.getLat(group_screen.actual_point + 1))
                        MainApp.get_running_app().root.carousel.slides[0].ids["marker_trasa_2"].lon = float(group_screen.punkty.getLon(group_screen.actual_point + 1))'''


                    else:
                        # sprawdzenie czy najblizszy punkt ma wskazowki jazdy i zmiana na kolejna instrukcje
                        if instruction_points.getLatitude(0) == punkty.getLat(
                                group_screen.actual_point) and instruction_points.getLongitude(0) == punkty.getLon(
                                group_screen.actual_point):
                            group_screen.actual_instruction += 1
                        if float(distanceIns) < 0.8:

                            group_screen.actual_instruction2 = group_screen.actual_instruction
                        else:
                            group_screen.actual_instruction2 = 0
                        group_screen.actual_point += 1
                        print "instrukcje"
                        print instruction_points.getLatitude(0)
                        print instruction_points.getLongitude(0)

                        if group_screen.actual_point == (punkty.getSize() - 1):
                            group_screen.ids.label_instruction.text = "Dotarłeś na miejsce."
                            group_screen.saveToGpx()
                            group_screen.Nawiguj = False
                            self.licz2 = 0

                    if self.lastInstruction != group_screen.ids.label_instruction.text:
                        activity.speaker.speak(group_screen.ids.label_instruction.text)
                        self.lastInstruction = group_screen.ids.label_instruction.text

                    if group_screen.actual_point >= group_screen.route_size[group_screen.travelled_points]:
                        group_screen.travelled_points += 1

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

                group_screen = MainApp.get_running_app().root.carousel.slides[0]
                if group_screen.recordPosition == True:
                    actualDate2 = strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
                    GraphHopperAndroid.addActualPosition(float(MainApp.lat), float(MainApp.lon), str(actualDate2))
                    group_screen.punktyTrasyLat.append(float(MainApp.lat))
                    group_screen.punktyTrasyLon.append(float(MainApp.lon))


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