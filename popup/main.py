#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.widget import Widget
from jnius import autoclass
import sqlite3
import sys
from kivy.core.window import Window
#Window.clearcolor = (.841, .941, .937, 1)
#Window.clearcolor = (1, 1, 1, 1)
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial


class ZoneList():

    ListaNazw = []
    ListaId = []


    if platform() == 'android':

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


    #ListaNazw = ["Basement","Sun Room","Den","Living Room","Front Door","Bed Room","Kitchen","Hall","Garden","Dinning Room fsfdsf","Study Room","Bathroom","Gamesroom","Garage", "fgsg"]
    #ListaId = [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]


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
        idBaza = c.fetchall()           # Pobiera ID_GRUPY z bazy
        c.execute("SELECT REAKCJA FROM Grupy")
        reakcjaBaza = c.fetchall()      # Pobiera REAKCJE z bazy
        c.execute("DELETE FROM Grupy")  # Czysci baze

        for x in ListaId:
            c.execute("INSERT INTO Grupy VALUES (?, ?)", (x, 0))

            if unicode(x) in unicode(idBaza):
                for y in xrange(0, len(idBaza)):
                    #if "("+x+",)" == str(idBaza[y]): # to nie dziala
                        if str(reakcjaBaza[y]) == "(1,)":
                            c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, x))
                            break

            '''
            if str((x,)) in str(idBaza):
                for y in xrange(0, len(idBaza)):
                    if str((x,)) == str(idBaza[y]):
                        if str(reakcjaBaza[y]) == str((1,)):
                            c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, x))
                            #break
            '''

    conn.commit()
    conn.close()


    '''
    # ta czesc kodu jest potrzebna w funkcji check2 w glownej aplikacji

    conn = sqlite3.connect('baza.db')
    c = conn.cursor()

    c.execute("SELECT ID_GRUPY FROM Grupy WHERE REAKCJA = 0")
    dane = c.fetchall()

    conn.commit()
    conn.close()

    zmienna = BooleanProperty(True)
    nrGrupy = 5039

    for x in dane:
        if int(nrGrupy) == x[0]:
            # self.rejectIncomingCall()
            print 'odrzucenie'
            zmienna = False
            print zmienna
            break

    if zmienna:
        print 'decyduj'

    '''


class ZoneElements(GridLayout):
    if len(ZoneList.ListaNazw) < 5:
        linia = .01
    else:
        linia = .03


class ZoneCheckBoxes(ToggleButtonBehavior, GridLayout):
    _instance_count = -1
    _zoneNames = ZoneList.ListaNazw

#    Window.clearcolor = (1, 1, 1, 1)
    decyduj = BooleanProperty(True)
    #odrzuc = BooleanProperty(True)
    #decyduj2 = BooleanProperty(True)
    #dec1 = BooleanProperty()
    #dec2 = BooleanProperty()
    #odrzuc = 'down'
    #color = ListProperty([1, 1, 1, 1])

#    bind(minimum_height=self.ids.scroll.setter('height'))
    a = BooleanProperty(1)

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
            #self.on_state1 = True
            #self.on_state2 = False
            #ZoneCheckBoxes.kolor = (.235, .529, .572, 1)

        elif dane[ZoneCheckBoxes._instance_count] == (1,):
            ZoneCheckBoxes.odrzuc = False
            ZoneCheckBoxes.decyduj = True
            #self.on_state1 = False
            #self.on_state2 = True
            #ZoneCheckBoxes.kolor = [.1,.1,.1,.1]
        #self.ids.scroll.add_widget(ZoneCheckBoxes)

        conn.commit()
        conn.close()

    def odrzucenie(self, x):

        #ZoneCheckBoxes.odrzuc = True
        #ZoneCheckBoxes.odrzuc = True
        #self.odrzuc = False
        #self.odrzuc = True
        #self.odrzuc = a
        #self.decyduj = False

        #self.state = 'normal'
        #self.state = 'down'

        #ZoneCheckBoxes.drukuj = True
        self.on_state1 = True
        self.on_state2 = False

        #ZoneCheckBoxes.dec1 = True
        #ZoneCheckBoxes.dec2 = False

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        for i in range(0, len(ZoneList.ListaNazw)):
            if ZoneList.ListaNazw[i] == x[5:len(x)]:
                c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (0, ZoneList.ListaId[i]))

        #self.odrzuc2 = not self.odrzuc


        #checkbox = CheckBox()
        #checkbox.bind(active=on_checkbox_active)
        #checkbox = ToggleButton(group='Den')
        #checkbox.state = 'normal'
        #CheckBox(group="Den", odrzuc=True)
        conn.commit()
        conn.close()
        #self.decyduj = not self.odrzuc

        #self.decyduj = False
        #self.decyduj = 'normal'


    def decyzja(self, x):

        self.on_state1 = False
        self.on_state2 = True

        #ZoneCheckBoxes.dec1 = False
        #ZoneCheckBoxes.dec2 = True
        #self.decyduj = 'normal'
        #self.odrzuc = True
        #self.decyduj2 = True
        #self.active = True
        #self.value = True
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

        if platform() == 'android':
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

            projection = [RawContactsColumns.CONTACT_ID, GroupMembership.CONTACT_ID]

            grupa = resolver.query(Data.CONTENT_URI, projection, GroupMembership.GROUP_ROW_ID + "=" + groupID, None, None)
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

        #groupID = '1'

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
            ZoneButton.Kontakty.append("Ta grupa przeznaczona jest dla nieznanych numerów i nie zawiera żadnego kontaktu.")

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
        scrlv.scroll_y = value



        '''
        content = GridLayout(cols=1)
        zamknij = Button(text='Zamknij', background_color = (.235, .529, .572, 1), size_hint_y=None, height=40)

        if len(ZoneButton.Kontakty) < 1 or groupID == '999':
            ZoneButton.Kontakty = []
            ZoneButton.Kontakty.append("Brak kontaktow w tej grupie.")

        for i in range(0, len(ZoneButton.Kontakty)):
            content.add_widget(Label(text=ZoneButton.Kontakty[i], color=(.235, .529, .572, 1)))

        content.add_widget(zamknij)


        popup = Popup(title=tytul, title_color = (.235, .529, .572, 1), title_align='center',
                      separator_color = (.235, .529, .572, 1),
                      #background= 'atlas://data/images/defaulttheme/filechooser_selected',
                      content=content, auto_dismiss=False,
                      size_hint=(None, None),
                      size=(400, 400))
        popup.normal_color= (1,1,1,0)

        zamknij.bind(on_release=popup.dismiss)
        popup.open()
        '''
        #ZoneButton.Kontakty = []


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


class Grupy(App):
    pass


def main():
    Grupy().run()

    return 0

if __name__ == '__main__':
    main()
